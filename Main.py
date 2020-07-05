import tkinter as tk
from tkinter import ttk
from datetime import date
from sqlite import SQLiteHandler

class MainApplication():
    
    # tk-Variablen "Deklarieren"

    def __init__(self, root):
        self.root = root
        
        self.max_tage   = tk.StringVar()
        self.var        = tk.IntVar()
        self.dauer      = tk.StringVar()
        self.personen   = tk.StringVar()
        self.gesund     = tk.StringVar()
        
        self.menge      = tk.StringVar()
        self.einheit    = tk.StringVar()
        self.zutatToAdd = tk.StringVar()
        self.dauer      = tk.StringVar()
        self.personen   = tk.StringVar()
        self.gesund     = tk.StringVar()

        self.sqlh       = SQLiteHandler()

        self.configure_gui()

    def configure_gui(self):

        root.title("Test Programm")
        #root.geometry("500x280")

        tab_parent = ttk.Notebook(root)
        
        tab_wochenplan = ttk.Frame(tab_parent)
        tab_solo       = ttk.Frame(tab_parent)
        tab_rezept     = ttk.Frame(tab_parent)
        tab_zutat      = ttk.Frame(tab_parent)
        
        tab_parent.add(tab_wochenplan, text="Wochenplan")
        tab_parent.add(tab_solo,       text="Spontan")
        tab_parent.add(tab_rezept,     text="Rezepte")
        tab_parent.add(tab_zutat,      text="Zutaten")
        
        tab_parent.pack(expand=1, fill='both')
        
        self.create_tab_wochenplan(tab_wochenplan)
        self.create_tab_solo(tab_solo)
        self.create_tab_rezept(tab_rezept)
        self.create_tab_zutat(tab_zutat)
    
    
    def create_tab_solo(self, tab):
        pass
    
    def create_tab_zutat(self, tab):
        pass
    
    def create_tab_wochenplan(self, tab):

        WOCHENTAGE = ("Montag", "Dienstag", "Mittwoch", "Donnerstag",
                      "Freitag", "Samstag", "Sonntag")

        self.max_tage.set("7")
        
        heute = date.today()
        
        # -----------------------
        #    Struktur frames
        # -----------------------
        
        frame_left  = tk.Frame(tab)
        frame_right = tk.Frame(tab)
        
        frame_left.grid(row=0, column=0, padx=5, pady=5)
        frame_right.grid(row=0, column=1, padx=5, pady=5)
        
        # -----------------------
        #     linke Seite
        # -----------------------
        
        label0 = ttk.Label(frame_left, text='Anzahl der Tage:')
        label0.grid(row=0, column=0, sticky='W')
        
        entry = ttk.Entry(frame_left, textvariable=self.max_tage)
        entry.grid(row=0, column=1)
        
        listbox = tk.Listbox(frame_left)
        listbox.grid(row=1, columnspan=2, sticky='nsew')
        
        def listbox_edit(*_):
            nonlocal listbox
            n = int(self.max_tage.get())
            listbox.delete(0, tk.END)
            for i in range(int(n)):
                listbox.insert('end', WOCHENTAGE[(heute.weekday()+i) % 7])
                
        self.max_tage.trace("w", listbox_edit)
        listbox_edit(0, 0, 0)

        v = tk.IntVar(frame_right)
 
        rad1 = ttk.Radiobutton(frame_left, text="Mittag", variable=v, value=1)
        rad2 = ttk.Radiobutton(frame_left, text="Abends", variable=v, value=2)

        rad1.grid(row=2, column=0, sticky="W")
        rad2.grid(row=2, column=1, sticky="W")
        
        v.set(1)
        
        self.var.set(1)
        
        c = ttk.Checkbutton(frame_left, text="Mahlzeit planen?", variable=self.var)
        c.grid(row=3, column=0,sticky="W")

        # -----------------------
        #    rechte Seite
        # -----------------------
        
        label1 = ttk.Label(frame_right, text='Dauer:')
        label1.grid(row=0, column=0, sticky='W')
        
        entry1 = ttk.Entry(frame_right, textvariable=self.dauer)
        entry1.grid(row=0, column=1)
        
        label2 = ttk.Label(frame_right, text='Personen:')
        label2.grid(row=1, column=0, sticky='W')
        
        entry2 = ttk.Entry(frame_right, textvariable=self.personen)
        entry2.grid(row=1, column=1)
        
        label3 = ttk.Label(frame_right, text='Gesund:')
        label3.grid(row=2, column=0, sticky='W')
        
        opt3 = tk.OptionMenu(frame_right, self.gesund, "egal","sehr gesund","gesund","neutral","ungesund","sehr ungesund")
        opt3.grid(row=2, column=1)
        
        label4 = ttk.Label(frame_right, text='Geschmack:')
        label4.grid(row=3, column=0, sticky='W')
        
        opt4 = tk.OptionMenu(frame_right, self.gesund, "Sehr lecker","lecker","Okay...","Naja")
        opt4.grid(row=3, column=1)


        spinbox = tk.Spinbox(frame_right, from_=1, to=10)
        spinbox.grid(row=4, column=0)

        
    
    def create_tab_rezept(self, tab):
        
        gerichtliste = ["Sauerbraten", "Hühnerfrikasse", "Mettigel", "Hummer"]
        zutatenliste = ["Apfel", "Kasseler", "Ziebel(n)", "Gewürzgurken"]*8
        units = ["Stk.", "kg", "g", "l", "ml", "EL", "Priese"]
        # variable.set(units[0])
        
        # -----------------------
        #    Struktur frames
        # -----------------------
        
        frame_left  = tk.Frame(tab)
        frame_right = tk.Frame(tab)
        
        frame_left.grid( row=0, column=0, padx=5, pady=5)
        frame_right.grid(row=0, column=1, padx=5, pady=5)

        frame = tk.Frame(frame_right)
        frame.grid(row=4, columnspan=3)

        # -----------------------
        #     linke Seite
        # -----------------------
        
        label0 = ttk.Label(frame_left, text='Rezeptname:')
        label0.grid(row=0, column=0, sticky='W')
        
        opt = ttk.Combobox(frame_left, values=gerichtliste)
        opt.grid(row=0, column=1, sticky='nsew')
        
        rezept = tk.Text(frame_left, width=30, height=10)
        rezept.grid(row=1, columnspan=2, pady=5)

        # -----------------------
        #    rechte Seite
        # -----------------------

        zutaten_tf = tk.Text(frame_right, width=30, height=20)
        zutaten_tf.grid(row=0, column=0)

        zutaten_tf

        label1 = ttk.Label(frame, text='Dauer:')
        label1.grid(row=0, column=0, sticky='W')
        
        entry1 = ttk.Entry(frame, textvariable=self.dauer)
        entry1.grid(row=0, column=1)
        
        label2 = ttk.Label(frame, text='Personen:')
        label2.grid(row=1, column=0, sticky='W')
        
        entry2 = ttk.Entry(frame, textvariable=self.personen)
        entry2.grid(row=1, column=1)
        
        label3 = ttk.Label(frame, text='Gesund:')
        label3.grid(row=2, column=0, sticky='W')
        
        opt3 = tk.OptionMenu(frame, self.gesund, "sehr gesund", "gesund", "neutral", "ungesund", "sehr ungesund")
        opt3.grid(row=2, column=1)

    def add_zutat(self):
        pass

if __name__ == '__main__':
    root = tk.Tk()
    main_app = MainApplication(root)
    root.mainloop()
