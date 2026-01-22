"""
Nom du fichier : admin_user_gestion.py
Auteur : Furkan Yilmaz
Date de création : 21.01.2026
"""

import customtkinter as ctk
from PIL import Image
import os
from Frontend.popups import ActionPopup, HistoryPopup

ctk.set_appearance_mode("light")

class AdminDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CPNV HUB - Gestion Admin")
        self.geometry("1100x700+400+150")

        # === CONFIGURATION GRILLE PRINCIPALE ===
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ========== SIDEBAR (GAUCHE) ===========
        self.sidebar = ctk.CTkFrame(self, fg_color="#1E5235", corner_radius=0, width=250)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)

        # Logo
        self.logo = ctk.CTkFrame(self.sidebar, fg_color="#C89F65", height=120, corner_radius=5, border_width=2, border_color="#5C4033")
        self.logo.pack(fill="x", padx=10, pady=20)

        try:
            logo_img = ctk.CTkImage(Image.open("assets/logo.png"), size=(80, 70))
            ctk.CTkLabel(self.logo, image=logo_img, text="").place(relx=0.5, rely=0.5, anchor="center")
        except:
            ctk.CTkLabel(self.logo, text="LOGO", text_color="black").place(relx=0.5, rely=0.5, anchor="center")

        # Boutons Sidebar
        self.btn_gestion = ctk.CTkButton(self.sidebar, text="Gestion des utilisateurs", fg_color="#3fa863", hover_color="#2d7a47", height=40)
        self.btn_gestion.pack(padx=10, pady=10, fill="x")

        self.btn_validation = ctk.CTkButton(self.sidebar, text="Validation", fg_color="#2d7a47", hover_color="#1E5235", height=40)
        self.btn_validation.pack(padx=10, pady=5, fill="x")

        #========= CONTENU (DROITE) ===========
        self.main_area = ctk.CTkFrame(self, fg_color="white", corner_radius=0)
        self.main_area.grid(row=0, column=1, sticky="nsew")

        # Header
        self.top_bar = ctk.CTkFrame(self.main_area, fg_color="transparent")
        self.top_bar.pack(fill="x", padx=20, pady=20)
        ctk.CTkButton(self.top_bar, text="← Retour", fg_color="#019136", width=100).pack(side="left")
        ctk.CTkButton(self.top_bar, text="Quitter", fg_color="#019136", width=100, command=self.destroy).pack(side="right")

        # Recherche
        self.search_bar = ctk.CTkEntry(self.main_area, placeholder_text="Rechercher...", height=40, fg_color="#86c49c", border_width=0, text_color="white", placeholder_text_color="#eeeeee")
        self.search_bar.pack(fill="x", padx=20, pady=(0, 20))

        #=========== TABLEAU =============
        self.header_frame = ctk.CTkFrame(self.main_area, fg_color="#019136", corner_radius=5, height=50)
        self.header_frame.pack(fill="x", padx=20, pady=5)

        self.columns_config = [("Username", 1), ("Email", 2), ("Date de naissance", 1), ("Création compte", 1), ("Role", 0.5), ("Actions", 2.5)]

        for i, (col_name, weight) in enumerate(self.columns_config):
            self.header_frame.grid_columnconfigure(i, weight=int(weight * 10))
            ctk.CTkLabel(self.header_frame, text=col_name, text_color="white", font=("Arial", 13, "bold")).grid(row=0, column=i, pady=10)

        self.scroll_frame = ctk.CTkScrollableFrame(self.main_area, fg_color="transparent")
        self.scroll_frame.pack(fill="both", expand=True, padx=20, pady=5)

        # Données
        users_data = [
            ("JoelFaria", "joel@cpnv.ch", "12.10.2002", "15.01.2024", "user", 1),
            ("AdminMaster", "admin@cpnv.ch", "01.01.1990", "10.01.2024", "admin", 0),
            ("Newbie23", "test@gmail.com", "22.05.2005", "16.01.2026", "user", 3),
            ("BadUser", "bad@banned.com", "09.09.1999", "12.12.2025", "user", 2)
        ]

        for user in users_data:
            self.add_user_row(user)

    def add_user_row(self, user_data):
        username, email, dob, created, role, warns = user_data

        # État spécifique à cette ligne
        state = {"ban": 0, "mute": 0}

        row = ctk.CTkFrame(self.scroll_frame, fg_color="#86c49c", corner_radius=5)
        row.pack(fill="x", pady=5)

        for i, (_, weight) in enumerate(self.columns_config):
            row.grid_columnconfigure(i, weight=int(weight * 10))

        text_style = {"text_color": "white", "font": ("Arial", 12)}
        ctk.CTkLabel(row, text=username, **text_style).grid(row=0, column=0, pady=10)
        ctk.CTkLabel(row, text=email, **text_style).grid(row=0, column=1, pady=10)
        ctk.CTkLabel(row, text=dob, **text_style).grid(row=0, column=2, pady=10)
        ctk.CTkLabel(row, text=created, **text_style).grid(row=0, column=3, pady=10)
        ctk.CTkLabel(row, text=role, **text_style).grid(row=0, column=4, pady=10)

        actions_frame = ctk.CTkFrame(row, fg_color="transparent")
        actions_frame.grid(row=0, column=5, pady=5, padx=5)

        btn_ban = ctk.CTkButton(actions_frame, width=60)
        btn_ban.pack(side="left", padx=2)

        btn_mute = ctk.CTkButton(actions_frame, width=60)
        btn_mute.pack(side="left", padx=2)

        def refresh_buttons():
            # Logique Ban (Vert si non-banni, Rouge si banni)
            if state["ban"] == 1:
                btn_ban.configure(text="Unban", fg_color="#A20909", hover_color="#8b0808",
                                  command=lambda: ActionPopup(self, "Unban", username, state, "ban", refresh_buttons))
            else:
                btn_ban.configure(text="Ban", fg_color="#019136", hover_color="#017a2d",
                                  command=lambda: ActionPopup(self, "Ban", username, state, "ban", refresh_buttons))

            # Logique Mute (Vert si non-muté, Rouge si muté)
            if state["mute"] == 1:
                btn_mute.configure(text="Unmute", fg_color="#A20909", hover_color="#8b0808",
                                   command=lambda: ActionPopup(self, "Unmute", username, state, "mute", refresh_buttons))
            else:
                btn_mute.configure(text="Mute", fg_color="#019136", hover_color="#017a2d",
                                   command=lambda: ActionPopup(self, "Mute", username, state, "mute", refresh_buttons))

        refresh_buttons()

        ctk.CTkButton(actions_frame, text=f"Voir l'historique ({warns})", fg_color="#019136", width=120,
                     command=lambda: HistoryPopup(self, username, [])).pack(side="left", padx=2)

if __name__ == "__main__":
    app = AdminDashboard()
    app.mainloop()