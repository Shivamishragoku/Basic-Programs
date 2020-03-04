
start=int(input("enter starting number"))
last=int(input("Enter the ending number"))

for i in range(start,last+1):
    flag = 0
    if i>1:
        for j in range(2,i):
            if (i%j)==0:
                flag=1
                break
        if(flag==0):
            print(i)