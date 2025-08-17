# CSS styles for UI components

REG_CSS = """
<style>
    body, .stApp, .main, .block-container, .stApp > header, .stApp > footer {
        background: #181a1b !important;
    }
    .reg-container {
        max-width: 500px;
        margin: 0 auto;
        background: #23272f;
        border-radius: 1.5rem;
        box-shadow: 0 2px 12px rgba(44,62,80,0.07);
        padding: 2rem 2.5rem;
        margin-top: 2rem;
    }
    .reg-title {
        text-align: center;
        font-size: 2rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        color: #e0e6ed;
    }
    .reg-desc {
        text-align: center;
        font-size: 1.1rem;
        color: #b0b8c1;
        margin-bottom: 2rem;
    }
    .stTextInput>div>input, .stTextArea>div>textarea {
        border-radius: 1rem !important;
        padding: 0.75rem 1rem !important;
        font-size: 1rem !important;
        background: #181a1b !important;
        color: #e0e6ed !important;
        border: 1px solid #23272f !important;
    }
    .stNumberInput>div>input {
        border-radius: 1rem !important;
        padding: 0.75rem 1rem !important;
        font-size: 1rem !important;
        background: #181a1b !important;
        color: #e0e6ed !important;
        border: 1px solid #23272f !important;
    }
    .stButton>button {
        border-radius: 1rem !important;
        padding: 0.75rem 1.5rem !important;
        font-size: 1rem !important;
        background: #3498db !important;
        color: #fff !important;
        border: none !important;
    }
    .spinner {
        width: 40px;
        height: 40px;
        border: 4px solid #23272f;
        border-top: 4px solid #3498db;
        border-radius: 50%;
        animation: spin 1s linear infinite;
        margin: 0 auto;
    }
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    .chat-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 2rem 0;
    }
    .stChatMessage {
        background: transparent !important;
    }
    .stChatMessageContent {
        background: #23272f !important;
        border-radius: 1rem !important;
        padding: 1rem 1.5rem !important;
        margin: 0.5rem 0 !important;
        border: 1px solid #2c3e50 !important;
    }
    .stChatInput {
        background: #181a1b !important;
        border-radius: 1rem !important;
        border: 1px solid #23272f !important;
    }
    .stChatInput textarea {
        background: #181a1b !important;
        color: #e0e6ed !important;
    }
    /* Position chat messages - system on left, user on right */
    .stChatMessage[data-testid="chatMessage"] {
        background: transparent !important;
    }
    .stChatMessage[data-testid="chatMessage"] .stChatMessageContent {
        background: #23272f !important;
        border-radius: 1rem !important;
        padding: 1rem 1.5rem !important;
        margin: 0.5rem 0 !important;
        border: 1px solid #2c3e50 !important;
        max-width: 80% !important;
    }
    /* System/Assistant messages on the left */
    .stChatMessage[data-testid="chatMessage"]:has(.stChatMessageContent[data-testid="chatMessageContent"]) {
        justify-content: flex-start !important;
    }
    /* User messages on the right */
    .stChatMessage[data-testid="chatMessage"]:has(.stChatMessageContent[data-testid="chatMessageContent"]) {
        justify-content: flex-end !important;
    }
    /* Ensure proper spacing */
    .stChatMessage {
        margin: 1rem 0 !important;
    }
    /* Additional background coverage */
    .stChatInputContainer, .stChatInputContainer > div {
        background: #181a1b !important;
    }
    /* Chat container styling */
    .chat-container {
        background: #181a1b !important;
        min-height: 100vh !important;
    }
    /* Ensure sidebar background */
    .css-1d391kg, .css-1lcbmhc {
        background: #181a1b !important;
    }
    /* Additional comprehensive background coverage */
    .stApp > div, .stApp > div > div, .stApp > div > div > div {
        background: #181a1b !important;
    }
    /* Ensure chat input area background */
    .stChatInputContainer, .stChatInputContainer > div, .stChatInputContainer > div > div {
        background: #181a1b !important;
    }
    /* Ensure all text areas and inputs have proper background */
    .stTextInput > div > div > input, .stTextArea > div > div > textarea {
        background: #181a1b !important;
        color: #e0e6ed !important;
    }
</style>
"""

CHAT_CSS = """
<style>
    .chat-container {
        max-width: 600px;
        margin: 0 auto;
        padding: 2rem 0;
    }
    .chat-title {
        text-align: center;
        font-size: 2rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        color: #2c3e50;
    }
    .chat-desc {
        text-align: center;
        font-size: 1.1rem;
        color: #7f8c8d;
        margin-bottom: 2rem;
    }
    .chat-bubble {
        display: flex;
        margin-bottom: 1rem;
    }
    .chat-bubble.bot {
        justify-content: flex-start;
    }
    .chat-bubble.user {
        justify-content: flex-end;
    }
    .bubble {
        padding: 1rem 1.5rem;
        border-radius: 1.5rem;
        max-width: 70%;
        font-size: 1rem;
        box-shadow: 0 2px 8px rgba(44,62,80,0.07);
    }
    .bubble.bot {
        background: #f4f6fb;
        color: #2c3e50;
        border-bottom-left-radius: 0.5rem;
    }
    .bubble.user {
        background: #3498db;
        color: #fff;
        border-bottom-right-radius: 0.5rem;
    }
    .chat-input {
        width: 100%;
        margin-top: 2rem;
        display: flex;
        gap: 0.5rem;
    }
    .stTextInput>div>input {
        border-radius: 1rem !important;
        padding: 0.75rem 1rem !important;
        font-size: 1rem !important;
    }
    .stButton>button {
        border-radius: 1rem !important;
        padding: 0.75rem 1.5rem !important;
        font-size: 1rem !important;
        background: #3498db !important;
        color: #fff !important;
        border: none !important;
    }
</style>
"""
