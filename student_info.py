class StudentInfo:
    def __init__(self, first_name, age, quiz_score):
        self.first_name = first_name
        self.age = age
        self.quiz_score = quiz_score
        self.status = None

    def evaluate_performance(self):
        if self.quiz_score is None:
            self.status = None
        elif self.quiz_score >= PASSING_SCORE:
            self.status = True
        else:
            self.status = False

    def display_info(self, label):
        print("=" * 30)
        print(f"{label}")
        print("-" * 30)
        print(f"Student Name: {self.first_name}")
        print(f"Age: {self.age}")
        print(f"Quiz Score: {self.quiz_score}")
        print(f"Passed: {self.status}")
        print("=" * 30)

# Constants
PASSING_SCORE = 7

# Defining student information
first_name = "Eugene"
age = 21
quiz_score = None  # Student has not taken the quiz initially

# Creating a student object
student = StudentInfo(first_name, age, quiz_score)
student.evaluate_performance()
student.display_info("Initial State")

# Updating quiz score to an integer value
quiz_score = 10  # Student took the quiz and scored 10
student.quiz_score = quiz_score
student.evaluate_performance()
student.display_info("After Taking Quiz (Integer Score)")

# Rebinding quiz score to a float
quiz_score = 9.5  # Changing type during runtime
student.quiz_score = quiz_score
student.evaluate_performance()
student.display_info("After Updating Quiz Score (Float)")
