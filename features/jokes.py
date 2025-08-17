import random

jokes = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I'm reading a book on anti-gravity. It's impossible to put down!",
    "Why don't skeletons fight each other? They don't have the guts.",
    "I told my computer I needed a break, and it said 'No problem — I'll go to sleep!'"
]

def tell_joke():
    return random.choice(jokes)
