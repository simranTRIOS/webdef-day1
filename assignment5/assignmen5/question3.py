def main():
    department=2 
    sum_salary=0
    employer=int(input("please the number user want:"))
    salary=[[],[]]
    avarage=0
    dept_name=['manufacture','selling']
    for i in range(department):
        for j in range(employer):
            list=int(input("enter the salary of the employer: " ))
            salary[i].append(list)
        sum_salary= sum(salary[i])
        avarage = sum_salary/employer
        print("the avarage salary for",dept_name[i],"is :" ,format(avarge,'.2f'))
        salary[i].sort()
        print("the salary of second richest person in", dept_name[i],"department is :", salary[i][-2])
    for i in salary[0]:
        if i in salary[1]:
            print("common salary is:",i)
        else:
            break
main()


