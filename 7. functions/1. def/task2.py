def check_password(password):
    upper = [i for i in password if i.isupper()]
    digit = [i for i in password if i.isdigit()]
    simb = [i for i in '!@#$%*' if i in password]
    if len(password) >= 10 and len(upper) > 0 and len(digit) > 2 and len(simb) >= 1:
        print('Perfect password')
    else:
        print('Easy peasy')
