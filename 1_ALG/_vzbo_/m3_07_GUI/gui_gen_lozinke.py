import tkinter as tk
import random as rd

root = tk.Tk()
root.title('Password generator')

# Definiranje varijabli koje se koriste

lozika_var = tk.StringVar()  # generirana lozinka koja se na kraju ispisuje

slova_var = tk.BooleanVar()       # varijable koje predstavljaju checkbox (označeno ili ne)
brojevi_var = tk.BooleanVar()
znakovi_var = tk.BooleanVar()

prikazi_lozinku = tk.StringVar()    # varijabla koja govori prikaži ili ne prikaži lozinku
prikazi_lozinku.set('prikazi')

duljina_lozinke = tk.IntVar()       # cijeli broj koji govori koliko lozinka ima znakova

# Funkcije

def set_duljina_lozinke(value):         # Postavljanje duljine lozinke
    duljina_lozinke.set(int(value))

def generiraj_lozinku():

    lozinka = ''
    broj_znakova = duljina_lozinke.get()

    for znak in range(broj_znakova):
        # odabir 1: slova
        if slova_var.get():
            a = rd.choice([(65,90),(97,122)])
        # odabir 2: brojevi
        elif brojevi_var.get():
            a = rd.choice([(48,57)])
        # odabir 3: znakovi
        elif znakovi_var.get():
            a = rd.choice([(33,47),(58,64),(91,96)])
        else:
            a = rd.choice([(33,122)])
        
        broj = rd.randint(*a)
        znak = chr(broj)
        lozinka += znak
    lozika_var.set(str(lozinka))

def kopiraj_lozinku():
    root.clipboard_clear()
    root.clipboard_append(lozika_var.get())

def resetiraj_lozinku():
    lozika_var.set('')

def set_prikaz_lozinke():
    if prikazi_lozinku.get() == 'prikazi':
        ent_lozinka.config(show='')
    else:
        ent_lozinka.config(show='*')

# Prikaz na GUI

# Frame POSTAVKE
frm_postavke = tk.Frame(root)
frm_postavke.grid(row=0, column=0, rowspan=3, columnspan=3)

lbl_frm_postavke = tk.LabelFrame(frm_postavke, text='Postavke')
lbl_frm_postavke.columnconfigure((0,1,2), weight=1, minsize=90)
lbl_frm_postavke.grid(row=0, column=0,columnspan=3, padx=30, pady=30, ipadx=20, ipady=10)

ch_box_slova = tk.Checkbutton(lbl_frm_postavke, text='Samo slova',variable=slova_var)   
ch_box_slova.grid(row=0, column=0)

ch_box_brojevi = tk.Checkbutton(lbl_frm_postavke, text='Samo brojevi',variable=brojevi_var) 
ch_box_brojevi.grid(row=0, column=1)

ch_box_znakovi = tk.Checkbutton(lbl_frm_postavke, text='Samo znakovi',variable=znakovi_var)  
ch_box_znakovi.grid(row=0, column=2)

rb_prikazi_lozinku = tk.Radiobutton(lbl_frm_postavke, text='Prikazi generiranu lozinku', variable=prikazi_lozinku, command=set_prikaz_lozinke, value='prikazi') 
rb_prikazi_lozinku.grid(row=1, column=0)

rb_sakrij_lozinku = tk.Radiobutton(lbl_frm_postavke, text='Sakrij generiranu lozinku', variable=prikazi_lozinku, command=set_prikaz_lozinke, value='sakrij') 
rb_sakrij_lozinku.grid(row=1, column=2)

scl_duljina = tk.Scale(lbl_frm_postavke, orient='horizontal', length=300, from_=8, to=40, variable=duljina_lozinke, command=set_duljina_lozinke)  
scl_duljina.grid(row=2, column=0, columnspan=3)

# Frame ACTION BUTTONS

frm_action_buttons = tk.Frame(root)
frm_action_buttons.grid(row=3, column=0, columnspan=3, padx=10, pady=10, ipadx=20, ipady=20)

# gumbi: generiraj, kopiraj, resetiraj
btn_generiraj = tk.Button(frm_action_buttons, text='Generiraj lozinku', command=generiraj_lozinku)        
btn_generiraj.grid(row=3, column=0, padx=10)

btn_kopiraj = tk.Button(frm_action_buttons, text='Kopiraj lozinku', command=kopiraj_lozinku)         
btn_kopiraj.grid(row=3, column=1, padx=10)

btn_resetiraj = tk.Button(frm_action_buttons, text='Resetiraj lozinku', command=resetiraj_lozinku)         
btn_resetiraj.grid(row=3, column=2, padx=10)

# Frame DISPLAY GENERATED PSSWD

frm_display_password = tk.Frame(root)
frm_display_password.grid(row=4, column=0, columnspan=3, rowspan=2, padx=10, pady=10, ipadx=20, ipady=20)

lbl_password = tk.Label(frm_display_password, text='Generirana lozinka', font=('Segoe UI', 14))
lbl_password.grid(row=4, column=0, columnspan=3, ipadx=15)

ent_lozinka = tk.Entry(frm_display_password, justify='center', font=('Segoe UI', 14), background='systembuttonface', bd=0, width = 40, textvariable=lozika_var)  # varijabla!!
ent_lozinka.grid(row=5, column=0, columnspan=3, ipadx=15, ipady=10, padx=15, pady=10)




root.mainloop()