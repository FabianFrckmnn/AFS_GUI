# ERÖFFNET EINE SEITE
import tkinter as TITELSEITE

window = TITELSEITE.Tk()

# SETZEN DER FENSTERGRÖßE
window.geometry("1920x1080")
# SETZT DEN FENSTERTITEL
window.title("STARTSEITE")

# ÜBERSCHRIFT HINZUFÜGEN
titelseite_label = TITELSEITE.Label(window, text="AFS SCHÄDLINGSBEKÄMPFUNG SOFTWARE", fg='#fff000', bg='grey', font=( 'times', 25, 'bold', 'italic'), width=100, heigh=2)
titelseite_label.place (x=5,y=5)
# BUTTON HINZUFÜGEN
titelseite_button = TITELSEITE.Button(window, text="BEENDEN",fg='#2F4F4F', bg='orange', width=20, heigh=5, command=window.quit)
titelseite_button.place(x=900, y=980)

window.mainloop()

