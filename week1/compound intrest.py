p=int(input("enter amounts:"))
r=int(input("enter rate of intrest:"))
t=int(input("enter time period:"))
a=p*(1+r/100)**t
ci=a-p
print("the compound intrest is",round(ci,2))
