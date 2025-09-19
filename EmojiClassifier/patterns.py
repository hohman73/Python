# patterns.py - Training data:

# Predefined emoji patterns (the smiley, heart, star patterns)
# Pattern generation utilities

from classes import *

# Heart
heart_canvas1 = DrawingCanvas()
heart_pattern1 = [
    ['.', 'X', '.', 'X', '.'],
    ['X', 'X', 'X', 'X', 'X'],
    ['.', 'X', 'X', 'X', '.'],
    ['.', '.', 'X', '.', '.'],
    ['.', '.', '.', '.', '.']
   ]
heart_canvas1.draw_shape(heart_pattern1)

heart_canvas2 = DrawingCanvas()
heart_pattern2 = [
    ['X', 'X', '.', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X'],
    ['.', 'X', 'X', 'X', '.'],
    ['.', '.', 'X', '.', '.'],
    ['.', '.', '.', '.', '.']
]
heart_canvas2.draw_shape(heart_pattern2)

heart_canvas3 = DrawingCanvas()
heart_pattern3 = [
    ['.', 'X', '.', 'X', '.'],
    ['X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X'],
    ['.', 'X', 'X', 'X', '.'],
    ['.', '.', 'X', '.', '.']
]
heart_canvas3.draw_shape(heart_pattern3)

# Star
star_canvas1 = DrawingCanvas()
star_pattern1 = [
    ['.', '.', 'X', '.', '.'],
    ['.', 'X', 'X', 'X', '.'],
    ['X', 'X', 'X', 'X', 'X'],
    ['.', 'X', '.', 'X', '.'],
    ['X', '.', '.', '.', 'X']
   ]
star_canvas1.draw_shape(star_pattern1)

star_canvas2 = DrawingCanvas()
star_pattern2 = [
    ['.', '.', 'X', '.', '.'],
    ['.', 'X', '.', 'X', '.'],
    ['X', 'X', 'X', 'X', 'X'],
    ['.', 'X', 'X', 'X', '.'],
    ['X', '.', '.', '.', 'X']
]
star_canvas2.draw_shape(star_pattern2)

star_canvas3 = DrawingCanvas()
star_pattern3 = [
    ['.', '.', 'X', '.', '.'],
    ['.', 'X', 'X', 'X', '.'],
    ['X', 'X', '.', 'X', 'X'],
    ['.', 'X', 'X', 'X', '.'],
    ['X', '.', '.', '.', 'X']
]
star_canvas3.draw_shape(star_pattern3)

# Smiley
smiley_canvas1 = DrawingCanvas()
smiley_pattern1 = [
    ['.', 'X', 'X', 'X', '.'],
    ['X', '.', '.', '.', 'X'],
    ['X', '.', 'X', '.', 'X'],
    ['X', '.', '.', '.', 'X'],
    ['.', 'X', 'X', 'X', '.']
   ]
smiley_canvas1.draw_shape(smiley_pattern1)

smiley_canvas2 = DrawingCanvas()
smiley_pattern2 = [
    ['.', 'X', 'X', 'X', '.'],
    ['X', '.', 'X', '.', 'X'],
    ['X', '.', '.', '.', 'X'],
    ['X', '.', 'X', '.', 'X'],
    ['.', 'X', 'X', 'X', '.']
]
smiley_canvas2.draw_shape(smiley_pattern2)

smiley_canvas3 = DrawingCanvas()
smiley_pattern3 = [
    ['X', 'X', 'X', 'X', 'X'],
    ['X', '.', '.', '.', 'X'],
    ['X', '.', 'X', '.', 'X'],
    ['X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X']
]
smiley_canvas3.draw_shape(smiley_pattern3)

heart = EmojiClass("❤️", "heart", 0, [heart_canvas1, heart_canvas2, heart_canvas3])
star = EmojiClass("⭐", "star", 1, [star_canvas1, star_canvas2, star_canvas3])
smiley = EmojiClass("😊", "smiley", 2, [smiley_canvas1, smiley_canvas2, smiley_canvas3])