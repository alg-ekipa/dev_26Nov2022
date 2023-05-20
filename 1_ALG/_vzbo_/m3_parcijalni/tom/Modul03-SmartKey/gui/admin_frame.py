import tkinter as tk

from data import get_tenants, create_update_tenant, delete_tenant
from data.tenant import Tenant


class AdminFrame(tk.Frame):
    def __init__(self, container, tenants):
        super().__init__(container)

        self.columnconfigure(0, weight=6)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)

        self.PIN = ''
        self.tenants = tenants
        self.selected_tenant = None

        options = {'padx': 5, 'pady': 5}

        #region WIDGETS
        self.label = tk.Label(self, text='ADMIN Panel!')
        self.label.grid(**options, sticky=tk.N, row=0, column=0, columnspan=2)

        self.lb_tenants = tk.Listbox(self, listvariable=self.tenants)
        for i, tenant in enumerate(self.tenants):
            self.lb_tenants.insert(i, f'{tenant.first_name} {tenant.last_name}')
        self.lb_tenants.grid(**options, sticky=tk.W, row=1, column=0, columnspan=2, rowspan=5)
        self.lb_tenants.bind("<<ListboxSelect>>", self.set_selected_tenant)


        # FORM
        # FIRST NAME
        self.lbl_first_name = tk.Label(self, text='Ime')
        self.lbl_first_name.grid(**options, sticky=tk.E, row=1, column=2)

        self.entry_first_name_var = tk.StringVar()
        self.entry_first_name = tk.Entry(self, textvariable=self.entry_first_name_var)
        self.entry_first_name.grid(**options, sticky=tk.W, row=1, column=3, columnspan=2)
        if self.selected_tenant is not None:
            self.entry_first_name_var.set(self.selected_tenant.first_name)
        else:
            self.entry_first_name_var.set('')

        # LAST NAME
        self.lbl_last_name = tk.Label(self, text='Prezime')
        self.lbl_last_name.grid(**options, sticky=tk.E, row=2, column=2)

        self.entry_last_name_var = tk.StringVar()
        self.entry_last_name = tk.Entry(self, textvariable=self.entry_last_name_var)
        self.entry_last_name.grid(**options, sticky=tk.W, row=2, column=3, columnspan=2)
        if self.selected_tenant is not None:
            self.entry_last_name_var.set(self.selected_tenant.last_name)
        else:
            self.entry_last_name_var.set('')


        # PIN
        self.lbl_pin = tk.Label(self, text='PIN')
        self.lbl_pin.grid(**options, sticky=tk.E, row=3, column=2)

        self.entry_pin_var = tk.StringVar()
        self.entry_pin = tk.Entry(self, textvariable=self.entry_pin_var)
        self.entry_pin.grid(**options, sticky=tk.W, row=3, column=3, columnspan=2)
        if self.selected_tenant is not None:
            self.entry_pin_var.set(self.selected_tenant.pin)
        else:
            self.entry_pin_var.set('')


        # IS ACTIVE
        self.lbl_is_active = tk.Label(self, text='Aktivan?')
        self.lbl_is_active.grid(**options, sticky=tk.E, row=4, column=2)

        self.entry_is_active_var = tk.BooleanVar()
        self.entry_is_active = tk.Checkbutton(self, variable=self.entry_is_active_var)
        self.entry_is_active.grid(**options, sticky=tk.W, row=4, column=3, columnspan=2)
        if self.selected_tenant is not None:
            self.entry_is_active_var.set(bool(self.selected_tenant.is_active))
        else:
            self.entry_is_active_var.set(value=False)


        # BUTTONS
        self.btn_save = tk.Button(self, text='Spremi', bg='#5cb85c', command=self.create_tenant_command)
        self.btn_save.grid(**options, sticky=tk.NSEW, row=5, column=2)

        self.btn_cancel = tk.Button(self, text='Odusatni', bg='#5bc0de', command=self.clear_selected_tenant_command)
        self.btn_cancel.grid(**options, sticky=tk.NSEW, row=5, column=3)

        self.btn_delete = tk.Button(self, text='Izbrisi', bg='#d9534f', command=self.delete_tenant_command)
        self.btn_delete.grid(**options, sticky=tk.NSEW, row=5, column=4)

        #endregion


    def set_selected_tenant(self, event):
        self.tenants = get_tenants()
        tenant = self.tenants[self.lb_tenants.curselection()[0]]
        self.entry_first_name_var.set(tenant.first_name)
        self.entry_last_name_var.set(tenant.last_name)
        self.entry_pin_var.set(tenant.pin)
        self.entry_is_active_var.set(bool(tenant.is_active))
        
   
    def create_tenant_command(self):
        tenant = Tenant(
            first_name = self.entry_first_name_var.get(),
            last_name = self.entry_last_name_var.get(),
            pin = self.entry_pin_var.get(),
            is_active = self.entry_is_active_var.get())

        create_update_tenant(tenant)
        self.tenants = get_tenants()

        self.lb_tenants.delete(0, tk.END)
        for i, tenant in enumerate(self.tenants):
            self.lb_tenants.insert(i, f'{tenant.first_name} {tenant.last_name}')


    def clear_selected_tenant_command(self):
        self.entry_first_name_var.set('')
        self.entry_last_name_var.set('')
        self.entry_pin_var.set('')
        self.entry_is_active_var.set(value=False)
        self.lb_tenants.selection_clear(0, tk.END)


    def delete_tenant_command(self):
        tenant = Tenant(
            first_name = self.entry_first_name_var.get(),
            last_name = self.entry_last_name_var.get(),
            pin = self.entry_pin_var.get(),
            is_active = self.entry_is_active_var.get())

        delete_tenant(tenant)
        self.tenants = get_tenants()

        self.lb_tenants.delete(0, tk.END)
        for i, tenant in enumerate(self.tenants):
            self.lb_tenants.insert(i, f'{tenant.first_name} {tenant.last_name}')

        self.clear_selected_tenant_command()
