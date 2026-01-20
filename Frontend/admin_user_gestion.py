import customtkinter as ctk

class admin_user_gestionApp(ctk.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.checkboxes = []

        for i, value in enumerate(self.values):
            checkbox = ctk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes



class scrollable_area(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("900x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        users = ["user 1 mail 1  13.06.2010   01.01.2025   User",
                 "user 2 mail 2  15.06.2010   01.01.2024   User",
                 "user 3 mail 3  13.06.2005   01.01.2020   Admin",
                 "user 4 mail 4  13.06.2000   01.01.2019   Admin",
                 "user 5 mail 5  13.06.2009   01.01.2024   User",
                 "user 6 mail 6  13.01.2010   01.01.2025   User"]

        self.scrollable_user = admin_user_gestionApp(self, title="Username   Email   Date de naissance   Role", values=users)
        self.scrollable_user.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")



        self.button = ctk.CTkButton(self, text="Bannir", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

    def button_callback(self):
        print("checkbox_frame:", self.checkbox_frame.get())
        print("radiobutton_frame:", self.radiobutton_frame.get())

app = scrollable_area()
app.mainloop()