"""
Name: Christoper Marquart

Date: 23 March 2022

Purpose: To emulate a real-life ATM banking system in Python.
"""


# Function for logging off a user
def logoff():
    print("    Thank you for using Pioneer Banking™!")
    quit()


# Function for booting off a user
def bootoff():
    print("    Too many failed attempts. Try again later.")
    quit()


# The prompt which follows each successful transaction
def do_next():
    print(do_next_prompt)
    t_choice = input(">> ")

    # input validation
    t_options = ["m", "l"]
    while t_choice not in t_options:
        print("    Please select a valid choice.")
        t_choice = input(">> ")
    if t_choice == "l":
        logoff()


welcome_prompt = """    Welcome! Please select an account action:

    (c) Check Balance
    (d) Deposit
    (w) Withdraw
    (l) Logoff"""

selection_prompt = """    Please select an account: 

    (c) Checking
    (s) Savings
    (x) Cancel"""

deposit_prompt = """
    (c) Cash deposit
    (h) Check deposit
    (x) Cancel"""

do_next_prompt = """    
    What would you like to do next?
    
    (m) Make another transaction
    (l) Logoff"""

# The valid options when selecting an account
acct_options = ["c", "s", "x"]

# Initial Account Balances
ch_bal = 1000  # checking
sav_bal = 1000  # savings
maximum_withdraw = 300

# Prompt user for initial PIN
print("    Welcome! Please create a four-digit PIN.")
init_pin = (input(">> "))
pin_num = init_pin.isdigit()

# Checks that initial PIN is correctly formatted
while not pin_num or len(init_pin) != 4:
    print("    Please enter a valid PIN.")
    init_pin = (input(">> "))
    pin_num = init_pin.isdigit()

# Confirm your PIN
print("    Please re-enter your PIN.")
conf_pin = (input(">> "))
pin_num = conf_pin.isdigit()

# Checks that confirmation PIN is correctly formatted
while not pin_num or len(init_pin) != 4:
    print("    Please enter a valid PIN.")
    conf_pin = (input(">> "))
    pin_num = conf_pin.isdigit()

# Checks that confirmation PIN matches initial PIN
while conf_pin and init_pin != conf_pin:
    print("    Incorrect PIN. Please try again.")
    conf_pin = input(">> ")  # confirm PIN

# Creates permanent PIN
user_pin = conf_pin
print("    PIN creation successful. You may now login. \n")

# The "main method"
while True:

    # Prompt user to Login
    attempts = 1
    print("    Enter your PIN: ")
    att_pin = input(">> ")

    # Boots off user if too many attempts have been tried
    while att_pin != user_pin:
        print("    Invalid PIN. Try again.")
        att_pin = input(">> ")
        attempts += 1
        if att_pin == user_pin:
            break
        if attempts == 3:
            bootoff()

    # Prompt user to specify account action once authenticated
    print(welcome_prompt)
    user_choice = input(">> ")
    welcome_options = ["c", "d", "w", "l"]

    # input validation for welcome screen
    while user_choice not in welcome_options:
        print("    Please select a valid choice.")
        user_choice = input(">> ")

    # Check balance
    if user_choice == "c":
        print(selection_prompt)
        user_choice = input(">> ")

        # input validation for account selection screen
        while user_choice not in acct_options:
            print("    Please select a valid choice.")
            user_choice = input(">> ")

        # Checks Checking Balance
        if user_choice == "c":
            formatted_bal = format(ch_bal, ",.2f")
            print(f"    Current balance: ${formatted_bal}")
            do_next()

        # Checks Savings Balance
        elif user_choice == "s":
            formatted_bal = format(sav_bal, ",.2f")
            print(f"    Current balance: ${formatted_bal}")
            do_next()

        # Cancel transaction
        elif user_choice == "x":
            continue

    # Deposit
    elif user_choice == "d":
        print(selection_prompt)
        user_choice = input(">> ")

        # input validation for account selection screen
        while user_choice not in acct_options:
            print("    Please select a valid choice.")
            user_choice = input(">> ")

        # Deposit in Checking
        if user_choice == "c":

            # Display current balance and prompt user for desired amount
            formatted_bal = format(ch_bal, ",.2f")
            print(f"    Current balance: ${formatted_bal}")
            print("    Enter amount to deposit: ")

            while True:
                try:
                    amt = float(input(">> $"))
                    if 10000 >= amt > 0:
                        ch_bal += amt
                        ch_bal = round(ch_bal, 2)
                        formatted_bal = format(ch_bal, ",.2f")
                        print(f"    New balance: ${formatted_bal}")
                        break
                    elif amt > 10000:
                        print("    Transaction denied. Please visit an in-person teller to complete transaction.")
                        break
                    else:
                        raise ValueError

                # Exception handling for deposit function
                except ValueError:
                    print("    Please enter a valid amount.")
                    continue
            do_next()

        # Deposit in Savings
        elif user_choice == "s":

            # Display current balance and prompt user for desired amount
            formatted_bal = format(sav_bal, ",.2f")
            print(f"    Current balance: ${formatted_bal}")
            print("    Enter amount to deposit: ")

            while True:
                try:
                    amt = float(input(">> $"))
                    if 10000 >= amt > 0:
                        sav_bal += amt
                        sav_bal = round(sav_bal, 2)
                        formatted_bal = format(sav_bal, ",.2f")
                        print(f"    New balance: ${formatted_bal}")
                        break
                    elif amt > 10000:
                        print("    Transaction denied. Please visit an in-person teller to complete transaction.")
                        break
                    else:
                        raise ValueError

                # Exception handling for deposit function
                except ValueError:
                    print("    Please enter a valid amount.")
                    continue
            do_next()

        # Cancel transaction
        elif user_choice == "x":
            continue

    # Withdraw
    elif user_choice == "w":
        print(selection_prompt)
        user_choice = input(">> ")

        # input validation for account selection screen
        while user_choice not in acct_options:
            print("    Please select a valid choice.")
            user_choice = input(">> ")

        # Withdraw from Checking
        if user_choice == "c":

            # Display current balance and prompt user for desired amount
            formatted_bal = format(ch_bal, ",.2f")
            print(f"    Current balance: ${formatted_bal}")
            print("    Enter amount to withdraw: ")

            # Determine whether amount should be withdrawn or rejected
            while True:
                try:
                    amt = float(input(">> $"))
                    if maximum_withdraw >= amt > 0:
                        if ch_bal >= amt:
                            ch_bal -= amt
                            ch_bal = round(ch_bal, 2)
                            formatted_bal = format(ch_bal, ",.2f")
                            print(f"    New balance: ${formatted_bal}")
                            break
                        else:
                            print("    Non-Sufficient Funds")
                            break
                    elif amt > maximum_withdraw:
                        print("    Transaction denied. Maximum daily withdraw is $300.00.")
                        break
                    else:
                        raise ValueError

                # Exception handling for withdraw function
                except ValueError:
                    print("    Please enter a valid amount.")
                    continue
            do_next()

        # Withdraw from Savings
        elif user_choice == "s":

            # Display current balance and prompt user for desired amount
            formatted_bal = format(sav_bal, ",.2f")
            print(f"    Current balance: ${formatted_bal}")
            print("    Enter amount to withdraw: ")

            # Determine whether amount should be withdrawn or rejected
            while True:
                try:
                    amt = float(input(">> $"))
                    if maximum_withdraw >= amt > 0:
                        if amt <= sav_bal:
                            sav_bal -= amt
                            sav_bal = round(sav_bal, 2)
                            formatted_bal = format(sav_bal, ",.2f")
                            print(f"    New balance: ${formatted_bal}")
                            break
                        else:
                            print("    Non-Sufficient Funds")
                            break
                    elif amt > maximum_withdraw:
                        print("    Transaction denied. Maximum daily withdraw is $300.00.")
                        break
                    else:
                        raise ValueError

                # Exception handling for withdraw function
                except ValueError:
                    print("    Please enter a valid amount.")
                    continue
            do_next()

        # Cancel transaction
        elif user_choice == "x":
            continue

    # Logoff
    elif user_choice == "l":
        logoff()

    continue
