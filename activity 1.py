String = input("please enter your word: ")
charecter =input("Please enter the charecter you want to find: ")
i = 0
count = 0
while(i<len(
    String)):
    if(String[i]==charecter):
        count=count+1
    i=i+1
print("The total number of times ",charecter,"has occured =", count)