import random
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Define responses
responses = {
    "hello": "Hello! How can I assist you today?",
    "how are you": "I'm just a chatbot, but I'm functioning well! How about you?",
    "your name": "I'm an AI-powered chatbot built with spaCy!",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm sorry, I don't understand that. Can you rephrase?"
}

def preprocess_input(user_input):
    """Tokenizes and normalizes user input using spaCy."""
    doc = nlp(user_input.lower())
    tokens = [token.text for token in doc]
    return " ".join(tokens)

def get_response(user_input):
    """Fetches response based on user input."""
    processed_input = preprocess_input(user_input)
    for key in responses.keys():
        if key in processed_input:
            return responses[key]
    return responses["default"]

def chatbot():
    """Runs the chatbot loop."""
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot:", responses["bye"])
            break
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chatbot()
