n=int(input("Enter no of students:"))
d={}
for i in range(n):
    k=input("Student name:")
    v=int(input("Attendance:"))
    d[k]=v
print("Defaulters(attendance<75%)")
for k,v in d.items():
    if v<75:
        print(k,":",v)

