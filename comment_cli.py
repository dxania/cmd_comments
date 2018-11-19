import click
import datetime

# @click.command
users = []
user_credentials = {"user_name":'', "password":''}
logged_in = []

def create_comment():
    comments = []
    comment = {"msg":'', 'timestamp':'', 'author':''}
    for user in logged_in:
        logged_in_user = user['user_name']
    msg = input('Enter a comment:')
    comment.update({"msg":msg, 'timestamp':datetime.datetime.now(), 'author':logged_in_user})
    comments.append(comment)
    print(comment)
    return comments

def login_user():
    user_name = input('Enter your user name:')
    user_password = input('Enter your password:')
    for user in users:
        if user_name == user['user_name'] and user_password == user['password']:
            print(f"You have successfully been logged in as {user_name}")
            logged_in.append({"user_name":user_name})
            return create_comment()

def signup():
    user_name = input('Enter a user name:')
    user_password = input('Enter a password:')
    user_credentials.update({"user_name":user_name, "password":user_password})
    users.append(user_credentials)
    print(users)
    return login_user()



if __name__ == "__main__":
    signup()

