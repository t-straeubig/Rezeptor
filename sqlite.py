import sqlite3 as sql
import os


db_file = 'test.db'


def create_new_db():
    
    # Löschen falls vorhanden
    if os.path.isfile(db_file):
        try:
            os.remove(db_file)
        except:
            print('Löschen der alten Datenbank nicht möglich.')
        
    # Datenbank öffnen / Erzeugen
    connection = sql.connect(db_file)
    
 
    # Rezept-Tabelle erstellen
    connection.execute("""
    create table Rezept (
    Name varchar(20) primary key,
    Dauer int(3),
    Gesund int(1),
    zuletzt date,
    zubereitung CLOB
    );""")
    
    # Zutaten Tabelle
    connection.execute("""
    create table Zutat (
    Name varchar(20) primary key,
    Kosten float(5),
    Kalorien int(4),
    Kategorie enum('Gemuese','Fleisch','Gewuerz')
    );""")
    
    
    # Menge Tabelle
    connection.execute("""
    create table Menge (
    Zutat varchar(20),
    Rezept varchar(20),
    Menge float(4),
    primary key(Rezept,Zutat)
    );""")
    
    
    # Vorrat Tabelle
    connection.execute("""
    create table Vorrat (
    ID int(4) primary key,
    Zutat varchar(20),
    Ablauf date,
    Menge float(4),
    );""")
  
    
    # Änderungen speichern
    try:
        connection.commit()
    except:
        print('Änderungen konnten nicht gespeichert werden')
    
    # Datenbank schließen
    try:
        connection.commit()
    except:
        print('Schließen der Datenbank nicht möglich')
    