from execises import *
import random

listOfExercises = [exercise_1, exercise_2]

def callRandomExercise():
    random.choice(listOfExercises)()

if __name__ == "__main__":
    callRandomExercise()