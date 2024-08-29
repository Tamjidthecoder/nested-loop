range_1=int(input("enter the first range"))
range_2=int(input("enter second range"))
for num in range(range_1,range_2 + 1):
    if num > 1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)