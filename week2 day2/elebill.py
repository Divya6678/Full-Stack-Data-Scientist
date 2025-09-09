try:
    a = int(input("Enter number of units: "))
    
    if a < 0:
        raise ValueError("Units cannot be negative!")
    if a <= 100:
        bill = a * 5
    elif a <= 200:
        bill = (100 * 5) + (a - 100) * 7
    else:
        bill = (100 * 5) + (100 * 7) + (a - 200) * 10

    print("Total bill is ₹", bill)

except ValueError as e:
    print("Invalid input:", e)

finally:
    print("Bill processing finished.")
