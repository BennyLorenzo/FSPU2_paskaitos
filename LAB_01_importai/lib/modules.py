users = [["test1","test1"], ["test2","test2"], ["test3","test3"]]

def login(users):
    tries = 3
    user_list = [username for username, password in users]
    username_input = input("Enter your username: ")
    if username_input in user_list:
        username_index = user_list.index(username_input)
        required_password = users[username_index][1]
        while True:
            password_input = input("Enter your password: ")
            if password_input == required_password:
                print("You have successfully logged in!")
                break
            else:
                tries -= 1
                if tries == 0:
                    print("You have tried too many times. Try again later.")
                    break
                print(f"Wrong password, try again. Tries left: {tries}")
    else:
        print("Such user does not exist.")

if __name__ == '__main__':
    login(users)