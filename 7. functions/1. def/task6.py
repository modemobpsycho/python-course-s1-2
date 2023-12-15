def print_initials(name, surname, middlename):
    print(f'{surname.title()} {name[0].upper()}.{middlename[0].upper()}.')


name = input()
surname = input()
middlename = input()

print_initials(name, surname, middlename)
