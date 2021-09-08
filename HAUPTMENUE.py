# ERÖFFNET EINE SEITE
from mongo_connection import *
from mongo_skeleton.data_schema import *
import tkinter
from tkinter import *
from tkinter.ttk import *
import tkinter as HAUPTMENUE
import time
import datetime
import calendar
import BILDER
from tkinter import ttk
import tkinter.font as tkFont
from functools import partial
from tkinter import messagebox
from math import *
from mongoengine import *
from pynput.keyboard import Key, Controller
import logging


#Create and configure logger
logging.basicConfig(filename="new_log.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')


mongo_connect()


# ******************************************************************************************************************
# ******************************************************************************************************************
# ************************  EINSTELLUNGEN UND DEFINITION HAUPTMENUE ERSTELLEN   ************************************
# ******************************************************************************************************************
# ******************************************************************************************************************

def HauptMenue():
    window = HAUPTMENUE.Tk()

    #                                    SETZEN DER FENSTERGRÖßE

    window.geometry("1920x1080")
    window.configure(bg="#BDBDBD")

    textExample = HAUPTMENUE.Text(window, height=10)
    fontExample = tkFont.Font(family="Courier New", size=12)
    textExample.configure(font=fontExample)

    #                                    SETZT DEN FENSTERTITEL

    window.title("HAUPTMENUE KUNDENVERWALTUNG")

    #                                    DATUM/UHRZEIT HINZUFÜGEN

    DatumUhrzeitUmrandung = HAUPTMENUE.Frame(window, width=200, heigh=1, bg='#BDBDBD', borderwidth=2, relief="groove")
    DatumUhrzeitUmrandung.grid(row=7, column=0, padx='5', pady='0', sticky='nw', columnspan=11)
    datumuhrzeitwochentag = datetime.datetime.now().strftime("%A")
    if datumuhrzeitwochentag == "Monday":
        datumuhrzeitwochentag = "Montag"
    elif datumuhrzeitwochentag == "Tuesday":
        datumuhrzeitwochentag = "Dienstag"
    elif datumuhrzeitwochentag == "Wednesday":
        datumuhrzeitwochentag = "Mittwoch"
    elif datumuhrzeitwochentag == "Thursday":
        datumuhrzeitwochentag = "Donnerstag"
    elif datumuhrzeitwochentag == "Friday":
        datumuhrzeitwochentag = "Freitag"
    elif datumuhrzeitwochentag == "Saturday":
        datumuhrzeitwochentag = "Samstag"
    elif datumuhrzeitwochentag == "Sunday":
        datumuhrzeitwochentag = "Sonntag"
    pass

    window_datum_label = HAUPTMENUE.Label(DatumUhrzeitUmrandung,
                                          text=datumuhrzeitwochentag + " " + datetime.datetime.now().strftime(
                                              "%d.%m.%Y"), font=('Courier New', 16,), fg='#2F4F4F', bg='#BDBDBD',
                                          width=25, height=1, relief=GROOVE)
    window_datum_label.grid(row=0, column=0, padx='10', pady='1', sticky='ew')
    window_zeit_label = HAUPTMENUE.Label(DatumUhrzeitUmrandung, text=time.strftime("%H:%M:%S"),
                                         font=('Courier New', 16,), fg='#2F4F4F', bg='#BDBDBD', width=10, heigh=1,
                                         relief=GROOVE)
    window_zeit_label.grid(row=0, column=1, padx='10', pady='1', sticky='ew')
    datumuhrzeitkalenderwoche = datetime.date.today().isocalendar()[1]
    window_Kw_label = HAUPTMENUE.Label(DatumUhrzeitUmrandung, text="Kalenderwoche " + str(datumuhrzeitkalenderwoche),
                                       font=('Courier New', 16,), fg='#2F4F4F', bg='#BDBDBD', width=20, heigh=1,
                                       relief=GROOVE)
    window_Kw_label.grid(row=0, column=2, padx='10', pady='1', sticky='ew')
    # print (datetime.date(2021,12,24).isocalendar()[1]) zu datum KW auslesen
    window_Sachbearbeiter_label = HAUPTMENUE.Label(DatumUhrzeitUmrandung, text="Sachbearbeiter",
                                                   font=('Courier New', 16,), fg='#2F4F4F', bg='#BDBDBD', width=25,
                                                   heigh=1, relief=GROOVE)
    window_Sachbearbeiter_label.grid(row=0, column=3, padx='10', pady='1', sticky='ew')
    window_Sachbearbeiterleer_label = HAUPTMENUE.Label(DatumUhrzeitUmrandung, text="                          ",
                                                       font=('Courier New', 16,), fg='#2F4F4F', bg='#BDBDBD', width=50,
                                                       heigh=1, relief=FLAT)
    window_Sachbearbeiterleer_label.grid(row=0, column=4, padx='10', pady='1', sticky='ew')

    # window_vorgangOk = Entry(DatumUhrzeitUmrandung, font=('Courier New', 8,), fg='#2F4F4F', bg='#BDBDBD', width=7, heigh=1, relief=GROOVE)
    # zusatzAgeber = Entry(DatumUhrzeitUmrandung, width=35, textvariable=zusatzAgebervar, font=('Courier New', 12))
    # window_vorgangOk.grid(row=0, column=5, padx='10', pady='1', sticky='ew')

    def digital_clock():
        time_live = time.strftime("%H:%M:%S")
        window_zeit_label.config(text=time_live)
        window_zeit_label.after(200, digital_clock)

    digital_clock()

    def funcReturn(event):
        print("You hit return.")
        keyboard = Controller()
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
    window.bind('<Return>', funcReturn)

    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # ************************   BEREICH AUFTRAGGEBER TEXTFELDERERSTELLEN *********************************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************

    textauswertungvar = StringVar()
    kdnrvar = StringVar()
    kundennummerAgebervar = StringVar()
    nachnameAgebervar = StringVar()
    vornameAgebervar = StringVar()
    zusatzAgebervar = StringVar()
    strAgebervar = StringVar()
    hnrAgebervar = StringVar()
    plzAgebervar = StringVar()
    ortAgebervar = StringVar()
    ansprechAgebervar = StringVar()
    telAgebervar = StringVar()
    mailAgebervar = StringVar()
    vorgangOkvar = StringVar()
    vorgangOk = Entry(DatumUhrzeitUmrandung, width=7, textvariable=vorgangOkvar, font=('Courier New', 6))
    vorgangOk.grid(row=0, column=5, padx='10', pady='1', sticky='ew')

    #                                UMRANDUNG AUFTRAGGEBER ERSTELLEN

    AgeberUmrandung = HAUPTMENUE.Frame(window, width=200, heigh=1, bg='#BDBDBD', borderwidth=2, relief="groove")
    AgeberUmrandung.grid(row=0, column=0, padx='5', pady='5', sticky='nw')
    AgeberUmrandungText_label = HAUPTMENUE.Label(AgeberUmrandung, text="Auftraggeber", fg='#2F4F4F', bg='#BDBDBD',
                                                 font=('Courier New', 10,), width=12, heigh=1, relief=GROOVE)
    AgeberUmrandungText_label.grid(row=0, column=0, padx='0', pady='0', sticky='ew', columnspan=2)

    #                                    Entry UND LABEL KUNDENNUMMER ZUFÜGEN

    kdnummerAgeber_label = HAUPTMENUE.Label(AgeberUmrandung, text="Kd-Nummer", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('Courier New', 12,), width=9, heigh=1)
    kdnummerAgeber_label.grid(row=1, column=0, padx='5', pady='20', sticky='nw')
    kdnummerAgeber = Entry(AgeberUmrandung, width=10, textvariable=kdnrvar, font=('Courier New', 12))
    kdnummerAgeber.grid(row=1, column=1, padx='5', pady='20', sticky='nw')

    #                                Entry UND LABEL KUNDENNACHNAME ZUFÜGEN

    nachnameAgeber_label = HAUPTMENUE.Label(AgeberUmrandung, text="Nachname", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('Courier New', 12,), width=8, heigh=1)
    nachnameAgeber_label.grid(row=2, column=0, padx='5', pady='0', sticky='nw')
    nachnameAgeber = Entry(AgeberUmrandung, width=35, textvariable=nachnameAgebervar, font=('Courier New', 12))
    nachnameAgeber.grid(row=2, column=1, padx='5', pady='0', sticky='nw')

    #                                Entry UND LABEL KUNDENNVORNAME ZUFÜGEN

    vornameAgeber_label = HAUPTMENUE.Label(AgeberUmrandung, text="Vorname", fg='#2F4F4F', bg='#BDBDBD',
                                           font=('Courier New', 12,), width=7, heigh=1)
    vornameAgeber_label.grid(row=3, column=0, padx='5', pady='0', sticky='nw')
    vornameAgeber = Entry(AgeberUmrandung, width=35, textvariable=vornameAgebervar, font=('Courier New', 12))
    vornameAgeber.grid(row=3, column=1, padx='5', pady='0', sticky='nw')

    #                                Entry UND LABEL ZUSATZ ZUFÜGEN

    zusatzAgeber_label = HAUPTMENUE.Label(AgeberUmrandung, text="Zusatz", fg='#2F4F4F', bg='#BDBDBD',
                                          font=('Courier New', 12), width=6, heigh=1)
    zusatzAgeber_label.grid(row=4, column=0, padx='5', pady='0', sticky='nw')
    zusatzAgeber = Entry(AgeberUmrandung, width=35, textvariable=zusatzAgebervar, font=('Courier New', 12))
    zusatzAgeber.grid(row=4, column=1, padx='5', pady='0', sticky='nw')

    #                                Entry UND LABEL STRASSE UND NR ZUFÜGEN

    strAageber_label = HAUPTMENUE.Label(AgeberUmrandung, text="Str./Nr.", fg='#2F4F4F', bg='#BDBDBD',
                                        font=('Courier New', 12,), width=8, heigh=1)
    strAageber_label.grid(row=5, column=0, padx='5', pady='0', sticky='nw')
    strAgeber = Entry(AgeberUmrandung, width=30, textvariable=strAgebervar, font=('Courier New', 12))
    strAgeber.grid(row=5, column=1, padx='5', pady='0', sticky='nw')
    hnrAgeber = Entry(AgeberUmrandung, width=4, textvariable=hnrAgebervar, font=('Courier New', 12))
    hnrAgeber.grid(row=5, column=1, padx='5', pady='0', sticky='ne')

    #                                Entry UND LABEL PLZ UND ORT ZUFÜGEN

    plzAgeber_label = HAUPTMENUE.Label(AgeberUmrandung, text="Plz/Ort", fg='#2F4F4F', bg='#BDBDBD',
                                       font=('Courier New', 12,), width=7, heigh=1)
    plzAgeber_label.grid(row=6, column=0, padx='5', pady='0', sticky='nw')
    plzAgeber = Entry(AgeberUmrandung, width=5, textvariable=plzAgebervar, font=('Courier New', 12))
    plzAgeber.grid(row=6, column=1, padx='5', pady='0', sticky='nw')
    ortAgeber = Entry(AgeberUmrandung, width=29, textvariable=ortAgebervar, font=('Courier New', 12))
    ortAgeber.grid(row=6, column=1, padx='5', pady='0', sticky='ne')

    #                                Entry UND LABEL ANSPRECHPARTNER ZUFÜGEN

    ansprechAgeber_label = HAUPTMENUE.Label(AgeberUmrandung, text="Ansprech", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('Courier New', 12,), width=8, heigh=1)
    ansprechAgeber_label.grid(row=7, column=0, padx='5', pady='0', sticky='nw')
    ansprechAgeber = Entry(AgeberUmrandung, width=35, textvariable=ansprechAgebervar, font=('Courier New', 12))
    ansprechAgeber.grid(row=7, column=1, padx='5', pady='0', sticky='nw')

    #                                Entry UND LABEL TELEFONNUMMER ZUFÜGEN

    telAgeber_label = HAUPTMENUE.Label(AgeberUmrandung, text="Telefon", fg='#2F4F4F', bg='#BDBDBD',
                                       font=('Courier New', 12,), width=7, heigh=1)
    telAgeber_label.grid(row=8, column=0, padx='5', pady='0', sticky='nw')
    telAgeber = Entry(AgeberUmrandung, width=35, textvariable=telAgebervar, font=('Courier New', 12))
    telAgeber.grid(row=8, column=1, padx='5', pady='0', sticky='nw')

    #                                Entry UND LABEL MAIL ZUFÜGEN

    mailAgeber_label = HAUPTMENUE.Label(AgeberUmrandung, text="Mail", fg='#2F4F4F', bg='#BDBDBD',
                                        font=('Courier New', 12,), width=4, heigh=1)
    mailAgeber_label.grid(row=9, column=0, padx='5', pady='0', sticky='nw')
    mailAgeber = Entry(AgeberUmrandung, width=35, textvariable=mailAgebervar, font=('Courier New', 12))
    mailAgeber.grid(row=9, column=1, padx='5', pady='0', sticky='nw')

    kdnrvar = "0000000001"

    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # ************************   FUNKTION AUFTRAGGEBER TEXTFELDER IN DB UPDATEN   **************************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************

    def ageberauswerten():
        vorgangOkvar = "Vorgang"
        vorgangOk.insert(0, vorgangOkvar)
        # vorgangOk.config(state='disabled')
        textauswertungvar = nachnameAgebervar.get().strip()
        if textauswertungvar == "":
            messagebox.showinfo(title='FEHLER', message="Nachname muss angegeben werden !")
            vorgangOk.config(state='normal')
            vorgangOkvar = "Fehler"
            vorgangOk.delete(0, END)
            vorgangOk.insert(0, vorgangOkvar)
            return
        else:
            textauswertungvar = nachnameAgebervar.get().strip()[0: 35]  # .ljust(35, " ")
            nachnameAgeber.delete(0, END)
            nachnameAgeber.insert(0, textauswertungvar)

        textauswertungvar = vornameAgebervar.get().strip()[0: 35]
        vornameAgeber.delete(0, END)
        vornameAgeber.insert(0, textauswertungvar)

        textauswertungvar = zusatzAgebervar.get().strip()[0: 35]
        zusatzAgeber.delete(0, END)
        zusatzAgeber.insert(0, textauswertungvar)

        textauswertungvar = strAgebervar.get().strip()
        if textauswertungvar == "":
            messagebox.showinfo(title='FEHLER', message="Strasse muss angegeben werden !")
            vorgangOk.config(state='normal')
            vorgangOkvar = "Fehler"
            vorgangOk.delete(0, END)
            vorgangOk.insert(0, vorgangOkvar)
            return
        else:
            textauswertungvar = strAgebervar.get().strip()[0: 30]  # .ljust(35, " ")
            strAgeber.delete(0, END)
            strAgeber.insert(0, textauswertungvar)

        textauswertungvar = hnrAgebervar.get().strip()
        if textauswertungvar == "":
            messagebox.showinfo(title='FEHLER', message="Hausnummer muss angegeben werden !")
            vorgangOk.config(state='normal')
            vorgangOkvar = "Fehler"
            vorgangOk.delete(0, END)
            vorgangOk.insert(0, vorgangOkvar)
            return
        else:
            textauswertungvar = hnrAgebervar.get().strip()[0: 4]  # .ljust(35, " ")

            textauswertungvar = hnrAgebervar.get().strip()[0: 4]  # .ljust(35, " ")
            textauswertungvar = textauswertungvar[-1:]
            if textauswertungvar.isnumeric() == True:
                textauswertungvar = hnrAgebervar.get().strip()[0: 4] + " "
            else:
                textauswertungvar = hnrAgebervar.get().strip()[0: 4]

            hnrAgeber.delete(0, END)
            hnrAgeber.insert(0, textauswertungvar)

        textauswertungvar = plzAgebervar.get().strip()
        if textauswertungvar == "" or len(textauswertungvar) < 5:
            messagebox.showinfo(title='FEHLER', message="Fehlende oder ungültige Plz !")
            vorgangOk.config(state='normal')
            vorgangOkvar = "Fehler"
            vorgangOk.delete(0, END)
            vorgangOk.insert(0, vorgangOkvar)
            return
        else:
            textauswertungvar = plzAgebervar.get().strip()[0: 5]  # .ljust(35, " ")
            plzAgeber.delete(0, END)
            plzAgeber.insert(0, textauswertungvar)

        textauswertungvar = ortAgebervar.get().strip()
        if textauswertungvar == "":
            messagebox.showinfo(title='FEHLER', message="Ort muss angegeben werden !")
            vorgangOk.config(state='normal')
            vorgangOkvar = "Fehler"
            vorgangOk.delete(0, END)
            vorgangOk.insert(0, vorgangOkvar)
            return
        else:
            textauswertungvar = ortAgebervar.get().strip()[0: 29]  # .ljust(35, " ")
            ortAgeber.delete(0, END)
            ortAgeber.insert(0, textauswertungvar)

        textauswertungvar = ansprechAgebervar.get().strip()[0: 35]
        ansprechAgeber.delete(0, END)
        ansprechAgeber.insert(0, textauswertungvar)

        textauswertungvar = telAgebervar.get().strip()[0: 35]
        telAgeber.delete(0, END)
        telAgeber.insert(0, textauswertungvar)

        textauswertungvar = mailAgebervar.get().strip()[0: 35]
        mailAgeber.delete(0, END)
        mailAgeber.insert(0, textauswertungvar)

    def ageberspeichern(kdnrvar):
        kdnrvar = kdnummerAgeber.get()
        if Kunde.objects(kunde_nr__exists=True, kunde_nr=kdnrvar):
            ageberauswerten()
            textauswertungvar = vorgangOk.get().strip()[0: 7]
            if textauswertungvar == "Fehler":
                vorgangOkvar = "Vorgang"
                vorgangOk.delete(0, END)
                vorgangOk.insert(0, vorgangOkvar)
                vorgangOk.config(state='disabled')
                return
            else:
                Kunde.objects(kunde_nr=kdnrvar).update_one(nachname=nachnameAgebervar.get().strip()[0: 35])
                Kunde.objects(kunde_nr=kdnrvar).update_one(vorname=vornameAgebervar.get().strip()[0: 35])
                Kunde.objects(kunde_nr=kdnrvar).update_one(zusatz=zusatzAgebervar.get().strip()[0: 35])
                Kunde.objects(kunde_nr=kdnrvar).update_one(strasse=strAgebervar.get().strip()[0: 30])
                Kunde.objects(kunde_nr=kdnrvar).update_one(haus_nr=hnrAgebervar.get().strip()[0: 4])
                Kunde.objects(kunde_nr=kdnrvar).update_one(plz=plzAgebervar.get().strip()[0: 5])
                Kunde.objects(kunde_nr=kdnrvar).update_one(stadt=ortAgebervar.get().strip()[0: 29])
                Kunde.objects(kunde_nr=kdnrvar).update_one(ansprech=ansprechAgebervar.get().strip()[0: 35])
                Kunde.objects(kunde_nr=kdnrvar).update_one(telefon_nr=telAgebervar.get().strip()[0: 35])
                Kunde.objects(kunde_nr=kdnrvar).update_one(email=mailAgebervar.get().strip()[0: 29])

                # User.objects(user_name=benutzer).update_one(user_password=passwort)
        else:
            messagebox.showerror(title='Fehler', message="keine gültige Kundennummer")
            pass

    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # ************************   FUNKTION AUFTRAGGEBER TEXTFELDER AUS DB FÜLLEN*****************************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************

    def ageberfuellen(kdnrvar):
            kdnummerAgeber.insert(0, Kunde.objects(kunde_nr=kdnrvar).scalar('kunde_nr')[0])
            nachnameAgeber.delete(0, END)
            nachnameAgeber.insert(0, Kunde.objects(kunde_nr=kdnrvar).scalar('nachname')[0])
            vornameAgeber.delete(0, END)
            if Kunde.objects(vorname__exists=True):
                vornameAgeber.insert(0, Kunde.objects(kunde_nr=kdnrvar).scalar('vorname')[0])
            else:
                pass

            zusatzAgeber.delete(0, END)
            if Kunde.objects(zusatz__exists=True):
                #zusatzAgeber.insert(0, Kunde.objects(kunde_nr=kdnrvar).scalar('zusatz')[0])
                try:
                    zusatzAgeber.insert(0, Kunde.objects(kunde_nr=kdnrvar).scalar('zusatz')[0])
                except TclError:
                    logging.exception(TclError)

            else:
                pass
            strAgeber.delete(0, END)
            strAgeber.insert(0, Kunde.objects(kunde_nr=kdnrvar).scalar('strasse')[0])
            hnrAgeber.delete(0, END)
            hnrAgeber.insert(0, Kunde.objects(kunde_nr=kdnrvar).scalar('haus_nr')[0])
            plzAgeber.delete(0, END)
            plzAgeber.insert(0, Kunde.objects(kunde_nr=kdnrvar).scalar('plz')[0])
            ortAgeber.delete(0, END)
            ortAgeber.insert(0, Kunde.objects(kunde_nr=kdnrvar).scalar('stadt')[0])
            ansprechAgeber.delete(0, END)

            if Kunde.objects(ansprech__exists=True):
                try:
                    ansprechAgeber.insert(0, Kunde.objects(kunde_nr=kdnrvar).scalar('ansprech')[0])
                except TclError:
                    logging.exception(TclError)
            else:
                pass
            telAgeber.delete(0, END)

            if Kunde.objects(telefon_nr__exists=True):
                try:
                    telAgeber.insert(0, Kunde.objects(kunde_nr=kdnrvar).scalar('telefon_nr')[0])
                except TclError:
                    logging.exception(TclError)
            else:
                pass
            mailAgeber.delete(0, END)

            if Kunde.objects(email__exists=True):
                try:
                    mailAgeber.insert(0, Kunde.objects(kunde_nr=kdnrvar).scalar('email')[0])
                except TclError:
                    logging.exception(TclError)
            else:
                pass


    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # ************************   ARBEITGEBERVARIABLEN DIE DATENFELDER DER DB ZUWEISEN    *******************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************

    def agebercalarliste():
        auftragkundennummer = Kunde.objects().scalar('kunde_nr')
        auftragnachname = Kunde.objects().scalar('nachname')
        auftragvorname = Kunde.objects().scalar('vorname')
        auftragzusatz = Kunde.objects().scalar('zusatz')
        auftragstrasse = Kunde.objects().scalar('strasse')
        auftraghausnummer = Kunde.objects().scalar('haus_nr')
        auftragplz = Kunde.objects().scalar('plz')
        auftragort = Kunde.objects().scalar('stadt')
        auftragansprech = Kunde.objects().scalar('ansprech')
        auftragtelefon = Kunde.objects().scalar('telefon_nr')
        auftragmail = Kunde.objects().scalar('vorname')

    ageberfuellen(kdnrvar)
    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # ************************   BEREICH OBJEKT TEXTFELDER ERSTELLEN   *************************************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************

    #                                UMRANDUNG OBJEKT ERSTELLEN

    ObjektUmrandung = HAUPTMENUE.Frame(AgeberUmrandung, width=200, heigh=263, bg='#BDBDBD', borderwidth=2,
                                       relief="flat", )
    ObjektUmrandung.grid(row=0, column=3, padx='40', pady='0', sticky='nw', rowspan=10)
    ObjektUmrandungText_label = HAUPTMENUE.Label(ObjektUmrandung, text="Objekt", fg='#2F4F4F', bg='#BDBDBD',
                                                 font=('Courier New', 10,), width=6, heigh=1, relief=GROOVE)
    ObjektUmrandungText_label.grid(row=0, column=0, padx='0', pady='0', sticky='ew', columnspan=2)

    #                                Entry UND LABEL OBJEKTNUMMER ZUFÜGEN

    obnrObjekt_label = HAUPTMENUE.Label(ObjektUmrandung, text="Objekt-Nr", fg='#2F4F4F', bg='#BDBDBD',
                                        font=('Courier New', 12,), width=9, heigh=1)
    obnrObjekt_label.grid(row=1, column=0, padx='5', pady='20', sticky='nw')
    obnrObjekt = Entry(ObjektUmrandung, width=5, justify=RIGHT, font=('Courier New', 12))
    obnrObjekt.grid(row=1, column=1, padx='5', pady='20', sticky='nw')

    #                               Entry UND LABEL OBJEKT KUNDENNACHNAME ZUFÜGEN

    objektnachname_label = HAUPTMENUE.Label(ObjektUmrandung, text="Nachname", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('Courier New', 12,), width=8, heigh=1)
    objektnachname_label.grid(row=2, column=0, padx='5', pady='2', sticky='nw')
    objektnachname = Entry(ObjektUmrandung, width=35, font=('Courier New', 12))
    objektnachname.grid(row=2, column=1, padx='5', pady='2', sticky='nw')

    #                               Entry UND LABEL OBJEKT KUNDENNVORNAME ZUFÜGEN

    objektvorname_label = HAUPTMENUE.Label(ObjektUmrandung, text="Vorname", fg='#2F4F4F', bg='#BDBDBD',
                                           font=('Courier New', 12,), width=7, heigh=1)
    objektvorname_label.grid(row=3, column=0, padx='5', pady='2', sticky='nw')
    objektvorname = Entry(ObjektUmrandung, width=35, font=('Courier New', 12))
    objektvorname.grid(row=3, column=1, padx='5', pady='2', sticky='nw')

    #                               Entry UND LABEL OBJEKT ZUSATZ ZUFÜGEN

    objektzusatz_label = HAUPTMENUE.Label(ObjektUmrandung, text="Zusatz", fg='#2F4F4F', bg='#BDBDBD',
                                          font=('Courier New', 12,), width=6, heigh=1)
    objektzusatz_label.grid(row=4, column=0, padx='5', pady='2', sticky='nw')
    objektzusatz = Entry(ObjektUmrandung, width=35, font=('Courier New', 12))
    objektzusatz.grid(row=4, column=1, padx='5', pady='2', sticky='nw')

    #                               Entry UND LABEL OBJEKT STRASSE UND NR ZUFÜGEN

    objektstrasse_label = HAUPTMENUE.Label(ObjektUmrandung, text="Str./Nr.", fg='#2F4F4F', bg='#BDBDBD',
                                           font=('Courier New', 12,), width=8, heigh=1)
    objektstrasse_label.grid(row=5, column=0, padx='5', pady='2', sticky='nw')
    objektstrasse = Entry(ObjektUmrandung, width=30, font=('Courier New', 12))
    objektstrasse.grid(row=5, column=1, padx='5', pady='2', sticky='nw')
    objektnr = Entry(ObjektUmrandung, width=4, justify=RIGHT, font=('Courier New', 12))
    objektnr.grid(row=5, column=1, padx='5', pady='2', sticky='ne')

    #                               Entry UND LABEL OBJEKT PLZ UND ORT ZUFÜGEN

    objektplz_label = HAUPTMENUE.Label(ObjektUmrandung, text="Plz/Ort", fg='#2F4F4F', bg='#BDBDBD',
                                       font=('Courier New', 12,), width=7, heigh=1)
    objektplz_label.grid(row=6, column=0, padx='5', pady='2', sticky='nw')
    objektplz = Entry(ObjektUmrandung, width=5, justify=RIGHT, font=('Courier New', 12))
    objektplz.grid(row=6, column=1, padx='5', pady='2', sticky='nw')
    objektort = Entry(ObjektUmrandung, width=29, font=('Courier New', 12))
    objektort.grid(row=6, column=1, padx='5', pady='2', sticky='ne')

    #                               Entry UND LABEL OBJEKT ANSPRECHPARTNER ZUFÜGEN

    objektansprechpartner_label = HAUPTMENUE.Label(ObjektUmrandung, text="Ansprech", fg='#2F4F4F', bg='#BDBDBD',
                                                   font=('Courier New', 12,), width=8, heigh=1)
    objektansprechpartner_label.grid(row=7, column=0, padx='5', pady='2', sticky='nw')
    objektansprechpartner = Entry(ObjektUmrandung, width=35, font=('Courier New', 12))
    objektansprechpartner.grid(row=7, column=1, padx='5', pady='2', sticky='nw')

    #                               Entry UND LABEL OBJEKT TELEFONNUMMER ZUFÜGEN

    objekttelefon_label = HAUPTMENUE.Label(ObjektUmrandung, text="Telefon", fg='#2F4F4F', bg='#BDBDBD',
                                           font=('Courier New', 12,), width=7, heigh=1)
    objekttelefon_label.grid(row=8, column=0, padx='5', pady='2', sticky='nw')
    objekttelefon = Entry(ObjektUmrandung, width=35, font=('Courier New', 12))
    objekttelefon.grid(row=8, column=1, padx='5', pady='2', sticky='nw')

    #                               Entry UND LABEL OBJEKT MAIL ZUFÜGEN

    objektmail_label = HAUPTMENUE.Label(ObjektUmrandung, text="Mail", fg='#2F4F4F', bg='#BDBDBD',
                                        font=('Courier New', 12,), width=4, heigh=1)
    objektmail_label.grid(row=9, column=0, padx='5', pady='2', sticky='nw')
    objektmail = Entry(ObjektUmrandung, width=35, font=('Courier New', 12))
    objektmail.grid(row=9, column=1, padx='5', pady='2', sticky='nw')

    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # *************** KUNDE + OBJEKT SUCHEN/NEU/SPEICHERN/ÄNDERN BUTTONS ERSTELLEN   ***********************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************

    Button1Umrandung = HAUPTMENUE.Frame(AgeberUmrandung, bd=2, width=200, heigh=263, bg='#BDBDBD', borderwidth=2,
                                        relief="flat", )
    Button1Umrandung.grid(row=0, column=4, padx='5', pady='0', sticky='nw', rowspan=10)
    Button1UmrandungText_label = HAUPTMENUE.Label(Button1Umrandung, text="Auswahl", fg='#2F4F4F', bg='#BDBDBD',
                                                  font=('Courier New', 10,), width=16, heigh=1, relief=GROOVE)
    Button1UmrandungText_label.grid(row=0, column=0, padx='0', pady='0', sticky='ew')

    ButtonSuchen = HAUPTMENUE.Button(Button1Umrandung, text="Suchen").grid(row=1, column=0, padx='10', pady='20',
                                                                           sticky='ew')
    ButtonNeu = HAUPTMENUE.Button(Button1Umrandung, text="Neu").grid(row=2, column=0, padx='10', pady='5', sticky='ew')
    ButtonAendern = HAUPTMENUE.Button(Button1Umrandung, text="Bearbeiten").grid(row=3, column=0, padx='10', pady='5',
                                                                                sticky='ew')
    ButtonSpeichern = HAUPTMENUE.Button(Button1Umrandung, text="Speichern",
                                        command=lambda: ageberspeichern(kdnrvar)).grid(row=4, column=0, padx='10',
                                                                                       pady='5', sticky='ew')
    ButtonFestpreise = HAUPTMENUE.Button(Button1Umrandung, text="Festpreise").grid(row=5, column=0, padx='10', pady='5',
                                                                                   sticky='ew')
    Button1UmrandungText_label = HAUPTMENUE.Label(Button1Umrandung, text="", bg='#BDBDBD', relief=FLAT).grid(row=6,
                                                                                                             column=0,
                                                                                                             padx='5',
                                                                                                             pady='5')
    ButtonDelete = HAUPTMENUE.Button(Button1Umrandung, text="Löschen", bg='#FF0040').grid(row=8, column=0, padx='10',
                                                                                          pady='5', sticky='ew',
                                                                                          columnspan=1)

    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # ************************   BEREICH LISTE TEXTFELDER ERSTELLEN   ************************************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************

    suchenbox = HAUPTMENUE.Listbox(AgeberUmrandung, bd=2, width=111, heigh=16, borderwidth=2, font=('Courier New', 8),
                                   relief="flat")
    suchenbox.grid(row=1, column=5, padx='15', pady='10', sticky='ne', rowspan=10)
    suchenboxText_label = HAUPTMENUE.Label(AgeberUmrandung, text="KUNDEN", fg='#2F4F4F', bg='#BDBDBD',
                                           font=('Courier New', 10,), width=6, heigh=1, relief=GROOVE)
    suchenboxText_label.grid(row=0, column=5, padx='15', pady='0', sticky='ew')

    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # ************************   BEREICH VERTRAG TEXTFELDER ERSTELLEN   ************************************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************

    #                                UMRANDUNG VERTRAGSARTAUSWAHL ERSTELLEN

    VertragsArtUmrandung = HAUPTMENUE.Frame(window, bd=2, width=400, heigh=58, bg='#D8D8D8', borderwidth=2,
                                            relief="groove", )
    VertragsArtUmrandung.grid(row=1, column=0, padx='5', pady='0', sticky='nw', columnspan=1)

    #                          *******************************************
    #                          ***  CHECKBOXEN FÜR VERTRAGSARTAUSWAHL ****
    #                          ********************************'**********

    def vertragsart_checkbox1_check(vertragsartcheckbox1var):
        if vertragsartcheckbox1var.get() == 1:
            BehandlungenRahmen1.grid(row=1, column=2, padx='0', pady='1', sticky='nw', columnspan=5, rowspan=5)
            BehandlungenRahmen2.grid_forget()
            vertragsartcheckbox2var.set(0)
            vertragsartcheckbox3var.set(0)
            vertragsartcheckbox4var.set(0)
        else:
            BehandlungenRahmen1.grid_forget()

    def vertragsart_checkbox2_check(vertragsartcheckbox2var):
        if vertragsartcheckbox2var.get() == 1:
            BehandlungenRahmen1.grid_forget()
            BehandlungenRahmen2.grid(row=1, column=2, padx='0', pady='1', sticky='nw', columnspan=5, rowspan=5)
            vertragsartcheckbox1var.set(0)
            vertragsartcheckbox3var.set(0)
            vertragsartcheckbox4var.set(0)
        else:
            BehandlungenRahmen2.grid_forget()

    def vertragsart_checkbox3_check(vertragsartcheckbox3var):
        if vertragsartcheckbox3var.get() == 1:
            BehandlungenRahmen1.grid_forget()
            BehandlungenRahmen2.grid(row=1, column=2, padx='0', pady='1', sticky='nw', columnspan=5, rowspan=5)
            vertragsartcheckbox1var.set(0)
            vertragsartcheckbox2var.set(0)
            vertragsartcheckbox4var.set(0)
        else:
            BehandlungenRahmen2.grid_forget()

    def vertragsart_checkbox4_check(vertragsartcheckbox4var):
        if vertragsartcheckbox4var.get() == 1:
            BehandlungenRahmen1.grid_forget()
            BehandlungenRahmen2.grid(row=1, column=2, padx='0', pady='1', sticky='nw', columnspan=5, rowspan=5)
            vertragsartcheckbox1var.set(0)
            vertragsartcheckbox2var.set(0)
            vertragsartcheckbox3var.set(0)
        else:
            BehandlungenRahmen2.grid_forget()

    vertragsartcheckbox1var = HAUPTMENUE.IntVar()
    vertragsartcheckbox2var = HAUPTMENUE.IntVar()
    vertragsartcheckbox3var = HAUPTMENUE.IntVar()
    vertragsartcheckbox4var = HAUPTMENUE.IntVar()

    vertragsart_checkbox1 = HAUPTMENUE.Checkbutton(VertragsArtUmrandung, text="Wartung      ",
                                                   variable=vertragsartcheckbox1var,
                                                   fg='#2F4F4F', bg='#D8D8D8', font=('Courier New', 12,), width=13,
                                                   heigh=1, onvalue=1,
                                                   offvalue=0, command=partial(vertragsart_checkbox1_check,
                                                                               vertragsartcheckbox1var))
    vertragsart_checkbox1.grid(row=1, column=0, padx='5', pady='1', sticky='nw')

    vertragsart_checkbox2 = HAUPTMENUE.Checkbutton(VertragsArtUmrandung, text="Einzel      ",
                                                   variable=vertragsartcheckbox2var,
                                                   fg='#2F4F4F', bg='#D8D8D8', onvalue=1, offvalue=0,
                                                   font=('Courier New', 12,), width=12,
                                                   heigh=1, command=partial(vertragsart_checkbox2_check,
                                                                            vertragsartcheckbox2var))
    vertragsart_checkbox2.grid(row=1, column=1, padx='5', pady='1', sticky='nw')

    vertragsart_checkbox3 = HAUPTMENUE.Checkbutton(VertragsArtUmrandung, text="Angebot      ",
                                                   variable=vertragsartcheckbox3var,
                                                   fg='#2F4F4F', onvalue=1, offvalue=0, bg='#D8D8D8',
                                                   font=('Courier New', 12,), width=13,
                                                   heigh=1, command=partial(vertragsart_checkbox3_check,
                                                                            vertragsartcheckbox3var))
    vertragsart_checkbox3.grid(row=2, column=0, padx='5', pady='1', sticky='nw')

    vertragsart_checkbox4 = HAUPTMENUE.Checkbutton(VertragsArtUmrandung, text="Mehrfach    ",
                                                   variable=vertragsartcheckbox4var,
                                                   fg='#2F4F4F', onvalue=1, offvalue=0, bg='#D8D8D8',
                                                   font=('Courier New', 12,), width=12,
                                                   heigh=1, command=partial(vertragsart_checkbox4_check,
                                                                            vertragsartcheckbox4var))
    vertragsart_checkbox4.grid(row=2, column=1, padx='5', pady='1', sticky='nw')

    vertragsartcheckbox1var.set(1)
    vertragsartcheckbox2var.set(0)
    vertragsartcheckbox3var.set(0)
    vertragsartcheckbox4var.set(0)

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #                        WECHSELRAHMEN1 FÜR BEHANDLUNGSART WARTUNG ERSTELLEN VERTRAGSKUNDE
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    BehandlungenRahmen1 = HAUPTMENUE.Frame(VertragsArtUmrandung, bd=1, width=400, heigh=58, bg='#D8D8D8', borderwidth=2,
                                           relief="flat")
    BehandlungenRahmen1.grid(row=1, column=2, padx='0', pady='0', sticky='nw', columnspan=5, rowspan=5)

    #                        EntryER FÜR VERTRAG VON BIS

    VertragVonBis_label = HAUPTMENUE.Label(BehandlungenRahmen1, text="Vertrag von-bis", fg='#2F4F4F', bg='#D8D8D8',
                                           font=('Courier New', 12,), width=15, heigh=1)
    VertragVonBis_label.grid(row=0, column=0, padx='5', pady='2', sticky='nw')

    VertragVonBis1 = Entry(BehandlungenRahmen1, width=10, font=('Courier New', 12))
    VertragVonBis1.grid(row=0, column=1, padx='5', pady='5', sticky='nw')

    VertragVonBis2 = Entry(BehandlungenRahmen1, width=10, font=('Courier New', 12))
    VertragVonBis2.grid(row=0, column=2, padx='5', pady='5', sticky='nw')

    #                        LETZTE BEHANDLUNGEN

    letztebehandlung1_label = HAUPTMENUE.Label(BehandlungenRahmen1, text="zuletzt am", fg='#2F4F4F', bg='#D8D8D8',
                                               font=('Courier New', 12,), width=10, heigh=1)
    letztebehandlung1_label.grid(row=1, column=0, padx='5', pady='5', sticky='nw')
    letztebehandlung1 = Entry(BehandlungenRahmen1, width=10, font=('Courier New', 12))
    letztebehandlung1.grid(row=1, column=1, padx='5', pady='8', sticky='nw')
    letztebehandlung2 = Entry(BehandlungenRahmen1, width=10, font=('Courier New', 12))
    letztebehandlung2.grid(row=1, column=2, padx='5', pady='8', sticky='nw')

    #                        Entry UND LABEL ANZAHL WARTUNG UND INTENSIV EINZEL ZUFÜGEN

    vertragsinterval_label = HAUPTMENUE.Label(BehandlungenRahmen1, text="Anzahl Wartung ", fg='#2F4F4F', bg='#D8D8D8',
                                              font=('Courier New', 12,), width=15, heigh=1)
    vertragsinterval_label.grid(row=0, column=3, padx='5', pady='2', sticky='nw')
    vertragsinterval = Entry(BehandlungenRahmen1, width=2, justify=RIGHT, font=('Courier New', 12))
    vertragsinterval.grid(row=0, column=4, padx='5', pady='5', sticky='nw')

    vertragsintensivinterval_label = HAUPTMENUE.Label(BehandlungenRahmen1, text="Anzahl Intensiv", fg='#2F4F4F',
                                                      bg='#D8D8D8', font=('Courier New', 12,), width=15, heigh=1)
    vertragsintensivinterval_label.grid(row=1, column=3, padx='5', pady='5', sticky='nw')
    vertragsintensivinterval = Entry(BehandlungenRahmen1, width=2, justify=RIGHT, font=('Courier New', 12))
    vertragsintensivinterval.grid(row=1, column=4, padx='5', pady='8', sticky='nw')

    #                        KUNDENHINWEISE UND WICHTIG UND UNTERSCHRIFT BENÖTIGT

    hinweis_label = HAUPTMENUE.Label(BehandlungenRahmen1, text="Hinweis", fg='#2F4F4F', bg='#D8D8D8',
                                     font=('Courier New', 12,), width=7, heigh=1)
    hinweis_label.grid(row=0, column=5, padx='5', pady='2', sticky='nw')
    hinweis = Entry(BehandlungenRahmen1, width=47, font=('Courier New', 12))
    hinweis.grid(row=0, column=6, padx='5', pady='5', sticky='nw')

    hinweis1_label = HAUPTMENUE.Label(BehandlungenRahmen1, text="Wichtig", fg='#2F4F4F', bg='#D8D8D8',
                                      font=('Courier New', 12,), width=7, heigh=1)
    hinweis1_label.grid(row=1, column=5, padx='5', pady='5', sticky='nw')
    hinweis1 = Entry(BehandlungenRahmen1, width=47, font=('Courier New', 12))
    hinweis1.grid(row=1, column=6, padx='5', pady='8', sticky='nw')

    barzahlung_checkbox1 = HAUPTMENUE.Checkbutton(BehandlungenRahmen1, text="EC/Bahrzahlung nötig             ",
                                                  fg='#2F4F4F', bg='#D8D8D8', font=('Courier New', 12,), width=32,
                                                  heigh=1)
    barzahlung_checkbox1.grid(row=0, column=7, padx='10', pady='2', sticky='nw')

    unterschrift_checkbox1 = HAUPTMENUE.Checkbutton(BehandlungenRahmen1, text="Unterschrift nötig", fg='#2F4F4F',
                                                    bg='#D8D8D8', font=('Courier New', 12,), width=18, heigh=1)
    unterschrift_checkbox1.grid(row=1, column=7, padx='5', pady='3', sticky='nw')

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #                        WECHSELRAHMEN2 FÜR BEHANDLUNGSART ANGEBOT/EINZEL/MEHRFACH ERSTELLEN
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    BehandlungenRahmen2 = HAUPTMENUE.Frame(VertragsArtUmrandung, bd=2, width=1301, heigh=58, bg='#D8D8D8',
                                           borderwidth=2, relief="flat", )
    BehandlungenRahmen2.grid(row=1, column=2, padx='0', pady='3', sticky='nw', columnspan=5, rowspan=5)

    #                             EINFÜGEN AUFTRAG ZÄHLER NR VON

    AuftragNrVon_label = HAUPTMENUE.Label(BehandlungenRahmen2, text="Nr.", fg='#2F4F4F', bg='#D8D8D8',
                                          font=('Courier New', 12,), width=3, heigh=1)
    AuftragNrVon_label.grid(row=0, column=0, padx='5', pady='2', sticky='nw')

    AuftragNrVon = Entry(BehandlungenRahmen2, width=2, justify=RIGHT, font=('Courier New', 12))
    AuftragNrVon.grid(row=0, column=1, padx='5', pady='5', sticky='nw')

    AuftragNrBis_label = HAUPTMENUE.Label(BehandlungenRahmen2, text="von", fg='#2F4F4F', bg='#D8D8D8',
                                          font=('Courier New', 12,), width=3, heigh=1)
    AuftragNrBis_label.grid(row=1, column=0, padx='5', pady='6', sticky='nw')

    AuftragNrBis = Entry(BehandlungenRahmen2, width=2, justify=RIGHT, font=('Courier New', 12))
    AuftragNrBis.grid(row=1, column=1, padx='5', pady='5', sticky='nw')

    #                             EINFÜGEN AUFTRAGSDATUM UND AUFTRAGSNUMMER

    AuftragNummer_label = HAUPTMENUE.Label(BehandlungenRahmen2, text="Auftrag Nr.", fg='#2F4F4F', bg='#D8D8D8',
                                           font=('Courier New', 12,), width=11, heigh=1)
    AuftragNummer_label.grid(row=0, column=2, padx='5', pady='2', sticky='nw')
    AuftragNummer = Entry(BehandlungenRahmen2, width=10, font=('Courier New', 12))
    AuftragNummer.grid(row=0, column=3, padx='5', pady='5', sticky='nw')

    AuftragVom_label = HAUPTMENUE.Label(BehandlungenRahmen2, text="Auftrag vom", fg='#2F4F4F', bg='#D8D8D8',
                                        font=('Courier New', 12,), width=11, heigh=1)
    AuftragVom_label.grid(row=1, column=2, padx='5', pady='5', sticky='nw')
    AuftragVom = Entry(BehandlungenRahmen2, width=10, font=('Courier New', 12))
    AuftragVom.grid(row=1, column=3, padx='3', pady='5', sticky='nw')

    #                            TERMINE UND ZEIT EINFÜGEN

    Termin1_label = HAUPTMENUE.Label(BehandlungenRahmen2, text="Termin/Zeit", fg='#2F4F4F', bg='#D8D8D8',
                                     font=('Courier New', 12,), width=11, heigh=1)
    Termin1_label.grid(row=0, column=4, padx='5', pady='2', sticky='nw')
    Termin1 = Entry(BehandlungenRahmen2, width=14, font=('Courier New', 12))
    Termin1.grid(row=0, column=5, padx='5', pady='5', sticky='nw')
    Termin2 = Entry(BehandlungenRahmen2, width=5, font=('Courier New', 12))
    Termin2.grid(row=0, column=5, padx='5', pady='5', sticky='ne')

    Techniker2_label = HAUPTMENUE.Label(BehandlungenRahmen2, text="Techniker", fg='#2F4F4F', bg='#D8D8D8',
                                        font=('Courier New', 12,), width=9, heigh=1)
    Techniker2_label.grid(row=1, column=4, padx='5', pady='3', sticky='nw')
    TechnikerCombo2 = ttk.Combobox(BehandlungenRahmen2, values=["Aus Liste Auslesen", "Frickmann", ],
                                   font=('Courier New', 10), width=15)
    TechnikerCombo2.grid(row=1, column=5, padx='5', pady='3', sticky='nw')
    TechnikerCombo2.current(0)

    #                        KUNDENHINWEISE UND WICHTIG

    hinweis2_label = HAUPTMENUE.Label(BehandlungenRahmen2, text="Hinweis", fg='#2F4F4F', bg='#D8D8D8',
                                      font=('Courier New', 12,), width=7, heigh=1)
    hinweis2_label.grid(row=0, column=8, padx='5', pady='2', sticky='nw')
    hinweis2 = Entry(BehandlungenRahmen2, width=47, font=('Courier New', 12))
    hinweis2.grid(row=0, column=9, padx='5', pady='5', sticky='nw')

    hinweis3_label = HAUPTMENUE.Label(BehandlungenRahmen2, text="Wichtig", fg='#2F4F4F', bg='#D8D8D8',
                                      font=('Courier New', 12,), width=7, heigh=1)
    hinweis3_label.grid(row=1, column=8, padx='5', pady='3', sticky='nw')
    hinweis3 = Entry(BehandlungenRahmen2, width=47, font=('Courier New', 12))
    hinweis3.grid(row=1, column=9, padx='5', pady='3', sticky='nw')

    #                        BARZAHLUNG NÖTIG UNTERSCHRIFT NÖTIG

    barzahlung_checkbox2 = HAUPTMENUE.Checkbutton(BehandlungenRahmen2, text="EC/Bahrzahlung nötig        ",
                                                  fg='#2F4F4F', bg='#D8D8D8', font=('Courier New', 12,), width=27,
                                                  heigh=1)
    barzahlung_checkbox2.grid(row=0, column=10, padx='12', pady='2', sticky='nw')

    unterschrift_checkbox2 = HAUPTMENUE.Checkbutton(BehandlungenRahmen2, text="Unterschrift nötig", fg='#2F4F4F',
                                                    bg='#D8D8D8', font=('Courier New', 12,), width=18, heigh=1)
    unterschrift_checkbox2.grid(row=1, column=10, padx='7', pady='0', sticky='nw')

    BehandlungenRahmen2.grid_forget()

    #                       UMRANDUNG SCHÄDLINGSAUSWAHL ERSTELLEN

    TierUmrandung = HAUPTMENUE.Frame(window, bd=2, width=1301, heigh=58, bg='#BDBDBD', borderwidth=2, relief="groove", )
    TierUmrandung.grid(row=3, column=0, padx='5', pady='3', sticky='nw', columnspan=1)

    #                       **********************************************
    #                       *****  CHECKBOXEN FÜR SCHÄDLINGSAUSWAHL ******
    #                       **********************************************

    Tier_checkbox1 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Ratten", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('Courier New', 12,), width=6, heigh=1)
    Tier_checkbox1.grid(row=0, column=0, padx='5', pady='5', sticky='nw')

    Tier_checkbox2 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Mäuse", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('Courier New', 12,), width=5, heigh=1)
    Tier_checkbox2.grid(row=0, column=1, padx='5', pady='5', sticky='nw')

    Tier_checkbox3 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Schaben", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('Courier New', 12,), width=7, heigh=1)
    Tier_checkbox3.grid(row=0, column=2, padx='5', pady='5', sticky='nw')

    Tier_checkbox4 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Ameisen", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('Courier New', 12,), width=7, heigh=1)
    Tier_checkbox4.grid(row=0, column=3, padx='5', pady='5', sticky='nw')

    Tier_checkbox5 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Wespen", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('Courier New', 12,), width=6, heigh=1)
    Tier_checkbox5.grid(row=0, column=4, padx='5', pady='5', sticky='nw')

    Tier_checkbox6 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Bettwanzen", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('Courier New', 12,), width=10, heigh=1)
    Tier_checkbox6.grid(row=0, column=5, padx='5', pady='5', sticky='nw')

    Tier_checkbox7 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Motten", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('Courier New', 12,), width=6, heigh=1)
    Tier_checkbox7.grid(row=0, column=6, padx='5', pady='5', sticky='nw')

    Tier_checkbox8 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Tauben", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('Courier New', 12,), width=6, heigh=1)
    Tier_checkbox8.grid(row=0, column=7, padx='5', pady='5', sticky='nw')

    Tier_checkbox9 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Käfer", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('Courier New', 12,), width=5, heigh=1)
    Tier_checkbox9.grid(row=0, column=8, padx='5', pady='5', sticky='nw')

    Tier_checkbox10 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Marder", fg='#2F4F4F', bg='#BDBDBD',
                                             font=('Courier New', 12,), width=6, heigh=1)
    Tier_checkbox10.grid(row=0, column=9, padx='5', pady='5', sticky='nw')

    Tier_checkbox11 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Fliegen", fg='#2F4F4F', bg='#BDBDBD',
                                             font=('Courier New', 12,), width=7, heigh=1)
    Tier_checkbox11.grid(row=0, column=10, padx='5', pady='5', sticky='nw')

    Tier_checkbox11 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Hornissen", fg='#2F4F4F', bg='#BDBDBD',
                                             font=('Courier New', 12,), width=9, heigh=1)
    Tier_checkbox11.grid(row=0, column=11, padx='5', pady='5', sticky='nw')

    Tier_checkbox13 = HAUPTMENUE.Checkbutton(TierUmrandung, text=" ?", fg='#2F4F4F', bg='#BDBDBD',
                                             font=('Courier New', 12,), width=1, heigh=1)
    Tier_checkbox13.grid(row=0, column=12, padx='5', pady='5', sticky='nw')

    TierCheckboxtext = Entry(TierUmrandung, width=36)
    TierCheckboxtext.grid(row=0, column=13, padx='15', pady='8', sticky='ne')

    #                       UMRANDUNG GESETZE UND BEHANDLUNGSBEREICHE UND BESCHRIFTUNG ERSTELLEN

    GesetzeUmrandung = HAUPTMENUE.Frame(window, bd=2, width=1301, heigh=58, bg='#D8D8D8', borderwidth=2,
                                        relief="groove", )
    GesetzeUmrandung.grid(row=4, column=0, padx='5', pady='3', sticky='nw', columnspan=1)

    #                       **********************************************
    #                       ***  CHECKBOXEN FÜR GESETZE UND BEREICHE  ****
    #                       **********************************************

    #                            CHECKBOXEN FÜR GESETZE

    Gesetzt_checkbox1 = HAUPTMENUE.Checkbutton(GesetzeUmrandung, text="LMHV/HACCP", fg='#2F4F4F', bg='#D8D8D8',
                                               font=('Courier New', 12,), width=10, heigh=1)
    Gesetzt_checkbox1.grid(row=0, column=0, padx='5', pady='0', sticky='nw')

    Gesetzt_checkbox2 = HAUPTMENUE.Checkbutton(GesetzeUmrandung, text="IFSG", fg='#2F4F4F', bg='#D8D8D8',
                                               font=('Courier New', 12,), width=4, heigh=1)
    Gesetzt_checkbox2.grid(row=0, column=1, padx='0', pady='0', sticky='nw')

    Gesetzt_checkbox3 = HAUPTMENUE.Checkbutton(GesetzeUmrandung, text="Biozid-VO", fg='#2F4F4F', bg='#D8D8D8',
                                               font=('Courier New', 12,), width=9, heigh=1)
    Gesetzt_checkbox3.grid(row=0, column=2, padx='0', pady='0', sticky='nw')

    #                            CHECKBOXEN FÜR BEREICHSAUSWAHL
    Bereich_checkbox1 = HAUPTMENUE.Checkbutton(GesetzeUmrandung, text="Köderstationen", fg='#2F4F4F', bg='#D8D8D8',
                                               font=('Courier New', 12,), width=14, heigh=1)
    Bereich_checkbox1.grid(row=0, column=3, padx='0', pady='0', sticky='nw')

    Bereich_checkbox2 = HAUPTMENUE.Checkbutton(GesetzeUmrandung, text="Innenbereich", fg='#2F4F4F', bg='#D8D8D8',
                                               font=('Courier New', 12,), width=12, heigh=1)
    Bereich_checkbox2.grid(row=0, column=4, padx='0', pady='0', sticky='nw')

    Bereich_checkbox3 = HAUPTMENUE.Checkbutton(GesetzeUmrandung, text="Wohnbereich", fg='#2F4F4F', bg='#D8D8D8',
                                               font=('Courier New', 12,), width=11, heigh=1)
    Bereich_checkbox3.grid(row=0, column=5, padx='0', pady='0', sticky='nw')

    Bereich_checkbox4 = HAUPTMENUE.Checkbutton(GesetzeUmrandung, text="Küchenbereich   ", fg='#2F4F4F', bg='#D8D8D8',
                                               font=('Courier New', 12,), width=16, heigh=1)
    Bereich_checkbox4.grid(row=0, column=6, padx='0', pady='0', sticky='nw')

    Bereich_checkbox5 = HAUPTMENUE.Checkbutton(GesetzeUmrandung, text="Aussenbereich   ", fg='#2F4F4F', bg='#D8D8D8',
                                               font=('Courier New', 12,), width=16, heigh=1)
    Bereich_checkbox5.grid(row=0, column=7, padx='0', pady='0', sticky='nw')

    Bereich_checkbox6 = HAUPTMENUE.Checkbutton(GesetzeUmrandung, text="Gartenbereich", fg='#2F4F4F', bg='#D8D8D8',
                                               font=('Courier New', 12,), width=15, heigh=1)
    Bereich_checkbox6.grid(row=0, column=8, padx='2', pady='0', sticky='nw')

    Bereich_checkbox7 = HAUPTMENUE.Checkbutton(GesetzeUmrandung, text="Kellerbereich", fg='#2F4F4F', bg='#D8D8D8',
                                               font=('Courier New', 12,), width=13, heigh=1)
    Bereich_checkbox7.grid(row=1, column=0, padx='5', pady='0', sticky='nw')

    Bereich_checkbox8 = HAUPTMENUE.Checkbutton(GesetzeUmrandung, text="Müllbereich", fg='#2F4F4F', bg='#D8D8D8',
                                               font=('Courier New', 12,), width=11, heigh=1)
    Bereich_checkbox8.grid(row=1, column=1, padx='0', pady='0', sticky='nw')

    Bereich_checkbox9 = HAUPTMENUE.Checkbutton(GesetzeUmrandung, text="Imbissbereich", fg='#2F4F4F', bg='#D8D8D8',
                                               font=('Courier New', 12,), width=13, heigh=1)
    Bereich_checkbox9.grid(row=1, column=2, padx='0', pady='0', sticky='nw')

    Bereich_checkbox10 = HAUPTMENUE.Checkbutton(GesetzeUmrandung, text="Tresenbereich", fg='#2F4F4F', bg='#D8D8D8',
                                                font=('Courier New', 12,), width=13, heigh=1)
    Bereich_checkbox10.grid(row=1, column=3, padx='0', pady='0', sticky='nw')

    Bereich_checkbox11 = HAUPTMENUE.Checkbutton(GesetzeUmrandung, text="Herstellung/Lager", fg='#2F4F4F', bg='#D8D8D8',
                                                font=('Courier New', 12,), width=17, heigh=1)
    Bereich_checkbox11.grid(row=1, column=4, padx='0', pady='0', sticky='nw')

    Bereich_checkbox12 = HAUPTMENUE.Checkbutton(GesetzeUmrandung, text="Ges. Restaurant", fg='#2F4F4F', bg='#D8D8D8',
                                                font=('Courier New', 12,), width=15, heigh=1)
    Bereich_checkbox12.grid(row=1, column=5, padx='0', pady='0', sticky='nw')

    Bereich_checkbox13 = HAUPTMENUE.Checkbutton(GesetzeUmrandung, text=" ?", fg='#2F4F4F', bg='#D8D8D8',
                                                font=('Courier New', 12,), width=2, heigh=1)
    Bereich_checkbox13.grid(row=1, column=6, padx='0', pady='0', sticky='nw')
    Bereichcheckboxtext = Entry(GesetzeUmrandung, width=80, font=('Courier New', 12))
    Bereichcheckboxtext.grid(row=1, column=6, padx='15', pady='3', sticky='ne', columnspan=3)

    #                       UMRANDUNG FÜR GETROFFENE MASSNAHMEN ERSTELLEN

    MassnahmenUmrandung = HAUPTMENUE.Frame(window, bd=2, width=1301, heigh=58, bg='#BDBDBD', borderwidth=2,
                                           relief="groove", )
    MassnahmenUmrandung.grid(row=5, column=0, padx='5', pady='3', sticky='nw', columnspan=1)

    #                  **********************************************
    #                  ********  CHECKBOXEN FÜR MAßNAHMEN   *********
    #                  **********************************************

    Massnahmen_checkbox1 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Inspektion/Wartung", fg='#2F4F4F',
                                                  bg='#BDBDBD', font=('Courier New', 12,), width=18, heigh=1)
    Massnahmen_checkbox1.grid(row=0, column=0, padx='5', pady='0', sticky='nw')

    Massnahmen_checkbox2 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Vorb.Schädlingsbekämpfung", fg='#2F4F4F',
                                                  bg='#BDBDBD', font=('Courier New', 12,), width=25, heigh=1)
    Massnahmen_checkbox2.grid(row=0, column=1, padx='0', pady='0', sticky='nw')

    Massnahmen_checkbox3 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Erneuerung Köderfallen", fg='#2F4F4F',
                                                  bg='#BDBDBD', font=('Courier New', 12,), width=22, heigh=1)
    Massnahmen_checkbox3.grid(row=0, column=2, padx='0', pady='0', sticky='nw')

    Massnahmen_checkbox4 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Einrichtung Köderfallen", fg='#2F4F4F',
                                                  bg='#BDBDBD', font=('Courier New', 12,), width=23, heigh=1)
    Massnahmen_checkbox4.grid(row=0, column=3, padx='0', pady='0', sticky='nw')

    Massnahmen_checkbox5 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Rodentizidbehandlung", fg='#2F4F4F',
                                                  bg='#BDBDBD', font=('Courier New', 12,), width=20, heigh=1)
    Massnahmen_checkbox5.grid(row=0, column=4, padx='0', pady='0', sticky='nw')

    Massnahmen_checkbox6 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Gelbehandlung", fg='#2F4F4F', bg='#BDBDBD',
                                                  font=('Courier New', 12,), width=13, heigh=1)
    Massnahmen_checkbox6.grid(row=0, column=5, padx='3', pady='0', sticky='nw')

    Massnahmen_checkbox7 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Stäubeverfahren", fg='#2F4F4F',
                                                  bg='#BDBDBD', font=('Courier New', 12,), width=15, heigh=1)
    Massnahmen_checkbox7.grid(row=1, column=0, padx='5', pady='0', sticky='nw')

    Massnahmen_checkbox8 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Schaumbehandlung", fg='#2F4F4F',
                                                  bg='#BDBDBD', font=('Courier New', 12,), width=16, heigh=1)
    Massnahmen_checkbox8.grid(row=1, column=1, padx='0', pady='0', sticky='nw')

    Massnahmen_checkbox9 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Wärmebehandlung", fg='#2F4F4F',
                                                  bg='#BDBDBD', font=('Courier New', 12,), width=15, heigh=1)
    Massnahmen_checkbox9.grid(row=1, column=2, padx='0', pady='0', sticky='nw')

    Massnahmen_checkbox10 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Mineralien/Plankton", fg='#2F4F4F',
                                                   bg='#BDBDBD', font=('Courier New', 12,), width=19, heigh=1)
    Massnahmen_checkbox10.grid(row=1, column=3, padx='0', pady='0', sticky='nw')

    Massnahmen_checkbox11 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Granulatbehandlung", fg='#2F4F4F',
                                                   bg='#BDBDBD', font=('Courier New', 12,), width=18, heigh=1)
    Massnahmen_checkbox11.grid(row=1, column=4, padx='0', pady='0', sticky='nw')

    Massnahmen_checkbox12 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Sprüh-/Spritzbehandlung      ",
                                                   fg='#2F4F4F', bg='#BDBDBD', font=('Courier New', 12,), width=29,
                                                   heigh=1)
    Massnahmen_checkbox12.grid(row=1, column=5, padx='3', pady='0', sticky='nw')

    Massnahmen_checkbox13 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Aerosolbehandlung", fg='#2F4F4F',
                                                   bg='#BDBDBD', font=('Courier New', 12,), width=17, heigh=1)
    Massnahmen_checkbox13.grid(row=2, column=0, padx='5', pady='0', sticky='nw')

    Massnahmen_checkbox14 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Ökologisches Verfahren", fg='#2F4F4F',
                                                   bg='#BDBDBD', font=('Courier New', 12,), width=22, heigh=1)
    Massnahmen_checkbox14.grid(row=2, column=1, padx='0', pady='0', sticky='nw')

    Massnahmen_checkbox15 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Reinigung/Desinfektion", fg='#2F4F4F',
                                                   bg='#BDBDBD', font=('Courier New', 12,), width=22, heigh=1)
    Massnahmen_checkbox15.grid(row=2, column=2, padx='0', pady='0', sticky='nw')

    Massnahmen_checkbox16 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Umstellung Toxisch", fg='#2F4F4F',
                                                   bg='#BDBDBD', font=('Courier New', 12,), width=18, heigh=1)
    Massnahmen_checkbox16.grid(row=2, column=3, padx='0', pady='0', sticky='nw')

    Massnahmen_checkbox17 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Umstellung auf Non-Tox", fg='#2F4F4F',
                                                   bg='#BDBDBD', font=('Courier New', 12,), width=22, heigh=1)
    Massnahmen_checkbox17.grid(row=2, column=4, padx='0', pady='0', sticky='nw')

    Massnahmen_checkbox18 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text=" ?", fg='#2F4F4F', bg='#BDBDBD',
                                                   font=('Courier New', 12,), width=2, heigh=1)
    Massnahmen_checkbox18.grid(row=2, column=5, padx='3', pady='0', sticky='nw')

    Massnahmen_checkbox18text = Entry(MassnahmenUmrandung, width=39, )
    Massnahmen_checkbox18text.grid(row=2, column=5, padx='15', pady='3', sticky='ne')

    #                       UMRANDUNG FÜR BEFALLSANALYSE UND MATERIALEINSATZ ERSTELLEN
    BefallanalyseUmrandung = HAUPTMENUE.Frame(window, bd=2, width=1301, heigh=58, bg='#BDBDBD', borderwidth=2,
                                              relief="groove", )
    BefallanalyseUmrandung.grid(row=6, column=0, padx='5', pady='3', sticky='nw', columnspan=1)

    #                     **********************************************
    #                     ********  BEREICH/CHECKBOXEN BEFALLSANALYSE  *
    #                     **********************************************

    #                     COMBOBOXEN UM BEFALLSSTÄRKE-HINWEISE ABZUFRAGEN

    Befallstaerke_label: Label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="Befall", fg='#2F4F4F', bg='#BDBDBD',
                                                  font=('Courier New', 12,), width=6)
    Befallstaerke_label.grid(row=0, column=0, padx='10', pady='13', sticky='nw')

    Befallstaerke = ttk.Combobox(BefallanalyseUmrandung,
                                 values=[" ", "Stärke:ohne", "Stärke:leicht", "Stärke:leicht-mittel", "Stärke:mittel",
                                         "Stärke:mittel-schwer", "Stärke:schwer"], font=('Courier New', 10), width=25)
    Befallstaerke.grid(row=0, column=1, padx='10', pady='10', sticky='nw')
    Befallstaerke.current(0)
    #                  ***********************************************************

    Befallzeichen1_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="Hinweis", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('Courier New', 12,), width=7, heigh=1)
    Befallzeichen1_label.grid(row=2, column=0, padx='10', pady='0', sticky='nw')

    Befallzeichen1 = ttk.Combobox(BefallanalyseUmrandung,
                                  values=["AUS LISTE AUSLESEN ", "Vorbekämpfung mit reinnehmen", "RKS angefressen",
                                          "RKS leergefressen", "MKS angefressen", "MKS leergefressen",
                                          "Kotspuren gesichtet", "Löcher gesichtet", "Fraßspuren gesichtet"
                                                                                     "Laufwege gesichtet",
                                          "Tiere gesichtet", "Tote Tiere gesichtet", "Larven/Eier/Nymphen gesichtet",
                                          "Kunde hat Tiere gesichtet"], font=('Courier New', 10), width=25)
    Befallzeichen1.grid(row=2, column=1, padx='10', pady='0', sticky='nw')
    Befallzeichen1.current(0)

    Befallzeichen1x_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                             font=('Courier New', 12,), width=1, heigh=1)
    Befallzeichen1x_label.grid(row=2, column=2, padx='5', pady='0', sticky='nw')
    Befallzeichen1x = Entry(BefallanalyseUmrandung, width=4, justify=RIGHT, font=('Courier New', 12))
    Befallzeichen1x.grid(row=2, column=3, padx='5', pady='0', sticky='nw')

    #                ***********************************************************

    Befallzeichen2_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="Hinweis", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('Courier New', 12,), width=7, heigh=1)
    Befallzeichen2_label.grid(row=3, column=0, padx='10', pady='0', sticky='nw')

    Befallzeichen2 = ttk.Combobox(BefallanalyseUmrandung,
                                  values=[" ", "RKS angefressen", "RKS leergefressen", "MKS angefressen",
                                          "MKS leergefressen", "Kotspuren gesichtet", "Löcher gesichtet",
                                          "Fraßspuren gesichtet"
                                          "Laufwege gesichtet", "Tiere gesichtet", "Tote Tiere gesichtet",
                                          "Larven/Eier/Nymphen gesichtet", "Kunde hat Tiere gesichtet"],
                                  font=('Courier New', 10), width=25)
    Befallzeichen2.grid(row=3, column=1, padx='10', pady='0', sticky='nw')
    Befallzeichen2.current(0)

    Befallzeichen2x_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                             font=('Courier New', 12,), width=1, heigh=1)
    Befallzeichen2x_label.grid(row=3, column=2, padx='5', pady='0', sticky='nw')
    Befallzeichen2x = Entry(BefallanalyseUmrandung, width=4, justify=RIGHT, font=('Courier New', 12))
    Befallzeichen2x.grid(row=3, column=3, padx='5', pady='0', sticky='nw')

    #                  ***********************************************************

    Befallzeichen3_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="Hinweis", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('Courier New', 12,), width=7, heigh=1)
    Befallzeichen3_label.grid(row=4, column=0, padx='10', pady='0', sticky='nw')

    Befallzeichen3 = ttk.Combobox(BefallanalyseUmrandung,
                                  values=[" ", "RKS angefressen", "RKS leergefressen", "MKS angefressen",
                                          "MKS leergefressen", "Kotspuren gesichtet", "Löcher gesichtet",
                                          "Fraßspuren gesichtet"
                                          "Laufwege gesichtet", "Tiere gesichtet", "Tote Tiere gesichtet",
                                          "Larven/Eier/Nymphen gesichtet", "Kunde hat Tiere gesichtet"],
                                  font=('Courier New', 10), width=25)
    Befallzeichen3.grid(row=4, column=1, padx='10', pady='0', sticky='nw')
    Befallzeichen3.current(0)

    Befallzeichen3x_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                             font=('Courier New', 12,), width=1, heigh=1)
    Befallzeichen3x_label.grid(row=4, column=2, padx='5', pady='0', sticky='nw')
    Befallzeichen3x = Entry(BefallanalyseUmrandung, width=4, justify=RIGHT, font=('Courier New', 12))
    Befallzeichen3x.grid(row=4, column=3, padx='5', pady='0', sticky='nw')

    #                  ***********************************************************

    Befallzeichen4_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="Hinweis", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('Courier New', 12,), width=7, heigh=1)
    Befallzeichen4_label.grid(row=5, column=0, padx='10', pady='0', sticky='nw')

    Befallzeichen4 = ttk.Combobox(BefallanalyseUmrandung,
                                  values=[" ", "RKS angefressen", "RKS leergefressen", "MKS angefressen",
                                          "MKS leergefressen", "Kotspuren gesichtet", "Löcher gesichtet",
                                          "Fraßspuren gesichtet"
                                          "Laufwege gesichtet", "Tiere gesichtet", "Tote Tiere gesichtet",
                                          "Larven/Eier/Nymphen gesichtet", "Kunde hat Tiere gesichtet"],
                                  font=('Courier New', 10), width=25)
    Befallzeichen4.grid(row=5, column=1, padx='10', pady='0', sticky='nw')
    Befallzeichen4.current(0)

    Befallzeichen4x_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                             font=('Courier New', 12,), width=1, heigh=1)
    Befallzeichen4x_label.grid(row=5, column=2, padx='5', pady='0', sticky='nw')
    Befallzeichen4x = Entry(BefallanalyseUmrandung, width=4, justify=RIGHT, font=('Courier New', 12))
    Befallzeichen4x.grid(row=5, column=3, padx='5', pady='0', sticky='nw')

    #                  ***********************************************************

    Befallzeichen5_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="Hinweis", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('Courier New', 12,), width=7, heigh=1)
    Befallzeichen5_label.grid(row=6, column=0, padx='10', pady='0', sticky='nw')

    Befallzeichen5 = ttk.Combobox(BefallanalyseUmrandung,
                                  values=[" ", "RKS angefressen", "RKS leergefressen", "MKS angefressen",
                                          "MKS leergefressen", "Kotspuren gesichtet", "Löcher gesichtet",
                                          "Fraßspuren gesichtet"
                                          "Laufwege gesichtet", "Tiere gesichtet", "Tote Tiere gesichtet",
                                          "Larven/Eier/Nymphen gesichtet", "Kunde hat Tiere gesichtet"],
                                  font=('Courier New', 10), width=25)
    Befallzeichen5.grid(row=6, column=1, padx='10', pady='0', sticky='nw')
    Befallzeichen5.current(0)

    Befallzeichen5x_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                             font=('Courier New', 12,), width=1, heigh=1)
    Befallzeichen5x_label.grid(row=6, column=2, padx='5', pady='0', sticky='nw')
    Befallzeichen5x = Entry(BefallanalyseUmrandung, width=4, justify=RIGHT, font=('Courier New', 12))
    Befallzeichen5x.grid(row=6, column=3, padx='5', pady='0', sticky='nw')

    #                    ***********************************************************

    Befallzeichen6_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="Hinweis", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('Courier New', 12,), width=7, heigh=1)
    Befallzeichen6_label.grid(row=7, column=0, padx='10', pady='0', sticky='nw')
    Befallzeichen6 = Entry(BefallanalyseUmrandung, width=36, font=('Courier New', 12))
    Befallzeichen6.grid(row=7, column=1, padx='10', pady='0', sticky='nw')
    Befallzeichen6x_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                             font=('Courier New', 12,), width=1, heigh=1)
    Befallzeichen6x_label.grid(row=7, column=2, padx='5', pady='0', sticky='nw')
    Befallzeichen6x = Entry(BefallanalyseUmrandung, width=4, justify=RIGHT, font=('Courier New', 12))
    Befallzeichen6x.grid(row=7, column=3, padx='5', pady='0', sticky='nw')

    Befallzeichen7_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="Hinweis", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('Courier New', 12,), width=7, heigh=1)
    Befallzeichen7_label.grid(row=8, column=0, padx='10', pady='0', sticky='nw')
    Befallzeichen7 = Entry(BefallanalyseUmrandung, width=36, font=('Courier New', 12))
    Befallzeichen7.grid(row=8, column=1, padx='10', pady='0', sticky='nw')
    Befallzeichen7x_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                             font=('Courier New', 12,), width=1, heigh=1)
    Befallzeichen7x_label.grid(row=8, column=2, padx='5', pady='0', sticky='nw')
    Befallzeichen7x = Entry(BefallanalyseUmrandung, width=4, justify=RIGHT, font=('Courier New', 12))
    Befallzeichen7x.grid(row=8, column=3, padx='5', pady='0', sticky='nw')

    # ******************************************************************************************************************
    # ************************   BEREICH MATERIALEINSATZ ***************************************************************
    # ******************************************************************************************************************

    BefallzeichenLeer_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text=" ", fg='#2F4F4F', bg='#BDBDBD',
                                               font=('Courier New', 12,), width=7, heigh=1)
    BefallzeichenLeer_label.grid(row=9, column=0, padx='10', pady='0', sticky='nw')

    materialauswahl1_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="Pos. 1 ", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('Courier New', 12,), width=7, heigh=1)
    materialauswahl1_label.grid(row=10, column=0, padx='10', pady='0', sticky='nw')
    materialauswahl1 = ttk.Combobox(BefallanalyseUmrandung,
                                    values=["MUSS ÜBER LISTE MATERIALVERWALTUNG EINGELESEN WERDENt"],
                                    font=('Courier New', 10), width=25)
    materialauswahl1.grid(row=10, column=1, padx='10', pady='0', sticky='nw')
    materialauswahl1.current(0)

    materialauswahltext1_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                                  font=('Courier New', 12,), width=1, heigh=1)
    materialauswahltext1_label.grid(row=10, column=2, padx='5', pady='0', sticky='nw')
    materialauswahlzaehlertext1 = Entry(BefallanalyseUmrandung, width=4, justify=RIGHT, font=('Courier New', 12))
    materialauswahlzaehlertext1.grid(row=10, column=3, padx='5', pady='0', sticky='nw')

    #                       ***********************************************************

    materialauswahl2_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="Pos. 2 ", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('Courier New', 12,), width=7, heigh=1)
    materialauswahl2_label.grid(row=11, column=0, padx='10', pady='0', sticky='nw')

    materialauswahl2 = ttk.Combobox(BefallanalyseUmrandung,
                                    values=[" ", "MUSS ÜBER LISTE MATERIALVERWALTUNG EINGELESEN WERDENt"],
                                    font=('Courier New', 10), width=25)
    materialauswahl2.grid(row=11, column=1, padx='10', pady='0', sticky='nw')
    materialauswahl2.current(0)

    materialauswahltext2_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                                  font=('Courier New', 12,), width=1, heigh=1)
    materialauswahltext2_label.grid(row=11, column=2, padx='5', pady='0', sticky='nw')
    materialauswahlzaehlertext2 = Entry(BefallanalyseUmrandung, width=4, justify=RIGHT, font=('Courier New', 12))
    materialauswahlzaehlertext2.grid(row=11, column=3, padx='5', pady='0', sticky='nw')

    #                    ***********************************************************

    materialauswahl3_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="Pos. 3 ", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('Courier New', 12,), width=7, heigh=1)
    materialauswahl3_label.grid(row=12, column=0, padx='10', pady='0', sticky='nw')

    materialauswahl3 = ttk.Combobox(BefallanalyseUmrandung,
                                    values=[" ", "MUSS ÜBER LISTE MATERIALVERWALTUNG EINGELESEN WERDENt"],
                                    font=('Courier New', 10), width=25)
    materialauswahl3.grid(row=12, column=1, padx='10', pady='0', sticky='nw')
    materialauswahl3.current(0)

    materialauswahltext3_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                                  font=('Courier New', 12,), width=1, heigh=1)
    materialauswahltext3_label.grid(row=12, column=2, padx='5', pady='0', sticky='nw')
    materialauswahlzaehlertext3 = Entry(BefallanalyseUmrandung, width=4, justify=RIGHT, font=('Courier New', 12))
    materialauswahlzaehlertext3.grid(row=12, column=3, padx='5', pady='0', sticky='nw')

    #                      ***********************************************************

    materialauswahl4_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="Pos. 4 ", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('Courier New', 12,), width=7, heigh=1)
    materialauswahl4_label.grid(row=13, column=0, padx='10', pady='0', sticky='nw')

    materialauswahl4 = ttk.Combobox(BefallanalyseUmrandung,
                                    values=[" ", "MUSS ÜBER LISTE MATERIALVERWALTUNG EINGELESEN WERDENt"],
                                    font=('Courier New', 10), width=25)
    materialauswahl4.grid(row=13, column=1, padx='10', pady='0', sticky='nw')
    materialauswahl4.current(0)

    materialauswahltext4_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                                  font=('Courier New', 12,), width=1, heigh=1)
    materialauswahltext4_label.grid(row=13, column=2, padx='5', pady='0', sticky='nw')
    materialauswahlzaehlertext4 = Entry(BefallanalyseUmrandung, width=4, justify=RIGHT, font=('Courier New', 12))
    materialauswahlzaehlertext4.grid(row=13, column=3, padx='5', pady='0', sticky='nw')

    #                     ***********************************************************

    materialauswahl5_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="Pos. 5 ", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('Courier New', 12,), width=7, heigh=1)
    materialauswahl5_label.grid(row=14, column=0, padx='10', pady='0', sticky='nw')
    materialauswahltext5 = Entry(BefallanalyseUmrandung, width=36, font=('Courier New', 12))
    materialauswahltext5.grid(row=14, column=1, padx='10', pady='0', sticky='nw')
    materialauswahltext5_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                                  font=('Courier New', 12,), width=1, heigh=1)
    materialauswahltext5_label.grid(row=14, column=2, padx='5', pady='0', sticky='nw')
    materialauswahlzaehlertext5 = Entry(BefallanalyseUmrandung, width=4, justify=RIGHT, font=('Courier New', 12))
    materialauswahlzaehlertext5.grid(row=14, column=3, padx='5', pady='0', sticky='nw')

    #                     ***********************************************************

    materialauswahl6_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="Pos. 6 ", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('Courier New', 12,), width=7, heigh=1)
    materialauswahl6_label.grid(row=15, column=0, padx='10', pady='0', sticky='nw')
    materialauswahltext6 = Entry(BefallanalyseUmrandung, width=36, font=('Courier New', 12))
    materialauswahltext6.grid(row=15, column=1, padx='10', pady='0', sticky='nw')
    materialauswahltext6_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                                  font=('Courier New', 12,), width=1, heigh=1)
    materialauswahltext6_label.grid(row=15, column=2, padx='5', pady='0', sticky='nw')
    materialauswahlzaehlertext6 = Entry(BefallanalyseUmrandung, width=4, justify=RIGHT, font=('Courier New', 12))
    materialauswahlzaehlertext6.grid(row=15, column=3, padx='5', pady='0', sticky='nw')

    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # ************************    BEREICH BEZAHLUNG ERSTELLEN           ************************************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #                        RAHMEN FÜR ZAHLUNGS- UND RECHNUNGSSTELLUNG
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    ZahlungsRahmen0 = HAUPTMENUE.Frame(window, width=659, heigh=360, bg='#BDBDBD', borderwidth=2, relief="groove", )
    ZahlungsRahmen0.grid(row=6, column=0, padx='420', pady='3', sticky='nw', columnspan=5)
    AbrechnungRahmen = HAUPTMENUE.Frame(ZahlungsRahmen0, width=659, heigh=360, bg='#BDBDBD', borderwidth=2,
                                        relief="flat", )
    AbrechnungRahmen.grid(row=1, column=0, padx='0', pady='0', sticky='nw', columnspan=5)
    AbrechnungKopfzeile1_label = HAUPTMENUE.Label(AbrechnungRahmen, text="Nr.", fg='#2F4F4F', bg='#BDBDBD',
                                                  font=('Courier New', 11,), width=3, heigh=1)
    AbrechnungKopfzeile1_label.grid(row=0, column=0, padx='5', pady='0', sticky='nw', columnspan=1)
    AbrechnungKopfzeile2_label = HAUPTMENUE.Label(AbrechnungRahmen, text=" Posten", fg='#2F4F4F', bg='#BDBDBD',
                                                  font=('Courier New', 11,), width=7, heigh=1)
    AbrechnungKopfzeile2_label.grid(row=0, column=1, padx='5', pady='0', sticky='nw', columnspan=1)
    AbrechnungKopfzeile3_label = HAUPTMENUE.Label(AbrechnungRahmen, text="Preis", fg='#2F4F4F', bg='#BDBDBD',
                                                  font=('Courier New', 11,), width=5, heigh=1)
    AbrechnungKopfzeile3_label.grid(row=0, column=4, padx='5', pady='0', sticky='nw', columnspan=1)
    AbrechnungKopfzeile4_label = HAUPTMENUE.Label(AbrechnungRahmen, text="X", fg='#2F4F4F', bg='#BDBDBD',
                                                  font=('Courier New', 11,), width=1, heigh=1)
    AbrechnungKopfzeile4_label.grid(row=0, column=6, padx='5', pady='0', sticky='ew', columnspan=1)
    AbrechnungKopfzeile5_label = HAUPTMENUE.Label(AbrechnungRahmen, text=" Summe", fg='#2F4F4F', bg='#BDBDBD',
                                                  font=('Courier New', 11,), width=6, heigh=1)
    AbrechnungKopfzeile5_label.grid(row=0, column=8, padx='5', pady='0', sticky='nw', columnspan=1)

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #                                      FELDER FÜR ABRECHNUNGSERSTELLUNG
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    PreisBehandlung_label = HAUPTMENUE.Label(AbrechnungRahmen, text="Behandlung €", fg='#2F4F4F', bg='#BDBDBD',
                                             font=('Courier New', 12,), width=12, heigh=1)
    PreisBehandlung_label.grid(row=2, column=0, padx='5', pady='0', sticky='nw')
    PreisBehandlungPos = Entry(AbrechnungRahmen, width=36, font=('Courier New', 12))
    PreisBehandlungPos.grid(row=2, column=1, padx='10', pady='0', sticky='nw')
    PreisBehandlungText = Entry(AbrechnungRahmen, width=9, justify=RIGHT, font=('Courier New', 12))
    PreisBehandlungText.grid(row=2, column=4, padx='5', pady='0', sticky='nw')
    PreisBehandlungX_label = HAUPTMENUE.Label(AbrechnungRahmen, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('Courier New', 12,), width=1, heigh=1)
    PreisBehandlungX_label.grid(row=2, column=5, padx='3', pady='0', sticky='nw')
    PreisBehandlungMultiText = Entry(AbrechnungRahmen, width=4, justify=RIGHT, font=('Courier New', 12))
    PreisBehandlungMultiText.grid(row=2, column=6, padx='5', pady='0', sticky='nw')
    PreisBehandlung = _label = HAUPTMENUE.Label(AbrechnungRahmen, text="=", fg='#2F4F4F', bg='#BDBDBD',
                                                font=('Courier New', 12,), width=1, heigh=1)
    PreisBehandlung = _label.grid(row=2, column=7, padx='3', pady='0', sticky='nw')
    PreisBehandlungNettoText = Entry(AbrechnungRahmen, width=9, justify=RIGHT, font=('Courier New', 12))
    PreisBehandlungNettoText.grid(row=2, column=8, padx='10', pady='0', sticky='nw')

    PreisBehandlung1_label = HAUPTMENUE.Label(AbrechnungRahmen, text="Behandlung €", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('Courier New', 12,), width=12, heigh=1)
    PreisBehandlung1_label.grid(row=3, column=0, padx='5', pady='0', sticky='nw')
    PreisBehandlung1Pos = Entry(AbrechnungRahmen, width=36, font=('Courier New', 12))
    PreisBehandlung1Pos.grid(row=3, column=1, padx='10', pady='0', sticky='nw')
    PreisBehandlung1Text = Entry(AbrechnungRahmen, width=9, justify=RIGHT, font=('Courier New', 12))
    PreisBehandlung1Text.grid(row=3, column=4, padx='5', pady='0', sticky='nw')
    PreisBehandlung1X_label = HAUPTMENUE.Label(AbrechnungRahmen, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                               font=('Courier New', 12,), width=1, heigh=1)
    PreisBehandlung1X_label.grid(row=3, column=5, padx='3', pady='0', sticky='nw')
    PreisBehandlung1MultiText = Entry(AbrechnungRahmen, width=4, justify=RIGHT, font=('Courier New', 12))
    PreisBehandlung1MultiText.grid(row=3, column=6, padx='5', pady='0', sticky='nw')
    PreisBehandlung1 = _label = HAUPTMENUE.Label(AbrechnungRahmen, text="=", fg='#2F4F4F', bg='#BDBDBD',
                                                 font=('Courier New', 12,), width=1, heigh=1)
    PreisBehandlung1 = _label.grid(row=3, column=7, padx='3', pady='0', sticky='nw')
    PreisBehandlung1NettoText = Entry(AbrechnungRahmen, width=9, justify=RIGHT, font=('Courier New', 12))
    PreisBehandlung1NettoText.grid(row=3, column=8, padx='10', pady='0', sticky='nw')

    PreisBehandlung2_label = HAUPTMENUE.Label(AbrechnungRahmen, text="Behandlung €", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('Courier New', 12,), width=12, heigh=1)
    PreisBehandlung2_label.grid(row=4, column=0, padx='5', pady='0', sticky='nw')
    PreisBehandlung2Pos = Entry(AbrechnungRahmen, width=36, font=('Courier New', 12))
    PreisBehandlung2Pos.grid(row=4, column=1, padx='10', pady='0', sticky='nw')
    PreisBehandlung2Text = Entry(AbrechnungRahmen, width=9, justify=RIGHT, font=('Courier New', 12))
    PreisBehandlung2Text.grid(row=4, column=4, padx='5', pady='0', sticky='nw')
    PreisBehandlung2X_label = HAUPTMENUE.Label(AbrechnungRahmen, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                               font=('Courier New', 12,), width=1, heigh=1)
    PreisBehandlung2X_label.grid(row=4, column=5, padx='3', pady='0', sticky='nw')
    PreisBehandlung2MultiText = Entry(AbrechnungRahmen, width=4, justify=RIGHT, font=('Courier New', 12))
    PreisBehandlung2MultiText.grid(row=4, column=6, padx='5', pady='0', sticky='nw')
    PreisBehandlung2 = _label = HAUPTMENUE.Label(AbrechnungRahmen, text="=", fg='#2F4F4F', bg='#BDBDBD',
                                                 font=('Courier New', 12,), width=1, heigh=1)
    PreisBehandlung2 = _label.grid(row=4, column=7, padx='3', pady='0', sticky='nw')
    PreisBehandlung2NettoText = Entry(AbrechnungRahmen, width=9, justify=RIGHT, font=('Courier New', 12))
    PreisBehandlung2NettoText.grid(row=4, column=8, padx='10', pady='0', sticky='nw')

    PreisBehandlung3_label = HAUPTMENUE.Label(AbrechnungRahmen, text="Behandlung €", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('Courier New', 12,), width=12, heigh=1)
    PreisBehandlung3_label.grid(row=5, column=0, padx='5', pady='0', sticky='nw')
    PreisBehandlung3Pos = Entry(AbrechnungRahmen, width=36, font=('Courier New', 12))
    PreisBehandlung3Pos.grid(row=5, column=1, padx='10', pady='0', sticky='nw')
    PreisBehandlung3Text = Entry(AbrechnungRahmen, width=9, justify=RIGHT, font=('Courier New', 12))
    PreisBehandlung3Text.grid(row=5, column=4, padx='5', pady='0', sticky='nw')
    PreisBehandlung3X_label = HAUPTMENUE.Label(AbrechnungRahmen, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                               font=('Courier New', 12,), width=1, heigh=1)
    PreisBehandlung3X_label.grid(row=5, column=5, padx='3', pady='0', sticky='nw')
    PreisBehandlung3MultiText = Entry(AbrechnungRahmen, width=4, justify=RIGHT, font=('Courier New', 12))
    PreisBehandlung3MultiText.grid(row=5, column=6, padx='5', pady='0', sticky='nw')
    PreisBehandlung3 = _label = HAUPTMENUE.Label(AbrechnungRahmen, text="=", fg='#2F4F4F', bg='#BDBDBD',
                                                 font=('Courier New', 12,), width=1, heigh=1)
    PreisBehandlung3 = _label.grid(row=5, column=7, padx='3', pady='0', sticky='nw')
    PreisBehandlung3NettoText = Entry(AbrechnungRahmen, width=9, justify=RIGHT, font=('Courier New', 12))
    PreisBehandlung3NettoText.grid(row=5, column=8, padx='10', pady='0', sticky='nw')

    PreisBehandlung3leer_label = HAUPTMENUE.Label(AbrechnungRahmen, text=" ", fg='#2F4F4F', bg='#BDBDBD',
                                                  font=('Courier New', 12,), width=12, heigh=1)
    PreisBehandlung3leer_label.grid(row=7, column=0, padx='5', pady='0', sticky='nw')

    PreisLohn_label = HAUPTMENUE.Label(AbrechnungRahmen, text="Lohn       €", fg='#2F4F4F', bg='#BDBDBD',
                                       font=('Courier New', 12,), width=12, heigh=1)
    PreisLohn_label.grid(row=8, column=0, padx='5', pady='0', sticky='nw')
    PreisLohnPos = Entry(AbrechnungRahmen, width=36, font=('Courier New', 12))
    PreisLohnPos.grid(row=8, column=1, padx='10', pady='0', sticky='nw')
    PreisLohnText = Entry(AbrechnungRahmen, width=9, justify=RIGHT, font=('Courier New', 12))
    PreisLohnText.grid(row=8, column=4, padx='5', pady='0', sticky='nw')
    PreisLohnX_label = HAUPTMENUE.Label(AbrechnungRahmen, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                        font=('Courier New', 12,), width=1, heigh=1)
    PreisLohnX_label.grid(row=8, column=5, padx='3', pady='0', sticky='nw')
    PreisLohnMultiText = Entry(AbrechnungRahmen, width=4, justify=RIGHT, font=('Courier New', 12))
    PreisLohnMultiText.grid(row=8, column=6, padx='5', pady='0', sticky='nw')
    PreisLohn = _label = HAUPTMENUE.Label(AbrechnungRahmen, text="=", fg='#2F4F4F', bg='#BDBDBD',
                                          font=('Courier New', 12,), width=1, heigh=1)
    PreisLohn = _label.grid(row=8, column=7, padx='3', pady='0', sticky='nw')
    PreisLohNettoText = Entry(AbrechnungRahmen, width=9, justify=RIGHT, font=('Courier New', 12))
    PreisLohNettoText.grid(row=8, column=8, padx='10', pady='0', sticky='nw')

    PreisAnfahrt_label = HAUPTMENUE.Label(AbrechnungRahmen, text="Anfahrt    €", fg='#2F4F4F', bg='#BDBDBD',
                                          font=('Courier New', 12,), width=12, heigh=1)
    PreisAnfahrt_label.grid(row=9, column=0, padx='5', pady='0', sticky='nw')
    PreisAnfahrtPos = Entry(AbrechnungRahmen, width=36, font=('Courier New', 12))
    PreisAnfahrtPos.grid(row=9, column=1, padx='10', pady='0', sticky='nw')
    PreisAnfahrtText = Entry(AbrechnungRahmen, width=9, justify=RIGHT, font=('Courier New', 12))
    PreisAnfahrtText.grid(row=9, column=4, padx='5', pady='0', sticky='nw')
    PreisAnfahrtX_label = HAUPTMENUE.Label(AbrechnungRahmen, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                           font=('Courier New', 12,), width=1, heigh=1)
    PreisAnfahrtX_label.grid(row=9, column=5, padx='3', pady='0', sticky='nw')
    PreisAnfahrtMultiText = Entry(AbrechnungRahmen, width=4, justify=RIGHT, font=('Courier New', 12))
    PreisAnfahrtMultiText.grid(row=9, column=6, padx='5', pady='0', sticky='nw')
    PreisAnfahrt = _label = HAUPTMENUE.Label(AbrechnungRahmen, text="=", fg='#2F4F4F', bg='#BDBDBD',
                                             font=('Courier New', 12,), width=1, heigh=1)
    PreisAnfahrt = _label.grid(row=9, column=7, padx='3', pady='0', sticky='nw')
    PreisAnfahrtNettoText = Entry(AbrechnungRahmen, width=9, justify=RIGHT, font=('Courier New', 12))
    PreisAnfahrtNettoText.grid(row=9, column=8, padx='10', pady='0', sticky='nw')

    PreisBehandlung4leer_label = HAUPTMENUE.Label(AbrechnungRahmen, text=" ", fg='#2F4F4F', bg='#BDBDBD',
                                                  font=('Courier New', 12,), width=12, heigh=1)
    PreisBehandlung4leer_label.grid(row=10, column=0, padx='5', pady='0', sticky='nw')

    PreisPos1_label = HAUPTMENUE.Label(AbrechnungRahmen, text="Pos.1      €", fg='#2F4F4F', bg='#BDBDBD',
                                       font=('Courier New', 12,), width=12, heigh=1)
    PreisPos1_label.grid(row=11, column=0, padx='5', pady='0', sticky='nw')
    PreisPos1Pos = Entry(AbrechnungRahmen, width=36, font=('Courier New', 12))
    PreisPos1Pos.grid(row=11, column=1, padx='10', pady='0', sticky='nw')
    PreisPos1Text = Entry(AbrechnungRahmen, width=9, justify=RIGHT, font=('Courier New', 12))
    PreisPos1Text.grid(row=11, column=4, padx='5', pady='0', sticky='nw')
    PreisPos1TextX_label = HAUPTMENUE.Label(AbrechnungRahmen, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('Courier New', 12,), width=1, heigh=1)
    PreisPos1TextX_label.grid(row=11, column=5, padx='3', pady='0', sticky='nw')
    PreisPos1MultiText = Entry(AbrechnungRahmen, width=4, justify=RIGHT, font=('Courier New', 12))
    PreisPos1MultiText.grid(row=11, column=6, padx='5', pady='0', sticky='nw')
    PreisPos1Text = _label = HAUPTMENUE.Label(AbrechnungRahmen, text="=", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('Courier New', 12,), width=1, heigh=1)
    PreisPos1Text = _label.grid(row=11, column=7, padx='3', pady='0', sticky='nw')
    PreisPos1NettoText = Entry(AbrechnungRahmen, width=9, justify=RIGHT, font=('Courier New', 12))
    PreisPos1NettoText.grid(row=11, column=8, padx='10', pady='0', sticky='nw')

    PreisPos2_label = HAUPTMENUE.Label(AbrechnungRahmen, text="Pos.2      €", fg='#2F4F4F', bg='#BDBDBD',
                                       font=('Courier New', 12,), width=12, heigh=1)
    PreisPos2_label.grid(row=12, column=0, padx='5', pady='0', sticky='nw')
    PreisPos2Pos = Entry(AbrechnungRahmen, width=36, font=('Courier New', 12))
    PreisPos2Pos.grid(row=12, column=1, padx='10', pady='0', sticky='nw')
    PreisPos2Text = Entry(AbrechnungRahmen, width=9, justify=RIGHT, font=('Courier New', 12))
    PreisPos2Text.grid(row=12, column=4, padx='5', pady='0', sticky='nw')
    PreisPos2TextX_label = HAUPTMENUE.Label(AbrechnungRahmen, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('Courier New', 12,), width=1, heigh=1)
    PreisPos2TextX_label.grid(row=12, column=5, padx='3', pady='0', sticky='nw')
    PreisPos2MultiText = Entry(AbrechnungRahmen, width=4, justify=RIGHT, font=('Courier New', 12))
    PreisPos2MultiText.grid(row=12, column=6, padx='5', pady='0', sticky='nw')
    PreisPos2Text = _label = HAUPTMENUE.Label(AbrechnungRahmen, text="=", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('Courier New', 12,), width=1, heigh=1)
    PreisPos2Text = _label.grid(row=12, column=7, padx='3', pady='0', sticky='nw')
    PreisPos2NettoText = Entry(AbrechnungRahmen, width=9, justify=RIGHT, font=('Courier New', 12))
    PreisPos2NettoText.grid(row=12, column=8, padx='10', pady='0', sticky='nw')

    PreisPos3_label = HAUPTMENUE.Label(AbrechnungRahmen, text="Pos.3      €", fg='#2F4F4F', bg='#BDBDBD',
                                       font=('Courier New', 12,), width=12, heigh=1)
    PreisPos3_label.grid(row=13, column=0, padx='5', pady='0', sticky='nw')
    PreisPos3Pos = Entry(AbrechnungRahmen, width=36, font=('Courier New', 12))
    PreisPos3Pos.grid(row=13, column=1, padx='10', pady='0', sticky='nw')
    PreisPos3Text = Entry(AbrechnungRahmen, width=9, justify=RIGHT, font=('Courier New', 12))
    PreisPos3Text.grid(row=13, column=4, padx='5', pady='0', sticky='nw')
    PreisPos3TextX_label = HAUPTMENUE.Label(AbrechnungRahmen, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('Courier New', 12,), width=1, heigh=1)
    PreisPos3TextX_label.grid(row=13, column=5, padx='3', pady='0', sticky='nw')
    PreisPos3MultiText = Entry(AbrechnungRahmen, width=4, justify=RIGHT, font=('Courier New', 12))
    PreisPos3MultiText.grid(row=13, column=6, padx='5', pady='0', sticky='nw')
    PreisPos3Text = _label = HAUPTMENUE.Label(AbrechnungRahmen, text="=", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('Courier New', 12,), width=1, heigh=1)
    PreisPos3Text = _label.grid(row=13, column=7, padx='3', pady='0', sticky='nw')
    PreisPos3NettoText = Entry(AbrechnungRahmen, width=9, justify=RIGHT, font=('Courier New', 12))
    PreisPos3NettoText.grid(row=13, column=8, padx='10', pady='0', sticky='nw')

    PreisPos4_label = HAUPTMENUE.Label(AbrechnungRahmen, text="Pos.4      €", fg='#2F4F4F', bg='#BDBDBD',
                                       font=('Courier New', 12,), width=12, heigh=1)
    PreisPos4_label.grid(row=14, column=0, padx='5', pady='0', sticky='nw')
    PreisPos4Pos = Entry(AbrechnungRahmen, width=36, font=('Courier New', 12))
    PreisPos4Pos.grid(row=14, column=1, padx='10', pady='0', sticky='nw')
    PreisPos4Text = Entry(AbrechnungRahmen, width=9, justify=RIGHT, font=('Courier New', 12))
    PreisPos4Text.grid(row=14, column=4, padx='5', pady='0', sticky='nw')
    PreisPos4TextX_label = HAUPTMENUE.Label(AbrechnungRahmen, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('Courier New', 12,), width=1, heigh=1)
    PreisPos4TextX_label.grid(row=14, column=5, padx='3', pady='0', sticky='nw')
    PreisPos4MultiText = Entry(AbrechnungRahmen, width=4, justify=RIGHT, font=('Courier New', 12))
    PreisPos4MultiText.grid(row=14, column=6, padx='5', pady='0', sticky='nw')
    PreisPos4Text = _label = HAUPTMENUE.Label(AbrechnungRahmen, text="=", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('Courier New', 12,), width=1, heigh=1)
    PreisPos4Text = _label.grid(row=14, column=7, padx='3', pady='0', sticky='nw')
    PreisPos4NettoText = Entry(AbrechnungRahmen, width=9, justify=RIGHT, font=('Courier New', 12))
    PreisPos4NettoText.grid(row=14, column=8, padx='10', pady='0', sticky='nw')

    PreisPos5_label = HAUPTMENUE.Label(AbrechnungRahmen, text="Pos.5      €", fg='#2F4F4F', bg='#BDBDBD',
                                       font=('Courier New', 12,), width=12, heigh=1)
    PreisPos5_label.grid(row=17, column=0, padx='5', pady='0', sticky='nw')
    PreisPos5Pos = Entry(AbrechnungRahmen, width=36, font=('Courier New', 12))
    PreisPos5Pos.grid(row=17, column=1, padx='10', pady='0', sticky='nw')
    PreisPos5Text = Entry(AbrechnungRahmen, width=9, justify=RIGHT, font=('Courier New', 12))
    PreisPos5Text.grid(row=17, column=4, padx='5', pady='0', sticky='nw')
    PreisPos5TextX_label = HAUPTMENUE.Label(AbrechnungRahmen, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('Courier New', 12,), width=1, heigh=1)
    PreisPos5TextX_label.grid(row=17, column=5, padx='3', pady='0', sticky='nw')
    PreisPos5MultiText = Entry(AbrechnungRahmen, width=4, justify=RIGHT, font=('Courier New', 12))
    PreisPos5MultiText.grid(row=17, column=6, padx='5', pady='0', sticky='nw')
    PreisPos5Text = _label = HAUPTMENUE.Label(AbrechnungRahmen, text="=", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('Courier New', 12,), width=1, heigh=1)
    PreisPos5Text = _label.grid(row=17, column=7, padx='3', pady='0', sticky='nw')
    PreisPos5NettoText = Entry(AbrechnungRahmen, width=9, justify=RIGHT, font=('Courier New', 12))
    PreisPos5NettoText.grid(row=17, column=8, padx='10', pady='0', sticky='nw')

    PreisPos6_label = HAUPTMENUE.Label(AbrechnungRahmen, text="Pos.6      €", fg='#2F4F4F', bg='#BDBDBD',
                                       font=('Courier New', 12,), width=12, heigh=1)
    PreisPos6_label.grid(row=18, column=0, padx='5', pady='0', sticky='nw')
    PreisPos6Pos = Entry(AbrechnungRahmen, width=36, font=('Courier New', 12))
    PreisPos6Pos.grid(row=18, column=1, padx='10', pady='0', sticky='nw')
    PreisPos6Text = Entry(AbrechnungRahmen, width=9, justify=RIGHT, font=('Courier New', 12))
    PreisPos6Text.grid(row=18, column=4, padx='5', pady='0', sticky='nw')
    PreisPos6TextX_label = HAUPTMENUE.Label(AbrechnungRahmen, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('Courier New', 12,), width=1, heigh=1)
    PreisPos6TextX_label.grid(row=18, column=5, padx='3', pady='0', sticky='nw')
    PreisPos6MultiText = Entry(AbrechnungRahmen, width=4, justify=RIGHT, font=('Courier New', 12))
    PreisPos6MultiText.grid(row=18, column=6, padx='5', pady='0', sticky='nw')
    PreisPos6Text = _label = HAUPTMENUE.Label(AbrechnungRahmen, text="=", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('Courier New', 12,), width=1, heigh=1)
    PreisPos6Text = _label.grid(row=18, column=7, padx='3', pady='0', sticky='nw')
    PreisPos6NettoText = Entry(AbrechnungRahmen, width=9, justify=RIGHT, font=('Courier New', 12))
    PreisPos6NettoText.grid(row=18, column=8, padx='10', pady='0', sticky='nw')

    PreisSonstiges_label = HAUPTMENUE.Label(AbrechnungRahmen, text="Sonstiges  €", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('Courier New', 12,), width=12, heigh=1)
    PreisSonstiges_label.grid(row=19, column=0, padx='5', pady='0', sticky='nw')
    PreisSonstigesPos = Entry(AbrechnungRahmen, width=36, font=('Courier New', 12))
    PreisSonstigesPos.grid(row=19, column=1, padx='10', pady='0', sticky='nw')
    PreisSonstigesText = Entry(AbrechnungRahmen, width=9, justify=RIGHT, font=('Courier New', 12))
    PreisSonstigesText.grid(row=19, column=4, padx='5', pady='0', sticky='nw')
    PreisSonstigesTextX_label = HAUPTMENUE.Label(AbrechnungRahmen, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                                 font=('Courier New', 12,), width=1, heigh=1)
    PreisSonstigesTextX_label.grid(row=19, column=5, padx='3', pady='0', sticky='nw')
    PreisSonstigesMultiText = Entry(AbrechnungRahmen, width=4, justify=RIGHT, font=('Courier New', 12))
    PreisSonstigesMultiText.grid(row=19, column=6, padx='5', pady='0', sticky='nw')
    PreisSonstigesText = _label = HAUPTMENUE.Label(AbrechnungRahmen, text="=", fg='#2F4F4F', bg='#BDBDBD',
                                                   font=('Courier New', 12,), width=1, heigh=1)
    PreisSonstigesText = _label.grid(row=19, column=7, padx='3', pady='0', sticky='nw')
    PreisSonstigesNettoText = Entry(AbrechnungRahmen, width=9, justify=RIGHT, font=('Courier New', 12))
    PreisSonstigesNettoText.grid(row=19, column=8, padx='10', pady='0', sticky='nw')

    RechnungBearbeiter_label = HAUPTMENUE.Label(AbrechnungRahmen, text="Bearbeiter", fg='#2F4F4F', bg='#BDBDBD',
                                                font=('Courier New', 12,), width=10, heigh=1)
    RechnungBearbeiter_label.grid(row=2, column=9, padx='5', pady='0', sticky='nw')
    RechnungBearbeiterText = Entry(AbrechnungRahmen, width=25, font=('Courier New', 12))
    RechnungBearbeiterText.grid(row=2, column=10, padx='5', pady='0', sticky='nw')

    Erstellt_label = HAUPTMENUE.Label(AbrechnungRahmen, text="Rg.-Datum", fg='#2F4F4F', bg='#BDBDBD',
                                      font=('Courier New', 12,), width=9, heigh=1)
    Erstellt_label.grid(row=3, column=9, padx='5', pady='0', sticky='nw')
    ErstelltText = Entry(AbrechnungRahmen, width=10, justify=RIGHT, font=('Courier New', 12))
    ErstelltText.grid(row=3, column=10, padx='5', pady='0', sticky='nw')

    ErstelltRgNummer_label = HAUPTMENUE.Label(AbrechnungRahmen, text="Rg.Nr.", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('Courier New', 12,), width=6, heigh=1)
    ErstelltRgNummer_label.grid(row=4, column=9, padx='5', pady='0', sticky='nw')
    ErstelltRgNummerText = Entry(AbrechnungRahmen, width=9, justify=RIGHT, font=('Courier New', 12))
    ErstelltRgNummerText.grid(row=4, column=10, padx='5', pady='0', sticky='nw')

    ErstelltAuftragNummer_label = HAUPTMENUE.Label(AbrechnungRahmen, text="Auftrag-Nr.", fg='#2F4F4F', bg='#BDBDBD',
                                                   font=('Courier New', 12,), width=11, heigh=1)
    ErstelltAuftragNummer_label.grid(row=5, column=9, padx='5', pady='0', sticky='nw')
    ErstelltAuftragNummerText = Entry(AbrechnungRahmen, width=9, justify=RIGHT, font=('Courier New', 12))
    ErstelltAuftragNummerText.grid(row=5, column=10, padx='5', pady='0', sticky='nw')

    ErstelltZiel_label = HAUPTMENUE.Label(AbrechnungRahmen, text="Zahlungsziel", fg='#2F4F4F', bg='#BDBDBD',
                                          font=('Courier New', 12,), width=12, heigh=1)
    ErstelltZiel_label.grid(row=7, column=9, padx='5', pady='0', sticky='nw')
    ErstelltZielText = Entry(AbrechnungRahmen, width=10, justify=RIGHT, font=('Courier New', 12))
    ErstelltZielText.grid(row=7, column=10, padx='5', pady='0', sticky='nw')

    ErstelltBezahlt_label = HAUPTMENUE.Label(AbrechnungRahmen, text="Bezahlt", fg='#2F4F4F', bg='#BDBDBD',
                                             font=('Courier New', 12,), width=7, heigh=1)
    ErstelltBezahlt_label.grid(row=8, column=9, padx='5', pady='0', sticky='nw')
    ErstelltBezahltText = Entry(AbrechnungRahmen, width=10, justify=RIGHT, font=('Courier New', 12))
    ErstelltBezahltText.grid(row=8, column=10, padx='5', pady='0', sticky='nw')

    ErledigtVon_label = HAUPTMENUE.Label(AbrechnungRahmen, text="Von", fg='#2F4F4F', bg='#BDBDBD',
                                         font=('Courier New', 12,), width=3, heigh=1)
    ErledigtVon_label.grid(row=9, column=9, padx='5', pady='0', sticky='nw')
    ErledigtVonCombo = ttk.Combobox(AbrechnungRahmen, values=["Aus Liste Auslesen", "Frickmann", ],
                                    font=('Courier New', 10), width=20, )
    ErledigtVonCombo.grid(row=9, column=10, padx='5', pady='0', sticky='nw')
    ErledigtVonCombo.current(0)

    BehandeltAm_label = HAUPTMENUE.Label(AbrechnungRahmen, text="Beh.-Datum", fg='#2F4F4F', bg='#BDBDBD',
                                         font=('Courier New', 12,), width=10, heigh=1)
    BehandeltAm_label.grid(row=10, column=9, padx='5', pady='0', sticky='nw')
    BehandeltAmText = Entry(AbrechnungRahmen, width=10, justify=RIGHT, font=('Courier New', 12))
    BehandeltAmText.grid(row=10, column=10, padx='5', pady='0', sticky='nw')

    BehandeltKw_label = HAUPTMENUE.Label(AbrechnungRahmen, text="Beh. KW", fg='#2F4F4F', bg='#BDBDBD',
                                         font=('Courier New', 12,), width=8, heigh=1)
    BehandeltKw_label.grid(row=11, column=9, padx='0', pady='0', sticky='nw')
    BehandeltKwText = Entry(AbrechnungRahmen, width=2, justify=RIGHT, font=('Courier New', 12))
    BehandeltKwText.grid(row=11, column=10, padx='5', pady='0', sticky='nw')

    ErstelltNaechste_label = HAUPTMENUE.Label(AbrechnungRahmen, text="Nächste Beh.", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('Courier New', 12,), width=12, heigh=1)
    ErstelltNaechste_label.grid(row=12, column=9, padx='5', pady='0', sticky='nw')
    ErstelltNaechsteText = Entry(AbrechnungRahmen, width=10, justify=RIGHT, font=('Courier New', 12))
    ErstelltNaechsteText.grid(row=12, column=10, padx='5', pady='0', sticky='nw')

    ErstelltNaechsteKw_label = HAUPTMENUE.Label(AbrechnungRahmen, text="oder KW", fg='#2F4F4F', bg='#BDBDBD',
                                                font=('Courier New', 12,), width=8, heigh=1)
    ErstelltNaechsteKw_label.grid(row=13, column=9, padx='0', pady='0', sticky='nw')
    ErstelltNaechsteKwText = Entry(AbrechnungRahmen, width=2, justify=RIGHT, font=('Courier New', 12))
    ErstelltNaechsteKwText.grid(row=13, column=10, padx='5', pady='0', sticky='nw')

    ErstelltLeer_label = HAUPTMENUE.Label(AbrechnungRahmen, text=" ", fg='#2F4F4F', bg='#BDBDBD',
                                          font=('Courier New', 12,), width=8, heigh=1)
    ErstelltLeer_label.grid(row=14, column=9, padx='0', pady='0', sticky='nw')

    PreisNetto_label = HAUPTMENUE.Label(AbrechnungRahmen, text="Netto      €", fg='#2F4F4F', bg='#BDBDBD',
                                        font=('Courier New', 12,), width=12, heigh=1)
    PreisNetto_label.grid(row=17, column=9, padx='5', pady='0', sticky='nw')
    PreisNettoText = Entry(AbrechnungRahmen, width=9, justify=RIGHT, font=('Courier New', 12))
    PreisNettoText.grid(row=17, column=10, padx='5', pady='0', sticky='nw')

    PreisMwst_label = HAUPTMENUE.Label(AbrechnungRahmen, text="Mwst       €", fg='#2F4F4F', bg='#BDBDBD',
                                       font=('Courier New', 12,), width=12, heigh=1)
    PreisMwst_label.grid(row=18, column=9, padx='5', pady='0', sticky='nw')
    PreisMwstText = Entry(AbrechnungRahmen, width=9, justify=RIGHT, font=('Courier New', 12))
    PreisMwstText.grid(row=18, column=10, padx='5', pady='0', sticky='nw')

    PreisEndsumme_label = HAUPTMENUE.Label(AbrechnungRahmen, text="Endbetrag  €", fg='#2F4F4F', bg='#BDBDBD',
                                           font=('Courier New', 12,), width=12, heigh=1)
    PreisEndsumme_label.grid(row=19, column=9, padx='5', pady='0', sticky='nw')
    PreisEndsummeText = Entry(AbrechnungRahmen, width=9, justify=RIGHT, font=('Courier New', 12))
    PreisEndsummeText.grid(row=19, column=10, padx='5', pady='0', sticky='nw')

    AbrechnungRahmen1 = HAUPTMENUE.Frame(ZahlungsRahmen0, width=659, heigh=360, bg='#BDBDBD', borderwidth=2,
                                         relief="groove", )
    AbrechnungRahmen1.grid(row=1, column=11, padx='0', pady='0', sticky='nw', columnspan=2)
    AbrechnungRahmen1Leer1_label = HAUPTMENUE.Label(AbrechnungRahmen1, text=" ", fg='#2F4F4F', bg='#BDBDBD',
                                                    font=('Courier New', 12,), width=22, heigh=1)
    AbrechnungRahmen1Leer1_label.grid(row=0, column=0, padx='5', pady='0', sticky='nw')
    HautbuttonDrucken = HAUPTMENUE.Button(AbrechnungRahmen1, text="Drucken").grid(row=0, column=0, padx='10', pady='20',
                                                                                  sticky='ew')

    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # ****************EINLESEN DER SUCHLISTEN WENN NACHNAME ODER STRASSE FOCUS BEKOMMEN ********************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************
    def TexteFocusIn(event):
        widget = window.focus_get()
        # frame2_entry = ".!frame2.!entry" # Feld AUFTRAGGEGBER KDNUMMER
        frame2_entry2 = ".!frame2.!entry2"  # Feld AUFTRAGGEGBER NACHNAME
        frame2_entry5 = ".!frame2.!entry5"  # Feld AUFTRAGGEGBER STRASSE

    #                              WENN AUSTRAGGEBER NACHNAME FOCUS BEKOMMT

        if str(widget) == frame2_entry2:
            textauswertungvar = nachnameAgebervar.get()
            agebercalarliste()
            suchenbox.delete(0, END)
            i = 0
            kundepos = 0
            z = len(Kunde.objects(nachname__istartswith=textauswertungvar).scalar('nachname'))
            while i < z:
                #suchenbox.insert(END, Kunde.objects(nachname__istartswith=textauswertungvar).scalar('kunde_nr','nachname', 'vorname', str('strasse')).order_by('nachname')[kundepos])
                auftragkundennummer = Kunde.objects(nachname__istartswith=textauswertungvar).scalar('kunde_nr').order_by('nachname')[kundepos]
                auftragnachname = Kunde.objects(nachname__istartswith=textauswertungvar).scalar('nachname').order_by('nachname')[kundepos]
                auftragvorname = Kunde.objects(nachname__istartswith=textauswertungvar).scalar('vorname').order_by('nachname')[kundepos]
                auftragstrasse = Kunde.objects(nachname__istartswith=textauswertungvar).scalar('strasse').order_by('nachname')[kundepos]
                auftraghausnummer = Kunde.objects(nachname__istartswith=textauswertungvar).scalar('haus_nr').order_by('nachname')[kundepos]
                suchenbox.insert(END, auftragkundennummer.ljust(10)[0:10] + "  " + auftragnachname.ljust(35)[0:35] + "  " +
                                      auftragvorname.ljust(35)[0:35] + "  " +auftragstrasse + " " +  auftraghausnummer)
                i += 1
                kundepos += 1

    #                              WENN AUSTRAGGEBER NACHNAME FOCUS BEKOMMT

        if str(widget) == frame2_entry5:
            textauswertungvar = strAgebervar.get()
            agebercalarliste()
            suchenbox.delete(0, END)
            i = 0
            kundepos = 0
            z = len(Kunde.objects(strasse__istartswith=textauswertungvar).scalar('strasse'))
            while i < z:
                #suchenbox.insert(END, Kunde.objects(nachname__istartswith=textauswertungvar).scalar('kunde_nr','nachname', 'vorname', str('strasse')).order_by('nachname')[kundepos])
                auftragkundennummer = Kunde.objects(strasse__istartswith=textauswertungvar).scalar('kunde_nr').order_by('strasse')[kundepos]
                auftragnachname = Kunde.objects(strasse__istartswith=textauswertungvar).scalar('nachname').order_by('strasse')[kundepos]
                auftragvorname = Kunde.objects(strasse__istartswith=textauswertungvar).scalar('vorname').order_by('strasse')[kundepos]
                auftragstrasse = Kunde.objects(strasse__istartswith=textauswertungvar).scalar('strasse').order_by('strasse')[kundepos]
                auftraghausnummer = Kunde.objects(strasse__istartswith=textauswertungvar).scalar('haus_nr').order_by('strasse')[kundepos]
                suchenbox.insert(END, auftragkundennummer.ljust(10)[0:10] + "  " + auftragnachname.ljust(35)[0:35] + "  " +
                                      auftragvorname.ljust(35)[0:35] + "  " +auftragstrasse + " " +  auftraghausnummer)
                i += 1
                kundepos += 1

    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # **************** ABARBEITEN WENN WIDGETS FOCUS VERLIEREN                          ********************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************


    def TexteFocusOutAgKdnr(event):
        textauswertungvar = kdnummerAgeber.get()
        auftragkundennummer = Kunde.objects(kunde_nr=textauswertungvar).scalar('kunde_nr')
        kdnrvar=textauswertungvar
        ageberfuellen(kdnrvar)
        suchenbox.delete(0, END)

    def suchenlisteclick(event):
        textauswertungvar = suchenbox.get(suchenbox.curselection()[0])
        textauswertungvar= textauswertungvar[0:10]
        kdnrvar=textauswertungvar
        ageberfuellen(kdnrvar)


    window.bind_all("<FocusIn>", TexteFocusIn)
    window.bind_all("<Key>", TexteFocusIn)
    kdnummerAgeber.bind("<FocusOut>", TexteFocusOutAgKdnr)
    suchenbox.bind("<Double-Button-1>", suchenlisteclick)
    kdnummerAgeber.focus_set()

    # ******************************************************************************************************************
    # ******************************************************************************************************************
    # ************************    BEREICH PERSONALRAHMEN BENUTZER UND PASSWORT *****************************************
    # ******************************************************************************************************************
    # ******************************************************************************************************************

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #                        BUTTON FUNKTIONEN PERSONALRAHMEN
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    #                        BUTTON FUNKTIONEN PERSONAL IM HAUPTMENUE

    def PersonalbuttonClick():
        PersonalRahmen.grid(row=2, column=0, padx='620', pady='3', sticky='nw', columnspan=5)

    #                        BUTTON FUNKTIONEN NEU PERSONAL IM PERSONALFRAME

    def Nutzerauswahl(nutzer_name, nutzer_passwort):
        listeaus = listboxNutzer.curselection()[0]
        nameaus = listboxNutzer.get(listeaus)
        nutzer_name = nameaus
        nutzer_name = nutzer_name[14:38].strip()
        nutzername.set(nutzer_name)
        passwortaus = listboxNutzer.get(listeaus)
        nutzer_passwort = passwortaus
        nutzer_passwort = nutzer_passwort[48:68].strip()
        nutzerpasswort.set(nutzer_passwort)

    nutzerpasswort = StringVar()
    nutzername = StringVar()

    def PersonalbuttonSpeichernClick():
        benutzer = NutzernameText.get().strip()
        passwort = NutzerpasswortText.get().strip()
        if benutzer == "" or passwort == "":
            messagebox.showinfo(title="Fehler !", message="Benutzer oder Passwort fehlt")
        else:
            listboxNutzer.delete(0, END)
            User.objects(user_name=benutzer).update_one(user_password=passwort)

            userpassword = User.objects().scalar('user_password')
            username = User.objects().scalar('user_name')
            user_number = 0

            for i in User.objects():
                listboxNutzer.insert(END,
                                     f'Benutzername: {username[user_number].ljust(20)[0:20]}    Passwort: {userpassword[user_number].ljust(20)[0:20]}')
                user_number += 1

    def PersonalbuttonLöschenClick():
        benutzer = NutzernameText.get().strip()
        passwort = NutzerpasswortText.get().strip()
        if benutzer == "" or passwort == "":
            messagebox.showinfo(title="Fehler !", message="Benutzer oder Passwort fehlt")
        else:
            listboxNutzer.delete(0, END)
            User.objects(user_name=benutzer).delete()

            userpassword = User.objects().scalar('user_password')
            username = User.objects().scalar('user_name')
            user_number = 0

            for i in User.objects():
                listboxNutzer.insert(END,
                                     f'Benutzername: {username[user_number].ljust(20)[0:20]}    Passwort: {userpassword[user_number].ljust(20)[0:20]}')
                user_number += 1

    def PersonalbuttonNeuClick():
        benutzer = NutzernameText.get().strip()
        passwort = NutzerpasswortText.get().strip()
        if benutzer == "" or passwort == "":
            messagebox.showinfo(title="Fehler !", message="Benutzer oder Passwort fehlt")
        else:
            listboxNutzer.delete(0, END)
            User(user_name=benutzer, user_password=passwort).save()

            userpassword = User.objects().scalar('user_password')
            username = User.objects().scalar('user_name')
            user_number = 0

            for i in User.objects():
                listboxNutzer.insert(END,
                                     f'Benutzername: {username[user_number].ljust(20)[0:20]}    Passwort: {userpassword[user_number].ljust(20)[0:20]}')
                user_number += 1

    def PersonalbuttonEndeClick():
        PersonalRahmen.grid_forget()
        nachnameAgeber.focus()

    # ******************************************************************************************************************
    # ****************    BEREICH PERSONALRAHMEN RAHMEN UND FELDER ERSTELLEN UND AUSBLENDEN LISTE EINLESEN *************
    # ******************************************************************************************************************

    PersonalRahmen = HAUPTMENUE.Frame(window, width=659, heigh=360, bg='#BDBDBD', borderwidth=2, relief="groove", )
    PersonalRahmen.grid(row=2, column=0, padx='620', pady='3', sticky='nw', columnspan=5)

    Nutzernametitel_label = HAUPTMENUE.Label(PersonalRahmen, text="PERSONAL ANLEGEN/ÄNDERN/LÖSCHEN", fg='#2F4F4F',
                                             bg='#BDBDBD', font=('Courier New', 14), width=31, heigh=1)
    Nutzernametitel_label.grid(row=0, column=0, padx='5', pady='5', sticky='nw', columnspan=5)

    Nutzernameleer_label = HAUPTMENUE.Label(PersonalRahmen, text=" ", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('Courier New', 12), width=31, heigh=1)
    Nutzernameleer_label.grid(row=1, column=0, padx='5', pady='5', sticky='nw', columnspan=5)

    Nutzername_label = HAUPTMENUE.Label(PersonalRahmen, text="Benutzername", fg='#2F4F4F', bg='#BDBDBD',
                                        font=('Courier New', 12,), width=12, heigh=1)
    Nutzername_label.grid(row=2, column=0, padx='5', pady='5', sticky='nw')

    Nutzerpasswort_label = HAUPTMENUE.Label(PersonalRahmen, text="Passwort", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('Courier New', 12,), width=8, heigh=1)
    Nutzerpasswort_label.grid(row=3, column=0, padx='5', pady='5', sticky='nw')

    NutzernameText = Entry(PersonalRahmen, width=20, textvariable=nutzername, font=('Courier New', 12))
    NutzernameText.grid(row=2, column=1, padx='5', pady='0', sticky='nw')

    NutzerpasswortText = Entry(PersonalRahmen, width=20, textvariable=nutzerpasswort, font=('Courier New', 12))
    NutzerpasswortText.grid(row=3, column=1, padx='5', pady='0', sticky='nw')

    listboxNutzer = HAUPTMENUE.Listbox(PersonalRahmen, bd=2, width=80, heigh=5, borderwidth=2, relief="flat",
                                       font=('Courier New', 12,), selectmode='browse')
    listboxNutzer.grid(row=4, column=0, padx='15', pady='10', sticky='ne', columnspan=5, )
    listboxNutzer.bind('<<ListboxSelect>>', lambda x: Nutzerauswahl(nutzername, nutzerpasswort))
    listboxNutzer.bind('<Double-Button-1>', lambda x: Nutzerauswahl(nutzername, nutzerpasswort))
    Nutzernameleer1_label = HAUPTMENUE.Label(PersonalRahmen, text=" ", fg='#2F4F4F', bg='#BDBDBD',
                                             font=('Courier New', 12), width=31, heigh=1)
    Nutzernameleer1_label.grid(row=5, column=0, padx='5', pady='5', sticky='nw', columnspan=5)

    Personalbutton1Neu = HAUPTMENUE.Button(PersonalRahmen, text="Neu", command=PersonalbuttonNeuClick).grid(row=8,
                                                                                                            column=0,
                                                                                                            padx='10',
                                                                                                            pady='20',
                                                                                                            sticky='ew')
    Personalbutton1Speichern = HAUPTMENUE.Button(PersonalRahmen, text="Speichern",
                                                 command=PersonalbuttonSpeichernClick).grid(row=8, column=1, padx='10',
                                                                                            pady='20', sticky='ew')
    Personalbutton1loeschen = HAUPTMENUE.Button(PersonalRahmen, text="Löschen",
                                                command=PersonalbuttonLöschenClick).grid(row=8, column=2, padx='10',
                                                                                         pady='20', sticky='ew')
    Personalbutton1Ende = HAUPTMENUE.Button(PersonalRahmen, text="Exit", command=PersonalbuttonEndeClick).grid(row=8,
                                                                                                               column=3,
                                                                                                               padx='10',
                                                                                                               pady='20',
                                                                                                               sticky='ew')

    userpassword = User.objects().scalar('user_password')
    username = User.objects().scalar('user_name')
    user_number = 0
    listboxNutzer.delete(0, END)
    for i in User.objects(user_number):
        listboxNutzer.insert(END,
                             f'Benutzername: {username[user_number].ljust(20)[0:20]}    Passwort: {userpassword[user_number].ljust(20)[0:20]}')
        user_number += 1
    # if NotUniqueError:
    #   messagebox.showinfo(title="Doppelt", message="Benutzer oder Passwort fehlt")
    PersonalRahmen.grid_forget()
    # if benutzer == "":
    #   messagebox.showinfo(title=benutzer, message=passwort)
    #  window.destroy()
    # HAUPTMENUE.HauptMenue()
    # else:
    #    pass

    Hautbuttonumrandung = HAUPTMENUE.Frame(window, bd=2, width=201, heigh=58, bg='#BDBDBD', borderwidth=2,
                                           relief="groove", )
    Hautbuttonumrandung.grid(row=0, column=1, padx='0', pady='3', sticky='nw', rowspan=7)
    HautbuttonDrucken = HAUPTMENUE.Button(Hautbuttonumrandung, text="Drucken").grid(row=0, column=0, padx='10',
                                                                                    pady='20', sticky='ew')
    HautbuttonDrucken = HAUPTMENUE.Button(Hautbuttonumrandung, text="Drucken").grid(row=1, column=0, padx='10',
                                                                                    pady='20', sticky='ew')
    HautbuttonDrucken = HAUPTMENUE.Button(Hautbuttonumrandung, text="Drucken").grid(row=2, column=0, padx='10',
                                                                                    pady='20', sticky='ew')
    HautbuttonDrucken = HAUPTMENUE.Button(Hautbuttonumrandung, text="Drucken").grid(row=3, column=0, padx='10',
                                                                                    pady='20', sticky='ew')
    HautbuttonDrucken = HAUPTMENUE.Button(Hautbuttonumrandung, text="Drucken").grid(row=4, column=0, padx='10',
                                                                                    pady='20', sticky='ew')
    HautbuttonDrucken = HAUPTMENUE.Button(Hautbuttonumrandung, text="Drucken").grid(row=5, column=0, padx='10',
                                                                                    pady='20', sticky='ew')
    HautbuttonDrucken = HAUPTMENUE.Button(Hautbuttonumrandung, text="Drucken").grid(row=6, column=0, padx='10',
                                                                                    pady='20', sticky='ew')
    HautbuttonDrucken = HAUPTMENUE.Button(Hautbuttonumrandung, text="Drucken").grid(row=7, column=0, padx='10',
                                                                                    pady='20', sticky='ew')
    HautbuttonDrucken = HAUPTMENUE.Button(Hautbuttonumrandung, text="Personal", command=PersonalbuttonClick).grid(row=8,
                                                                                                                  column=0,
                                                                                                                  padx='10',
                                                                                                                  pady='20',
                                                                                                                  sticky='ew')

    # messagebox.showinfo(message=kdnummerAgeber.grab_current(), title="Box-Titel")
    # HauptMenue()
    window.mainloop()


HauptMenue()
