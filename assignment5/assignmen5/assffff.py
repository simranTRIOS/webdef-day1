store_marks = 0
store_marks2 = 0
store_marks3 = 0
for i in range(0,3): # For students 
    print("\nPlease Enter the score of the student - "+str(i+1)+"\n")
    for j in range(0,1): # For marks in 3 subjects
        score1, score2, score3 = input("Enter marks of 3 subjects with space in between <Format- 10 20 30 >: ").split()
        store_marks[j+1] = int(score1)
        store_marks2[j+2] = int(score2)
        store_marks3[j+3] = int(score3)
    average[1] = average[1] + store_marks[j+1]/2 # Calculating average score of each subject and storing it in a dictionary
    average[2] = average[2] + store_marks[j+2]/2
    average[3] = average[3] + store_marks[j+3]/2
    if min_marks < min(store_marks.keys(), key=(lambda k: store_marks[k])):
        min_marks = min(store_marks.keys(), key=(lambda k: store_marks[k]))
    student_marks[i+1]= store_marks.copy() 
print(average)
print("The minimum average of marks is in subject - ", min(average.keys(), key=(lambda k: average[k]))) # Reference: https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-15.php
print("The maximum average of marks is in subject - ", max(average.keys(), key=(lambda k: average[k]))) # Reference: https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-15.php
print("The subject which has the minimum marks is subject - ", min_marks)