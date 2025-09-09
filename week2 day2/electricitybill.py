a=int(input("Enter no of units:"))
if a<=100:
    bill=a*5
    print("Total bill is",bill)
elif a<=200:
    bill=(100 * 5) + (a - 100) * 7
    print("Total bill is",bill)
elif a>200:
    bill=(100 * 5) + (100 * 7)+(a-200)*10
    print("Total bill is",bill)