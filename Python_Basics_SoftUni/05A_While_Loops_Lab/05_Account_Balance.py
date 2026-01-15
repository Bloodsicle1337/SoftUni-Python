bank_account = 0
addition_sum = ""
while True:
    addition_sum = input()

    if addition_sum != "NoMoreMoney":
        addition_sum = float(addition_sum)
        if addition_sum >= 0:
            bank_account += addition_sum
            print(f"Increase: {addition_sum:.2f}")
        else:
            print("Invalid operation!")
            print(f"Total: {bank_account:.2f}")
            break
    else:
        print(f"Total: {bank_account:.2f}")
        break



