import click
import datetime

# @click.command
users = []
user_credentials = {"user_name":'', "password":''}
logged_in = []

comments = []
comment = {"id":'',"msg":'', 'timestamp':'', 'author':''}

def edit_comment():
    for user in logged_in:
        logged_in_user = user['user_name']
    comment_to_edit = int(input('Enter the comment you want to edit:'))
    for comment in comments:
        if comment_to_edit == comment['id']:
            edit_msg = input('Enter new comment:')
            comment.update({"msg":edit_msg, 'timestamp':datetime.datetime.now()})
            comments.append(comment)
            print(comment)
            return comments
    return ('Comment not found')

def create_comment():
    for user in logged_in:
        logged_in_user = user['user_name']
    msg = input('Enter a comment:')
    comment.update({"id":len(comments)+1, "msg":msg, 'timestamp':datetime.datetime.now(), 'author':logged_in_user})
    comments.append(comment)
    print(comment)
    print('If you want to edit, select 1')
    print('Press: 1 to edit')
    print('Press: 2 to exit')
    option = int(input("Select an action: "))
    if option == 1:
        edit_comment()
    if option == 2:
        print('Okay bye')
    return comments



def choose_option():
    print("Press: 1 for Create")
    print("       2 for Edit")
    
    option = int(input("Select an action: "))
    if option == 1:
        create_comment()
    elif option == 2:
        edit_comment()
    else:
        print("Please choose an option from the list")
    
def login_user():
    user_name = input('Enter your user name then password to login:')
    user_password = input('Password:')
    for user in users:
        if user_name == user['user_name'] and user_password == user['password']:
            print(f"You have successfully been logged in as {user_name}")
            logged_in.append({"user_name":user_name})
            return choose_option()
        print('Invalid user name or login, Try again')

def signup():
    user_name = input('Enter a user name:')
    user_password = input('Enter a password:')
    user_credentials.update({"user_name":user_name, "password":user_password})
    users.append(user_credentials)
    print(users)
    return login_user()





if __name__ == "__main__":
    signup()

