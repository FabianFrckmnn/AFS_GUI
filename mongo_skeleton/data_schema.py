from mongo_connection import *

mongo_connect()

# This is for defining and changing the data model
# TO NOT TOUCH UNLESS INSTRUCTED AND SUPERVISED

class User(Document):
    user_name = StringField(max_lenght=20, required=True)
    user_password = StringField(min_lenght=5, max_lenght=20, required=True)



class Kunde(Document):
    kunde_nr = StringField(min_length=10, max_lenght=10, required=True)
    nachname = StringField(max_length=35, required=True)
    vorname = StringField(max_length=35)
    zusatz = StringField(max_length=35)
    strasse = StringField(max_length=30, required=True)
    haus_nr = StringField(max_length=4, required=True)
    plz = StringField(length=5, required=True)
    stadt = StringField(max_length=29, required=True)
    ansprech = StringField(max_length=35)
    telefon_nr = StringField(max_length=35)
    email = StringField(max_length=35)
    kunde_typ = StringField()

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