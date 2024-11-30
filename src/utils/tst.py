from validate_email import validate_email

x = validate_email('1@gmail.com', check_mx=True)
print(x)