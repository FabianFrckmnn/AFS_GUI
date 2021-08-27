# ERÖFFNET EINE SEITE
from tkinter import *
import tkinter as TITELSEITE
import datetime
import BILDER
import HAUPTMENUE

def StartSeite():
    window = TITELSEITE.Tk()

    # SETZEN DER FENSTERGRÖßE
    window.geometry("1920x1080")
    window.configure(bg="#A9E2F3")
    # SETZT DEN FENSTERTITEL
    window.title("STARTSEITE")

    # ÜBERSCHRIFT HINZUFÜGEN
    titelseite_label = TITELSEITE.Label(window, text="DR. MOTTE SCHÄDLINGSBEKÄMPFUNG OFFICE-SOFTWARE",
                                        fg='#2F4F4F', bg='#2E9AFE',
                                        font=('times', 29, 'bold'), width=85, heigh=2)
    titelseite_label.place(x=0, y=0)

    # TITELBILD IMAGE EINFÜGEN

    startbild = TITELSEITE.PhotoImage(file=BILDER.startseiteimage)
    titelseite_startbild = Label(image=startbild)
    titelseite_startbild.image = startbild
    titelseite_startbild.place(x=760, y=260)

    # DATUM/UHRZEIT HINZUFÜGEN
    titelzeit_label = TITELSEITE.Label(window, text=datetime.datetime.now().strftime("%d.%m.%Y     %H:%M"),
                                       fg='#2F4F4F', bg='#2E9AFE',
                                       font=('times', 25, 'bold'), width=96, heigh=2)
    titelzeit_label.place(x=0, y=60)
    window.after(10*50, window.quit)
    window.mainloop()

    # FORTSCHRITTSBALKEN STARTEN
    prozent = 14
    titelseite1_button = TITELSEITE.Button(window, text= str(prozent) + " %" ,font=('times', 10, 'bold'),
                                           fg='#0B0719', bg='#CEF6F5', width=40, heigh=3, relief=GROOVE)
    titelseite1_button.place(x=50, y=940)

    # FUNKTION1 HINZUFÜGEN
    funktion1_label = TITELSEITE.Label(window, text=" - KUNDENVERWALTUNG         ", fg='#2F4F4F', bg="#A9E2F3",
                                       font=('times', 25, 'bold'), width=30, heigh=2)
    funktion1_label.place(x=0, y=200)
    window.after(10*100, window.quit)
    window.mainloop()

    # FORTSCHRITTSBALKEN WEITER
    prozent = 28
    titelseite1_button = TITELSEITE.Button(window, text=str(prozent) + " %",
                                           font=('times', 10, 'bold'),
                                           fg='#0B0719', bg='#CEF6F5', width=80, heigh=3, relief=GROOVE)
    titelseite1_button.place(x=50, y=940)

    # FUNKTION2 HINZUFÜGEN
    funktion2_label = TITELSEITE.Label(window, text=" - BEHANDLUNGSNACHWEISE",
                                       fg='#2F4F4F', bg="#A9E2F3",
                                       font=('times', 25, 'bold'), width=30, heigh=2)
    funktion2_label.place(x=0, y=300)
    window.after(10*100, window.quit)
    window.mainloop()

    # FORTSCHRITTSBALKEN WEITER
    prozent = 42
    titelseite1_button = TITELSEITE.Button(window, text=str(prozent) + " %",
                                           font=('times', 10, 'bold'),
                                           fg='#0B0719', bg='#CEF6F5', width=120, heigh=3, relief=GROOVE)
    titelseite1_button.place(x=50, y=940)

    # FUNKTION3 HINZUFÜGEN
    funktion3_label = TITELSEITE.Label(window, text=" - RECHNUNGEN SCHREIBEN ", fg='#2F4F4F',bg="#A9E2F3",
                                       font=('times', 25, 'bold'), width=30, heigh=2)
    funktion3_label.place(x=0, y=400)
    window.after(10*100, window.quit)
    window.mainloop()

    # FORTSCHRITTSBALKEN WEITER
    prozent = 56
    titelseite1_button = TITELSEITE.Button(window, text=str(prozent) + " %" ,
                                           font=('times', 10, 'bold'),
                                           fg='#0B0719', bg='#CEF6F5', width=160, heigh=3, relief=GROOVE)
    titelseite1_button.place(x=50, y=940)

    # FUNKTION4 HINZUFÜGEN
    funktion4_label = TITELSEITE.Label(window, text=" - TERMINE ÜBERBLICKEN    ", fg='#2F4F4F',bg="#A9E2F3",
                                       font=('times', 25, 'bold'), width=30, heigh=2)
    funktion4_label.place(x=0, y=500)
    window.after(10*100, window.quit)
    window.mainloop()

    # FORTSCHRITTSBALKEN WEITER
    prozent = 70
    titelseite1_button = TITELSEITE.Button(window, text=str(prozent) + " %",
                                           font=('times', 10, 'bold'), fg='#0B0719',
                                           bg='#CEF6F5', width=200, heigh=3, relief=GROOVE)
    titelseite1_button.place(x=50, y=940)

    # FUNKTION5 HINZUFÜGEN
    funktion5_label = TITELSEITE.Label(window, text=" - ARBEITSPLÄNE DRUCKEN  ",
                                       fg='#2F4F4F',bg="#A9E2F3",
                                       font=('times', 25, 'bold'), width=30, heigh=2)
    funktion5_label.place(x=0, y=600)
    window.after(10*100, window.quit)
    window.mainloop()

    # FORTSCHRITTSBALKEN WEITER
    prozent = 100
    titelseite1_button = TITELSEITE.Button(window, text=str(prozent) + " %",
                                           font=('times', 10, 'bold'), fg='#0B0719',
                                           bg='#CEF6F5', width=258, heigh=3, relief=GROOVE)
    titelseite1_button.place(x=50, y=940)

    # FUNKTION6 HINZUFÜGEN
    funktion6_label = TITELSEITE.Label(window, text=" - ALLES VOLL INTEGRIERT  ",
                                       fg='#2F4F4F', bg="#A9E2F3",
                                       font=('times', 25, 'bold'), width=30, heigh=2)
    funktion6_label.place(x=0, y=700)

    #window.mainloop()

    # FUNKTION7 HINZUFÜGEN
    funktion7_label = TITELSEITE.Label(window, text=" - (C) 2021 FABIAN UND ANDRE FRICKMANN",
                                       fg='#2F4F4F', bg="#A9E2F3",
                                       font=('times', 25, 'bold'), width=38, heigh=2)
    funktion7_label.place(x=35, y=810)
    window.after(10 * 100, window.quit)
    window.mainloop()

    # FORTSCHRITTSBALKEN WEITER
    prozent = 100
    titelseite1_button = TITELSEITE.Button(window, text=str(prozent) + " %",
                                           font=('times', 10, 'bold'),
                                           fg='#0B0719', bg='#CEF6F5', width=258, heigh=3, relief=GROOVE)
    titelseite1_button.place(x=50, y=940)
    window.after(10*300, window.quit)
    window.destroy()
    window.mainloop()


StartSeite()
HAUPTMENUE.HauptMenue()