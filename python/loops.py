# num=int(input("enter a number:"))
# for i in range(1,num+1):
#     if num%i==0:
#         print(i, "number is a factor" ) 

# for i in range(1,101):
#     if i%2==0:
#         print(i,"is a even number")
#     else:
#         print(i,"is a odd number")

# number=int(input("enter a number"))
# count=0
# for i in range(1,number+1):
#     if number%i==0:
#         count+=1
# if count==2:
#    print(number,"prime number" )
# else:
#     print(number,"not prime number")

# for i in range(2,101):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         print(i,"is a prime number ")

# number1=int(input("enter a first number"))
# number2=int(input("enter second number"))
# sum=number1+number2
# print("sum is:",number1+number2)


# n=int(input("enter a number"))
# total=0
# for i in range(1,n+1):
#     total+=i
# print("sum of number from 1 to",n,"is:", total)

# n=int(input("enter a number"))
# total=0
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if j==i:
#             total+=j
# print("sum of number from 1 to",n,"is:", total)

for i in range(1,4):
    for j in range(1,4):
        print(i,'-',j, end=',')
    print(' ')

      
for i in range(1,6):
    for j in range(1,6):
        print("*",end='')
    print('')
    
for i in range(1,6):
    for j in range(1,6):
        if i<=j:
          print("*",end='')
    print('')

for i in range(1,6):
    for j in range(1,6):
        if i>=j:
          print("*",end='')
    print('')
            


