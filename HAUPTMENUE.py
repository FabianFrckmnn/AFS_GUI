# ERÖFFNET EINE SEITE
import tkinter
from tkinter import *
import tkinter as HAUPTMENUE
import time
import datetime
import calendar
import BILDER
from tkinter import ttk
import tkinter.font as tkFont
from functools import partial
from tkinter import messagebox

# ******************************************************************************************************************
# ******************************************************************************************************************
# ************************  EINSTELLUNGEN UND DEFINITION HAUPTMENUE ERSTELLEN   ************************************
# ******************************************************************************************************************
# ******************************************************************************************************************

# def HauptMenue():
window = HAUPTMENUE.Tk()

#                                    SETZEN DER FENSTERGRÖßE

window.geometry("1920x1080")
window.configure(bg="#BDBDBD")

textExample = HAUPTMENUE.Text(window, height=10)
fontExample = tkFont.Font(family="Courier", size=12)
textExample.configure(font=fontExample)

#                                    SETZT DEN FENSTERTITEL

window.title("HAUPTMENUE KUNDENVERWALTUNG")

#                                    DATUM/UHRZEIT HINZUFÜGEN

window_datum_label = HAUPTMENUE.Label(window, text=datetime.datetime.now().strftime("%A, %d.%m.%Y"), fg='#2F4F4F',
                                      bg='#BDBDBD', width=25, height=1, relief=GROOVE)
window_datum_label.place(x=1500, y=11)
window_zeit_label = HAUPTMENUE.Label(window, text=time.strftime("%H:%M:%S"), fg='#2F4F4F', bg='#BDBDBD', width=10,
                                     heigh=1, relief=GROOVE)
window_zeit_label.place(x=1800, y=11)


def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    window_zeit_label.config(text=time_live)
    window_zeit_label.after(200, digital_clock)


digital_clock()

# ******************************************************************************************************************
# ******************************************************************************************************************
# ************************   UMRANDUNGEN ALLER BEREICHE IM HAUPTMENUE ERSTELLEN   **********************************
# ******************************************************************************************************************
# ******************************************************************************************************************

#                               LABEL ALS RAHMEN FÜR VERTRAGSRAHMEN HINZUFÜGEN

VertragsrahmenBefall_label = HAUPTMENUE.Label(window, text=" ", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,),
                                              width=46, heigh=22, relief=GROOVE)
VertragsrahmenBefall_label.place(x=588, y=636)

VertragsrahmenStatus_label = HAUPTMENUE.Label(window, text=" ", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,),
                                              width=45, heigh=11, relief=GROOVE)
VertragsrahmenStatus_label.place(x=593, y=648)
VertragsrahmenStatusTitel_label: Label = HAUPTMENUE.Label(window, text="Befallsanalyse", fg='#2F4F4F', bg='#BDBDBD',
                                                          font=('courier', 10,), width=18, heigh=1, relief=GROOVE)
VertragsrahmenStatusTitel_label.place(x=618, y=641)

VertragsrahmenMaterial_label = HAUPTMENUE.Label(window, text=" ", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,),
                                                width=45, heigh=9, relief=GROOVE)
VertragsrahmenMaterial_label.place(x=593, y=867)
VertragsrahmenMaterialTitel_label: Label = HAUPTMENUE.Label(window, text="Materialeinsatz", fg='#2F4F4F', bg='#BDBDBD',
                                                            font=('courier', 10,), width=19, heigh=1, relief=GROOVE)
VertragsrahmenMaterialTitel_label.place(x=618, y=861)

Vertragsrahmenzahlung_label = HAUPTMENUE.Label(window, text="", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,),
                                               width=18, heigh=4, relief=GROOVE)
Vertragsrahmenzahlung_label.place(x=219, y=400)

# ******************************************************************************************************************
# ******************************************************************************************************************
# ******************************************************************************************************************
# ************************   BEREICH AUFTRAGGEBER TEXTFELDER ERSTELLEN *********************************************
# ******************************************************************************************************************
# ******************************************************************************************************************
# ******************************************************************************************************************

#                                UMRANDUNG AUFTRAGGEBER ERSTELLEN

AgeberUmrandung = HAUPTMENUE.Frame(window, bd=2, width=406, heigh=250, bg='#BDBDBD', borderwidth=2, relief="groove", )
AgeberUmrandung.place(x=5, y=10)
AgeberUmrandungText_label = HAUPTMENUE.Label(window, text="Auftraggeber", fg='#2F4F4F', bg='#BDBDBD',
                                             font=('courier', 10,), width=16, heigh=1, relief=GROOVE)
AgeberUmrandungText_label.place(x=25, y=5)

#                                    TEXTFELD UND LABEL KUNDENNUMMER ZUFÜGEN

kdnummerAgeber_label = HAUPTMENUE.Label(AgeberUmrandung, text="Kd-Nummer", fg='#2F4F4F', bg='#BDBDBD',
                                        font=('courier', 12,), width=9, heigh=1)
kdnummerAgeber_label.place(x=10, y=30)
kdnummerAgeber_textfeld = Text(AgeberUmrandung, width=10, height=1, wrap='word')
kdnummerAgeber_textfeld.place(x=110, y=30)

#                                TEXTFELD UND LABEL KUNDENNACHNAME ZUFÜGEN

nachnameAgeber_label = HAUPTMENUE.Label(AgeberUmrandung, text="Nachname", fg='#2F4F4F', bg='#BDBDBD',
                                        font=('courier', 12,), width=8, heigh=1)
nachnameAgeber_label.place(x=10, y=60)
nachnameAgeber_textfeld = Text(AgeberUmrandung, width=35, height=1, wrap='word')
nachnameAgeber_textfeld.place(x=110, y=60)

#                                TEXTFELD UND LABEL KUNDENNVORNAME ZUFÜGEN

vornameAgeber_label = HAUPTMENUE.Label(AgeberUmrandung, text="Vorname", fg='#2F4F4F', bg='#BDBDBD',
                                       font=('courier', 12,), width=7, heigh=1)
vornameAgeber_label.place(x=10, y=85)
vornameAgeber_textfeld = Text(AgeberUmrandung, width=35, height=1, wrap='word')
vornameAgeber_textfeld.place(x=110, y=85)

#                                TEXTFELD UND LABEL STRASSE UND NR ZUFÜGEN

strAageber_label = HAUPTMENUE.Label(AgeberUmrandung, text="Str./Nr.", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,),
                                    width=8, heigh=1)
strAageber_label.place(x=10, y=110)
strAgeber_textfeld = Text(AgeberUmrandung, width=30, height=1, wrap='word')
strAgeber_textfeld.place(x=110, y=110)
hnrAgeber_textfeld = Text(AgeberUmrandung, width=4, height=1, wrap='word')
hnrAgeber_textfeld.place(x=358, y=110)

#                                TEXTFELD UND LABEL PLZ UND ORT ZUFÜGEN

plzAgeber_label = HAUPTMENUE.Label(AgeberUmrandung, text="Plz/Ort", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,),
                                   width=7, heigh=1)
plzAgeber_label.place(x=10, y=135)
plzAgeber_textfeld = Text(AgeberUmrandung, width=5, height=1, wrap='word')
plzAgeber_textfeld.place(x=110, y=135)
ortAgeber_textfeld = Text(AgeberUmrandung, width=29, height=1, wrap='word')
ortAgeber_textfeld.place(x=158, y=135)

#                                TEXTFELD UND LABEL ANSPRECHPARTNER ZUFÜGEN

ansprechAgeber_label = HAUPTMENUE.Label(AgeberUmrandung, text="Ansprech", fg='#2F4F4F', bg='#BDBDBD',
                                        font=('courier', 12,), width=8, heigh=1)
ansprechAgeber_label.place(x=10, y=160)
ansprechAgeber_textfeld = Text(AgeberUmrandung, width=35, height=1, wrap='word')
ansprechAgeber_textfeld.place(x=110, y=160)

#                                TEXTFELD UND LABEL TELEFONNUMMER ZUFÜGEN

telAgeber_label = HAUPTMENUE.Label(AgeberUmrandung, text="Telefon", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,),
                                   width=7, heigh=1)
telAgeber_label.place(x=10, y=185)
telAgeber_textfeld = Text(AgeberUmrandung, width=35, height=1, wrap='word')
telAgeber_textfeld.place(x=110, y=185)

#                                TEXTFELD UND LABEL MAIL ZUFÜGEN

mailAgeber_label = HAUPTMENUE.Label(AgeberUmrandung, text="Mail", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,),
                                    width=4, heigh=1)
mailAgeber_label.place(x=10, y=210)
mailAgeber_textfeld = Text(AgeberUmrandung, width=35, height=1, wrap='word')
mailAgeber_textfeld.place(x=110, y=210)

# ******************************************************************************************************************
# ******************************************************************************************************************
# ******************************************************************************************************************
# ************************   BEREICH OBJEKT TEXTFELDER ERSTELLEN   *************************************************
# ******************************************************************************************************************
# ******************************************************************************************************************
# ******************************************************************************************************************

#                                UMRANDUNG OBJEKT ERSTELLEN

ObjektUmrandung = HAUPTMENUE.Frame(window, bd=2, width=406, heigh=263, bg='#BDBDBD', borderwidth=2, relief="groove", )
ObjektUmrandung.place(x=5, y=270)
ObjektUmrandungText_label = HAUPTMENUE.Label(window, text="Objekt", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 10,),
                                             width=16, heigh=1, relief=GROOVE)
ObjektUmrandungText_label.place(x=25, y=266)

#                                TEXTFELD UND LABEL OBJEKTNUMMER ZUFÜGEN

obnrObjekt_label = HAUPTMENUE.Label(ObjektUmrandung, text="Objekt-Nr", fg='#2F4F4F', bg='#BDBDBD',
                                    font=('courier', 12,), width=9, heigh=1)
obnrObjekt_label.place(x=10, y=30)
obnrObjekt_textfeld = Text(ObjektUmrandung, width=5, height=1, wrap='word')
obnrObjekt_textfeld.place(x=110, y=30)

#                               TEXTFELD UND LABEL OBJEKT KUNDENNACHNAME ZUFÜGEN

objektnachname_label = HAUPTMENUE.Label(ObjektUmrandung, text="Nachname", fg='#2F4F4F', bg='#BDBDBD',
                                        font=('courier', 12,), width=8, heigh=1)
objektnachname_label.place(x=10, y=60)
objektnachname_textfeld = Text(ObjektUmrandung, width=35, height=1, wrap='word')
objektnachname_textfeld.place(x=110, y=60)

#                               TEXTFELD UND LABEL OBJEKT KUNDENNVORNAME ZUFÜGEN

objektvorname_label = HAUPTMENUE.Label(ObjektUmrandung, text="Vorname", fg='#2F4F4F', bg='#BDBDBD',
                                       font=('courier', 12,), width=7, heigh=1)
objektvorname_label.place(x=10, y=85)
objektvorname_textfeld = Text(ObjektUmrandung, width=35, height=1, wrap='word')
objektvorname_textfeld.place(x=110, y=85)

#                               TEXTFELD UND LABEL OBJEKT STRASSE UND NR ZUFÜGEN


objektstrasse_label = HAUPTMENUE.Label(ObjektUmrandung, text="Str./Nr.", fg='#2F4F4F', bg='#BDBDBD',
                                       font=('courier', 12,), width=8, heigh=1)
objektstrasse_label.place(x=10, y=110)
objektstrasse_textfeld = Text(ObjektUmrandung, width=30, height=1, wrap='word')
objektstrasse_textfeld.place(x=110, y=110)
objektnr_textfeld = Text(ObjektUmrandung, width=4, height=1, wrap='word')
objektnr_textfeld.place(x=358, y=110)

#                               TEXTFELD UND LABEL OBJEKT PLZ UND ORT ZUFÜGEN

objektplz_label = HAUPTMENUE.Label(ObjektUmrandung, text="Plz/Ort", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,),
                                   width=7, heigh=1)
objektplz_label.place(x=10, y=135)
objektplz_textfeld = Text(ObjektUmrandung, width=5, height=1, wrap='word')
objektplz_textfeld.place(x=110, y=135)
objektort_textfeld = Text(ObjektUmrandung, width=29, height=1, wrap='word')
objektort_textfeld.place(x=158, y=135)

#                               TEXTFELD UND LABEL OBJEKT ZUSATZ ZUFÜGEN

objektzusatz_label = HAUPTMENUE.Label(ObjektUmrandung, text="Zusatz", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,),
                                      width=6, heigh=1)
objektzusatz_label.place(x=10, y=160)
objektzusatz_textfeld = Text(master=ObjektUmrandung, width=35, height=1, wrap='word')
objektzusatz_textfeld.place(x=110, y=160)

#                               TEXTFELD UND LABEL OBJEKT ANSPRECHPARTNER ZUFÜGEN

objektansprechpartner_label = HAUPTMENUE.Label(ObjektUmrandung, text="Ansprech", fg='#2F4F4F', bg='#BDBDBD',
                                               font=('courier', 12,), width=8, heigh=1)
objektansprechpartner_label.place(x=10, y=185)
objektansprechpartner_textfeld = Text(master=ObjektUmrandung, width=35, height=1, wrap='word')
objektansprechpartner_textfeld.place(x=110, y=185)

#                               TEXTFELD UND LABEL OBJEKT TELEFONNUMMER ZUFÜGEN

objekttelefon_label = HAUPTMENUE.Label(ObjektUmrandung, text="Telefon", fg='#2F4F4F', bg='#BDBDBD',
                                       font=('courier', 12,), width=7, heigh=1)
objekttelefon_label.place(x=10, y=210)
objekttelefon_textfeld = Text(master=ObjektUmrandung, width=35, height=1, wrap='word')
objekttelefon_textfeld.place(x=110, y=210)

#                               TEXTFELD UND LABEL OBJEKT MAIL ZUFÜGEN

objektmail_label = HAUPTMENUE.Label(ObjektUmrandung, text="Mail", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,),
                                    width=4, heigh=1)
objektmail_label.place(x=10, y=235)
objektmail_textfeld = Text(master=ObjektUmrandung, width=35, height=1, wrap='word')
objektmail_textfeld.place(x=110, y=235)

# ******************************************************************************************************************
# ******************************************************************************************************************
# ******************************************************************************************************************
# ************************   BEREICH VERTRAG TEXTFELDER ERSTELLEN   ************************************************
# ******************************************************************************************************************
# ******************************************************************************************************************
# ******************************************************************************************************************

#                                UMRANDUNG VERTRAGSART ERSTELLEN

VertragsArtUmrandung = HAUPTMENUE.Frame(window, bd=2, width=411, heigh=58, bg='#BDBDBD', borderwidth=2,
                                        relief="groove", )
VertragsArtUmrandung.place(x=5, y=535)


#                          *******************************************
#                          ***  CHECKBOXEN FÜR VERTRAGSARTAUSWAHL ****
#                          ********************************'**********

def vertragsart_checkbox1_check(vertragsartcheckbox1var):
    if vertragsartcheckbox1var.get() == 1:
        BehandlungenRahmen1.place(x=410, y=535)
        BehandlungenRahmen2.place_forget()
        BehandlungenRahmen3.place_forget()
        vertragsartcheckbox2var.set(0)
        vertragsartcheckbox3var.set(0)
        vertragsartcheckbox4var.set(0)
    else:
        BehandlungenRahmen1.place_forget()


def vertragsart_checkbox2_check(vertragsartcheckbox2var):
    if vertragsartcheckbox2var.get() == 1:
        BehandlungenRahmen1.place_forget()
        BehandlungenRahmen2.place(x=410, y=535)
        BehandlungenRahmen3.place_forget()
        vertragsartcheckbox1var.set(0)
        vertragsartcheckbox3var.set(0)
        vertragsartcheckbox4var.set(0)
    else:
        BehandlungenRahmen2.place_forget()


def vertragsart_checkbox3_check(vertragsartcheckbox3var):
    if vertragsartcheckbox3var.get() == 1:
        BehandlungenRahmen1.place_forget()
        BehandlungenRahmen2.place(x=410, y=535)
        BehandlungenRahmen3.place_forget()
        vertragsartcheckbox1var.set(0)
        vertragsartcheckbox2var.set(0)
        vertragsartcheckbox4var.set(0)
    else:
        BehandlungenRahmen2.place_forget()


def vertragsart_checkbox4_check(vertragsartcheckbox4var):
    if vertragsartcheckbox4var.get() == 1:
        BehandlungenRahmen1.place_forget()
        BehandlungenRahmen2.place_forget()
        BehandlungenRahmen3.place(x=410, y=535)
        vertragsartcheckbox1var.set(0)
        vertragsartcheckbox2var.set(0)
        vertragsartcheckbox3var.set(0)
    else:
        BehandlungenRahmen3.place_forget()


vertragsartcheckbox1var = HAUPTMENUE.IntVar()
vertragsartcheckbox2var = HAUPTMENUE.IntVar()
vertragsartcheckbox3var = HAUPTMENUE.IntVar()
vertragsartcheckbox4var = HAUPTMENUE.IntVar()

vertragsart_checkbox1 = HAUPTMENUE.Checkbutton(VertragsArtUmrandung, text="Wartung", variable=vertragsartcheckbox1var,
                                               fg='#2F4F4F',
                                               bg='#BDBDBD', font=('courier', 12,), width=7, heigh=1, onvalue=1,
                                               offvalue=0,
                                               command=partial(vertragsart_checkbox1_check, vertragsartcheckbox1var))
vertragsart_checkbox1.place(x=5, y=5)

vertragsart_checkbox2 = HAUPTMENUE.Checkbutton(VertragsArtUmrandung, text="Einzel", variable=vertragsartcheckbox2var,
                                               fg='#2F4F4F',
                                               bg='#BDBDBD', onvalue=1, offvalue=0, font=('courier', 12,), width=6,
                                               heigh=1,
                                               command=partial(vertragsart_checkbox2_check, vertragsartcheckbox2var))
vertragsart_checkbox2.place(x=135, y=25)

vertragsart_checkbox3 = HAUPTMENUE.Checkbutton(VertragsArtUmrandung, text="Angebot", variable=vertragsartcheckbox3var,
                                               fg='#2F4F4F',
                                               onvalue=1, offvalue=0, bg='#BDBDBD', font=('courier', 12,), width=7,
                                               heigh=1,
                                               command=partial(vertragsart_checkbox3_check, vertragsartcheckbox3var))
vertragsart_checkbox3.place(x=5, y=25)

vertragsart_checkbox4 = HAUPTMENUE.Checkbutton(VertragsArtUmrandung, text="Mehrfach", variable=vertragsartcheckbox4var,
                                               fg='#2F4F4F',
                                               onvalue=1, offvalue=0, bg='#BDBDBD', font=('courier', 12,), width=8,
                                               heigh=1,
                                               command=partial(vertragsart_checkbox4_check, vertragsartcheckbox4var))
vertragsart_checkbox4.place(x=135, y=5)

vertragsartcheckbox1var.set(1)
vertragsartcheckbox2var.set(0)
vertragsartcheckbox3var.set(0)
vertragsartcheckbox4var.set(0)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                        WECHSELRAHMEN1 FÜR BEHANDLUNGSART WARTUNG ERSTELLEN VERTRAGSKUNDE
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

BehandlungenRahmen1 = HAUPTMENUE.Frame(window, bd=2, width=1301, heigh=58, bg='#BDBDBD', borderwidth=2,
                                       relief="groove", )
BehandlungenRahmen1.place(x=410, y=535)

#                        TEXTFELDER FÜR VERTRAG VON BIS

VertragVonBis_label = HAUPTMENUE.Label(BehandlungenRahmen1, text="Vertrag von-bis", fg='#2F4F4F', bg='#BDBDBD',
                                       font=('courier', 12,), width=15, heigh=1)
VertragVonBis_label.place(x=5, y=5)

VertragVonBis1_textfeld = Text(BehandlungenRahmen1, width=11, height=1, wrap='word')
VertragVonBis1_textfeld.place(x=160, y=5)

VertragVonBis2_textfeld = Text(BehandlungenRahmen1, width=11, height=1, wrap='word')
VertragVonBis2_textfeld.place(x=255, y=5)

#                        TEXTFELD UND LABEL ANZAHL WARTUNG UND INTENSIV EINZEL ZUFÜGEN

vertragsinterval_label = HAUPTMENUE.Label(BehandlungenRahmen1, text="Anzahl Wartung ", fg='#2F4F4F', bg='#BDBDBD',
                                          font=('courier', 12,), width=15, heigh=1)
vertragsinterval_label.place(x=375, y=5)
vertragsinterval_textfeld = Text(BehandlungenRahmen1, width=4, height=1, wrap='word')
vertragsinterval_textfeld.place(x=532, y=5)
vertragsintensivinterval_label = HAUPTMENUE.Label(BehandlungenRahmen1, text="Anzahl Intensiv", fg='#2F4F4F',
                                                  bg='#BDBDBD', font=('courier', 12,), width=15, heigh=1)
vertragsintensivinterval_label.place(x=375, y=30)
vertragsintensivinterval_textfeld = Text(BehandlungenRahmen1, width=4, height=1, wrap='word')
vertragsintensivinterval_textfeld.place(x=532, y=30)

#                        LETZTE BEHANDLUNGEN

letztebehandlung1_label = HAUPTMENUE.Label(BehandlungenRahmen1, text="zuletzt am", fg='#2F4F4F', bg='#BDBDBD',
                                           font=('courier', 12,), width=10, heigh=1)
letztebehandlung1_label.place(x=5, y=30)
letztebehandlung1_textfeld = Text(BehandlungenRahmen1, width=11, height=1, wrap='word')
letztebehandlung1_textfeld.place(x=160, y=30)
letztebehandlung2_textfeld = Text(BehandlungenRahmen1, width=11, height=1, wrap='word')
letztebehandlung2_textfeld.place(x=255, y=30)

#                        KUNDENHINWEISE UND WICHTIG UND UNTERSCHRIFT BENÖTIGT

hinweis_label = HAUPTMENUE.Label(BehandlungenRahmen1, text="Hinweis", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,),
                                 width=7, heigh=1)
hinweis_label.place(x=595, y=5)
hinweis_textfeld = Text(BehandlungenRahmen1, width=47, height=1, wrap='word')
hinweis_textfeld.place(x=677, y=5)

hinweis1_label = HAUPTMENUE.Label(BehandlungenRahmen1, text="Wichtig", fg='#2F4F4F', bg='#BDBDBD',
                                  font=('courier', 12,), width=7, heigh=1)
hinweis1_label.place(x=595, y=30)
hinweis1_textfeld = Text(BehandlungenRahmen1, width=47, height=1, wrap='word')
hinweis1_textfeld.place(x=677, y=30)

barzahlung_checkbox1 = HAUPTMENUE.Checkbutton(BehandlungenRahmen1, text="Bahrzahlung nötig", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('courier', 12,), width=17, heigh=1)
barzahlung_checkbox1.place(x=1080, y=2)

unterschrift_checkbox1 = HAUPTMENUE.Checkbutton(BehandlungenRahmen1, text="Unterschrift nötig", fg='#2F4F4F',
                                                bg='#BDBDBD', font=('courier', 12,), width=18, heigh=1)
unterschrift_checkbox1.place(x=1080, y=25)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                        WECHSELRAHMEN2 FÜR BEHANDLUNGSART ANGEBOT ERSTELLEN
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#                             EINFÜGEN AUFTRAG ZÄHLER NR VON

BehandlungenRahmen2 = HAUPTMENUE.Frame(window, bd=2, width=1301, heigh=58, bg='#BDBDBD', borderwidth=2,
                                       relief="groove", )

#                             EINFÜGEN AUFTRAGSDATUM UND AUFTRAGSNUMMER

AuftragNummer_label = HAUPTMENUE.Label(BehandlungenRahmen2, text="Auftrag Nr.", fg='#2F4F4F', bg='#BDBDBD',
                                       font=('courier', 12,), width=11, heigh=1)
AuftragNummer_label.place(x=5, y=5)
AuftragNummer_textfeld = Text(BehandlungenRahmen2, width=11, height=1, wrap='word')
AuftragNummer_textfeld.place(x=125, y=5)

AuftragVom_label = HAUPTMENUE.Label(BehandlungenRahmen2, text="Auftrag vom", fg='#2F4F4F', bg='#BDBDBD',
                                    font=('courier', 12,), width=11, heigh=1)
AuftragVom_label.place(x=230, y=5)
AuftragVom_textfeld = Text(BehandlungenRahmen2, width=11, height=1, wrap='word')
AuftragVom_textfeld.place(x=350, y=5)

#                            TERMINE UND ZEIT EINFÜGEN

Termin1_label = HAUPTMENUE.Label(BehandlungenRahmen2, text="Termin/Zeit", fg='#2F4F4F', bg='#BDBDBD',
                                 font=('courier', 12,), width=11, heigh=1)
Termin1_label.place(x=495, y=5)
Termin1_textfeld = Text(BehandlungenRahmen2, width=11, height=1, wrap='word')
Termin1_textfeld.place(x=610, y=5)
Termin2_textfeld = Text(BehandlungenRahmen2, width=5, height=1, wrap='word')
Termin2_textfeld.place(x=700, y=5)

Techniker2_label = HAUPTMENUE.Label(BehandlungenRahmen2, text="Techniker", fg='#2F4F4F', bg='#BDBDBD',
                                    font=('courier', 12,), width=9, heigh=1)
Techniker2_label.place(x=775, y=5)
TechnikerCombo2 = ttk.Combobox(BehandlungenRahmen2, values=["Aus Liste Auslesen", "Frickmann", ], font=('courier', 10),
                               width=20)
print(dict(TechnikerCombo2))
TechnikerCombo2.grid(column=1, row=1)
TechnikerCombo2.current(0)
TechnikerCombo2.place(x=875, y=5)
print(TechnikerCombo2.current(), TechnikerCombo2.get())

#                        KUNDENHINWEISE UND WICHTIG UND UNTERSCHRIFT BENÖTIGT

hinweis2_label = HAUPTMENUE.Label(BehandlungenRahmen2, text="Hinweis", fg='#2F4F4F', bg='#BDBDBD',
                                  font=('courier', 12,), width=7, heigh=1)
hinweis2_label.place(x=5, y=30)
hinweis2_textfeld = Text(BehandlungenRahmen2, width=47, height=1, wrap='word')
hinweis2_textfeld.place(x=87, y=30)

hinweis3_label = HAUPTMENUE.Label(BehandlungenRahmen2, text="Wichtig", fg='#2F4F4F', bg='#BDBDBD',
                                  font=('courier', 12,), width=7, heigh=1)
hinweis3_label.place(x=495, y=30)
hinweis3_textfeld = Text(BehandlungenRahmen2, width=47, height=1, wrap='word')
hinweis3_textfeld.place(x=575, y=30)

barzahlung_checkbox2 = HAUPTMENUE.Checkbutton(BehandlungenRahmen2, text="Bahrzahlung nötig", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('courier', 12,), width=17, heigh=1)
barzahlung_checkbox2.place(x=1080, y=2)

unterschrift_checkbox2 = HAUPTMENUE.Checkbutton(BehandlungenRahmen2, text="Unterschrift nötig", fg='#2F4F4F',
                                                bg='#BDBDBD', font=('courier', 12,), width=18, heigh=1)
unterschrift_checkbox2.place(x=1080, y=25)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                        WECHSELRAHMEN3 FÜR BEHANDLUNGSART EINFACH ERSTELLEN
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#                        EINFÜGEN AUFTRAG ZÄHLER NR VON

BehandlungenRahmen3 = HAUPTMENUE.Frame(window, bd=2, width=1301, heigh=58, bg='#BDBDBD', borderwidth=2,
                                       relief="groove", )

NrVon3_label = HAUPTMENUE.Label(BehandlungenRahmen3, text="Nr", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,),
                                width=2, heigh=1)
NrVon3_label.place(x=5, y=5)

NrVon3_textfeld = Text(BehandlungenRahmen3, width=2, height=1, wrap='word')
NrVon3_textfeld.place(x=45, y=5)

NrVon4_label = HAUPTMENUE.Label(BehandlungenRahmen3, text="von", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,),
                                width=3, heigh=1)
NrVon4_label.place(x=5, y=30)

NrVon4_textfeld = Text(BehandlungenRahmen3, width=2, height=1, wrap='word')
NrVon4_textfeld.place(x=45, y=30)

#                        EINFÜGEN AUFTRAGSDATUM UND AUFTRAGSNUMMER

AuftragVom1_label = HAUPTMENUE.Label(BehandlungenRahmen3, text="Auftrag vom", fg='#2F4F4F', bg='#BDBDBD',
                                     font=('courier', 12,), width=11, heigh=1)
AuftragVom1_label.place(x=80, y=5)
AuftragVom1_textfeld = Text(BehandlungenRahmen3, width=11, height=1, wrap='word')
AuftragVom1_textfeld.place(x=200, y=5)

AuftragNummer1_label = HAUPTMENUE.Label(BehandlungenRahmen3, text="Auftrag Nr.", fg='#2F4F4F', bg='#BDBDBD',
                                        font=('courier', 12,), width=11, heigh=1)
AuftragNummer1_label.place(x=80, y=30)
AuftragNummer1_textfeld = Text(BehandlungenRahmen3, width=11, height=1, wrap='word')
AuftragNummer1_textfeld.place(x=200, y=30)

#                        TERMINE UND ZEIT EINFÜGEN

Termin3_label = HAUPTMENUE.Label(BehandlungenRahmen3, text="Termin am", fg='#2F4F4F', bg='#BDBDBD',
                                 font=('courier', 12,), width=9, heigh=1)
Termin3_label.place(x=300, y=5)
Termin3_textfeld = Text(BehandlungenRahmen3, width=11, height=1, wrap='word')
Termin3_textfeld.place(x=397, y=5)
Termin4_label = HAUPTMENUE.Label(BehandlungenRahmen3, text="Zeit", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,),
                                 width=4, heigh=1)
Termin4_label.place(x=496, y=5)
Termin4_textfeld = Text(BehandlungenRahmen3, width=5, height=1, wrap='word')
Termin4_textfeld.place(x=541, y=5)

#                        LETZTE TERMINE

LetzteTermine3_label = HAUPTMENUE.Label(BehandlungenRahmen3, text="Techniker", fg='#2F4F4F', bg='#BDBDBD',
                                        font=('courier', 12,), width=9, heigh=1)
LetzteTermine3_label.place(x=300, y=30)
LetzteTermine3_textfeld = Text(BehandlungenRahmen3, width=23, height=1, wrap='word')
LetzteTermine3_textfeld.place(x=397, y=30)
Termin5_label = HAUPTMENUE.Label(BehandlungenRahmen3, text="Zeit", fg='#2F4F4F', bg='#BDBDBD',
                                 font=('courier', 12,), width=4, heigh=1)
Termin5_label.place(x=496, y=5)
Termin5_textfeld = Text(BehandlungenRahmen3, width=5, height=1, wrap='word')
Termin5_textfeld.place(x=541, y=5)

#                        KUNDENHINWEISE UND WICHTIG UND UNTERSCHRIFT BENÖTIGT

hinweis4_label = HAUPTMENUE.Label(BehandlungenRahmen3, text="Hinweis", fg='#2F4F4F', bg='#BDBDBD',
                                  font=('courier', 12,), width=7, heigh=1)
hinweis4_label.place(x=595, y=5)
hinweis4_textfeld = Text(BehandlungenRahmen3, width=47, height=1, wrap='word')
hinweis4_textfeld.place(x=677, y=5)

hinweis5_label = HAUPTMENUE.Label(BehandlungenRahmen3, text="Wichtig", fg='#2F4F4F', bg='#BDBDBD',
                                  font=('courier', 12,), width=7, heigh=1)
hinweis5_label.place(x=595, y=30)
hinweis5_textfeld = Text(BehandlungenRahmen3, width=47, height=1, wrap='word')
hinweis5_textfeld.place(x=677, y=30)

barzahlung_checkbox3 = HAUPTMENUE.Checkbutton(BehandlungenRahmen3, text="Bahrzahlung nötig", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('courier', 12,), width=17, heigh=1)
barzahlung_checkbox3.place(x=1080, y=2)

unterschrift_checkbox3 = HAUPTMENUE.Checkbutton(BehandlungenRahmen3, text="Unterschrift nötig", fg='#2F4F4F',
                                                bg='#BDBDBD', font=('courier', 12,), width=18, heigh=1)
unterschrift_checkbox3.place(x=1080, y=25)

#                       UMRANDUNG SCHÄDLINGSAUSWAHL ERSTELLEN

TierUmrandung = HAUPTMENUE.Frame(window, bd=2, width=1706, heigh=47, bg='#BDBDBD', borderwidth=2, relief="groove", )
TierUmrandung.place(x=5, y=591)

#                       **********************************************
#                       *****  CHECKBOXEN FÜR SCHÄDLINGSAUSWAHL ******
#                       **********************************************


Tier_checkbox1 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Ratten", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,),
                                        width=6, heigh=1)
Tier_checkbox1.place(x=5, y=8)

Tier_checkbox2 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Mäuse", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,),
                                        width=5, heigh=1)
Tier_checkbox2.place(x=110, y=8)

Tier_checkbox3 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Schaben", fg='#2F4F4F', bg='#BDBDBD',
                                        font=('courier', 12,), width=7, heigh=1)
Tier_checkbox3.place(x=203, y=8)

Tier_checkbox4 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Ameisen", fg='#2F4F4F', bg='#BDBDBD',
                                        font=('courier', 12,), width=7, heigh=1)
Tier_checkbox4.place(x=310, y=8)

Tier_checkbox5 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Wespen", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,),
                                        width=6, heigh=1)
Tier_checkbox5.place(x=420, y=8)

Tier_checkbox6 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Bettwanzen", fg='#2F4F4F', bg='#BDBDBD',
                                        font=('courier', 12,), width=10, heigh=1)
Tier_checkbox6.place(x=520, y=8)

Tier_checkbox7 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Motten", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,),
                                        width=6, heigh=1)
Tier_checkbox7.place(x=660, y=8)

Tier_checkbox8 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Tauben", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,),
                                        width=6, heigh=1)
Tier_checkbox8.place(x=760, y=8)

Tier_checkbox9 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Käfer", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,),
                                        width=5, heigh=1)
Tier_checkbox9.place(x=870, y=8)

Tier_checkbox10 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Marder", fg='#2F4F4F', bg='#BDBDBD',
                                         font=('courier', 12,), width=6, heigh=1)
Tier_checkbox10.place(x=960, y=8)

Tier_checkbox11 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Fliegen", fg='#2F4F4F', bg='#BDBDBD',
                                         font=('courier', 12,), width=7, heigh=1)
Tier_checkbox11.place(x=1060, y=8)

Tier_checkbox11 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Hornissen", fg='#2F4F4F', bg='#BDBDBD',
                                         font=('courier', 12,), width=9, heigh=1)
Tier_checkbox11.place(x=1170, y=8)

Tier_checkbox13 = HAUPTMENUE.Checkbutton(TierUmrandung, text=" ", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,),
                                         width=1, heigh=1)
Tier_checkbox13.place(x=1300, y=8)

TierCheckboxtext_textfeld = Text(TierUmrandung, width=45, height=1, wrap='word')
TierCheckboxtext_textfeld.place(x=1330, y=11)

#                       UMRANDUNG GESETZE UND BEHANDLUNGSBEREICHE UND BESCHRIFTUNG ERSTELLEN

TierUmrandung = HAUPTMENUE.Frame(window, bd=2, width=218, heigh=403, bg='#BDBDBD', borderwidth=2, relief="groove", )
TierUmrandung.place(x=5, y=636)
TierUmrandungText_label: Label = HAUPTMENUE.Label(TierUmrandung, text="GESETZE/BEREICHE", fg='#2F4F4F', bg='#BDBDBD',
                                                  font=('courier', 10,), width=16, heigh=1, relief=GROOVE)
TierUmrandungText_label.place(x=37, y=5)

#                       **********************************************
#                       ***  CHECKBOXEN FÜR GESETZE UND BEREICHE  ****
#                       **********************************************

#                            CHECKBOXEN FÜR GESETZE

Gesetzt_checkbox1 = HAUPTMENUE.Checkbutton(TierUmrandung, text="LMHV/HACCP", fg='#2F4F4F', bg='#BDBDBD',
                                           font=('courier', 12,), width=10, heigh=1)
Gesetzt_checkbox1.place(x=5, y=30)

Gesetzt_checkbox2 = HAUPTMENUE.Checkbutton(TierUmrandung, text="IFSG", fg='#2F4F4F', bg='#BDBDBD',
                                           font=('courier', 12,), width=4, heigh=1)
Gesetzt_checkbox2.place(x=5, y=50)

Gesetzt_checkbox3 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Biozid-VO", fg='#2F4F4F', bg='#BDBDBD',
                                           font=('courier', 12,), width=9, heigh=1)
Gesetzt_checkbox3.place(x=5, y=70)

#                            CHECKBOXEN FÜR BEREICHSAUSWAHL
Bereich_checkbox1 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Köderstationen", fg='#2F4F4F', bg='#BDBDBD',
                                           font=('courier', 12,), width=14, heigh=1)
Bereich_checkbox1.place(x=5, y=95)

Bereich_checkbox2 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Innenbereich", fg='#2F4F4F', bg='#BDBDBD',
                                           font=('courier', 12,), width=12, heigh=1)
Bereich_checkbox2.place(x=5, y=115)

Bereich_checkbox3 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Wohnbereich", fg='#2F4F4F', bg='#BDBDBD',
                                           font=('courier', 12,), width=11, heigh=1)
Bereich_checkbox3.place(x=5, y=135)

Bereich_checkbox4 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Küchenbereich", fg='#2F4F4F', bg='#BDBDBD',
                                           font=('courier', 12,), width=13, heigh=1)
Bereich_checkbox4.place(x=5, y=155)

Bereich_checkbox5 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Aussenbereich", fg='#2F4F4F', bg='#BDBDBD',
                                           font=('courier', 12,), width=13, heigh=1)
Bereich_checkbox5.place(x=5, y=175)

Bereich_checkbox6 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Gartenbereich", fg='#2F4F4F', bg='#BDBDBD',
                                           font=('courier', 12,), width=13, heigh=1)
Bereich_checkbox6.place(x=5, y=195)

Bereich_checkbox7 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Kellerbereich", fg='#2F4F4F', bg='#BDBDBD',
                                           font=('courier', 12,), width=13, heigh=1)
Bereich_checkbox7.place(x=5, y=215)

Bereich_checkbox8 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Müllbereich", fg='#2F4F4F', bg='#BDBDBD',
                                           font=('courier', 12,), width=11, heigh=1)
Bereich_checkbox8.place(x=5, y=235)

Bereich_checkbox9 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Imbissbereich", fg='#2F4F4F', bg='#BDBDBD',
                                           font=('courier', 12,), width=13, heigh=1)
Bereich_checkbox9.place(x=5, y=255)

Bereich_checkbox10 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Tresenbereich", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('courier', 12,), width=13, heigh=1)
Bereich_checkbox10.place(x=5, y=275)

Bereich_checkbox11 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Herstellung/Lager", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('courier', 12,), width=17, heigh=1)
Bereich_checkbox11.place(x=5, y=295)

Bereich_checkbox12 = HAUPTMENUE.Checkbutton(TierUmrandung, text="Ges. Restaurant", fg='#2F4F4F', bg='#BDBDBD',
                                            font=('courier', 12,), width=15, heigh=1)
Bereich_checkbox12.place(x=5, y=315)

Bereich_checkbox13 = HAUPTMENUE.Checkbutton(TierUmrandung, text=" ", fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,),
                                            width=1, heigh=1)
Bereich_checkbox13.place(x=5, y=335)
Bereichcheckboxtext_textfeld = Text(TierUmrandung, width=20, height=1, wrap='word')
Bereichcheckboxtext_textfeld.place(x=29, y=340)

#                       UMRANDUNG FÜR GETROFFENE MASSNAHMEN ERSTELLEN

MassnahmenUmrandung = HAUPTMENUE.Frame(window, bd=2, width=360, heigh=403, bg='#BDBDBD', borderwidth=2,
                                       relief="groove", )
MassnahmenUmrandung.place(x=220, y=636)
MassnahmenUmrandung_label: Label = HAUPTMENUE.Label(MassnahmenUmrandung, text="MASSNAHMEN GETROFFEN", fg='#2F4F4F',
                                                    bg='#BDBDBD', font=('courier', 10,), width=20, heigh=1,
                                                    relief=GROOVE)
MassnahmenUmrandung_label.place(x=90, y=5)

#                  **********************************************
#                  ********  CHECKBOXEN FÜR MAßNAHMEN   *********
#                  **********************************************

Massnahmen_checkbox1 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Inspektion/Wartung der Bereiche", fg='#2F4F4F',
                                              bg='#BDBDBD', font=('courier', 12,), width=31, heigh=1)
Massnahmen_checkbox1.place(x=5, y=30)

Massnahmen_checkbox2 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Vorbeugende Schädlingsbekämpfung",
                                              fg='#2F4F4F', bg='#BDBDBD', font=('courier', 12,), width=32, heigh=1)
Massnahmen_checkbox2.place(x=5, y=50)

Massnahmen_checkbox3 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Erneuerung Köder-/Systemfallen", fg='#2F4F4F',
                                              bg='#BDBDBD', font=('courier', 12,), width=30, heigh=1)
Massnahmen_checkbox3.place(x=5, y=70)

Massnahmen_checkbox4 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Einrichtung Köder-/Systemfallen", fg='#2F4F4F',
                                              bg='#BDBDBD', font=('courier', 12,), width=31, heigh=1)
Massnahmen_checkbox4.place(x=5, y=90)

Massnahmen_checkbox5 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Rodentizidbehandlung", fg='#2F4F4F',
                                              bg='#BDBDBD', font=('courier', 12,), width=20, heigh=1)
Massnahmen_checkbox5.place(x=5, y=110)

Massnahmen_checkbox6 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Gelbehandlung", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('courier', 12,), width=13, heigh=1)
Massnahmen_checkbox6.place(x=5, y=130)

Massnahmen_checkbox7 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Stäubeverfahren", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('courier', 12,), width=15, heigh=1)
Massnahmen_checkbox7.place(x=5, y=150)

Massnahmen_checkbox8 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Schaumbehandlung", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('courier', 12,), width=16, heigh=1)
Massnahmen_checkbox8.place(x=5, y=170)

Massnahmen_checkbox9 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Wärmebehandlung", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('courier', 12,), width=15, heigh=1)
Massnahmen_checkbox9.place(x=5, y=190)

Massnahmen_checkbox10 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Mineralien/Planktonprodukte", fg='#2F4F4F',
                                               bg='#BDBDBD', font=('courier', 12,), width=27, heigh=1)
Massnahmen_checkbox10.place(x=5, y=210)

Massnahmen_checkbox11 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Granulatbehandlung", fg='#2F4F4F',
                                               bg='#BDBDBD', font=('courier', 12,), width=18, heigh=1)
Massnahmen_checkbox11.place(x=5, y=230)

Massnahmen_checkbox12 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Sprüh-/Spritzbehandlung", fg='#2F4F4F',
                                               bg='#BDBDBD', font=('courier', 12,), width=23, heigh=1)
Massnahmen_checkbox12.place(x=5, y=250)

Massnahmen_checkbox13 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Aerosolbehandlung", fg='#2F4F4F',
                                               bg='#BDBDBD', font=('courier', 12,), width=17, heigh=1)
Massnahmen_checkbox13.place(x=5, y=270)

Massnahmen_checkbox14 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Ökologisches Verfahren", fg='#2F4F4F',
                                               bg='#BDBDBD', font=('courier', 12,), width=22, heigh=1)
Massnahmen_checkbox14.place(x=5, y=290)

Massnahmen_checkbox15 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Reinigung/Desinfektion", fg='#2F4F4F',
                                               bg='#BDBDBD', font=('courier', 12,), width=22, heigh=1)
Massnahmen_checkbox15.place(x=5, y=310)

Massnahmen_checkbox16 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Umstellung Toxisch", fg='#2F4F4F',
                                               bg='#BDBDBD', font=('courier', 12,), width=18, heigh=1)
Massnahmen_checkbox16.place(x=5, y=330)

Massnahmen_checkbox17 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text="Umstellung auf Non-Tox", fg='#2F4F4F',
                                               bg='#BDBDBD', font=('courier', 12,), width=22, heigh=1)
Massnahmen_checkbox17.place(x=5, y=350)

Massnahmen_checkbox18 = HAUPTMENUE.Checkbutton(MassnahmenUmrandung, text=" ", fg='#2F4F4F', bg='#BDBDBD',
                                               font=('courier', 12,), width=1, heigh=1)
Massnahmen_checkbox18.place(x=5, y=370)
Massnahmen_checkbox18_textfeld = Text(MassnahmenUmrandung, width=40, height=1, wrap='word')
Massnahmen_checkbox18_textfeld.place(x=27, y=375)

#                       UMRANDUNG FÜR BEFALLSANALYSE UND MATERIALEINSATZ ERSTELLEN

BefallanalyseUmrandung = HAUPTMENUE.Frame(window, bd=2, width=476, heigh=403, bg='#BDBDBD', borderwidth=2,
                                          relief="groove", )
BefallanalyseUmrandung.place(x=578, y=636)
BefallanalyseUmrandung1_label: Label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="BEFALLSANALYSE", fg='#2F4F4F',
                                                        bg='#BDBDBD', font=('courier', 10,), width=14, heigh=1,
                                                        relief=GROOVE)
BefallanalyseUmrandung1_label.place(x=160, y=5)
BefallanalyseUmrandung2_label: Label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="MATERIALEINSATZ", fg='#2F4F4F',
                                                        bg='#BDBDBD', font=('courier', 10,), width=15, heigh=1,
                                                        relief=GROOVE)
BefallanalyseUmrandung2_label.place(x=155, y=207)

#                     **********************************************
#                     ********  BEREICH/CHECKBOXEN BEFALLSANALYSE  *
#                     **********************************************

#                     COMBOBOXEN UM BEFALLSSTÄRKE-HINWEISE ABZUFRAGEN


Befallstaerke_label: Label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="Befall", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('courier', 12,), width=6)
Befallstaerke_label.place(x=5, y=35)

Befallstaerke = ttk.Combobox(BefallanalyseUmrandung,
                             values=[" ", "Stärke:ohne", "Stärke:leicht", "Stärke:leicht-mittel", "Stärke:mittel",
                                     "Stärke:mittel-schwer", "Stärke:schwer"], font=('courier', 10), width=35)
print(dict(Befallstaerke))
Befallstaerke.grid(column=1, row=1)
Befallstaerke.current(0)
Befallstaerke.place(x=85, y=35)
print(Befallstaerke.current(), Befallstaerke.get())

#                  ***********************************************************

Befallzeichen1_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="Hinweis", fg='#2F4F4F', bg='#BDBDBD',
                                        font=('courier', 12,), width=7, heigh=1)
Befallzeichen1_label.place(x=5, y=55)

Befallzeichen1 = ttk.Combobox(BefallanalyseUmrandung,
                              values=["AUS LISTE AUSLESEN ", "Vorbekämpfung mit reinnehmen", "RKS angefressen",
                                      "RKS leergefressen", "MKS angefressen", "MKS leergefressen",
                                      "Kotspuren gesichtet", "Löcher gesichtet", "Fraßspuren gesichtet"
                                                                                 "Laufwege gesichtet",
                                      "Tiere gesichtet", "Tote Tiere gesichtet", "Larven/Eier/Nymphen gesichtet",
                                      "Kunde hat Tiere gesichtet"], font=('courier', 10), width=35)
print(dict(Befallzeichen1))
Befallzeichen1.grid(column=1, row=1)
Befallzeichen1.current(0)
Befallzeichen1.place(x=85, y=55)
print(Befallzeichen1.current(), Befallzeichen1.get())

Befallzeichen1x_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                         font=('courier', 12,), width=1, heigh=1)
Befallzeichen1x_label.place(x=390, y=52)
Befallzeichen1x_textfeld = Text(BefallanalyseUmrandung, width=4, height=1, wrap='word')
Befallzeichen1x_textfeld.place(x=410, y=55)

#                ***********************************************************

Befallzeichen2_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="Hinweis", fg='#2F4F4F', bg='#BDBDBD',
                                        font=('courier', 12,), width=7, heigh=1)
Befallzeichen2_label.place(x=5, y=75)

Befallzeichen2 = ttk.Combobox(BefallanalyseUmrandung,
                              values=[" ", "RKS angefressen", "RKS leergefressen", "MKS angefressen",
                                      "MKS leergefressen", "Kotspuren gesichtet", "Löcher gesichtet",
                                      "Fraßspuren gesichtet"
                                      "Laufwege gesichtet", "Tiere gesichtet", "Tote Tiere gesichtet",
                                      "Larven/Eier/Nymphen gesichtet", "Kunde hat Tiere gesichtet"],
                              font=('courier', 10), width=35)
print(dict(Befallzeichen2))
Befallzeichen2.grid(column=1, row=1)
Befallzeichen2.current(0)
Befallzeichen2.place(x=85, y=75)
print(Befallzeichen2.current(), Befallzeichen2.get())

Befallzeichen2x_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                         font=('courier', 12,), width=1, heigh=1)
Befallzeichen2x_label.place(x=390, y=72)
Befallzeichen2x_textfeld = Text(BefallanalyseUmrandung, width=4, height=1, wrap='word')
Befallzeichen2x_textfeld.place(x=410, y=75)

#                  ***********************************************************

Befallzeichen3_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="Hinweis", fg='#2F4F4F', bg='#BDBDBD',
                                        font=('courier', 12,), width=7, heigh=1)
Befallzeichen3_label.place(x=5, y=95)

Befallzeichen3 = ttk.Combobox(BefallanalyseUmrandung,
                              values=[" ", "RKS angefressen", "RKS leergefressen", "MKS angefressen",
                                      "MKS leergefressen", "Kotspuren gesichtet", "Löcher gesichtet",
                                      "Fraßspuren gesichtet"
                                      "Laufwege gesichtet", "Tiere gesichtet", "Tote Tiere gesichtet",
                                      "Larven/Eier/Nymphen gesichtet", "Kunde hat Tiere gesichtet"],
                              font=('courier', 10), width=35)
print(dict(Befallzeichen3))
Befallzeichen3.grid(column=1, row=1)
Befallzeichen3.current(0)
Befallzeichen3.place(x=85, y=95)
print(Befallzeichen3.current(), Befallzeichen3.get())

Befallzeichen3x_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                         font=('courier', 12,), width=1, heigh=1)
Befallzeichen3x_label.place(x=390, y=92)
Befallzeichen3x_textfeld = Text(BefallanalyseUmrandung, width=4, height=1, wrap='word')
Befallzeichen3x_textfeld.place(x=410, y=95)

#                  ***********************************************************

Befallzeichen4_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="Hinweis", fg='#2F4F4F', bg='#BDBDBD',
                                        font=('courier', 12,), width=7, heigh=1)
Befallzeichen4_label.place(x=5, y=115)

Befallzeichen4 = ttk.Combobox(BefallanalyseUmrandung,
                              values=[" ", "RKS angefressen", "RKS leergefressen", "MKS angefressen",
                                      "MKS leergefressen", "Kotspuren gesichtet", "Löcher gesichtet",
                                      "Fraßspuren gesichtet"
                                      "Laufwege gesichtet", "Tiere gesichtet", "Tote Tiere gesichtet",
                                      "Larven/Eier/Nymphen gesichtet", "Kunde hat Tiere gesichtet"],
                              font=('courier', 10), width=35)
print(dict(Befallzeichen4))
Befallzeichen4.grid(column=1, row=1)
Befallzeichen4.current(0)
Befallzeichen4.place(x=85, y=115)
print(Befallzeichen4.current(), Befallzeichen4.get())

Befallzeichen4x_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                         font=('courier', 12,), width=1, heigh=1)
Befallzeichen4x_label.place(x=390, y=113)
Befallzeichen4x_textfeld = Text(BefallanalyseUmrandung, width=4, height=1, wrap='word')
Befallzeichen4x_textfeld.place(x=410, y=115)

#                  ***********************************************************

Befallzeichen5_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="Hinweis", fg='#2F4F4F', bg='#BDBDBD',
                                        font=('courier', 12,), width=7, heigh=1)
Befallzeichen5_label.place(x=5, y=135)

Befallzeichen5 = ttk.Combobox(BefallanalyseUmrandung,
                              values=[" ", "RKS angefressen", "RKS leergefressen", "MKS angefressen",
                                      "MKS leergefressen", "Kotspuren gesichtet", "Löcher gesichtet",
                                      "Fraßspuren gesichtet"
                                      "Laufwege gesichtet", "Tiere gesichtet", "Tote Tiere gesichtet",
                                      "Larven/Eier/Nymphen gesichtet", "Kunde hat Tiere gesichtet"],
                              font=('courier', 10), width=35)
print(dict(Befallzeichen5))
Befallzeichen5.grid(column=1, row=1)
Befallzeichen5.current(0)
Befallzeichen5.place(x=85, y=135)
print(Befallzeichen5.current(), Befallzeichen5.get())

Befallzeichen5x_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                         font=('courier', 12,), width=1, heigh=1)
Befallzeichen5x_label.place(x=390, y=133)
Befallzeichen5x_textfeld = Text(BefallanalyseUmrandung, width=4, height=1, wrap='word')
Befallzeichen5x_textfeld.place(x=410, y=135)

#                    ***********************************************************

Befallzeichen6_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="Hinweis", fg='#2F4F4F', bg='#BDBDBD',
                                        font=('courier', 12,), width=7, heigh=1)
Befallzeichen6_label.place(x=5, y=160)
Befallzeichen6_textfeld = Text(BefallanalyseUmrandung, width=37, height=1, wrap='word')
Befallzeichen6_textfeld.place(x=85, y=160)
Befallzeichen7_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="Hinweis", fg='#2F4F4F', bg='#BDBDBD',
                                        font=('courier', 12,), width=7, heigh=1)
Befallzeichen7_label.place(x=5, y=180)
Befallzeichen8_textfeld = Text(BefallanalyseUmrandung, width=37, height=1, wrap='word')
Befallzeichen8_textfeld.place(x=85, y=180)

# ******************************************************************************************************************
# ************************   BEREICH MATERIALEINSATZ ***************************************************************
# ******************************************************************************************************************

materialauswahl1_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="Pos. 1 ", fg='#2F4F4F', bg='#BDBDBD',
                                          font=('courier', 12,), width=7, heigh=1)
materialauswahl1_label.place(x=5, y=237)

materialauswahl1 = ttk.Combobox(BefallanalyseUmrandung,
                                values=["MUSS ÜBER LISTE MATERIALVERWALTUNG EINGELESEN WERDENt"], font=('courier', 10),
                                width=35)
print(dict(materialauswahl1))
materialauswahl1.grid(column=1, row=1)
materialauswahl1.current(0)
materialauswahl1.place(x=85, y=237)
print(materialauswahl1.current(), materialauswahl1.get())

materialauswahltext1_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('courier', 12,), width=1, heigh=1)
materialauswahltext1_label.place(x=390, y=234)
materialauswahlzaehlertext1_textfeld = Text(BefallanalyseUmrandung, width=4, height=1, wrap='word')
materialauswahlzaehlertext1_textfeld.place(x=410, y=237)

#                       ***********************************************************

materialauswahl2_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="Pos. 2 ", fg='#2F4F4F', bg='#BDBDBD',
                                          font=('courier', 12,), width=7, heigh=1)
materialauswahl2_label.place(x=5, y=257)

materialauswahl2 = ttk.Combobox(BefallanalyseUmrandung,
                                values=[" ", "MUSS ÜBER LISTE MATERIALVERWALTUNG EINGELESEN WERDENt"],
                                font=('courier', 10), width=35)
print(dict(materialauswahl2))
materialauswahl2.grid(column=1, row=1)
materialauswahl2.current(0)
materialauswahl2.place(x=85, y=257)
print(materialauswahl2.current(), materialauswahl2.get())

materialauswahltext2_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('courier', 12,), width=1, heigh=1)
materialauswahltext2_label.place(x=390, y=253)
materialauswahlzaehlertext2_textfeld = Text(BefallanalyseUmrandung, width=4, height=1, wrap='word')
materialauswahlzaehlertext2_textfeld.place(x=410, y=257)

#                    ***********************************************************

materialauswahl3_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="Pos. 3 ", fg='#2F4F4F', bg='#BDBDBD',
                                          font=('courier', 12,), width=7, heigh=1)
materialauswahl3_label.place(x=5, y=277)

materialauswahl3 = ttk.Combobox(BefallanalyseUmrandung,
                                values=[" ", "MUSS ÜBER LISTE MATERIALVERWALTUNG EINGELESEN WERDENt"],
                                font=('courier', 10), width=35)
print(dict(materialauswahl3))
materialauswahl3.grid(column=1, row=1)
materialauswahl3.current(0)
materialauswahl3.place(x=85, y=277)
print(materialauswahl3.current(), materialauswahl3.get())

materialauswahltext3_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('courier', 12,), width=1, heigh=1)
materialauswahltext3_label.place(x=390, y=273)
materialauswahlzaehlertext3_textfeld = Text(BefallanalyseUmrandung, width=4, height=1, wrap='word')
materialauswahlzaehlertext3_textfeld.place(x=410, y=277)

#                      ***********************************************************

materialauswahl4_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="Pos. 4 ", fg='#2F4F4F', bg='#BDBDBD',
                                          font=('courier', 12,), width=7, heigh=1)
materialauswahl4_label.place(x=5, y=297)

materialauswahl4 = ttk.Combobox(BefallanalyseUmrandung,
                                values=[" ", "MUSS ÜBER LISTE MATERIALVERWALTUNG EINGELESEN WERDENt"],
                                font=('courier', 10), width=35)
print(dict(materialauswahl4))
materialauswahl4.grid(column=1, row=1)
materialauswahl4.current(0)
materialauswahl4.place(x=85, y=297)
print(materialauswahl4.current(), materialauswahl4.get())

materialauswahltext4_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('courier', 12,), width=1, heigh=1)
materialauswahltext4_label.place(x=390, y=293)
materialauswahlzaehlertext4_textfeld = Text(BefallanalyseUmrandung, width=4, height=1, wrap='word')
materialauswahlzaehlertext4_textfeld.place(x=410, y=297)

#                     ***********************************************************

materialauswahl5_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="Pos. 5 ", fg='#2F4F4F', bg='#BDBDBD',
                                          font=('courier', 12,), width=7, heigh=1)
materialauswahl5_label.place(x=5, y=327)
materialauswahltext5_textfeld = Text(BefallanalyseUmrandung, width=37, height=1, wrap='word')
materialauswahltext5_textfeld.place(x=85, y=327)
materialauswahltext5_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('courier', 12,), width=1, heigh=1)
materialauswahltext5_label.place(x=390, y=324)
materialauswahlzaehlertext5_textfeld = Text(BefallanalyseUmrandung, width=4, height=1, wrap='word')
materialauswahlzaehlertext5_textfeld.place(x=410, y=327)

#                     ***********************************************************
materialauswahl6_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="POs. 6 ", fg='#2F4F4F', bg='#BDBDBD',
                                          font=('courier', 12,), width=7, heigh=1)
materialauswahl6_label.place(x=5, y=347)
materialauswahltext6_textfeld = Text(BefallanalyseUmrandung, width=37, height=1, wrap='word')
materialauswahltext6_textfeld.place(x=85, y=347)
materialauswahltext6_label = HAUPTMENUE.Label(BefallanalyseUmrandung, text="x", fg='#2F4F4F', bg='#BDBDBD',
                                              font=('courier', 12,), width=1, heigh=1)
materialauswahltext6_label.place(x=390, y=344)
materialauswahlzaehlertext6_textfeld = Text(BefallanalyseUmrandung, width=4, height=1, wrap='word')
materialauswahlzaehlertext6_textfeld.place(x=410, y=347)

# ******************************************************************************************************************
# ******************************************************************************************************************
# ************************    BEREICH BEZAHLUNG ERSTELLEN           ************************************************
# ******************************************************************************************************************
# ******************************************************************************************************************

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                        RAHMEN FÜR ZAHLUNGS- UND RECHNUNGSSTELLUNG
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

ZahlungsRahmen0 = HAUPTMENUE.Frame(window, bd=2, width=659, heigh=403, bg='#BDBDBD', borderwidth=2, relief="groove", )
ZahlungsRahmen0.place(x=1052, y=636)

#                        DURCHGEFÜHRT AM UND VON WELCHEN TECHNIKER

ErledigtAm_label = HAUPTMENUE.Label(ZahlungsRahmen0, text="Durchgeführt am", fg='#2F4F4F', bg='#BDBDBD',
                                    font=('courier', 12,), width=15, heigh=1)
ErledigtAm_label.place(x=5, y=7)
ErledigtAm_textfeld = Text(ZahlungsRahmen0, width=11, height=1, wrap='word')
ErledigtAm_textfeld.place(x=165, y=7)
ErledigtVon_label = HAUPTMENUE.Label(ZahlungsRahmen0, text="von Techniker", fg='#2F4F4F', bg='#BDBDBD',
                                     font=('courier', 12,), width=13, heigh=1)
ErledigtVon_label.place(x=265, y=7)

ErledigtVonCombo = ttk.Combobox(ZahlungsRahmen0, values=["Aus Liste Auslesen", "Frickmann", ], font=('courier', 10),
                                width=20)
print(dict(ErledigtVonCombo))
ErledigtVonCombo.grid(column=1, row=1)
ErledigtVonCombo.current(0)
ErledigtVonCombo.place(x=410, y=7)
print(ErledigtVonCombo.current(), ErledigtVonCombo.get())


#                        ZAHLUNGSARTEN HINZUGEFÜGT

def Zahlart_checkbox1_check(Zahlartcheckbox1var):
    messagebox.showinfo(message="Infotext", title="Box-Titel")
    if Zahlartcheckbox1var.get() == 1:
        Zahlartcheckbox2var.set(0)
        Zahlartcheckbox3var.set(0)
        Zahlartcheckbox4var.set(0)
    else:
        pass


def Zahlart_checkbox2_check(Zahlartcheckbox2var):
    if Zahlartcheckbox2var.get() == 1:
        Zahlartcheckbox1var.set(0)
        Zahlartcheckbox3var.set(0)
        Zahlartcheckbox4var.set(0)
    else:
        pass


def Zahlart_checkbox3_check(Zahlartcheckbox3var):
    if Zahlartcheckbox3var.get() == 1:
        Zahlartcheckbox1var.set(0)
        Zahlartcheckbox2var.set(0)
        Zahlartcheckbox4var.set(0)
    else:
        pass


def Zahlart_checkbox4_check(Zahlartcheckbox4var):
    if Zahlartcheckbox4var.get() == 1:
        Zahlartcheckbox1var.set(0)
        Zahlartcheckbox2var.set(0)
        Zahlartcheckbox3var.set(0)
    #    messagebox.showinfo(message="Infotext", title="Box-Titel")
    else:
        BehandlungenRahmen1.place_forget()


Zahlartcheckbox1var = HAUPTMENUE.IntVar()
Zahlartcheckbox2var = HAUPTMENUE.IntVar()
Zahlartcheckbox3var = HAUPTMENUE.IntVar()
Zahlartcheckbox4var = HAUPTMENUE.IntVar()

Zahlart_checkbox1 = HAUPTMENUE.Checkbutton(ZahlungsRahmen0, text="Überweisung", fg='#2F4F4F', bg='#BDBDBD',
                                           font=('courier', 12,), width=11, heigh=1, onvalue=1, offvalue=0,
                                           variable=Zahlartcheckbox1var,
                                           command=partial(Zahlart_checkbox1_check, Zahlartcheckbox1var))
Zahlart_checkbox1.place(x=5, y=30)

Zahlart_checkbox2 = HAUPTMENUE.Checkbutton(ZahlungsRahmen0, text="EC-Zahlung", fg='#2F4F4F', bg='#BDBDBD',
                                           font=('courier', 12,), width=10, heigh=1, onvalue=1, offvalue=0,
                                           variable=Zahlartcheckbox2var,
                                           command=partial(Zahlart_checkbox2_check, Zahlartcheckbox2var))
Zahlart_checkbox2.place(x=155, y=30)

Zahlart_checkbox3 = HAUPTMENUE.Checkbutton(ZahlungsRahmen0, text="Barzahlung", fg='#2F4F4F', bg='#BDBDBD',
                                           font=('courier', 12,), width=10, heigh=1, onvalue=1, offvalue=0,
                                           variable=Zahlartcheckbox3var,
                                           command=partial(Zahlart_checkbox3_check, Zahlartcheckbox3var))
Zahlart_checkbox3.place(x=295, y=30)

Zahlart_checkbox4 = HAUPTMENUE.Checkbutton(ZahlungsRahmen0, text="Monatlich", fg='#2F4F4F', bg='#BDBDBD',
                                           font=('courier', 12,), width=9, heigh=1, onvalue=1, offvalue=0,
                                           variable=Zahlartcheckbox4var,
                                           command=partial(Zahlart_checkbox4_check, Zahlartcheckbox4var))
Zahlart_checkbox4.place(x=435, y=30)

Zahlartcheckbox1var.set(1)
Zahlartcheckbox2var.set(0)
Zahlartcheckbox3var.set(0)
Zahlartcheckbox4var.set(0)

nachnameAgeber_textfeld.focus()

# def tab_order():
#    widgets = [1.textfeld,
#              2.textfeld
#             3.textfeld]
# for w in widgets
#    w.lift()
# tab_order()

# kdnummer_textfeld = Text(BehandlungenRahmen1, width=50, height=5, wrap='word')
# kdnummer_textfeld.place(x=1, y=1)
#   AUSBELNDEN BehandlungenRahmen1.place_forget()
#   EINBLENDEN BehandlungenRahmen1.place(x=600, y=400)
#                       EINGABEFELDER FÜR VERTRAGSPREISE

#                     CHECKLISTE FÜR ZAHLUNG


# ******************************************************************************************************************
# ******************************************************************************************************************
# ************************   BEREICH OBJEKT DROPDOWNLISTE ERSTELLEN   **********************************************
# ******************************************************************************************************************
# ******************************************************************************************************************

# DROPDOWNMENUE FÜR VERTRAGSSTATUS ZUFÜGEN
# objektstatus_label = HAUPTMENUE.Label(window, text="Status", fg='#2F4F4F', bg='#BDBDBD',  width=6, heigh=1)
# objektstatus_label.place(x=10, y=550)
# Ostatusliste = [
#  "",
#  "Wartungskunden mit Vertrag",
# "Wartungskunden ohne Vertrag",
# "Mehrfachauftrag",
# "Einzelauftrag",
# ]
# variable = HAUPTMENUE.StringVar(window)
# variable.set(Ostatusliste[0])
# Ostatusliste1 = HAUPTMENUE.OptionMenu(window, variable, *Ostatusliste)
# Ostatusliste1.config(width=30,font=('courier', 10), bg='#FFFFFF', relief=FLAT)
# Ostatusliste1.pack(side="left")
# Ostatusliste1.place(x=111, y=550)

# messagebox.showinfo(message=kdnummerAgeber_textfeld.grab_current(), title="Box-Titel")
window.mainloop()
# HauptMenue()
