import datetime

now = datetime.datetime.now()

import random

database = {1234567890: ['Tyrion', 'Lannister', 'tyrion@zuri.team', 'poseidon'],
            2435465768: ['Tywin', 'Lannister', 'tywin@zuri.team', 'castlerock'],
            3546576879: ['Eddard', 'Stark', 'winterfell@zuri.team', 'winterfell'],
            1111112222: ['Theone', 'Greyjoy', 'theone@zuri.team', 'ironisland'],
            5555566666: ['Ramsey', 'Bolton', 'ramsey@zuri.team', 'impaler'],
            6666688888: ['Manns', 'Raydar', 'wildlings@zuri.team', 'beyondwall'],
            3333311111: ['Cleagor', 'Clegane', 'mountain@zuri.team', 'themountain'],
            4424435410: ['Daenerys', 'Targaryen', 'khaleesi@zuri.team', 'drakaris'],
            1992202105: ['Jon', 'Snow', 'jon@zuri.team', 'youknownothing']}


def init():
    print('***** Welcome to The Iron Bank of Braavos *****'.upper())

    haveAccount = int(input('Do you have an account with us? 1 (yes) 2 (no) \n'))

    if haveAccount == 1:
        login()
    elif haveAccount == 2:
        print(register())
    else:
        print('You have selected an invalid option')
        init()


def login():
    print('*******  LOGIN PORTAL ******* \n')

    print('Please, Enter The Appropriate Details')

    account_number_from_user = int(input('Enter Your Account Number: \n'))
    password = (input('Enter Your Password: \n'))

    for account_number, user_details in database.items():
        if account_number == account_number_from_user:
            if user_details[3] == password:
                bankOperation(user_details)

    print('Invalid Account or Password')
    login()


def register():
    print('******** REGISTRATION PORTAL ********')

    print('To Register Your Account With Us, Please, Follow The Instructions Below: \n')

    first_name = input(" Enter Your First Name Here : \n")
    last_name = input(" Enter Your last Name Here : \n")
    password = input('Create Your Preferred Password Here: \n')
    email = input('Enter Your Email Here: \n')

    account_number = generationAccountNumber()
    database[account_number] = [first_name, last_name, email, password]

    print('***** CONGRATULATIONS! ACCOUNT CREATION SUCCESSFUL *****')

    print(f'Your Account Number is {account_number}')
    print('Ensure You Keep It Safe')

    is_selected_request_valid = False

    while is_selected_request_valid == False:

        selected_request = int(input('Would You Like To (1) Continue or (2) Exit ?  \n'))

        if selected_request == 1:
            is_selected_request_valid = True
            login()
        elif selected_request == 2:
            is_selected_request_valid = True
            print('Thanks For Banking With Us! ')
            exit()

        else:
            print('Invalid Operation Command')


def bankOperation(user):
    print('Date/Time: ' + now.strftime("%y-%m-%d %H:%M:%S"))

    print('Welcome {} {}'.format(user[0], user[1]))

    selected_option = int(
        input('What Would You Like To Do? (1) Deposit (2) Withdrawal (3) Logout (4) Complaints (5) Exit   \n'))

    if selected_option == 1:

        deposit_operation()
    elif selected_option == 2:

        withdrawal_operation()
    elif selected_option == 3:

        login()
    elif selected_option == 4:
        complaint()

    elif selected_option == 5:
        print('Thank You For Banking With Us. You May Take Your Card')
        exit()

    else:
        print('Invalid Option Selected')


def deposit_operation():
    print('***** DEPOSIT PORTAL *****')

    cash_deposited = int(input('Kindly Input The Preferred Deposit Amount Here: \n'))
    current_balance = 200000
    print('Kindly Note That Your current balance is {}'.format(cash_deposited + current_balance))

    is_selected_request_valid = False

    while is_selected_request_valid == False:

        selected_request = int(input('Would You Like To (1) Continue or (2) Exit ?  \n'))

        if selected_request == 1:
            is_selected_request_valid = True
            login()
        elif selected_request == 2:
            is_selected_request_valid = True
            print('Thanks For Banking With Us! ')
            exit()
        else:
            print('You Entered An Invalid Option')


def withdrawal_operation():
    print('***** WITHDRAWAL PORTAL ******')

    is_withdraw_amount_valid = False

    while is_withdraw_amount_valid == False:

        withdraw_amount = int(input('Enter Amount To Be Withdrawn: \n'))
        current_balance = 200000

        if withdraw_amount > current_balance:
            print('Insufficient Funds')
        elif withdraw_amount < current_balance:
            print('Your Account Balance Is {}'.format(current_balance - withdraw_amount))
            print('Kindly Take Your Cash.')
            break

    is_selected_request_valid = False

    while is_selected_request_valid == False:

        selected_request = int(input('Would You Like To (1) Continue or (2) Exit ?  \n'))

        if selected_request == 1:
            is_selected_request_valid = True
            login()
        elif selected_request == 2:
            is_selected_request_valid = True
            print('Thanks For Banking With Us! ')
            exit()
        else:
            print('You Entered An Invalid Option')


def complaint():
    print('***** COMPLAINT PORTAL *****')

    complaint_detail = input(' Kindly Enter Your Complaint Here: \n')
    print('Your Complaint Have Been Duly Documented And Sent To The Customer Care Department \n')
    print('We Shall Get In Touch With You Shortly.')

    is_selected_request_valid = False

    while is_selected_request_valid == False:

        selected_request = int(input('Would You Like To (1) Continue or (2) Exit ?  \n'))

        if selected_request == 1:
            is_selected_request_valid = True
            login()
        elif selected_request == 2:
            is_selected_request_valid = True
            print('Thanks For Banking With Us! ')
            exit()
        else:
            print('You Entered An Invalid Option')


def generationAccountNumber():
    return random.randrange(1111111111, 9999999999)


init()

