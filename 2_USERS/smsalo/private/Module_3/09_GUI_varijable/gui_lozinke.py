from tkinter import *
import random as rd

root=Tk()
root.title('Generiranje lozinke')

#definiranje varijabli koje se koriste

lozinka_var = StringVar()   #lozinka koja se ispisuje
slova_var = BooleanVar()    #varijable koje predstavljaju checkbox (označeno ili ne)
broj_var = BooleanVar()
znak_var = BooleanVar()

prikazi_lozinku = StringVar()   #varijabla koja govori prikaži ili ne 
prikazi_lozinku.set('prikazi')

duljina_lozinke=IntVar()        #cijeli broj koji pokazuje koliko lozinka ima znakova

#Funkcije koje koristimo

def set_duljina_lozinke(value):
    duljina_lozinke.set(int(value))

def generiraj_lozinku():
    lozinka=''
    broj_znakova = duljina_lozinke.get()

    for i in range(broj_znakova):
        if slova_var.get():
            a=rd.choice([(65,90), (97,122)])
        elif broj_var.get():
            a=rd.choice([(48,57)])
        elif znak_var.get():
            a=rd.choice([(33,47), (58,64), (91,96)])
        else:
            a = rd.choice([(33,122)])

        broj=rd.randint(*a)
        znak = chr(broj)
        lozinka+=znak
    lozinka_var.set(str(lozinka))

def kopiraj_lozinku():
    root.clipboard_clear()
    root.clipboard_append(lozinka_var.get())

def resetiraj_lozinku():
    lozinka_var.set('')

def set_prikaz_lozinke():
    if prikazi_lozinku.get() == 'prikazi':
        ent_lozinka.config(show='')
    else:
        ent_lozinka.config(show='*')


#prikaz na GUI

frame_postavke=Frame(root)
frame_postavke.grid(row=0, column=0,rowspan=3,columnspan=3)

label_frame_postavke=LabelFrame(frame_postavke, text='Postavke')
label_frame_postavke.columnconfigure((0,1,2), weight=1, minsize=90)
label_frame_postavke.grid(row=0, column=0,columnspan=3, padx=30,pady=30,ipadx=20,ipady=10)

ch_box_slova = Checkbutton(label_frame_postavke, text='Samo slova', variable=slova_var)   #TO DO dodati varijablu!  - naknadno dodano, nakon definiranja
ch_box_slova.grid(row=0, column=0)

ch_box_broj=Checkbutton(label_frame_postavke, text='Samo brojevi', variable=broj_var)
ch_box_broj.grid(row=0, column=1)

ch_box_znak=Checkbutton(label_frame_postavke, text='Samo znakovi', variable=znak_var)
ch_box_znak.grid(row=0, column=2)

rb_prikazi=Radiobutton(label_frame_postavke, text='Prikazi generiranu lozinku', variable=prikazi_lozinku, command=set_prikaz_lozinke, value='prikazi' )     #to do command, varijabla, value
rb_prikazi.grid(row=1, column=0)

rb_sakri=Radiobutton(label_frame_postavke, text='Sakrij generiranu lozinku', variable=prikazi_lozinku, command=set_prikaz_lozinke, value='sakrij')     #to do command, varijabla
rb_sakri.grid(row=1, column=2)

scl_duljina = Scale(label_frame_postavke, orient='horizontal', length=350, from_=8, to=40, variable=duljina_lozinke, command=set_duljina_lozinke)      #definiranje duljine slidera te vrijednosti koje može poprimiti
scl_duljina.grid(row=2, column=0, columnspan=3)

#frame odabir
frame_gumbi=Frame(root)
frame_gumbi.grid(row=3,column=0, columnspan=3, padx=10, pady=10, ipadx=20, ipady=20)

#gumbi generiraj, kopiraj, resetiraj
btn_generiraj = Button(frame_gumbi, text='Generiraj lozinku', command=generiraj_lozinku)           #command
btn_kopiraj = Button(frame_gumbi, text='Kopiraj lozinku', command=kopiraj_lozinku)
btn_resetiraj=Button(frame_gumbi, text='Resetiraj lozinku', command=resetiraj_lozinku)

btn_generiraj.grid(row=3, column=0, padx=30)
btn_kopiraj.grid(row=3, column=1, padx=30)
btn_resetiraj.grid(row=3, column=2, padx=30)

#frame prikaži lozinku
frm_display=Frame(root)
frm_display.grid(row=4, column=0, columnspan=3, rowspan=2, padx=10, pady=10, ipadx=20, ipady=20)

lbl_display = Label(frm_display, text='Generirana lozinka', font=('Verdana', 12))
lbl_display.grid(row=4, column=0, columnspan=3, ipadx=15)

ent_lozinka=Entry(frm_display, justify='center', font=('Verdana', 12), background='systembuttonface', bd=0, width=50 ,textvariable=lozinka_var)   #systembuttonface za skrivanje prozora, okvir bd=0
ent_lozinka.grid(row=5, column=0, columnspan=3, ipadx=15, ipady=10, padx=15, pady=10)


root.mainloop()