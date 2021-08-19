# ERÖFFNET EINE SEITE
from tkinter import *
import tkinter as TITELSEITE
import datetime
import BILDER

window = TITELSEITE.Tk()

# SETZEN DER FENSTERGRÖßE
window.geometry("1920x1080")
window.configure(bg="#848484")
# SETZT DEN FENSTERTITEL
window.title("STARTSEITE")

# ÜBERSCHRIFT HINZUFÜGEN
titelseite_label = TITELSEITE.Label(window, text="SCHÄDLINGSBEKÄMPFUNG OFFICE-SOFTWARE", fg='#2F4F4F', bg='#6E6E6E',
                                    font=('times', 25, 'bold', 'italic'), width=105, heigh=2)
titelseite_label.place(x=0, y=50)


# BUTTON HINZUFÜGEN
titelseite_button = TITELSEITE.Button(window, text="WEITER", fg='#2F4F4F', bg='#6E6E6E', width=30, heigh=5,
                                      command=window.quit)
titelseite_button.place(x=860, y=940)

# TITELBILD IMAGE EINFÜGEN
startbild = TITELSEITE.PhotoImage(file=BILDER.startseiteimage)
titelseite_startbild = Label(image = startbild)
titelseite_startbild.image = startbild
titelseite_startbild.place(x=400, y=400)

# DATUM/UHRZEIT HINZUFÜGEN
titelzeit_label = TITELSEITE.Label(window, text=datetime.datetime.now().strftime("%d.%m.%Y     %H:%M"), fg='#2F4F4F', bg='#6E6E6E',
                                    font=('times', 25, 'bold', 'italic'), width=105, heigh=2)
titelzeit_label.place(x=0, y=110)

window.mainloop()
