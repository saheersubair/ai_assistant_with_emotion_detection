from transformers import pipeline

# Load the sentiment-analysis pipeline, which can be modified for emotion detection
emotion_model = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

def detect_emotion(text):
    result = emotion_model(text)
    return result[0]['label']

if __name__ == "__main__":
    query = "I'm feeling unwell"
    print(detect_emotion(query))