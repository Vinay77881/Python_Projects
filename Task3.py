def validator(email):
    if '@' in email and '.' in email:
        local_part, domain = email.split('@', 1)
        if '.' in domain and local_part and domain.split('.')[0]:
            print("Valid email")
        else:
            print("Not a valid email")
    else:
        print("Not a valid email")
user_input = input("Enter the mail id: ")
validator(user_input)