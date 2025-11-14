#

students = {
    "Pleasant" : (85, 70),
    "Drake" : (20, 70),
    "Josh" : (30, 63)
}

# create an empty dictionary
average_score = {}

# loop through the student dict to get students name and value
for student, score in students.items():

    # calculate average score and create an item with the students name as key and average score as value
    average_score[student] = sum(score) / len(score)

# get the student with the highest average score
highest_avg = max(average_score, key=average_score.get)

# print the name of the student with the highest score
print(f"Student with highest score {average_score[highest_avg]} is {highest_avg}")



