import sqlite3 as sql
import os
import sys

DB_FILE = 'test.db'


class SQLiteHandler:

    def __init__(self):

        if os.path.isfile(DB_FILE):
            self.connection = sql.connect(DB_FILE)
        else:
            self.connection = sql.connect(DB_FILE)
            self.create_db_schema()

        self.cur = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def insert(self, table, dict):

        attributes = ""
        values = ""
        for key, value in dict.items():
            attributes += key+","
            values += values+","

        attributes = attributes[:-1]
        values = values[:-1]

        sqlcode = "INSERT INTO {}({}) VALUES {}".format(table, attributes, values)

        self.cur.execute(sqlcode)
        self.connection.commit()

    def create_db_schema(self):

        # Rezept-Tabelle erstellen
        self.cur.execute("""
        DROP Rezept IF EXISTS;
        CREATE TABLE Rezept (
        Name            TEXT PRIMARY KEY,
        Dauer           INTEGER,
        Gesund          INTEGER,
        zuletzt         TEXT,
        zubereitung     TEXT
        );""")

        # Zutaten Tabelle
        self.cur.execute("""
        DROP Zutat IF EXISTS;
        CREATE TABLE Zutat (
        Name            TEXT PRIMARY KEY,
        Kosten          REAL,
        Eiweiß          INTEGER,
        Kohlenhydrate   INTEGER,
        Fett            INTEGER,
        Saisonstart     TEXT,
        Saisonende      TEXT,
        Kategorie       TEXT,
        );""")

        # Menge Tabelle
        self.cur.execute("""
        DROP Enthalten IF EXISTS;
        CREATE TABLE Enthalten (
        Zutat           TEXT,
        Rezept          TEXT,
        Menge           REAL,
        PRIMARY KEY(Rezept, Zutat),
        FOREIGN KEY(Zutat) REFERENCES Zutat(Name),
        FOREIGN KEY(Rezept) REFERENCES Rezept(Name)
        );""")

        # Vorrat Tabelle
        self.cur.execute("""
        DROP Vorrat if EXISTS;
        create table Vorrat (
        ID INTEGER PRIMARY KEY,
        Zutat TEXT,
        Ablauf NUMERIC,
        Menge REAL,
        FOREIGN KEY(Zutat) REFERENCES Zutat(Name)
        );""")

        # Änderungen speichern
        try:
            self.connection.commit()
        except:
            print('create_db_schema(): Änderungen konnten nicht gespeichert werden')
            sys.exit(-1)

