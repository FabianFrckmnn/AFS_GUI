from HAUPTMENUE import *
from mongo_connection import *
from mongo_skeleton.data_schema import *

mongo_connect()

def buttonClick():
    messagebox.showinfo(title="Greetings", message="AUS LISTE AUSLESEN!")
    # window.destroy()
    window = HAUPTMENUE.HauptMenue()

    HAUPTMENUE.HauptMenue()


username = input('Username: ')
password = input('Password: ')

userpassword = User.objects(user_name = username).scalar('user_password')

if password == userpassword[0]:
    print(userpassword[0])
else:
    print('Wrong')