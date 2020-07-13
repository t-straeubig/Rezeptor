import tkinter as tk
from tkinter import ttk
from datetime import date
from sqlite import SQLiteHandler
from utilities import CustomText
from os import system

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
        self.zutat      = tk.StringVar()
        self.zusatz     = tk.StringVar()
        self.zutaten    = tk.StringVar()
        self.dauer      = tk.StringVar()
        self.personen   = tk.StringVar()
        self.gesund     = tk.StringVar()

        self.sqlh       = SQLiteHandler()

        self.check_numbers_only = (root.register(self.numbers_only), '%S')

        self.configure_gui()

    @staticmethod
    def numbers_only(what):
        try:
            float(what)
            return True
        except:
            return False

    def configure_gui(self):

        root.title("Test Programm")
        #root.geometry("500x280")

        tab_parent = ttk.Notebook(root)
        
        tab_wochenplan = ttk.Frame(tab_parent)
        tab_sql       = ttk.Frame(tab_parent)
        tab_rezept     = ttk.Frame(tab_parent)
        tab_zutat      = ttk.Frame(tab_parent)
        
        tab_parent.add(tab_wochenplan, text="Wochenplan")
        tab_parent.add(tab_rezept,     text="Rezepte")
        tab_parent.add(tab_zutat,      text="Zutaten")
        tab_parent.add(tab_sql, text="SQL")
        
        tab_parent.pack(expand=1, fill='both')
        
        self.create_tab_wochenplan(tab_wochenplan)
        self.create_tab_sql(tab_sql)
        self.create_tab_rezept(tab_rezept)
        self.create_tab_zutat(tab_zutat)
    
    
    def create_tab_sql(self, tab):
        pass
    
    def create_tab_zutat(self, tab):

        zutatenliste = ['Apfel', 'Dörrpflaume', 'Mehl', 'Kneckebrot']
        kategorien   = ['Fleisch','Fisch','Gemüse','Gewürze']
        monate = ['Januar','Februar','März','April','Mai','Juni','Juli','August','September','Oktober','November','Dezember']

        # -----------------------
        #    Struktur frames
        # -----------------------

        frame_left = tk.Frame(tab)
        frame_right = tk.Frame(tab)

        frame_left.grid(row=0, column=0, padx=5, pady=5)
        frame_right.grid(row=0, column=1, padx=5, pady=5)

        # -----------------------
        #     linke Seite
        # -----------------------

        label0 = ttk.Label(frame_left, text='Zutat:')
        label0.grid(row=0, column=0, sticky='W')

        comb0 = ttk.Combobox(frame_left, values=zutatenliste)
        comb0.grid(row=1, column=0, sticky='nsew')

        label1 = ttk.Label(frame_left, text='Undefinierte Zutaten:')
        label1.grid(row=2, column=0, sticky='W')

        listbox1 = tk.Listbox(frame_left)
        listbox1.grid(row=3, columnspan=2, sticky='nsew')

        label2 = ttk.Label(frame_left, text='Überschreiben durch:')
        label2.grid(row=4, column=0, sticky='W')

        comb3 = ttk.Combobox(frame_left, values=zutatenliste)
        comb3.grid(row=5, column=0, sticky='nsew')

        # -----------------------
        #    rechte Seite
        # -----------------------

        label4 = ttk.Label(frame_right, text='Kategorie:')
        label4.grid(row=0, column=0, sticky='W')

        comb4 = ttk.Combobox(frame_right, values=kategorien)
        comb4.grid(row=0, column=1, sticky='nsew')

        frame = tk.Frame(frame_right, relief="sunken",borderwidth = 2)
        frame.grid(row=1, columnspan=2)

        label5 = ttk.Label(frame, text='Übliche Angabe der Kaufmenge:')
        label5.grid(row=0, column=0, sticky='W', columnspan=2)

        v = tk.IntVar(frame_right)

        rad1 = ttk.Radiobutton(frame, text="Stück",   variable=v, value=1)
        rad2 = ttk.Radiobutton(frame, text="Masse",   variable=v, value=2)
        rad3 = ttk.Radiobutton(frame, text="Volumen", variable=v, value=3)

        rad1.grid(row=1, column=0)
        rad2.grid(row=1, column=1)
        rad3.grid(row=1, column=2)

        label51 = ttk.Label(frame, text='g pro Stück /// g pro ml')
        label51.grid(row=2, column=0, sticky='W', columnspan=2)

        entry6 = tk.Entry(frame, validate='all', validatecommand=self.check_numbers_only)
        entry6.grid(row=2, column=2, sticky='nsew')


        frame0 = tk.Frame(frame_right, relief="sunken", borderwidth=2)
        frame0.grid(row=2, columnspan=2, pady=5)

        label60 = ttk.Label(frame0, text='Nährstoffe je 100 g:')
        label60.grid(row=0, column=0, sticky='W', columnspan=2)

        label6 = ttk.Label(frame0, text='Kohlenhydrate:')
        label6.grid(row=1, column=0, sticky='W')

        entry6 = tk.Entry(frame0, validate='all', validatecommand=self.check_numbers_only)
        entry6.grid(row=1, column=1, sticky='nsew')

        label7 = ttk.Label(frame0, text='Eiweiß:')
        label7.grid(row=2, column=0, sticky='W')

        entry7 = tk.Entry(frame0, validate='all', validatecommand=self.check_numbers_only)
        entry7.grid(row=2, column=1, sticky='nsew')

        label8 = ttk.Label(frame0, text='Fett:')
        label8.grid(row=3, column=0, sticky='W')

        entry8 = tk.Entry(frame0, validate='all', validatecommand=self.check_numbers_only)
        entry8.grid(row=3, column=1, sticky='nsew')

        frame1 = tk.Frame(frame_right, relief="sunken", borderwidth=2)
        frame1.grid(row=3, columnspan=2, pady=5)

        label7 = ttk.Label(frame1, text='Saison')
        label7.grid(row=0, column=0, sticky='W', columnspan=3)

        label71 = ttk.Label(frame1, text='von')
        label71.grid(row=1, column=0, sticky='W')

        label72 = ttk.Label(frame1, text='bis')
        label72.grid(row=2, column=0, sticky='W')

        entry71 = tk.Entry(frame1, validate='all', validatecommand=self.check_numbers_only,width=2)
        entry71.grid(row=1, column=1)

        entry72 = tk.Entry(frame1, validate='all', validatecommand=self.check_numbers_only,width=2)
        entry72.grid(row=2, column=1)

        opt71 = tk.OptionMenu(frame1, self.gesund, *monate)
        opt71.grid(row=1, column=2, sticky='nsew')

        opt72 = tk.OptionMenu(frame1, self.gesund, *monate)
        opt72.grid(row=2, column=2, sticky='nsew')




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
        
        entry = ttk.Entry(frame_left, textvariable=self.max_tage,
                          validate='all', validatecommand=self.check_numbers_only)
        entry.grid(row=0, column=1)
        
        listbox = tk.Listbox(frame_left)
        listbox.grid(row=1, columnspan=2, sticky='nsew')
        
        def listbox_edit(*_):
            nonlocal listbox
            if self.max_tage.get() == '':
                n = 0
            else:
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

        zutaten_tf = CustomText(frame_right, width=30, height=20)
        zutaten_tf.tag_configure("accepted", foreground="darkgreen")
        zutaten_tf.tag_configure("critical", foreground="brown")
        zutaten_tf.grid(row=0, column=0, columnspan=4, sticky="NEWS")

        def parse_zutaten(event):
            print("\n"*50)  # clear screen
            woerter = {
                "einheiten": ["Gramm", "Kilogramm", "Priese", "gehäufter Teelöffel"],
                "zutaten": ["Salz", "Hackfleisch", "Tomate"],
                "zusatz": ["gestückelt"]
            }
            tf = event.widget
            for tag in tf.tag_names():  # delete previous tags
                tf.tag_remove(tag, "1.0", "end")
            line = 1
            count = tk.IntVar()
            while True:  # Iterate over Rows
                tf.mark_set("pointer", "{}.0".format(line))

                # parse number first, because it behaves differently
                index = tf.search("\d+(\.\d*)?", "pointer", "{}.end".format(line), count=count, regexp=True)
                if index == "":
                    print("amount is not set")
                else:
                    tf.mark_set("pointer", "{}+{}c".format(index, count.get()))
                    amount = float(tf.get(index, "pointer"))
                    print("amount is", str(amount))
                    tf.tag_add("accepted", index, "pointer")

                for part in woerter.keys():  # Iterate over Unit, Ingredient etc.
                    while True:  # Search for useful delimiter
                        comma = tf.search(",", "pointer", "{}.end".format(line))
                        if comma == "":
                            comma = "{}.end".format(line)
                            break
                        if tf.search("[[:alpha:]]*[[:>:]]", "pointer", comma, count=count, regexp=True) != "":
                            break
                        tf.mark_set("pointer", "{}+1c".format(comma))

                    initial = tf.index("pointer")
                    word = ""
                    while True:  # Iterate over multiple Words in Ingredient etc.
                        index = tf.search("[[:alpha:]]+[[:>:]]", "pointer", comma, count=count, regexp=True)
                        if index == "":  # if no matching words until comma, assume word to be meant
                            print(part, "is apparently", word)
                            tf.tag_add("critical", initial, "pointer")
                            break
                        tf.mark_set("pointer", "{}+{}c".format(index, count.get()))
                        word += tf.get(index, "pointer")
                        if word in woerter[part]:
                            print(part, "is", word)
                            tf.tag_add("accepted", initial, "pointer")
                            break
                        word += ' '
                line += 1
                if tf.index("{}.0".format(line)) == tf.index("end"):
                    break

        zutaten_tf.bind("<<TextModified>>", parse_zutaten)

        def add_zutat():
            nonlocal zutaten_tf

            if not self.menge.get() or not self.zutat:
                return
            if self.einheit.get() == DEFAULT:
                return
            if self.zutat.get() == DEFAULT:
                return

            if zutaten_tf.index("end-1c") != zutaten_tf.index("end-1l"):
                zutaten_tf.insert("end", "\n")
            zusatz_text = " , {}".format(self.zusatz.get()) if self.zusatz.get() else ""
            zutaten_tf.insert("end", "{} {} {}{}".format(self.menge.get(), self.einheit.get(),
                                                           self.zutat.get(), zusatz_text))

            self.menge.set("")
            self.einheit.set(DEFAULT)
            self.zutat.set(DEFAULT)
            self.zusatz.set("")

        DEFAULT = "Bitte auswählen"
        DEFAULT_SIZE = len(DEFAULT)

        menge_entry = ttk.Entry(frame_right, width=5, textvariable=self.menge, validate='all', validatecommand=self.check_numbers_only)
        menge_entry.grid(row=1, column=0)

        einheit_opt = tk.OptionMenu(frame_right, self.einheit, DEFAULT, *units)
        einheit_opt.config(width=DEFAULT_SIZE)
        einheit_opt.grid(row=1, column=1)
        self.einheit.set(DEFAULT)

        zutat_opt = tk.OptionMenu(frame_right, self.zutat, DEFAULT, *zutatenliste)
        zutat_opt.config(width=DEFAULT_SIZE)
        zutat_opt.grid(row=1, column=2)
        self.zutat.set(DEFAULT)

        zusatz_entry = ttk.Entry(frame_right, textvariable=self.zusatz)
        zusatz_entry.grid(row=1, column=3)

        add_zutat_button = tk.Button(frame_right, text="Hinzufügen", command=add_zutat)
        add_zutat_button.grid(row=2, column=0, columnspan=4, sticky="WE")

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
