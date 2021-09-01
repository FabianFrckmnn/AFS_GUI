from mongoengine import *

def mongo_connect():
    connect('afs-db')