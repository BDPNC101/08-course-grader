def course_grader(param):
    test_scores = param
    average = sum(test_scores)/len(test_scores)
    if average >= 70 and all(i >= 50 for i in test_scores):
        return "pass"
    else:
        return "fail"
