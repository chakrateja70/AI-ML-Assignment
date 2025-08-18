from groq import Groq
from langchain.prompts import PromptTemplate
from typing import List
import os

from app.core.exceptions import LLMError, ConfigurationError
from app.utils.prompts import TECH_QUESTION_SINGLE_PROMPT
from app.utils.prompts import EVALUATE_ANSWER_PROMPT
from app.utils.prompts import FINAL_REPORT_PROMPT
from app.utils.prompts import POLITE_NEXT_QUESTION_PROMPT

class LLMService:
    """Service for LLM interactions and response generation"""

    def __init__(self, model: str = "meta-llama/llama-4-scout-17b-16e-instruct"):
        self.model = model
        self._client = None
        self._initialized = False

    def _initialize(self):
        """Lazy initialization of the LLM service"""
        if self._initialized:
            return
        self.groq_api_key = os.getenv("GROQ_API_KEY")
        if not self.groq_api_key:
            raise ConfigurationError(
                "GROQ_API_KEY not found in environment variables",
                config_key="GROQ_API_KEY"
            )
        self._client = Groq(api_key=self.groq_api_key)
        self._initialized = True

    def generate_technical_question(self, tech_stack: List[str], experience: int) -> str:
        """
        Generate a single technical question based on tech stack and experience.
        """
        self._initialize()
        prompt = PromptTemplate.from_template(TECH_QUESTION_SINGLE_PROMPT)
        input_text = prompt.format(tech_stack=", ".join(tech_stack), experience=experience)
        try:
            response = self._client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": input_text}]
            )
            question = response.choices[0].message.content.strip()
            return question
        except Exception as e:
            raise LLMError(f"Failed to generate technical question: {str(e)}")

    def evaluate_answer(self, question: str, answer: str, tech_stack: List[str], experience: int) -> dict:
        """
        Evaluate candidate's answer and return score (0-5) and feedback.
        """
        self._initialize()
        prompt = PromptTemplate.from_template(EVALUATE_ANSWER_PROMPT)
        input_text = prompt.format(question=question, answer=answer, tech_stack=", ".join(tech_stack), experience=experience)
        try:
            response = self._client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": input_text}]
            )
            content = response.choices[0].message.content.strip()
            # Expecting: "Score: X\nFeedback: ..."
            score = 0
            feedback = ""
            for line in content.split("\n"):
                if line.lower().startswith("score:"):
                    score = int(line.split(":", 1)[1].strip())
                elif line.lower().startswith("feedback:"):
                    feedback = line.split(":", 1)[1].strip()
            return {"score": score, "feedback": feedback}
        except Exception as e:
            raise LLMError(f"Failed to evaluate answer: {str(e)}")

    def polite_next_question(self, tech_stack: List[str], experience: int, prev_question: str) -> str:
        """
        Politely handle no answer and ask another question.
        """
        self._initialize()
        prompt = PromptTemplate.from_template(POLITE_NEXT_QUESTION_PROMPT)
        input_text = prompt.format(tech_stack=", ".join(tech_stack), experience=experience, prev_question=prev_question)
        try:
            response = self._client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": input_text}]
            )
            question = response.choices[0].message.content.strip()
            return question
        except Exception as e:
            raise LLMError(f"Failed to generate polite next question: {str(e)}")

    def generate_report(self, answers: list, scores: list, tech_stack: List[str], experience: int) -> str:
        """
        Generate a final report and polite closing statement.
        """
        self._initialize()
        prompt = PromptTemplate.from_template(FINAL_REPORT_PROMPT)
        input_text = prompt.format(answers="\n".join(answers), scores=", ".join(str(s) for s in scores), tech_stack=", ".join(tech_stack), experience=experience)
        try:
            response = self._client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": input_text}]
            )
            report = response.choices[0].message.content.strip()
            return report
        except Exception as e:
            raise LLMError(f"Failed to generate final report: {str(e)}")
