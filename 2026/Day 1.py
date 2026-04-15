# Today ill learn new stuff from python, using my own knowledge.
# Now i will create a fully working password checker.

import time

# Variables


isvalid = False
minlength = 6
valid_users = ["Max", "Timothy", "Kevin"]
Creator = "Deyhan"

# Create user or check for user
while True:
  user_name = str(input("User Name: "))

  if user_name in valid_users:
    print(f"User '{user_name}' already exists, login with password following.")
    login_user = str(input("Log in?"))
    
    if login_user.strip().capitalize() == "Yes":
        time.sleep
        print("Initializing ")
      # I will continue this tomrrow
