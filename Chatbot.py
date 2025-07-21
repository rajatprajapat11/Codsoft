import random
from datetime import datetime, date

# Rule definitions
rules = {
    "greeting": ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"],
    "name": ["your name", "who are you", "what's your name"],
    "how_are_you": ["how are you", "how are you doing", "how's it going"],
    "thanks": ["thank you", "thanks", "thx"],
    "bye": ["bye", "goodbye", "see you", "exit"],
    "time": ["what time", "current time", "tell me time", "time now"],
    "date": ["what date", "today's date", "current date", "date today"],
    "joke": ["tell me a joke", "make me laugh", "joke", "funny"],
    "weather": ["weather", "is it hot", "is it cold", "what's the weather"],
    "age": ["how old are you", "your age", "what's your age"],
    "help": ["help", "what can you do", "how to use", "guide me"],
    "creator": ["who made you", "who created you", "your creator"],
    "hobby": ["what's your hobby", "do you have a hobby", "your hobbies"],
    "love": ["do you love me", "i love you", "can you love"],
    "eat": ["what do you eat", "do you eat", "can you eat"],
    "sleep": ["do you sleep", "when do you sleep", "sleep time"],
    "location": ["where are you", "your location", "where do you live"],
    "language": ["what language do you speak", "do you speak", "can you talk"],
    "work": ["what do you do", "your job", "your work"],
    "robot": ["are you a robot", "are you human", "bot or human"],
}

# Response mapping
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!", "Greetings!"],
    "name": ["I'm RuleBot!", "You can call me RuleBot.", "RuleBot at your service!"],
    "how_are_you": ["I'm doing great!", "I'm fine, thanks!", "All systems go!"],
    "thanks": ["You're welcome!", "No problem!", "Glad to help!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "time": [f"The time is {datetime.now().strftime('%H:%M:%S')}"],
    "date": [f"Today's date is {date.today()}"],
    "joke": ["Why don't scientists trust atoms? Because they make up everything!", "I'm reading a book on anti-gravity. It's impossible to put down!"],
    "weather": ["I'm not connected to live weather, but I hope it's nice!", "Weather's a mystery to me. I'm a bot!"],
    "age": ["I'm timeless!", "I'm just a fresh line of code."],
    "help": ["Ask me about time, date, jokes, weather, or say 'hi' to start."],
    "creator": ["I was created by a passionate Python programmer!", "Someone smart and curious wrote my code."],
    "hobby": ["I enjoy talking to you!", "Processing words is fun for me!"],
    "love": ["I appreciate you!", "Love is complex for a bot."],
    "eat": ["I consume electricity, not food!", "I run on code, not calories."],
    "sleep": ["Sleep is for humans. I'm 24/7!", "Never sleep, always ready."],
    "location": ["I'm right here with you, inside your screen!", "In the digital space."],
    "language": ["I speak Python and English.", "Currently, I communicate in English."],
    "work": ["I chat and help you with small tasks.", "I keep you company and informed."],
    "robot": ["Yes, I'm a chatbot coded in Python!", "Definitely a bot, but a friendly one!"],
}

# Smart fallback options
fallback_responses = [
    "Hmm, I didn’t get that. Try asking about time, date, or a joke!",
    "I'm still learning! Try saying something like 'hello' or 'who are you?'",
    "That’s outside my training... but I'm improving every day!",
    "Maybe rephrase that? I can answer basic stuff like weather or your name.",
    "Interesting! But I don’t know how to respond to that yet. Ask me what I can do!",
]

# Matching logic
def get_response(user_input):
    user_input = user_input.lower()
    for intent, keywords in rules.items():
        for keyword in keywords:
            if keyword in user_input:
                return random.choice(responses[intent])
    return random.choice(fallback_responses)

# Chat loop
def chatbot():
    print("Chatbot: Hi! I'm RuleBot. Ask me anything or type 'exit' to quit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye! 👋")
            break
        reply = get_response(user_input)
        print(f"Chatbot: {reply}")

# Run it
if __name__ == "__main__":
    chatbot()
