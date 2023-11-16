list1 = [1,2,3,4,5,6,]
user_input = int (input("enter the number you wanna find : "))

for i in range(len(list1)) :
    if user_input==list1[i] :
        print( list1.index(list1[i]))