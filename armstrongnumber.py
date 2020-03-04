"""Python program to check Armstrong number
Armstrong number is a number that is equal to the sum of cubes of its digits.
For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.
"""
num=int(input("Enter a number you want to check"))
c=0
sum=0
temp=num
while(temp>0):
    c=c+1
    temp=temp//10                 #int divide
temp=num
while(temp>0):
    digit=temp%10
    sum=sum+(digit**c)
    temp = temp//10
if(sum==num):
    print(f"{num} is an armstrong number")
else:
    print("Number is not an armstrong number")