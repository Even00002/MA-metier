import customtkinter as ctk
from Frontend.popups import ValidationPopup

class ValidationPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="white", corner_radius=0)
        self.controller = controller

        # --- Header ---
        top_bar = ctk.CTkFrame(self, fg_color="transparent")
        top_bar.pack(fill="x", padx=20, pady=20)

        ctk.CTkButton(top_bar, text="← Retour", fg_color="#019136",
                      width=100, command=controller.show_gestion).pack(side="left")
        ctk.CTkButton(top_bar, text="Quitter", fg_color="#019136",
                      width=100, command=controller.destroy).pack(side="right")

        ctk.CTkLabel(self, text="Publications et Modifications en attente",
                     font=("Arial", 16, "bold"), text_color="black").pack(anchor="w", padx=25)

        # --- Filtres ---
        filter_frame = ctk.CTkFrame(self, fg_color="transparent")
        filter_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkButton(filter_frame, text="Tout (5)", fg_color="#019136", width=80).pack(side="left", padx=5)
        ctk.CTkButton(filter_frame, text="Edits (2)", fg_color="white", text_color="black", border_width=1).pack(side="left", padx=5)
        ctk.CTkButton(filter_frame, text="Ajouts (3)", fg_color="white", text_color="black", border_width=1).pack(side="left", padx=5)

        # --- Liste ---
        self.scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.scroll.pack(fill="both", expand=True, padx=20, pady=10)

        data = [
            ("Titre de l'ajout / modification", "Username", "16.01.2026", "Ajout"),
            ("Titre de l'ajout / modification", "Username", "16.01.2026", "Edit")
        ]
        for d in data:
            self.add_item(d)

    def add_item(self, data):
        # Correction : suppression de 'global ValidationPage' qui causait le bug
        titre, user, date, type_v = data
        row = ctk.CTkButton(self.scroll, fg_color="#86c49c", text="", height=80, corner_radius=10,
                            command=lambda: ValidationPopup(self, data))
        row.pack(fill="x", pady=5)

        ctk.CTkLabel(row, text=titre, font=("Arial", 14, "bold")).place(x=20, y=15)
        ctk.CTkLabel(row, text=f"Par : {user}   {date}", font=("Arial", 11)).place(x=20, y=45)

        badge_color = "#019136" if type_v == "Ajout" else "#00b140"
        ctk.CTkLabel(row, text=type_v, fg_color=badge_color, corner_radius=5, width=50).place(relx=0.9, y=25)