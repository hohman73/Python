# interface.py - User interaction and display:

# ConsoleInterface

from classifier import *
import os

class ConsoleInterface:
    def __init__(self, classifier):
        self.classifier = classifier
    
    def display_canvas_interactive(self, canvas):
        # print("-" * 17)
        print("    " + " ".join(str(i) for i in range(self.classifier.canvas_size)))
        horizontal_line = "  "
        for num in range(self.classifier.canvas_size * 2 + 3):
            horizontal_line += "-"
        print(horizontal_line)
        for index, row in enumerate(canvas.grid):
            canvas_row = []
            separator = " "
            for pixel in row:
                if pixel == 0:
                    canvas_row.append(".")
                elif pixel == 1:
                    canvas_row.append("X")
            print(f"{index} | {separator.join(canvas_row)} |")
        print(horizontal_line)
    
    
    def show_main_menu(self):
        while True:
            print("-" * 17)
            menu_choice = input(
                "Choose an option: \n" \
                "[1] Draw and classify emoji \n" \
                "[2] Quick train with random patterns \n" \
                "[3] Test network accuracy \n" \
                "[4] View training progress \n" \
                "[5] Save/Load network \n" \
                "[6] Quit \n" \
                "Enter: ")
            if not menu_choice.isdigit():
                print("Invalid input")
                continue
            else:
                return int(menu_choice)
    
    def get_user_confirmation(self, message):
        while True:
            confirmation_input = input(message)
            if confirmation_input.lower() == "y":
                return True
            elif confirmation_input.lower() == "n":
                return False
            else:
                print("Invalid input, try again.")
                continue 
    
    def animate_learning(self):
        print("🧠 Learning from your feedback...")
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')