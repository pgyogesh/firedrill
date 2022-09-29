from exercises import exercise_1
from exercises import exercise_2
import random

listOfExercises = [exercise_2, exercise_5, exercise_3, exercise_4]

def callRandomExercise():
    random.choice(listOfExercises)()

if __name__ == "__main__":
    callRandomExercise()