from mongo_connection import *
from mongo_skeleton.data_schema import *

mongo_connect()

# def buttonClick():
#     messagebox.showinfo(title="Greetings", message="AUS LISTE AUSLESEN!")
#     # window.destroy()
#     window = HAUPTMENUE.HauptMenue()
#
#     HAUPTMENUE.HauptMenue()
#
#
# username = input('Username: ')
# password = input('Password: ')
#
# userpassword = User.objects(user_name = username).scalar('user_password')
#
# if password == userpassword[0]:
#     print(userpassword[0])
# else:
#    print('Wrong')



y = '0001092021'
x = Kunde.objects(kunde_nr=y).count()
z = Kunde.objects(kunde_nr=y).scalar('kunde_nr')
if x >= 1:
    #print(z[0])
    pass
elif x < 1:
    print('Nummer existerit nicht')


# if x >= 1:
#     print(x[0])
# else:
#     print('no')