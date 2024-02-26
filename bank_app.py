import sys

from account import Account
from account import Statement

# print(dir(Account))
pin = '1234'
# instantiation
# this is when we create objects based on classes

lisa_account = Account(100, 'Lisa', 'Simpson')
# print(lisa_account)
for attempts in range(1, 4):
    lisa_pin = lisa_account.get_pin()
    outcome = lisa_account.verify_pin(attempts)
    print(outcome)
    if outcome in 'Welcome how can I help?':
        lisa_initial_balance = lisa_account.getbalance()
        print(f"Lisa's balance is ${lisa_initial_balance}")
# add some cash to Lisa's account
# OOP notation: object.method()
        lisa_deposit = lisa_account.deposit()
        lisa_new_balance = lisa_account.getbalance()
        print(f"Lisa's new balance is ${lisa_new_balance}")
# accesses field directly because public
        firstname = lisa_account.first_name
        print(firstname)
# doesnt work because private
# lastname = lisa_account.lastname

# public method to access code
        lastname = lisa_account.get_last_name()
        print(lastname)

        new_last_name = lisa_account.set_lastname("Van Houten")
        print(f"Lisa's old last name was {lastname} and her new lastname is {new_last_name}")
        answer = input('Would you like a statement?')
        if answer in 'yes':
            statement_print = Statement(lisa_deposit, lisa_new_balance)
            # statement = open('lisastatement.txt', 'w')
            # write_report(statement, firstname, new_last_name, lisa_initial_balance, lisa_deposit, lisa_new_balance)
            print('Please take your statement')
            sys.exit()
        else:
            print('Thank you! Have a nice day!')

#  instantiate account for bart simpson and experiment with it

bart_account = Account(5, 'Bart', 'Simpson')
bart_account.withdraw(20)
bart_balance = bart_account.getbalance()
print(f"Bart's new balance is ${bart_balance}")

bart_account.withdraw(-5000)
print(bart_account)

bart_account.set_firstname('El Barto')
print(f"Bart's nickname is {bart_account.get_firstname()}")

