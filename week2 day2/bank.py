balance = 50000

try:
    amount = int(input("Enter withdrawal amount: "))
    
    if amount > balance:
        raise ValueError("Insufficient balance!")
    
    balance -= amount
    print(f"Withdrawal successful. Remaining balance: ₹{balance}")
except ValueError as e:
    print("Error:", e)
