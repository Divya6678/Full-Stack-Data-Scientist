n=int(input("Enter no of items:"))
d={}
for i in range(n):
    k=input("Item name:")
    v=int(input("price:"))
    d[k]=v
tot=sum(d.values())
print("Total Bill:",tot)