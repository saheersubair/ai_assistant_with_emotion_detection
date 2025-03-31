import streamlit as st
import openai
from emotion_detector import detect_emotion
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

# Set up OpenAI client
client = openai.Client(api_key=openai_api_key)

SYSTEM_PROMPT = """You are an AI assistant that adjusts responses based on the user's emotional state. 
Follow these guidelines:

Tone Adjustment:
- Positive: Enthusiastic and uplifting
- Negative: Compassionate and supportive
- Neutral: Professional and informative

Empathy Level:
- High: Explicit emotional acknowledgment
- Moderate: Brief empathetic remarks
- Low: Focus on query resolution

Response Depth:
- High Intensity: Detailed response addressing underlying concerns
- Moderate Intensity: Balanced response with key information
- Low Intensity: Concise and straightforward answer

Consider cultural context and provide urgent assistance when needed. 
The user's emotion will be prefixed in their messages as 'Emotion: [detected emotion]'."""

# Initialize session state
if 'conversation' not in st.session_state:
    st.session_state.conversation = [{"role": "system", "content": SYSTEM_PROMPT}]
if 'last_emotion' not in st.session_state:
    st.session_state.last_emotion = None

# Sidebar controls
with st.sidebar:
    st.header("Controls")

    # Reset button
    if st.button("🧹 Reset Chat"):
        st.session_state.conversation = [{"role": "system", "content": SYSTEM_PROMPT}]
        st.session_state.last_emotion = None
        st.rerun()

    # Emotion display
    st.divider()
    st.subheader("Current Emotion Status")
    emotion_display = st.session_state.last_emotion or "Not detected yet"
    st.markdown(f"**{emotion_display}**")
    st.caption("Emotion detected from latest message")

# Main chat interface
st.title("Emotion-Aware Chatbot 💬")
st.caption("A conversational AI that adapts to your emotions")

# Display chat history
for msg in st.session_state.conversation:
    if msg["role"] == "system":
        continue

    with st.chat_message(msg["role"]):
        content = msg["content"]
        if msg["role"] == "user":
            # Extract and display both emotion and query
            parts = content.split("\nQuery: ", 1)
            if len(parts) > 1:
                st.caption(f"Emotion: {parts[0].replace('Emotion: ', '')}")
                st.write(parts[1])
            else:
                st.write(content)
        else:
            st.write(content)

# Chat input and processing
if user_input := st.chat_input("How can I help you today?"):
    # Detect and store emotion
    emotion = detect_emotion(user_input)
    st.session_state.last_emotion = emotion

    # Add to conversation
    st.session_state.conversation.append({
        "role": "user",
        "content": f"Emotion: {emotion}\nQuery: {user_input}"
    })

    # Generate response
    with st.spinner("Crafting response..."):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=st.session_state.conversation,
                temperature=1,
            )
            ai_response = response.choices[0].message.content.strip()

            st.session_state.conversation.append({
                "role": "assistant",
                "content": ai_response
            })

        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.session_state.conversation.append({
                "role": "assistant",
                "content": "⚠️ I'm having trouble responding. Please try again."
            })

    st.rerun()