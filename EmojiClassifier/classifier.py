from classes import *
from interface import ConsoleInterface
from patterns import *
from interface import *


# classifier.py - Main orchestrator:

# EmojiClassifier

class EmojiClassifier:
    def __init__(self, canvas_size, emoji_list):
        self.canvas_size = canvas_size # 5
        self.emoji_list = emoji_list # ["😊", "❤️", "⭐"]
        self.neural_network = NeuralNetwork(canvas_size * canvas_size, 10, len(emoji_list))
        self.current_emoji_classes = self.setup_emoji_classes()
        self.training_data = TrainingData(self.current_emoji_classes)
        self.canvas = DrawingCanvas(self.canvas_size, self.canvas_size)
        self.training_history = []
    
    def setup_emoji_classes(self):
        emojiclass_objects = [heart, star, smiley]
        selected_emojis = []
        for emojiclass_obj in emojiclass_objects:
            if emojiclass_obj.emoji_symbol in self.emoji_list:
                selected_emojis.append(emojiclass_obj)
        selected_emojis.sort(key=lambda x: x.class_index)
        return selected_emojis
    
    def run_interactive_training(self):
        interface = ConsoleInterface(self)
        flag = True
        while flag:
            menu_choice = interface.show_main_menu()
            match menu_choice:
                case 1: # Done
                    interface.clear_screen()
                    self.draw_mode()
                    emoji, confidence = self.predict_drawing(self.canvas)
                    print("-" * 17)
                    print(f"I am {confidence}% confident this is a {emoji}")
                    confirmation_input = interface.get_user_confirmation("Was I correct? (y/n): ")
                    match confirmation_input:
                        case True:
                            self.train_on_current_drawing(emoji)
                            interface.clear_screen()
                            interface.animate_learning()
                            print(f"Network accuracy: {self.test_network()}%")
                        case False:
                            emoji_list_dict = {}
                            print("Which emoji was it?")
                            for index, emoji_obj in enumerate(self.current_emoji_classes):
                                if emoji_obj.emoji_symbol != emoji:
                                    emoji_list_dict[index] = emoji_obj
                                    print(f"[{index}] {emoji_obj.emoji_symbol}")
                            while True:
                                    correct_emoji_input = input("Enter: ")
                                    if correct_emoji_input.isdigit() and int(correct_emoji_input) in emoji_list_dict:
                                        self.train_on_current_drawing(self.current_emoji_classes[int(correct_emoji_input)].emoji_symbol)
                                        interface.clear_screen()
                                        interface.animate_learning()
                                        print(f"Network accuracy: {self.test_network()}%")
                                        break
                                    else:
                                        print("Invalid input, try again.")
                case 2: # Done
                    self.quick_draw_mode()
                case 3:
                    interface.clear_screen()
                    print(f"Network accuracy: {self.test_network()}%")
                case 4:
                    interface.clear_screen()
                    print(self.show_training_progress())
                case 5:
                    interface.clear_screen()
                    save_load_choice = input("[1] Save \n[2] Load \nEnter: ")
                    if save_load_choice.isdigit():
                        if int(save_load_choice) == 1:
                            filename = input("Enter filename: ")
                            root, ext = os.path.splitext(filename)
                            if ext == "":
                                filename += ".json"
                            self.save_classifier(filename)
                        elif int(save_load_choice) == 2:
                            try:
                                filename = input("Enter filename: ")
                                root, ext = os.path.splitext(filename)
                                if ext == "":
                                    filename += ".json"
                                self.load_classifier(filename)
                            except FileNotFoundError:
                                print("File not found")
                        else:
                            print("Invalid choice")
                case 6:
                    flag = False
                case _:
                    print("Invalid input")
        
    def draw_mode(self):
        # self.canvas.clear_canvas()
        interface = ConsoleInterface(self)
        flag = True
        self.canvas.clear_canvas()
        while flag:
            interface.clear_screen()
            interface.display_canvas_interactive(self.canvas)
            user_response = input("Enter 'done' to quit \nEnter 'clear' to clear the board\nEnter coordinates (x y): ")
            if user_response.lower() == "done":
                flag = False
            elif user_response.lower() == "clear":
                self.canvas.clear_canvas()
            else:
                coordinates = user_response.split()
                if len(coordinates) != 2 or not coordinates[0].isdigit() or not coordinates[1].isdigit():
                    print("Invalid choice")
                    continue
                if not (0 <= int(coordinates[0]) < self.canvas_size) or not (0 <= int(coordinates[1]) < self.canvas_size):
                    print("Invalid choice.")
                    continue
                pixel_value = input(f"Set ({coordinates[0]}, {coordinates[1]}) to '.' or 'X': ")
                if pixel_value.lower() == "x" or pixel_value == ".":
                    if pixel_value.lower() == "x":
                        pixel_value = 1
                    else:
                        pixel_value = 0
                    self.canvas.set_pixel(int(coordinates[0]), int(coordinates[1]), pixel_value)
                else:
                    print("Invalid choice")

    def quick_draw_mode(self):
        self.canvas.clear_canvas()
        interface = ConsoleInterface(self)
        emoji_dict = {}
        pattern_dict = {}
        horizontal_line = ""
        for num in range(self.canvas_size * 2):
            horizontal_line += "-"
        print("-" * 17)
        print("Emojis:")
        for index, emoji in enumerate(self.current_emoji_classes):
            emoji_dict[index] = emoji
            print(f"{index}. {emoji.name}:{emoji.emoji_symbol}")
        while True:
            emoji_choice = input("Enter the number of the emoji you want to draw: ")
            if not emoji_choice.isdigit() or int(emoji_choice) not in emoji_dict:
                print("Invalid choice")
            else:
                interface.clear_screen()
                for index, canvas_obj in enumerate(emoji_dict[int(emoji_choice)].training_patterns):
                    pattern_dict[index] = canvas_obj
                    print(f"{index}")
                    canvas_obj.display_canvas()
                    print(horizontal_line)
                break
        while True:
            pattern_choice = input("Enter the number of the pattern you want to draw: ")
            if not pattern_choice.isdigit() or int(pattern_choice) not in pattern_dict:
                print("Invalid choice")
            else:
                interface.clear_screen()
                self.canvas.grid = [row[:] for row in pattern_dict[int(pattern_choice)].grid]
                self.canvas.display_canvas()
                break
        emoji, confidence = self.predict_drawing(self.canvas)
        print(f"I am {confidence}% confident this is a {emoji}")
        confirmation_input = interface.get_user_confirmation("Was I correct? (y/n): ")
        match confirmation_input:
            case True:
                self.train_on_current_drawing(emoji)
                interface.clear_screen()
                interface.animate_learning()
                print(f"Network accuracy: {self.test_network()}%")
            case False:
                emoji_list_dict = {}
                print("Which emoji was it?")
                for index, emoji_obj in enumerate(self.current_emoji_classes):
                    if emoji_obj.emoji_symbol != emoji:
                        emoji_list_dict[index] = emoji_obj
                        print(f"[{index}] {emoji_obj.emoji_symbol}")
                while True:
                        correct_emoji_input = input("Enter: ")
                        if correct_emoji_input.isdigit() and int(correct_emoji_input) in emoji_list_dict:
                            self.train_on_current_drawing(self.current_emoji_classes[int(correct_emoji_input)].emoji_symbol)
                            interface.clear_screen()
                            interface.animate_learning()
                            print(f"Network accuracy: {self.test_network()}%")
                            break
                        else:
                            print("Invalid input, try again.")

    def test_network(self):
        correct = 0
        emoji_symbols = []
        for emoji_class in self.current_emoji_classes:
            emoji_symbols.append(emoji_class.emoji_symbol)
        self.training_data.split_train_test()
        test_canvas = DrawingCanvas()
        for index, training_example in enumerate(self.training_data.test_inputs):
            test_canvas.load_from_input_array(training_example)
            prediction_emoji, confidence_percent = self.predict_drawing(test_canvas)
            if self.training_data.test_labels[index] == emoji_symbols.index(prediction_emoji):
                correct += 1
            test_canvas.clear_canvas()
        accuracy = round(correct / len(self.training_data.test_inputs) * 100, 2)
        self.training_history.append(accuracy)
        return accuracy
    
    def predict_drawing(self, canvas):
        probability_confidence_list = []
        input_array = canvas.convert_to_input_array()
        confidence_list = self.neural_network.predict(input_array)
        total_confidence_sum = sum(confidence_list)
        for confidence in confidence_list:
            probability_confidence_list.append((confidence / total_confidence_sum) * 100)
        highest_output_index = confidence_list.index(max(confidence_list))
        return self.emoji_list[highest_output_index], round(max(probability_confidence_list),2)

    def train_on_current_drawing(self, correct_emoji):
        if correct_emoji not in self.emoji_list:
            return None
        input_array = self.canvas.convert_to_input_array()
        for emoji_obj in self.current_emoji_classes:
            if emoji_obj.emoji_symbol == correct_emoji:
                target_class = emoji_obj
                target_vector = emoji_obj.get_target_vector(len(self.current_emoji_classes))
                break
        self.neural_network.train_single_example(input_array, target_vector)
        self.training_data.add_user_drawing(self.canvas, target_class)

    
    def show_training_progress(self):
        if not self.training_history:
            return "No training history"
        if len(self.training_history) == 1:
            return "Not enough training"
        starting_accuracy = self.training_history[0]
        current_accuracy = self.training_history[-1]
        improvement = current_accuracy - starting_accuracy
        improvement_str = f"+{improvement}" if improvement >= 0 else str(improvement)
        return f"Started at: {starting_accuracy}%, Now at: {current_accuracy}%, Improvement: {improvement_str}%"
    
    def save_classifier(self, filename):
        network_data = {}
        classifier_data = {}

        # Network settings
        network_data['input_size'] = self.neural_network.input_size
        network_data['hidden_size'] = self.neural_network.hidden_size
        network_data['output_size'] = self.neural_network.output_size
        network_data['learning_rate'] = self.neural_network.learning_rate

        # Hidden layer neurons
        network_data['hidden_layer'] = []
        for neuron in self.neural_network.hidden_layer:
            neuron_data = {
                'weights': neuron.weights,
                'bias': neuron.bias
            }
            network_data['hidden_layer'].append(neuron_data)
        
        # Output layer neurons
        network_data['output_layer'] = []
        for neuron in self.neural_network.output_layer:
            neuron_data = {
                'weights': neuron.weights,
                'bias': neuron.bias
            }
            network_data['output_layer'].append(neuron_data)
        
        # Classifier data
        classifier_data['canvas_size'] = self.canvas_size
        classifier_data['emoji_list'] = self.emoji_list
        classifier_data['training_history'] = self.training_history
        classifier_data['training_inputs'] = self.training_data.all_training_inputs
        classifier_data['training_labels'] = self.training_data.all_training_labels

        master_dict = {**network_data, **classifier_data}

        # Write to file
        with open(filename, "w") as file:
            json.dump(master_dict, file)
        
    def load_classifier(self, filename, deduplicate=False):
        # Check if file exists
        if not os.path.exists(filename):
            print(f"File {filename} not found!")  
            return False

        # Read from file
        with open(filename, 'r') as file:
            master_dict = json.load(file)
        
        # Restore network settings
        self.neural_network.input_size = master_dict['input_size']
        self.neural_network.hidden_size = master_dict['hidden_size']
        self.neural_network.output_size = master_dict['output_size']
        self.neural_network.learning_rate = master_dict['learning_rate']

        # Recreate hidden layer neurons
        self.neural_network.hidden_layer = []
        for neuron_data in master_dict['hidden_layer']:
            neuron = SimpleNeuron(neuron_data['weights'], neuron_data['bias'])
            self.neural_network.hidden_layer.append(neuron)
        
        # Recreate output layer neurons
        self.neural_network.output_layer = []
        for neuron_data in master_dict['output_layer']:
            neuron = SimpleNeuron(neuron_data['weights'], neuron_data['bias'])
            self.neural_network.output_layer.append(neuron)
        
        # Restore classifier data
        self.canvas_size = master_dict['canvas_size']
        self.emoji_list = master_dict['emoji_list']
        self.training_history = master_dict['training_history']

        self.current_emoji_classes = self.setup_emoji_classes()
        self.training_data = TrainingData(self.current_emoji_classes)
        self.training_data.all_training_inputs.extend(master_dict['training_inputs'])
        self.training_data.all_training_labels.extend(master_dict['training_labels'])

        # If deduplicate=False (default): all duplicates are preserved.
        # If deduplicate=True: duplicates are collapsed, keeping only the first occurrence.
        if deduplicate:
            unique_pairs = list(dict.fromkeys(
                zip(self.training_data.all_training_inputs, self.training_data.all_training_labels)
            ))
            self.training_data.all_training_inputs, self.training_data.all_training_labels = zip(*unique_pairs)
            self.training_data.all_training_inputs = list(self.training_data.all_training_inputs)
            self.training_data.all_training_labels = list(self.training_data.all_training_labels)

        self.canvas = DrawingCanvas(self.canvas_size, self.canvas_size)

        # Validation check
        loaded_emojis = set(self.emoji_list)
        available_emojis = set([cls.emoji_symbol for cls in self.current_emoji_classes])
        if loaded_emojis != available_emojis:
            print("⚠️ Warning: Some emojis from the save file are not available in patterns.py")