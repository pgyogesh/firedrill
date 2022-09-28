from exercises import exercise_1
from exercises import exercise_2


listOfExercises = [exercise_1, exercise_2]

def callRandomExercise():
    import random
    random.choice(listOfExercises)()

if __name__ == "__main__":
    callRandomExercise()