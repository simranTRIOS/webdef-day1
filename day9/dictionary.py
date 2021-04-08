def main():
    first_name ={'s111':'simranjit','s112':'singh'}
    last_name = {'s111':'lubana','s11':'saab'}
    course = {'s111':'computer program', 's112':'physical education'}
    compus = {'s111':'trios','s112':'college'}
    
    student_id = input("enter the id of student")

    if student_id not in first_name:
        print(student_id, "the student is register in college.invalid")

    else:
        print("the details of the student",student_id, "is as follow:")
        print("firstname of student",student_id,"is:",first_name[student_id])
        print("lastname of the student",student_id,"is",last_name[student_id])
        print("course of the student",student_id,"is",course[student_id])
        print("compus of the student",student_id,"is",compus[student_id])

main()