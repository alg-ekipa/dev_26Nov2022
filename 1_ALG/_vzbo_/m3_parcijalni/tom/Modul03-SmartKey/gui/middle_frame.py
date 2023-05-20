import tkinter as tk

from gui.admin_frame import AdminFrame
from data import get_tenants


class MiddleFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=6)

        self.PIN = ''
        self.tenants = []
        self.get_all_tenants()

        options = {'padx': 5, 'pady': 5}


        #region LABELS
        self.label = tk.Label(self, text='PIN panel!')
        self.label.grid(**options, sticky=tk.N, row=0, column=0, columnspan=5)

        self.lbl_pin_1_var = tk.StringVar(value='_')
        self.lbl_pin_1 = tk.Label(self, textvariable=self.lbl_pin_1_var)
        self.lbl_pin_1.grid(**options, sticky=tk.NSEW, row=1, column=0)

        self.lbl_pin_2_var = tk.StringVar(value='_')
        self.lbl_pin_2 = tk.Label(self, textvariable=self.lbl_pin_2_var)
        self.lbl_pin_2.grid(**options, sticky=tk.NSEW, row=1, column=1)

        self.lbl_pin_3_var = tk.StringVar(value='_')
        self.lbl_pin_3 = tk.Label(self, textvariable=self.lbl_pin_3_var)
        self.lbl_pin_3.grid(**options, sticky=tk.NSEW, row=1, column=2)

        self.lbl_pin_4_var = tk.StringVar(value='_')
        self.lbl_pin_4 = tk.Label(self, textvariable=self.lbl_pin_4_var)
        self.lbl_pin_4.grid(**options, sticky=tk.NSEW, row=1, column=3)


        self.lbl_txt_message_var = tk.StringVar()
        self.lbl_txt_message_var.set('Status i poruke\n')
        self.lbl_txt_message = tk.Label(self, textvariable=self.lbl_txt_message_var, font=('Segoe UI', '20', 'bold'))
        self.lbl_txt_message.grid(**options, sticky=tk.N, row=1, column=4, rowspan=5)
        
        #endregion
        

        #region BUTTONS
        self.btn_1 = tk.Button(self, text='1', command=lambda n='1': self.show_number(n))
        self.btn_1.grid(**options, sticky=tk.NSEW, row=2, column=0)

        self.btn_2 = tk.Button(self, text='2', command=lambda n='2': self.show_number(n))
        self.btn_2.grid(**options, sticky=tk.NSEW, row=2, column=1)

        self.btn_3 = tk.Button(self, text='3', command=lambda n='3': self.show_number(n))
        self.btn_3.grid(**options, sticky=tk.NSEW, row=2, column=2)

        self.btn_4 = tk.Button(self, text='4', command=lambda n='4': self.show_number(n))
        self.btn_4.grid(**options, sticky=tk.NSEW, row=3, column=0)

        self.btn_5 = tk.Button(self, text='5', command=lambda n='5': self.show_number(n))
        self.btn_5.grid(**options, sticky=tk.NSEW, row=3, column=1)

        self.btn_6 = tk.Button(self, text='6', command=lambda n='6': self.show_number(n))
        self.btn_6.grid(**options, sticky=tk.NSEW, row=3, column=2)

        self.btn_7 = tk.Button(self, text='7', command=lambda n='7': self.show_number(n))
        self.btn_7.grid(**options, sticky=tk.NSEW, row=4, column=0)

        self.btn_8 = tk.Button(self, text='8', command=lambda n='8': self.show_number(n))
        self.btn_8.grid(**options, sticky=tk.NSEW, row=4, column=1)

        self.btn_9 = tk.Button(self, text='9', command=lambda n='9': self.show_number(n))
        self.btn_9.grid(**options, sticky=tk.NSEW, row=4, column=2)

        self.btn_0 = tk.Button(self, text='0', command=lambda n='0': self.show_number(n))
        self.btn_0.grid(**options, sticky=tk.NSEW, row=5, column=1)

        self.btn_ok = tk.Button(self, text='OK', command=self.check_pin, bg='#5bc0de', fg='#fff')
        self.btn_ok.grid(**options, sticky=tk.NSEW, row=5, column=0)
        
        self.btn_c = tk.Button(self, text='C', command=self.cancel_number, bg='#d9534f', fg='#fff')
        self.btn_c.grid(**options, sticky=tk.NSEW, row=5, column=2)

        #endregion


        self.admin_frame_active = AdminFrame(self, self.tenants)
        self.admin_frame_active.grid(**options, sticky=tk.NSEW, row=6, column=0, columnspan=5)

        self.admin_frame_blank = tk.Frame(self)
        self.admin_frame_blank.grid(**options, sticky=tk.NSEW, row=6, column=0, columnspan=5)



    def show_number(self, number):
        if self.lbl_pin_1_var.get() == '_':
            self.lbl_pin_1_var.set(number)
            if len(self.PIN) <= 4:
                self.PIN += number
        elif self.lbl_pin_2_var.get() == '_':
            self.lbl_pin_2_var.set(number)
            if len(self.PIN) <= 4:
                self.PIN += number
        elif self.lbl_pin_3_var.get() == '_':
            self.lbl_pin_3_var.set(number)
            if len(self.PIN) <= 4:
                self.PIN += number
        elif self.lbl_pin_4_var.get() == '_':
            self.lbl_pin_4_var.set(number)
            if len(self.PIN) <= 4:
                self.PIN += number


    def cancel_number(self):
        if self.lbl_pin_4_var.get() != '_':
            self.lbl_pin_4_var.set('_')
            self.lbl_txt_message_var.set('Status i poruke\n')
            self.PIN = self.PIN[ : -1]
            self.deactivate_admin_frame()
        elif self.lbl_pin_3_var.get() != '_':
            self.lbl_pin_3_var.set('_')
            self.lbl_txt_message_var.set('Status i poruke\n')
            self.PIN = self.PIN[ : -1]
            self.deactivate_admin_frame()
        elif self.lbl_pin_2_var.get() != '_':
            self.lbl_pin_2_var.set('_')
            self.lbl_txt_message_var.set('Status i poruke\n')
            self.PIN = self.PIN[ : -1]
            self.deactivate_admin_frame()
        elif self.lbl_pin_1_var.get() != '_':
            self.lbl_pin_1_var.set('_')
            self.lbl_txt_message_var.set('Status i poruke\n')
            self.PIN = self.PIN[ : -1]
            self.deactivate_admin_frame()
        else:
            self.deactivate_admin_frame()
            return


    def check_pin(self):
        for tenant in self.tenants:
            tenant = tenant
            if self.PIN == tenant.pin:
                self.lbl_txt_message_var.set(f'\nDobro dosli\n{tenant.first_name} {tenant.last_name}!\n')
                self.activate_admin_frame()
                return 
            else:
                self.lbl_txt_message_var.set('\nPogresan PIN!\n')


    def activate_admin_frame(self):
        self.admin_frame_active.tkraise()


    def get_all_tenants(self):
        self.tenants = get_tenants()      
