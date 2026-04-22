from operator import index


class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, score):
        score = self.get_by_index(index)
        if score > 90:
            return "A"
        elif score > 80:
            return "B"
        elif score > 70:
            return "C"
        elif score > 60:
            return "D"
        elif score >= 50:
            return "E"
        elif score >= 0:
            return "F"



if __name__ == "__main__":
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print(results.count())  # 9
    print(results.get_by_index(2))  # 91
    print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]
    print(results.get_grade(3))