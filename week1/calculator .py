a=int(input("Enter the value of a:\n"))
b=int(input("Enter the value of b:\n"))
ans=input("choose the operator")
if(ans=="+"):
    print(a+b)
elif(ans=="-"):
    if(a>b):
        print(a-b)
    print(a-b)
elif(ans=="*"):
    print(a*b)
elif(ans=="/"):
    if(b==0):
        print("Take another value of b\nDenominator cannot be zero")
    print(a/b)
else:
    print("Choose the Valid Operator !")
