# Emotion-Aware Chatbot 🤖💬

An intelligent chatbot that adapts its responses based on detected user emotions, featuring conversation memory and an interactive UI.


## Features ✨

- **Emotion Detection**: Real-time sentiment analysis of user inputs
- **Adaptive Responses**: GPT-4o powered responses tailored to emotional context
- **Conversation Memory**: Context-aware dialogue maintenance
- **Streamlit UI**: Modern web interface with chat history
- **Reset Functionality**: One-click conversation reset
- **Emotion Status**: Real-time emotion display in sidebar
- **Error Handling**: Graceful error recovery and user notifications
- **Customizable**: Adjustable system prompts and parameters

## Installation ⚙️

1. Clone repository:
```bash
git clone https://github.com/saheersubair/ai_assistant_with_emotion_detection.git
cd emotion-aware-chatbot
```

2. Install dependencies:
```bash
pip install transformers torch openai flask streamlit python-dotenv
```

3. Set up environment:
```bash
echo "OPENAI_API_KEY='your-api-key-here'" > .env
```

## Configuration 🔧

1. **API Keys**:
   - Obtain OpenAI API key.
   - Store in .env file.

## Usage 🚀

1. Start the application:
```bash
streamlit run app.py
```

2. Interface components:
   - **Main Chat**: Input messages at bottom
   - **Sidebar**: Contains reset button and emotion status
   - **History**: Scrollable conversation window

3. Example interaction:
   ```
   You: I'm feeling really stressed today
   Bot: I'm sorry to hear you're feeling stressed. Let's work through this together...
   ```

## Dependencies 📦

- python 3.10+
- streamlit >= 1.44.0
- openai >= 1.69.0
- transformers >= 4.50.3
- torch >= 2.6.0
- python-dotenv >= 1.1.0

## Security 🔒

**Important**: Never commit API keys
- Use `.env` file for local development
- Use Streamlit Secrets for deployed apps
- Add `.env` to `.gitignore`
