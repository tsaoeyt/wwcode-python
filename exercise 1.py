total_bill = 0
total_money = 0


total_bill = input('how much is your total bill?')
total_money = input('how much is your total payment?')
change = 0
change = int(total_money) - int(total_bill)
print ("Hi! Your change is ",change)