import customtkinter as ctk
from Frontend.popups import ValidationPopup


class ValidationPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="white", corner_radius=0)
        self.controller = controller

        self.all_data = [
            ("Titre de l'ajout / modification", "Username", "16.01.2026", "Ajout"),
            ("Titre de l'ajout / modification", "Username", "16.01.2026", "Edit"),
            ("Nouvelle ressource", "Admin", "17.01.2026", "Ajout"),
            ("Correction texte", "User2", "18.01.2026", "Edit"),
            ("Document PDF", "Furkan", "21.01.2026", "Ajout")
        ]

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

        self.btn_all = ctk.CTkButton(filter_frame, text="Tout", width=80, command=lambda: self.filter_items("Tout"))
        self.btn_all.pack(side="left", padx=5)

        self.btn_edits = ctk.CTkButton(filter_frame, text="Edits", width=80, command=lambda: self.filter_items("Edit"))
        self.btn_edits.pack(side="left", padx=5)

        self.btn_ajouts = ctk.CTkButton(filter_frame, text="Ajouts", width=80,
                                        command=lambda: self.filter_items("Ajout"))
        self.btn_ajouts.pack(side="left", padx=5)

        # --- Liste ---
        self.scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.scroll.pack(fill="both", expand=True, padx=20, pady=10)

        self.filter_items("Tout")

    def filter_items(self, filter_type):
        for widget in self.scroll.winfo_children():
            widget.destroy()

        for d in self.all_data:
            if filter_type == "Tout" or d[3] == filter_type:
                self.add_item(d)

    def add_item(self, data):
        titre, user, date, type_v = data

        # Container principal (on utilise une Frame pour mieux gérer l'espace que sur un bouton direct)
        item_frame = ctk.CTkFrame(self.scroll, fg_color="#86c49c", height=85, corner_radius=10)
        item_frame.pack(fill="x", pady=5, padx=5)
        item_frame.pack_propagate(False)  # Garde la hauteur fixe

        # Rendre toute la frame cliquable en mettant un bouton invisible par-dessus ou en bindant
        item_frame.bind("<Button-1>", lambda e: ValidationPopup(self, data))

        # --- Côté Gauche (Infos) ---
        info_frame = ctk.CTkFrame(item_frame, fg_color="transparent")
        info_frame.pack(side="left", fill="y", padx=20, pady=10)

        lbl_titre = ctk.CTkLabel(info_frame, text=titre, font=("Arial", 14, "bold"), text_color="black")
        lbl_titre.pack(anchor="w")

        lbl_sub = ctk.CTkLabel(info_frame, text=f"Par : {user}   {date}", font=("Arial", 11), text_color="#333333")
        lbl_sub.pack(anchor="w")

        # --- Côté Droit (Badge) ---
        badge_color = "#019136" if type_v == "Ajout" else "#00b140"
        badge_container = ctk.CTkFrame(item_frame, fg_color="transparent")
        badge_container.pack(side="right", fill="y", padx=20)

        badge = ctk.CTkLabel(badge_container, text=type_v, fg_color=badge_color,
                             corner_radius=5, width=60, text_color="white", font=("Arial", 11, "bold"))
        badge.pack(expand=True)

        # On s'assure que les labels aussi ouvrent la popup si on clique dessus
        for w in [lbl_titre, lbl_sub, badge]:
            w.bind("<Button-1>", lambda e: ValidationPopup(self, data))