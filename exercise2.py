print("This program checks if an e-mail is valid or not.")
def is_valid():
    mail = None
    while mail == None:
        mail = input("Please enter an e-mail: ")
        if "@" not in mail and "." not in mail:
          print("Please enter a valid e-mail, This one doesn't have any '@' and '.' signs in it")
          mail = None
        elif "@" in mail and "." not in mail:
          print("Please enter a valid e-mail, This one doesn't have any '.' signs in it")
          mail = None
        elif "@" not in mail and "." in mail:
          print("Please enter a valid e-mail, This one doesn't have any '@' signs in it")
          mail = None
        else:
          print("That's a valid e-mail, Thanks!")
is_valid()