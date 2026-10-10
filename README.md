# Bug2Brain 🧠

*Debug the code. Understand the cause. Learn to prevent it.*

Bug2Brain is an AI-powered debugging and learning copilot designed for hackathons and educational environments. When developers and students encounter errors they cannot understand, existing AI coding assistants often produce quick fixes without teaching the underlying concept. Bug2Brain solves this by analyzing the code, providing a clear explanation of the root cause, and then generating a minimal correction along with learning materials to prevent the error in the future.

## 🌟 Features

- **Developer Workspace**: A polished code-analysis workspace to input your buggy code and stack traces.
- **Root Cause Explorer**: Clearly explains why the code failed and which part is responsible.
- **Fix Workspace**: Provides the corrected code, highlights the changes, and allows you to download the fix.
- **Learn Mode**: Explains the programming concept behind the error in beginner-friendly language, using analogies when appropriate.
- **Test Lab**: Generates a relevant test case and expected output to verify the fix.
- **Knowledge Check**: Tests your understanding with an AI-generated multiple-choice quiz.
- **Resilient UX**: Clear loading states, error handling, and a responsive Cyberpunk-themed design.

## 🏗️ Architecture & AI Transparency

Bug2Brain relies on the **Google Gemini API** (via the official `google-genai` SDK) to perform intelligent analysis.

**Exactly where AI is used:**
1. The user inputs buggy code and an error message.
2. The Streamlit frontend securely sends this context, along with specific system instructions (asking for line numbers, examples, and tests), to the Gemini model (e.g., `gemini-3.8-flash`).
3. The AI is responsible **only** for generating the analytical content: the diagnosis, root cause explanation, corrected code, concept explanation, test cases, and quiz.
4. The response is highly structured using the SDK's `response_schema` feature, which enforces our Pydantic `AnalysisResult` schema.
5. The Python backend validates this structured JSON response.
6. Streamlit presents the generated results dynamically in distinct learning sections, rendering diffs using Python's native `difflib`. 

*Note: The AI generates the insights, but Python and Streamlit handle the validation, parsing, error handling, and presentation independently. No arbitrary AI code is executed on your machine.*

## 🚀 Technology Stack

- **Python**: Core application logic.
- **Streamlit**: Web application framework and UI rendering.
- **Google GenAI SDK** (`google-genai`): Official Google SDK for interacting with the Gemini API.
- **Pydantic**: Data validation and structured output schema definition.

## 🛠️ Installation & Setup

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd Bug2Brain
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your Gemini API Key**:
   You can either input your API key directly in the application's sidebar, or set it as an environment variable:
   - **Windows (Command Prompt)**: `set GEMINI_API_KEY=your_api_key_here`
   - **Windows (PowerShell)**: `$env:GEMINI_API_KEY="your_api_key_here"`
   - **Linux/Mac**: `export GEMINI_API_KEY="your_api_key_here"`

4. **Launch the application**:
   ```bash
   python -m streamlit run app.py
   ```

## 🔒 Privacy

When you click "Analyze Bug", the code snippet and error message you provide are securely sent to the configured Google Gemini API for analysis. Do not submit sensitive company secrets or proprietary code unless you are comfortable with your configured API's data retention policies.

## ⚠️ Limitations & Future Improvements

**Current Limitations:**
- **AI Fallibility**: AI-generated code and explanations may be incomplete, unoptimized, or incorrect. Always manually review the proposed fixes.
- **No Execution**: AI-generated code is not executed automatically on the host machine for security reasons. Test cases are suggested but not run.
- **Size Limits**: Very large codebases cannot be analyzed due to context window limits; the tool is best suited for targeted snippets and specific errors.
- Depends on the availability and quota of the Gemini API.

**Future Improvements:**
- **Safe Sandboxed Execution**: Implement a secure sandbox (e.g., Docker container) to actually run the generated test cases and verify the fixes automatically.
- **IDE Integration**: Package the core logic as a VS Code or JetBrains plugin.
- **Conversation History**: Save past debugging sessions for users to review later.

## 🤖 AI Development Disclosure

This project was built with the assistance of **Google Deepmind's Antigravity (AGY)** AI coding assistant, powered by Gemini. Antigravity was utilized for structural implementation, Streamlit UI scaffolding, Pydantic schema generation, and security hardening of the codebase.
