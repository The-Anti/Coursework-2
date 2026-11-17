def get_performer_amount(amount):
    try:
        int(amount)
    except ValueError:
        return "invalid"

    if int(amount) <= 0:
        return "invalid"
    
    else:
        return "valid"

amount = input("Please input the amount of performers there will be: ")
while get_performer_amount(amount) == "invalid":
    amount = input("Please input the amount of performers there will be: ")

print("Success")