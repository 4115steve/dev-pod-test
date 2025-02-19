#ask the user their current cash balance
current_cash_balance= 0
current_cash_balance += float(input("What's your current cash balance?   $"))

# loop that allows user to input more transactions
while True: 
  #print a new line so output is in sections
  print("\n")
  deposit_or_expense = input("Would you like to enter a deposit or an expence? (d/e) ") 
  # if user enters d then ask for deposit amount, date, and description
  if  deposit_or_expense == "d":
    deposit_amount = float(input("How much would you like to deposit?   $"))
    deposit_date = input("What was the date of this deposit?    ")
    deposit_description = input("Give a description of this deposit.   ")
    # add deposit to current_cash_balance
    current_cash_balance += deposit_amount
    #print  the current_cash_balance
    print("Your current cash balance is now = $" + str(current_cash_balance))
    #if user entersd then ask for expence amount, date, and description
  elif deposit_or_expense == "e":
    expense_amount = float (input("How much was the expense?   -$"))
    expense_date = input("What was the date of this expense?  ")
    expense_description = input("Give a description of this expense.  ")
    # subtract expense from current_cash_balance
    current_cash_balance -= expense_amount
    #print the current_cash_balance after expense_amount is subtracted
    print("Your current cash balance is now = $" + str(current_cash_balance))