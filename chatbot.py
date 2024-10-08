import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I assist you today?"]
    ],
    [
        r"what is your name ?",
        ["My name is Chatbot.", "You can call me Chatbot!"]
    ],
    [
        r"how are you ?",
        ["I'm doing great, thank you! How about you?", "I'm fine! How can I help you today?"]
    ],
    [
        r"sorry (.*)",
        ["No problem at all!", "It's okay, no worries."]
    ],
    [
        r"(.*) your age?",
        ["I’m timeless!", "Age is just a number for me."]
    ],
    [
        r"(.*) (location|city) ?",
        ["I am from the digital world."]
    ],
    [
        r"what (.*) you do?",
        ["I'm here to chat with you and help you with any questions."]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day.", "It was nice talking to you! Bye!"]
    ],
]

def chatbot():
    print("Chatbot: Hi! Type 'quit' to end the conversation.")
    chat = Chat(pairs, reflections)
    chat.converse()

chatbot()
