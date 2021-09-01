from mongo_connection import *

mongo_connect()

# This is for defining and changing the data model
# TO NOT TOUCH UNLESS INSTRUCTED AND SUPERVISED

class User(Document):
    user_name = StringField(max_lenght=20, required=True)
    user_password = StringField(min_lenght=5, max_lenght=20, required=True)



class Kunde(Document):
    kunde_nr = StringField(min_length=10, max_lenght=10, required=True)
    kunde_typ = StringField()
    vorname = StringField(max_length=50, required=True)
    nachname = StringField(max_length=50, required=True)
    voll_name = str(nachname) + " " + str(vorname)
    strasse = StringField(required=True)
    haus_nr = IntField(required=True)
    plz = IntField(length=5, required=True)
    stadt = StringField(required=True)
    telefon_nr = StringField()
    fax_nr = StringField()
    email = StringField()

    meta = {'allow_inheritance': True}


class KundeEinmalig(Kunde):
    anzahl_bh = 1

class KundeWartung(Kunde):
    anzahl_bh = IntField(required=True)

class KundeIntensiv(Kunde):
    anzahl_bh = IntField(required=True)


class Objekt(Document):
    objekt_nr = IntField(required=True)
    besitzer = ReferenceField(Kunde)

    meta = {'allow_inheritance': True}


class Schaedlinge(Document):
    name = StringField(required=True)


class Wirkstoffe(Document):
    name = StringField(required=True)
    anzahl_lager = IntField()


class Rechnung(EmbeddedDocumentField):
    pdf_loc = StringField()
    rechnung_nr = LongField(lenght=10, required=True)