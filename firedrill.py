from inspect import getmembers, isfunction
import sys
from exercises import *
import random

# Get list of all exercises
listOfExercises = []
for function in getmembers(sys.modules[__name__]):
    if isfunction(function[1]) and function[0].startswith('exercise_'):
        listOfExercises.append(function[0])

# Pick a random exercise
def callRandomExercise():
    exercise = random.choice(listOfExercises)
    eval(exercise + "()")
if __name__ == "__main__":
    # Call the random exercise
    callRandomExercise()