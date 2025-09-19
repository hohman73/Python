from classifier import *
from patterns import *
from interface import *

# main.py - Entry point and program flow:

emoji_classifier = EmojiClassifier(5, ["😊", "❤️", "⭐"])

emoji_classifier.run_interactive_training()


