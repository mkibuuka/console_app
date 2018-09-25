from core.helper_functions import user_signup_and_login
from core.helper_functions import user_login


# Console implementation function
def user_input():

    print('Welcome to your todo-list app')
    print('1.sign up')
    print('2.login')

    choice = int(input('select a choice from the above options:'))
    if choice == 1:
        user_signup_and_login()

    if choice == 2:
        user_login()


if __name__ == '__main__':
    user_input()
