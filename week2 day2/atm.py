crt_pin = "1125"  
attempts = 3

for i in range(attempts):
    pin = input("Enter your PIN: ")
    
    if pin == crt_pin:
        print("PIN accepted. Access granted.")
        break
    else:
        print("Incorrect PIN.")
        if i < attempts - 1:
            print(f"You have {attempts - i - 1} attempts left.\n")
        else:
            print("No attempts left. Access denied.")
