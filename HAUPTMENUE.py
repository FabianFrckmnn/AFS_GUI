# ERÖFFNET EINE SEITE
from tkinter import *
from tkinter import font, Label
import tkinter as HAUPTMENUE
import time
import datetime
import calendar
import BILDER
import tkinter.font as tkFont
from tkinter import ttk

def HauptMenue():
    window = HAUPTMENUE.Tk()

    # SETZEN DER FENSTERGRÖßE
    window.geometry("1920x1080")
    window.configure(bg="#BDBDBD")

    # SETZT DEN FENSTERTITEL
    window.title("HAUPTMENUE KUNDENVERWALTUNG")

    # DATUM/UHRZEIT HINZUFÜGEN
    window_datum_label = HAUPTMENUE.Label(window, text=datetime.datetime.now().strftime("%A, %d.%m.%Y"), fg = '#2F4F4F', bg = '#BDBDBD', font = ('courier', 12), width = 25, heigh = 1, relief = GROOVE)
    window_datum_label.place(x=1500, y=11)
    window_zeit_label = HAUPTMENUE.Label(window, text=time.strftime("%H:%M:%S"), fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12), width=10, heigh=1, relief=GROOVE)
    window_zeit_label.place(x=1800, y=11)
    def digital_clock():
        time_live = time.strftime("%H:%M:%S")
        window_zeit_label.config(text=time_live)
        window_zeit_label.after(200, digital_clock)
    digital_clock()

# *********************************************************************************************************************
# ************************   UMRANDUNGEN ALLER BEREICHE IM HAUPTMENUE ERSTELLEN
# *********************************************************************************************************************

    # LABEL ALS RAHMEN FÜR AUFTRAGGEBER HINZUFÜGEN
    auftraggeber_label = HAUPTMENUE.Label(window, text=" ", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12), width=40, heigh=13, relief=GROOVE)
    auftraggeber_label.place(x=5, y=12)
    auftraggeber1_label = HAUPTMENUE.Label(window, text="AUFTRAGGEBER", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12), width=14, heigh=1,relief=GROOVE)
    auftraggeber1_label.place(x=30, y=5)

    # LABEL ALS RAHMEN FÜR OBJEKTRAHMEN HINZUFÜGEN
    objektrahmen_label = HAUPTMENUE.Label(window, text=" ", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=40, heigh=14, relief=GROOVE)
    objektrahmen_label.place(x=5, y=265)
    objektrahmen1_label = HAUPTMENUE.Label(window, text="OBJEKT", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=14, heigh=1, relief=GROOVE)
    objektrahmen1_label.place(x=30, y=258)

    # LABEL ALS RAHMEN FÜR VERTRAGSRAHMEN HINZUFÜGEN
    vertragsrahmen_label = HAUPTMENUE.Label(window, text=" ", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=40, heigh=27, relief=GROOVE)
    vertragsrahmen_label.place(x=5, y=535)
    vertragsrahmen1_label: Label = HAUPTMENUE.Label(window, text="VERTRAG", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=14, heigh=1, relief=GROOVE)
    vertragsrahmen1_label.place(x=30, y=528)
    vertragsrahmenschädlinge_label = HAUPTMENUE.Label(window, text="", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=39, heigh=4, relief=GROOVE)
    vertragsrahmenschädlinge_label.place(x=9, y=611)
    vertragsrahmenbereiche_label = HAUPTMENUE.Label(window, text="", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=20, heigh=18, relief=GROOVE)
    vertragsrahmenbereiche_label.place(x=9, y=691)
    vertragsrahmengesetze_label = HAUPTMENUE.Label(window, text="", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,),  width=18, heigh=4, relief=GROOVE)
    vertragsrahmengesetze_label.place(x=219, y=691)
    vertragsrahmenzahlung_label = HAUPTMENUE.Label(window, text="", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=18, heigh=4, relief=GROOVE)
    vertragsrahmenzahlung_label.place(x=219, y=770)
    vertragsrahmenpreis_label = HAUPTMENUE.Label(window, text="", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=18, heigh=2, relief=GROOVE)
    vertragsrahmenpreis_label.place(x=219, y=860)

    # LABEL ALS RAHMEN FÜR INTENSIV/EINZELBEHANDLUNG HINZUFÜGEN
    behandlungsrahmen_label = HAUPTMENUE.Label(window, text=" ", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,),
                                            width=50, heigh=27, relief=GROOVE)
    behandlungsrahmen_label.place(x=420, y=535)
    behandlungsrahmen1_label = HAUPTMENUE.Label(window, text="EINZEL-/MEHRFACHAUFTRAG", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=27, heigh=1, relief=GROOVE)
    behandlungsrahmen1_label.place(x=445, y=528)

# *********************************************************************************************************************
# ************************   BEREICH AUFTRAGGEBER TEXTFELDER ERSTELLEN
# *********************************************************************************************************************

    # TEXTFELD UND LABEL KUNDENNUMMER ZUFÜGEN
    kdnummer_label = HAUPTMENUE.Label(window, text="Kd-Nummer", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=9, heigh=1)
    kdnummer_label.place(x=10, y=35)
    kdnummer_textfeld = Text(master=window, width=10, height=1, wrap='word')
    kdnummer_textfeld.place(x=110, y=35)

    # TEXTFELD UND LABEL KUNDENNACHNAME ZUFÜGEN
    nachname_label = HAUPTMENUE.Label(window, text="Nachname", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=8, heigh=1)
    nachname_label.place(x=10, y=60)
    nachname_textfeld = Text(master=window, width=35, height=1, wrap='word')
    nachname_textfeld.place(x=110, y=60)

    # TEXTFELD UND LABEL KUNDENNVORNAME ZUFÜGEN
    vorname_label = HAUPTMENUE.Label(window, text="Vorname", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=7, heigh=1)
    vorname_label.place(x=10, y=85)
    vorname_textfeld = Text(master=window, width=35, height=1, wrap='word')
    vorname_textfeld.place(x=110, y=85)

    # TEXTFELD UND LABEL STRASSE UND NR ZUFÜGEN
    strasse_label = HAUPTMENUE.Label(window, text="Str./Nr.", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12), width=8, heigh=1)
    strasse_label.place(x=10, y=110)
    strasse_textfeld = Text(master=window, width=30, height=1, wrap='word')
    strasse_textfeld.place(x=110, y=110)
    nr_textfeld = Text(master=window, width=4, height=1, wrap='word')
    nr_textfeld.place(x=358, y=110)

    # TEXTFELD UND LABEL PLZ UND ORT ZUFÜGEN
    plz_label = HAUPTMENUE.Label(window, text="Plz/Ort", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12), width=7, heigh=1)
    plz_label.place(x=10, y=135)
    plz_textfeld = Text(master=window, width=5, height=1, wrap='word')
    plz_textfeld.place(x=110, y=135)
    ort_textfeld = Text(master=window, width=29, height=1, wrap='word')
    ort_textfeld.place(x=158, y=135)

    # TEXTFELD UND LABEL ANSPRECHPARTNER ZUFÜGEN
    ansprechpartner_label = HAUPTMENUE.Label(window, text="Ansprech", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12), width=8, heigh=1)
    ansprechpartner_label.place(x=10, y=160)
    ansprechpartner_textfeld = Text(master=window, width=35, height=1, wrap='word')
    ansprechpartner_textfeld.place(x=110, y=160)

    # TEXTFELD UND LABEL TELEFONNUMMER ZUFÜGEN
    telefon_label = HAUPTMENUE.Label(window, text="Telefon", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12), width=7, heigh=1)
    telefon_label.place(x=10, y=185)
    telefon_textfeld = Text(master=window, width=35, height=1, wrap='word')
    telefon_textfeld.place(x=110, y=185)

    # TEXTFELD UND LABEL MAIL ZUFÜGEN
    mail_label = HAUPTMENUE.Label(window, text="Mail", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12), width=4, heigh=1)
    mail_label.place(x=10, y=210)
    mail_textfeld = Text(master=window, width=35, height=1, wrap='word')
    mail_textfeld.place(x=110, y=210)

# *********************************************************************************************************************
# ************************   BEREICH OBJEKT TEXTFELDER ERSTELLEN
# *********************************************************************************************************************

    # TEXTFELD UND LABEL OBJEKTNUMMER ZUFÜGEN
    objektnummer_label = HAUPTMENUE.Label(window, text="Objekt-Nr", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=9, heigh=1)
    objektnummer_label.place(x=10, y=290)
    objektnummer_textfeld = Text(master=window, width=3, height=1, wrap='word')
    objektnummer_textfeld.place(x=110, y=290)
    # CHECKBOX OB VERTRAGSKUND ZUFÜGEN
    objekt_checkbox = HAUPTMENUE.Checkbutton(window, text="Vertrag", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 13,), width=7, heigh=1)
    objekt_checkbox.place(x=200, y=285)
    # TEXTFELD UND LABEL OBJEKT KUNDENNACHNAME ZUFÜGEN
    objektnachname_label = HAUPTMENUE.Label(window, text="Nachname", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=8, heigh=1)
    objektnachname_label.place(x=10, y=315)
    objektnachname_textfeld = Text(master=window, width=35, height=1, wrap='word')
    objektnachname_textfeld.place(x=110, y=315)

    # TEXTFELD UND LABEL OBJEKT KUNDENNVORNAME ZUFÜGEN
    objektvorname_label = HAUPTMENUE.Label(window, text="Vorname", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=7, heigh=1)
    objektvorname_label.place(x=10, y=340)
    objektvorname_textfeld = Text(master=window, width=35, height=1, wrap='word')
    objektvorname_textfeld.place(x=110, y=340)

    # TEXTFELD UND LABEL OBJEKT STRASSE UND NR ZUFÜGEN
    objektstrasse_label = HAUPTMENUE.Label(window, text="Str./Nr.", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12), width=8, heigh=1)
    objektstrasse_label.place(x=10, y=365)
    objektstrasse_textfeld = Text(master=window, width=30, height=1, wrap='word')
    objektstrasse_textfeld.place(x=110, y=365)
    objektnr_textfeld = Text(master=window, width=4, height=1, wrap='word')
    objektnr_textfeld.place(x=358, y=365)

    # TEXTFELD UND LABEL OBJEKT PLZ UND ORT ZUFÜGEN
    objektplz_label = HAUPTMENUE.Label(window, text="Plz/Ort", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12), width=7, heigh=1)
    objektplz_label.place(x=10, y=390)
    objektplz_textfeld = Text(master=window, width=5, height=1, wrap='word')
    objektplz_textfeld.place(x=110, y=390)
    objektort_textfeld = Text(master=window, width=29, height=1, wrap='word')
    objektort_textfeld.place(x=158, y=390)

    # TEXTFELD UND LABEL OBJEKT ZUSATZ ZUFÜGEN
    objektzusatz_label = HAUPTMENUE.Label(window, text="Zusatz", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12), width=6, heigh=1)
    objektzusatz_label.place(x=10, y=415)
    objektzusatz_textfeld = Text(master=window, width=35, height=1, wrap='word')
    objektzusatz_textfeld.place(x=110, y=415)

    # TEXTFELD UND LABEL OBJEKT ANSPRECHPARTNER ZUFÜGEN
    objektansprechpartner_label = HAUPTMENUE.Label(window, text="Ansprech", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12), width=8, heigh=1)
    objektansprechpartner_label.place(x=10, y=440)
    objektansprechpartner_textfeld = Text(master=window, width=35, height=1, wrap='word')
    objektansprechpartner_textfeld.place(x=110, y=440)

    # TEXTFELD UND LABEL OBJEKT TELEFONNUMMER ZUFÜGEN
    objekttelefon_label = HAUPTMENUE.Label(window, text="Telefon", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12), width=7, heigh=1)
    objekttelefon_label.place(x=10, y=465)
    objekttelefon_textfeld = Text(master=window, width=35, height=1, wrap='word')
    objekttelefon_textfeld.place(x=110, y=465)

    # TEXTFELD UND LABEL OBJEKT MAIL ZUFÜGEN
    objektmail_label = HAUPTMENUE.Label(window, text="Mail", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12), width=4, heigh=1)
    objektmail_label.place(x=10, y=490)
    objektmail_textfeld = Text(master=window, width=35, height=1, wrap='word')
    objektmail_textfeld.place(x=110, y=490)

# *********************************************************************************************************************
# ************************   BEREICH OBJEKT DROPDOWNLISTE ERSTELLEN
# *********************************************************************************************************************


    # DROPDOWNMENUE FÜR VERTRAGSSTATUS ZUFÜGEN
    #objektstatus_label = HAUPTMENUE.Label(window, text="Status", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12), width=6, heigh=1)
    #objektstatus_label.place(x=10, y=550)
    #Ostatusliste = [
     #  "",
     #  "Wartungskunden mit Vertrag",
      # "Wartungskunden ohne Vertrag",
       #"Mehrfachauftrag",
      # "Einzelauftrag",
    #]
    #variable = HAUPTMENUE.StringVar(window)
   # variable.set(Ostatusliste[0])
    #Ostatusliste1 = HAUPTMENUE.OptionMenu(window, variable, *Ostatusliste)
    #Ostatusliste1.config(width=30,font=('courier', 10), bg='#FFFFFF', relief=FLAT)
    #Ostatusliste1.pack(side="left")
    #Ostatusliste1.place(x=111, y=550)

    # *********************************************************************************************************************
    # ************************   BEREICH VERTRAG TEXTFELDER ERSTELLEN
    # *********************************************************************************************************************

    # TEXTFELD UND LABEL ANZAHL WARTUNG UND INTENSIV ZUFÜGEN
    vertragsinterval_label = HAUPTMENUE.Label(window, text="Anzahl Wartung", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12), width=14, height=1)
    vertragsinterval_label.place(x=10, y=560)
    vertragsinterval_textfeld = Text(window, width=4, height=1, wrap='word')
    vertragsinterval_textfeld.place(x=157, y=560)
    vertragsintensivinterval_label = HAUPTMENUE.Label(window, text="Anzahl Intensiv", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12), width=15, heigh=1)
    vertragsintensivinterval_label.place(x=200, y=560)
    vertragsintensivinterval_textfeld = Text(master=window, width=4, height=1, wrap='word')
    vertragsintensivinterval_textfeld.place(x=357, y=560)

    # TEXTFELD UND LABEL VERTRAGSBEGINN UND ENDE ZUFÜGEN
    vertragbeginn_label = HAUPTMENUE.Label(window, text="V-Beginn", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=8, heigh=1)
    vertragbeginn_label.place(x=10, y=587)
    vertragbeginn_textfeld = Text(master=window, width=10, height=1, wrap='word')
    vertragbeginn_textfeld.place(x=110, y=587)

    vertragsende_label = HAUPTMENUE.Label(window, text="V-Ablauf", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=8, heigh=1)
    vertragsende_label.place(x=210, y=587)
    vertragsende_textfeld = Text(master=window, width=10, height=1, wrap='word')
    vertragsende_textfeld.place(x=310, y=587)

    # ********** CHECKBOXEN FÜR SCHÄDLINGSAUSWAHL
    vertrags_checkbox1 = HAUPTMENUE.Checkbutton(window, text="Ratten",fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=6, heigh=1)
    vertrags_checkbox1.place(x=11, y=620)

    vertrags_checkbox2 = HAUPTMENUE.Checkbutton(window, text="Mäuse",fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=5, heigh=1)
    vertrags_checkbox2.place(x=110, y=620)

    vertrags_checkbox3 = HAUPTMENUE.Checkbutton(window, text="Schaben",fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=7, heigh=1)
    vertrags_checkbox3.place(x=203, y=620)

    vertrags_checkbox4 = HAUPTMENUE.Checkbutton(window, text="Käfer",fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=5, heigh=1)
    vertrags_checkbox4.place(x=310, y=620)

    vertrags_checkbox5 = HAUPTMENUE.Checkbutton(window, text=" ", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=1, heigh=1)
    vertrags_checkbox5.place(x=11, y=645)

    vertragcheckboxtext_textfeld = Text(master=window, width=44, height=1, wrap='word')
    vertragcheckboxtext_textfeld.place(x=35, y=650)

    # ********** CHECKBOXEN FÜR BEREICHSAUSWAHL
    vertrags_checkbox6 = HAUPTMENUE.Checkbutton(window, text="Köderstationen", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=14, heigh=1)
    vertrags_checkbox6.place(x=11, y=695)

    vertrags_checkbox7 = HAUPTMENUE.Checkbutton(window, text="Innenbereich", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=12, heigh=1)
    vertrags_checkbox7.place(x=11, y=715)

    vertrags_checkbox8 = HAUPTMENUE.Checkbutton(window, text="Wohnbereich", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=11, heigh=1)
    vertrags_checkbox8.place(x=11, y=735)

    vertrags_checkbox9 = HAUPTMENUE.Checkbutton(window, text="Küchenbereich", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=13, heigh=1)
    vertrags_checkbox9.place(x=11, y=755)

    vertrags_checkbox10 = HAUPTMENUE.Checkbutton(window, text="Aussenbereich", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=13, heigh=1)
    vertrags_checkbox10.place(x=11, y=775)

    vertrags_checkbox11 = HAUPTMENUE.Checkbutton(window, text="Gartenbereich", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=13, heigh=1)
    vertrags_checkbox11.place(x=11, y=795)

    vertrags_checkbox12 = HAUPTMENUE.Checkbutton(window, text="Kellerbereich", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=13, heigh=1)
    vertrags_checkbox12.place(x=11, y=815)

    vertrags_checkbox13 = HAUPTMENUE.Checkbutton(window, text="Müllbereich", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=11, heigh=1)
    vertrags_checkbox13.place(x=11, y=835)

    vertrags_checkbox14 = HAUPTMENUE.Checkbutton(window, text="Imbissbereich", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=13, heigh=1)
    vertrags_checkbox14.place(x=11, y=855)

    vertrags_checkbox15 = HAUPTMENUE.Checkbutton(window, text="Tresenbereich", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=13, heigh=1)
    vertrags_checkbox15.place(x=11, y=875)

    vertrags_checkbox16 = HAUPTMENUE.Checkbutton(window, text="Herstellung/Lager", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=17, heigh=1)
    vertrags_checkbox16.place(x=11, y=895)

    vertrags_checkbox17 = HAUPTMENUE.Checkbutton(window, text="Ges. Restaurant", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=15, heigh=1)
    vertrags_checkbox17.place(x=11, y=918)

    vertrags_checkbox18 = HAUPTMENUE.Checkbutton(window, text=" ", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=1, heigh=1)
    vertrags_checkbox18.place(x=11, y=938)
    vertragscheckboxtext_textfeld = Text(window, width=20, height=1, wrap='word')
    vertragscheckboxtext_textfeld.place(x=35, y=943)

    # ********** CHECKBOXEN FÜR GESETZE
    vertrags_checkbox19 = HAUPTMENUE.Checkbutton(window, text="LMHV/HACCP", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=10, heigh=1)
    vertrags_checkbox19.place(x=221, y=695)

    vertrags_checkbox20 = HAUPTMENUE.Checkbutton(window, text="IFSG", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=4, heigh=1)
    vertrags_checkbox20.place(x=221, y=715)

    vertrags_checkbox21 = HAUPTMENUE.Checkbutton(window, text="Biozid-VO", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=9, heigh=1)
    vertrags_checkbox21.place(x=221, y=735)

    # ********** CHECKBOXEN FÜR ZAHLUNG
    vertrags_checkbox22 = HAUPTMENUE.Checkbutton(window, text="Überweisung", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=11, heigh=1)
    vertrags_checkbox22.place(x=221, y=775)

    vertrags_checkbox23 = HAUPTMENUE.Checkbutton(window, text="EC", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,),
                                                 width=2, heigh=1)
    vertrags_checkbox23.place(x=221, y=795)

    vertrags_checkbox24 = HAUPTMENUE.Checkbutton(window, text="bar", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=3, heigh=1)
    vertrags_checkbox24.place(x=221, y=815)

    # ********** EINGABEFELDER FÜR VERTRAGSPREISE
    wartungspreis_label = HAUPTMENUE.Label(window, text="Preis", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=5, heigh=1)
    wartungspreis_label.place(x=221, y=867)
    wartungspreis_textfeld = Text(window, width=7, height=1, wrap='word')
    wartungspreis_textfeld.place(x=281, y=869)

 # *********************************************************************************************************************
 # ************************   BEREICH VERTRAG TEXTFELDER ERSTELLEN
 # *********************************************************************************************************************

    # COMBOBOX UM BEHANDLUNGSART UND DATUM ABZUFRAGEN

    behandlungsart_label = HAUPTMENUE.Label(window, text="Behandlung", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=10, heigh=1)
    behandlungsart_label.place(x=430, y=570)

    behandlungsart = ttk.Combobox(window, values=["Einzelauftrag", "Mehrfachauftrag",],font=('courier', 10), width=15 )
    print(dict(behandlungsart))
    behandlungsart.grid(column=1, row=1)
    behandlungsart.current(1)
    behandlungsart.place(x=540, y=572)
    print(behandlungsart.current(), behandlungsart.get())

    behandlungszähler1_label = HAUPTMENUE.Label(window, text="Zähler", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=6, heigh=1)
    behandlungszähler1_label.place(x=690, y=570)

    behandlungszähler1_textfeld = Text(window, width=2, height=1, wrap='word')
    behandlungszähler1_textfeld.place(x=760, y=572)

    behandlungszähler2_label = HAUPTMENUE.Label(window, text="von", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=3, heigh=1)
    behandlungszähler2_label.place(x=790, y=570)

    behandlungszähler2_textfeld = Text(window, width=2, height=1, wrap='word')
    behandlungszähler2_textfeld.place(x=830, y=572)

    behandlungszähler3_label = HAUPTMENUE.Label(window, text="erfolgt am", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=10, heigh=1)
    behandlungszähler3_label.place(x=430, y=596)

    behandlungszähler3_textfeld = Text(window, width=10, height=1, wrap='word')
    behandlungszähler3_textfeld.place(x=540, y=598)

    behandlungszähler4_textfeld = Text(window, width=10, height=1, wrap='word')
    behandlungszähler4_textfeld.place(x=625, y=598)

    behandlungszähler5_textfeld = Text(window, width=10, height=1, wrap='word')
    behandlungszähler5_textfeld.place(x=710, y=598)

    behandlungszähler6_textfeld = Text(window, width=10, height=1, wrap='word')
    behandlungszähler6_textfeld.place(x=795, y=598)

    # COMBOBOX UM SCHÄDLING ABZUFRAGEN

    behandlungsart_label = HAUPTMENUE.Label(window, text="Schädling", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('courier', 12,), width=9, heigh=1)
    behandlungsart_label.place(x=430, y=638)

    behandlungstier1 = ttk.Combobox(window, values=["Auswahl", "Ratte", "Maus", "Schabe", "Ameise", "Käfer", "Motte", "Wespe", "Marder", "Hornisse", "Bettwanzen", "Tauben" ], font=('courier', 10), width=15)
    print(dict(behandlungstier1))
    behandlungstier1.grid(column=1, row=1)
    behandlungstier1.current(0)
    behandlungstier1.place(x=540, y=638)
    print(behandlungstier1.current(), behandlungstier1.get())

    behandlungstier2 = ttk.Combobox(window, values=["Auswahl", "Ratte", "Maus", "Schabe", "Ameise", "Käfer", "Motte", "Wespe", "Marder", "Hornisse", "Bettwanzen", "Tauben"], font=('courier', 10), width=15)
    print(dict(behandlungstier2))
    behandlungstier2.grid(column=1, row=1)
    behandlungstier2.current(0)
    behandlungstier2.place(x=690, y=638)
    print(behandlungstier2.current(), behandlungstier2.get())

    # ********** CHECKBOXEN FÜR GESETZE
    behandlung_checkbox1 = HAUPTMENUE.Checkbutton(window, text="LMHV/HACCP", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=10, heigh=1)
    behandlung_checkbox1.place(x=430, y=675)

    behandlung_checkbox2 = HAUPTMENUE.Checkbutton(window, text="IFSG", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=4, heigh=1)
    behandlung_checkbox2.place(x=570, y=675)

    behandlung_checkbox3 = HAUPTMENUE.Checkbutton(window, text="BIOZID-VERORDNUNG", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=17, heigh=1)
    behandlung_checkbox3.place(x=650, y=675)

    # ********** CHECKBOXEN FÜR ZAHLUNG
    behandlung_checkbox4 = HAUPTMENUE.Checkbutton(window, text="Überweisung", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=11, heigh=1)
    behandlung_checkbox4.place(x=430, y=705)

    behandlung_checkbox5 = HAUPTMENUE.Checkbutton(window, text="EC", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=2, heigh=1)
    behandlung_checkbox5.place(x=570, y=705)

    behandlung_checkbox6 = HAUPTMENUE.Checkbutton(window, text="bar", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=3, heigh=1)
    behandlung_checkbox6.place(x=650, y=705)

    # ********** CHECKBOXEN FÜR MAßNAHMEN

    massnahmen_checkbox1 = HAUPTMENUE.Checkbutton(window, text="Vorbeugende Schädlingsbekämpfung", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=32, heigh=1)
    massnahmen_checkbox1.place(x=430, y=740)

    massnahmen_checkbox2 = HAUPTMENUE.Checkbutton(window, text="Erneuerung Köder-/Systemfallen", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=30, heigh=1)
    massnahmen_checkbox2.place(x=430, y=760)

    massnahmen_checkbox3 = HAUPTMENUE.Checkbutton(window, text="Mineralien/Planktonprodukte", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=27, heigh=1)
    massnahmen_checkbox3.place(x=430, y=780)

    massnahmen_checkbox4 = HAUPTMENUE.Checkbutton(window, text="Gelbehandlung", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=13, heigh=1)
    massnahmen_checkbox4.place(x=430, y=800)

    massnahmen_checkbox5 = HAUPTMENUE.Checkbutton(window, text="Rodentizidbehandlung", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=20, heigh=1)
    massnahmen_checkbox5.place(x=430, y=820)

    massnahmen_checkbox6 = HAUPTMENUE.Checkbutton(window, text="Stäubeverfahren", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=15, heigh=1)
    massnahmen_checkbox6.place(x=430, y=840)

    massnahmen_checkbox7 = HAUPTMENUE.Checkbutton(window, text="Schaumbehandlung", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=16, heigh=1)
    massnahmen_checkbox7.place(x=430, y=800)

    massnahmen_checkbox7 = HAUPTMENUE.Checkbutton(window, text="Vorbeugende Rodentizidbehandlung", fg='#2F4F4F',
                                                  bg='#BDBDBD', font=('courier', 12,), width=32, heigh=1)
    massnahmen_checkbox7.place(x=430, y=820)

    massnahmen_checkbox7 = HAUPTMENUE.Checkbutton(window, text="Stäubeverfahren", fg='#2F4F4F', bg='#BDBDBD',
                                                  font=('courier', 12,), width=15, heigh=1)
    massnahmen_checkbox6.place(x=430, y=840)
    window.mainloop()
HauptMenue()