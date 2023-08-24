ACCOUNTS = {"Ahmed":"1394","Ali":"6078","Amr":"9345"}

usr_name = input("User Name: ")
psswrd = input("Password: ")

if usr_name in ACCOUNTS.keys() and psswrd==ACCOUNTS[usr_name]:
    print("Signed in")
else:
    print("Wrong Username or Passowrd")    