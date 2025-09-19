import math
import random
import json
import os

# classes.py - Core neural network and data structures:

class SimpleNeuron:
    def __init__(self, weights, bias):
        self.weights = weights #(list of floats)
        self.bias = bias #(float)
    
    # Takes inputs and returns the final neuron output (0-1) after applying sigmoid activation.
    def activate(self, inputs):
        return self.sigmoid(self.calculate_output(inputs))
    
    # Combines all inputs with their weights, adds bias, and returns the raw result.
    def calculate_output(self, inputs):
        new_inputs = []
        for i, input in enumerate(inputs):
            new_inputs.append(input * self.weights[i])
        return sum(new_inputs) + self.bias

    #  Adjusts the connection strengths based on the error the neuron made.
    def update_weights(self, inputs, error, learning_rate):
        new_weights = []
        for i, weight in enumerate(self.weights):
            new_weights.append(weight + learning_rate * error * inputs[i])
        self.weights = new_weights
    
    # Adjusts the neuron's baseline tendency based on the error it made.
    def update_bias(self, error, learning_rate):
        self.bias += learning_rate * error

    # Converts any number into a value between 0 and 1 using the sigmoid math formula.
    @staticmethod
    def sigmoid(x):
        return 1 / (1 + math.exp(-x))
    
    # Calculates how sensitive the sigmoid function is at a given point (used for learning).
    @staticmethod
    def sigmoid_derivative(x):
        s = SimpleNeuron.sigmoid(x)
        return s * (1 - s)

class DrawingCanvas:
    def __init__(self, width=5, height=5):
        # Creates a grid of 0s (empty pixels) with given width and height.
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
    
    # Resets the entire canvas so all pixels are 0 (empty).
    def clear_canvas(self):
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
    
    # Sets a single pixel at (x, y) to 0 or 1 (empty or filled).
    def set_pixel(self, x, y, value):
        if 0 <= x < self.width and 0 <= y < self.height:
            if value not in (0, 1):
                raise ValueError("Pixel value must be 0 or 1.")
            self.grid[y][x] = value
    
    # Draws a full shape from a pattern of "X" (filled) and "." (empty).
    def draw_shape(self, shape_pattern):
        for row_index, row in enumerate(shape_pattern):
            for element_index, element in enumerate(row):
                if element == "X":
                    element = 1
                else:
                    element = 0
                self.grid[row_index][element_index] = element
    
    # Returns the value of a single pixel at (x, y)
    def get_pixel(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
    
    # Prints the canvas to the console with "X" for filled pixels and "." for empty ones.
    def display_canvas(self):
        canvas = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for row_index, row in enumerate(self.grid):
            for element_index, element in enumerate(row):
                if element == 1:
                    canvas[row_index][element_index] = "X"
                else:
                    canvas[row_index][element_index] = "."
            print("".join(canvas[row_index]))
    
    # Flattens the 2D grid into a 1D list (for neural network input).
    def convert_to_input_array(self):
        flattened_list = []
        for row in self.grid:
            for element in row:
                flattened_list.append(element)
        return flattened_list
    
    # Loads a 1D list back into the 2D grid (for display or testing).
    def load_from_input_array(self, input_array):
        if len(input_array) == self.width * self.height:
            grid = []
            for num in range(len(input_array) // self.width):
                grid.append([])
            for index, element in enumerate(input_array):
                grid[index // self.width].append(element)
            self.grid = grid

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size # 25 for a 5x5 grid
        self.hidden_size = hidden_size # 10, these are the pattern detectors
        self.output_size = output_size # number of emoji classes
        self.hidden_layer = [SimpleNeuron([random.uniform(-1, 1) for n in range(input_size)], random.uniform(-1, 1)) for _ in range(hidden_size)]
        self.output_layer = [SimpleNeuron([random.uniform(-1, 1) for n in range(hidden_size)], random.uniform(-1, 1)) for _ in range(output_size)]
        self.learning_rate = 0.1

    # Takes an input list, passes it through the hidden and output layers, 
    # and returns the network’s raw predictions.
    def feedforward(self, inputs):
        hidden_outputs = []
        output_outputs = []
        for node in self.hidden_layer:
            hidden_outputs.append(node.activate(inputs))
        for node in self.output_layer:
            output_outputs.append(node.activate(hidden_outputs))
        return output_outputs

    # Runs one training step: does feedforward, calculates error,
    # and adjusts weights and biases using backpropagation.
    def train_single_example(self, inputs, target_outputs):
        actual_outputs = self.feedforward(inputs)
        output_errors = []
        hidden_outputs = []
        hidden_errors = []
        for iter in range(len(target_outputs)):
            output_errors.append(target_outputs[iter] - actual_outputs[iter])
        for node in self.hidden_layer:
            hidden_outputs.append(node.activate(inputs))
        for node in self.output_layer:
            node.update_weights(hidden_outputs, output_errors[self.output_layer.index(node)], self.learning_rate)
        for output_index, output_neuron in enumerate(self.output_layer):
            output_neuron.update_bias(output_errors[output_index], self.learning_rate)
        for hidden_index, hidden_neuron in enumerate(self.hidden_layer):
            error_sum = 0
            for output_index, output_neuron in enumerate(self.output_layer):
                weight = output_neuron.weights[hidden_index]
                error_sum += output_errors[output_index] * weight
            hidden_output = hidden_outputs[hidden_index]
            derivative = SimpleNeuron.sigmoid_derivative(hidden_output)
            hidden_error = error_sum * derivative
            hidden_errors.append(hidden_error)
        for hidden_index, hidden_neuron in enumerate(self.hidden_layer):
            hidden_neuron.update_weights(inputs, hidden_errors[hidden_index], self.learning_rate)
            hidden_neuron.update_bias(hidden_errors[hidden_index], self.learning_rate)

    # Uses feedforward to return the network’s output values (0–1 floats) without changing any weights.
    def predict(self, inputs):
        if len(inputs) != self.input_size:
            raise ValueError("Wrong input size")
        raw_output = self.feedforward(inputs)
        # Maybe convert to percentages
        return [x * 100 for x in raw_output]
    
    # Runs predict and returns the index (or label) of the strongest output neuron as the network’s “choice.”
    def get_prediction_label(self, inputs):
        prediction = self.predict(inputs)
        return prediction.index(max(prediction))

    # Tests the network on a dataset and returns the percentage of correct predictions.
    def calculate_accuracy(self, test_inputs, test_labels):
        correct_guesses = 0
        for iter in range(len(test_inputs)):
            prediction_label = self.get_prediction_label(test_inputs[iter])
            if prediction_label == test_labels[iter]:
                correct_guesses += 1
        return correct_guesses / len(test_inputs)
    
    def softmax(self, values):
        exp_vals = [math.exp(v) for v in values]
        total = sum(exp_vals)
        return [v / total for v in exp_vals]
    
    # Saves the network’s weights, biases, and settings to a file so training progress isn’t lost.
    def save_network(self, filename):
        # Create a dictionary to hold all network data
        network_data = {}

        # Save network settings
        network_data['input_size'] = self.input_size
        network_data['hidden_size'] = self.hidden_size
        network_data['output_size'] = self.output_size
        network_data['learning_rate'] = self.learning_rate

        # Save hidden layer neurons
        network_data['hidden_layer'] = []
        for neuron in self.hidden_layer:
            neuron_data = {
                'weights': neuron.weights,
                'bias': neuron.bias
            }
            network_data['hidden_layer'].append(neuron_data)

        # Save output layer neurons  
        network_data['output_layer'] = []
        for neuron in self.output_layer:
            neuron_data = {
                'weights': neuron.weights,
                'bias': neuron.bias
            }
            network_data['output_layer'].append(neuron_data)

        # Write to file
        with open(filename, 'w') as file:
            json.dump(network_data, file)
    
    # Loads the saved network’s weights, biases, and settings back in to continue using it.
    def load_network(self, filename):
        # Check if file exists
        if not os.path.exists(filename):
            print(f"File {filename} not found!")
            return False
        
        # Read from file
        with open(filename, 'r') as file:
            network_data = json.load(file)
        
        # Restore network settings
        self.input_size = network_data['input_size']
        self.hidden_size = network_data['hidden_size'] 
        self.output_size = network_data['output_size']
        self.learning_rate = network_data['learning_rate']
        
        # Recreate hidden layer neurons
        self.hidden_layer = []
        for neuron_data in network_data['hidden_layer']:
            neuron = SimpleNeuron(neuron_data['weights'], neuron_data['bias'])
            self.hidden_layer.append(neuron)
        
        # Recreate output layer neurons
        self.output_layer = []
        for neuron_data in network_data['output_layer']:
            neuron = SimpleNeuron(neuron_data['weights'], neuron_data['bias'])
            self.output_layer.append(neuron)

class EmojiClass:
    def __init__(self, emoji_symbol, name, class_index, training_patterns):
        self.emoji_symbol = emoji_symbol
        self.name = name
        self.class_index = class_index
        self.training_patterns = training_patterns
    
    # Add new example of a training pattern
    def add_training_pattern(self, canvas):
        self.training_patterns.append(canvas)
    
    # Returns random pattern from training patterns
    def get_random_pattern(self):
        return random.choice(self.training_patterns)
    
    # This tells the network which class is the correct answer for the pattern
    def get_target_vector(self, total_classes):
        target_vector = [0 for n in range(total_classes)]
        target_vector[self.class_index] = 1
        return target_vector

class TrainingData:
    def __init__(self, emoji_classes):
        self.emoji_classes = emoji_classes
        self.all_training_inputs = []
        self.all_training_labels = []
        self.train_inputs = []
        self.train_labels = []
        self.test_inputs = []
        self.test_labels = []
        for EmojiClass in emoji_classes:
            for pattern in EmojiClass.training_patterns:
                self.all_training_inputs.append(pattern.convert_to_input_array())
                self.all_training_labels.append(EmojiClass.class_index)
    
    # Randomly selects a batch of input-label pairs for training.
    def generate_training_batch(self, batch_size):
        if batch_size > len(self.all_training_inputs):
            batch_size = len(self.all_training_inputs)
        batch_inputs = []
        batch_labels = []
        batch_indexes = random.sample(range(len(self.all_training_inputs)), batch_size)
        for batch_index in batch_indexes:
            batch_inputs.append(self.all_training_inputs[batch_index])
            batch_labels.append(self.all_training_labels[batch_index])
        return batch_inputs, batch_labels
    
    # Adds a new user-generated drawing to the training set with its corresponding label.
    def add_user_drawing(self, canvas, emoji_class):
        self.all_training_inputs.append(canvas.convert_to_input_array())
        self.all_training_labels.append(emoji_class.class_index)
    
    # Finds and returns the emoji class object that matches a given emoji symbol.
    def get_class_by_emoji(self, emoji_symbol):
        for emoji_class in self.emoji_classes:
            if emoji_symbol == emoji_class.emoji_symbol:
                return emoji_class
        return None
    
    # Randomizes the order of training inputs and labels to prevent learning bias.
    def shuffle_training_data(self):
        training_tuples = []
        for iter in range(len(self.all_training_inputs)):
            training_tuples.append((self.all_training_inputs[iter], self.all_training_labels[iter]))
        random.shuffle(training_tuples)
        self.all_training_inputs = []
        self.all_training_labels = []
        for iter in range(len(training_tuples)):
            self.all_training_inputs.append(training_tuples[iter][0])
            self.all_training_labels.append(training_tuples[iter][1])
    
    # Splits the full dataset into training and testing sets based on a given ratio.
    def split_train_test(self, test_ratio=0.2):
        self.shuffle_training_data()
        split_index = int(len(self.all_training_inputs) * test_ratio)
        self.train_inputs = self.all_training_inputs[split_index:]
        self.train_labels = self.all_training_labels[split_index:]
        self.test_inputs = self.all_training_inputs[:split_index]
        self.test_labels = self.all_training_labels[:split_index]