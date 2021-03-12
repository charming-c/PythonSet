flag = 1
while flag == 1:
    grade = int(input("please input the grade:"))
    if grade < 0 or grade >100:
        print("the grade in invalide")
    elif grade >= 90 and grade <= 100:
        print("the level of the grade:  A")
    elif grade > 70 and grade < 90:
        print("the level of the grade:  B")
    elif grade >= 60 and grade < 70:
        print("the level of the grade:  C")
    else:
        print("the level of the grade:  D")
    flag = int(input("do you want continue? 1-yes,0-no\n"))