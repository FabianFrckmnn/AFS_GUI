# ERÖFFNET EINE SEITE
from tkinter import *
import tkinter as TITELSEITE
import datetime
import BILDER
#import HAUPTMENUE
from tkinter import messagebox
from mongo_connection import *
from mongo_skeleton.data_schema import *

mongo_connect()

def StartSeite():
    window = TITELSEITE.Tk()

    # SETZEN DER FENSTERGRÖßE

    window.geometry("1920x1080")
    window.configure(bg="#A9E2F3")

    # SETZT DEN FENSTERTITEL

    window.title("STARTSEITE")

    # ÜBERSCHRIFT HINZUFÜGEN

    titelseiteTitel_label = TITELSEITE.Label(window, text="DR. MOTTE SCHÄDLINGSBEKÄMPFUNG OFFICE-SOFTWARE", fg='#2F4F4F', bg='#2E9AFE', font=('times', 29, 'bold'), width=85, heigh=1)
    titelseiteTitel_label.grid(row=0, column=0, columnspan=3)

    # DATUM/UHRZEIT HINZUFÜGEN

    titelseiteZeit_label = TITELSEITE.Label(window, text=datetime.datetime.now().strftime("%d.%m.%Y     %H:%M"), fg='#2F4F4F', bg='#2E9AFE', font=('times', 25, 'bold'), width=98, heigh=1)
    titelseiteZeit_label.grid(row=1, column=0, columnspan=3)
    window.after(10 * 50, window.quit)
    window.mainloop()

    # TITELBILD IMAGE EINFÜGEN

    funktionleer_label = TITELSEITE.Label(window, text=" ", fg='#2F4F4F', bg="#A9E2F3", font=('times', 25, 'bold'), width=38, heigh=1)
    funktionleer_label.grid(row=2, column=1, padx='15', pady='0', sticky='nw', columnspan=2)

    funktionleer1_label = TITELSEITE.Label(window, text=" ", fg='#2F4F4F', bg="#A9E2F3", font=('times', 25, 'bold'), width=38, heigh=1)
    funktionleer1_label.grid(row=3, column=1, padx='15', pady='0', sticky='nw', columnspan=2)

    funktionleer2_label = TITELSEITE.Label(window, text=" ", fg='#2F4F4F', bg="#A9E2F3", font=('times', 25, 'bold'), width=38, heigh=1)
    funktionleer2_label.grid(row=4, column=1, padx='15', pady='0', sticky='nw', columnspan=2)

    funktionleer3_label = TITELSEITE.Label(window, text=" ", fg='#2F4F4F', bg="#A9E2F3", font=('times', 25, 'bold'), width=38, heigh=1)
    funktionleer3_label.grid(row=5, column=1, padx='15', pady='0', sticky='nw', columnspan=2)

    funktionleer4_label = TITELSEITE.Label(window, text=" ", fg='#2F4F4F', bg="#A9E2F3", font=('times', 25, 'bold'), width=38, heigh=1)
    funktionleer4_label.grid(row=6, column=1, padx='15', pady='0', sticky='nw', columnspan=2)

    funktionleer5_label = TITELSEITE.Label(window, text=" ", fg='#2F4F4F', bg="#A9E2F3", font=('times', 25, 'bold'), width=38, heigh=1)
    funktionleer5_label.grid(row=7, column=1, padx='15', pady='0', sticky='nw', columnspan=2)

    startbild = TITELSEITE.PhotoImage(file=BILDER.startseiteimage)
    titelseite_startbild = Label(image=startbild)
    titelseite_startbild.image = startbild
    titelseite_startbild.grid(row=3,column=1 ,rowspan=1,columnspan=2)

    auflistungUmrandung = TITELSEITE.Frame(window, width=200, heigh=1, bg="#A9E2F3", borderwidth=2, relief="flat")
    auflistungUmrandung.grid(row=2, column=0, padx='5', pady='5', sticky='nw',columnspan=6, rowspan=30)

    # FUNKTION1 HINZUFÜGEN

    funktionleer_label = TITELSEITE.Label(auflistungUmrandung, text=" ", fg='#2F4F4F', bg="#A9E2F3", font=('times', 25, 'bold'), width=38, heigh=1)
    funktionleer_label.grid(row=0, column=1, padx='15', pady='0', sticky='nw', columnspan=2)

    funktionleer1_label = TITELSEITE.Label(auflistungUmrandung, text=" ", fg='#2F4F4F', bg="#A9E2F3", font=('times', 25, 'bold'), width=38, heigh=1)
    funktionleer1_label.grid(row=1, column=1, padx='15', pady='0', sticky='nw', columnspan=2)

    funktionleer2_label = TITELSEITE.Label(auflistungUmrandung, text=" ", fg='#2F4F4F', bg="#A9E2F3", font=('times', 25, 'bold'), width=38, heigh=1)
    funktionleer2_label.grid(row=2, column=1, padx='15', pady='0', sticky='nw', columnspan=2)

    funktionleer3_label = TITELSEITE.Label(auflistungUmrandung, text=" ", fg='#2F4F4F', bg="#A9E2F3", font=('times', 25, 'bold'), width=38, heigh=1)
    funktionleer3_label.grid(row=3, column=1, padx='15', pady='0', sticky='nw', columnspan=2)

    funktion1_label = TITELSEITE.Label(auflistungUmrandung, text="- KUNDENVERWALTUNG", fg='#2F4F4F', bg="#A9E2F3", font=('times', 25, 'bold'), width=38, heigh=2)
    funktion1_label.grid(row=4, column=0,padx='15', pady='0', sticky='nw',columnspan=2)

    # FUNKTION2 HINZUFÜGEN

    funktion2_label = TITELSEITE.Label(auflistungUmrandung, text="- BEHANDLUNGSNACHWEISE", fg='#2F4F4F', bg="#A9E2F3", font=('times', 25, 'bold'), width=38, heigh=2)
    funktion2_label.grid(row=5, column=0,padx='15', pady='0', sticky='nw',columnspan=2)

    # FUNKTION3 HINZUFÜGEN

    funktion3_label = TITELSEITE.Label(auflistungUmrandung, text="- RECHNUNGEN SCHREIBEN", fg='#2F4F4F',bg="#A9E2F3", font=('times', 25, 'bold'), width=38, heigh=2)
    funktion3_label.grid(row=6, column=0,padx='15', pady='0', sticky='nw',columnspan=2)

    # FUNKTION4 HINZUFÜGEN

    funktion4_label = TITELSEITE.Label(auflistungUmrandung, text=" - TERMINE ÜBERBLICKEN", fg='#2F4F4F',bg="#A9E2F3", font=('times', 25, 'bold'), width=38, heigh=2)
    funktion4_label.grid(row=7, column=0, sticky='nw',columnspan=2)

    # FUNKTION5 HINZUFÜGEN

    funktion5_label = TITELSEITE.Label(auflistungUmrandung, text=" - ARBEITSPLÄNE DRUCKEN", fg='#2F4F4F',bg="#A9E2F3", font=('times', 25, 'bold'), width=38, heigh=2)
    funktion5_label.grid(row=8, column=0, sticky='nw',columnspan=2)

    # FUNKTION6 HINZUFÜGEN

    funktion6_label = TITELSEITE.Label(auflistungUmrandung, text=" - ALLES VOLL INTEGRIERT", fg='#2F4F4F', bg="#A9E2F3", font=('times', 25, 'bold'), width=38, heigh=2)
    funktion6_label.grid(row=9, column=0, sticky='nw',columnspan=2)

    # FUNKTION7 HINZUFÜGEN

    funktion7_label = TITELSEITE.Label(auflistungUmrandung, text=" - (C) 2021 FABIAN UND ANDRE FRICKMANN", fg='#2F4F4F', bg="#A9E2F3", font=('times', 25, 'bold'), width=38, heigh=4)
    funktion7_label.grid(row=10, column=0, sticky='nw',columnspan=2)

    loginUmrandung = TITELSEITE.Frame(window, width=250, heigh=50, bg='#A9E2F3', borderwidth=2, relief="groove")
    loginUmrandung.grid(row=6, column=2, padx='5', pady='5', sticky='nw' ,columnspan=4)
    einlockhinweis1_label = TITELSEITE.Label(loginUmrandung, text="Benutzername", fg='#2F4F4F', bg="#A9E2F3",  font=('times', 12, 'bold'), width=30, heigh=1)
    einlockhinweis1_label.grid(row=0, column=0, sticky='nw', columnspan=2)
    Benutzernametext = Entry(loginUmrandung, width=35)
    Benutzernametext.grid(row=1, column=1, padx='5', pady='1', sticky='nw')
    einlockhinweis1_label = TITELSEITE.Label(loginUmrandung, text=" ", fg='#2F4F4F', bg="#A9E2F3", font=('times', 12, 'bold'), width=30, heigh=1)
    einlockhinweis1_label.grid(row=2, column=0, sticky='nw', columnspan=2)
    einlockhinweis1_label = TITELSEITE.Label(loginUmrandung, text="Passwort", fg='#2F4F4F', bg="#A9E2F3", font=('times', 12, 'bold'), width=30, heigh=1)
    einlockhinweis1_label.grid(row=3, column=0, sticky='nw', columnspan=2)
    passworttext = Entry(loginUmrandung, width=35)#, show = '*')
    passworttext.grid(row=4, column=1, padx='5', pady='1', sticky='nw')

    def buttonClick():
        benutzer = Benutzernametext.get().strip()
        passwort=  passworttext.get().strip()
        username = User.objects(user_name=benutzer).scalar('user_name')
        userpassword = User.objects(user_password=passwort).scalar('user_password')
        if benutzer=="":
           messagebox.showinfo (title="Fehler", message="leeres Eingabefeld")
           pass
        elif benutzer == username[0] and passwort == userpassword[0]:
           window.destroy()
           import HAUPTMENUE
           #HAUPTMENUE.HauptMenue()
           pass
        else:
           pass

    passwortbutton =TITELSEITE.Button(loginUmrandung, text="       OK       ", bg="#A9E2F3", command=buttonClick)
    passwortbutton.grid(row=5, column=1, padx='80', pady='30', sticky='nw')

    window.mainloop()

StartSeite()
