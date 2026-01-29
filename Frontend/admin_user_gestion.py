"""
Nom du fichier : admin_user_gestion.py
Auteur : Furkan Yilmaz
Date de création : 21.01.2026
Dernier changement : 28.01.2026
"""

import customtkinter as ctk
from PIL import Image
import os
from Frontend.admin_validation import ValidationPage
from Frontend.popups import ActionPopup, HistoryPopup
from Backend.DB.db_schema import get_session
from Backend.Class.Class_User import User
from Backend.Services.user_service import set_user_ban

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
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
        # Couleur de la sidebar : #1E5235
        self.sidebar = ctk.CTkFrame(self, fg_color="#1E5235", corner_radius=0, width=250)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)

        # Logo - Correction pour enlever le cadre marron
        # On met le fg_color identique à la sidebar (#1E5235) pour qu'il soit invisible
        self.logo_container = ctk.CTkFrame(self.sidebar, fg_color="#1E5235", height=100, corner_radius=0)
        self.logo_container.pack(fill="x", padx=10, pady=(20, 10))

        try:
            logo_path = os.path.join(ASSETS_DIR, "Logo.jpg")
            img = Image.open(logo_path)
            # On ajuste la taille pour qu'il ne soit pas trop écrasé
            self.logo_image = ctk.CTkImage(light_image=img, dark_image=img, size=(160, 80))

            self.logo_label = ctk.CTkLabel(self.logo_container, image=self.logo_image, text="")
            self.logo_label.pack(expand=True)
        except Exception as e:
            print(f"Erreur logo: {e}")
            ctk.CTkLabel(self.logo_container, text="CPNV HUB", text_color="white", font=("Arial", 16, "bold")).pack(expand=True)

        # Boutons Sidebar
        self.btn_gestion = ctk.CTkButton(self.sidebar, text="Gestion des utilisateurs", fg_color="#3fa863", hover_color="#2d7a47", height=40, command=self.show_gestion)
        self.btn_gestion.pack(padx=10, pady=10, fill="x")

        self.btn_validation = ctk.CTkButton(self.sidebar, text="Validation", fg_color="#2d7a47", hover_color="#1E5235", height=40, command=self.open_validation_page)
        self.btn_validation.pack(padx=10, pady=5, fill="x")

        #========= CONTENEUR DE PAGES (DROITE) ===========
        self.container = ctk.CTkFrame(self, fg_color="white", corner_radius=0)
        self.container.grid(row=0, column=1, sticky="nsew")

        # Initialisation des vues
        self.main_area = self.create_main_area()
        self.validation_view = ValidationPage(self.container, self)

        # Affichage par défaut
        self.show_gestion()

    def load_users_from_db(self):

        session = get_session()
        users = session.query(User).filter(User.role != "admin").all()

        session.close()

        users_data = []
        for user in users:
            users_data.append((
                user.username,
                user.email,
                user.birthdate.strftime("%d.%m.%Y"),
                user.role,
                0
            ))

        return users_data

    def create_main_area(self):
        frame = ctk.CTkFrame(self.container, fg_color="white", corner_radius=0)

        # Header
        top_bar = ctk.CTkFrame(frame, fg_color="transparent")
        top_bar.pack(fill="x", padx=20, pady=20)
        ctk.CTkButton(top_bar, text="← Retour", fg_color="#019136", width=100, command=self.retourchoixdomaine).pack(side="left")
        ctk.CTkButton(top_bar, text="Quitter", fg_color="#019136", width=100, command=self.destroy).pack(side="right")

        # Recherche
        self.search_bar = ctk.CTkEntry(frame, placeholder_text="Rechercher...", height=40, fg_color="#86c49c", border_width=0, text_color="white", placeholder_text_color="#eeeeee")
        self.search_bar.pack(fill="x", padx=20, pady=(0, 20))

        #=========== TABLEAU =============
        header_frame = ctk.CTkFrame(frame, fg_color="#019136", corner_radius=5, height=50)
        header_frame.pack(fill="x", padx=20, pady=5)

        self.columns_config = [("Username", 1), ("Email", 2), ("Date de naissance", 1), ("Role", 0.5), ("Actions", 2.5)]

        for i, (col_name, weight) in enumerate(self.columns_config):
            header_frame.grid_columnconfigure(i, weight=int(weight * 10))
            ctk.CTkLabel(header_frame, text=col_name, text_color="white", font=("Arial", 13, "bold")).grid(row=0, column=i, pady=10)

        self.scroll_frame = ctk.CTkScrollableFrame(frame, fg_color="transparent")
        self.scroll_frame.pack(fill="both", expand=True, padx=20, pady=5)

        # Données fictives
        users_data = self.load_users_from_db()

        for user in users_data:
            self.add_user_row(user)
        return frame

    def retourchoixdomaine(self):
        self.destroy()
        from Frontend.Choix_du_domaine import ChoixDomaineApp
        app = ChoixDomaineApp()
        app.mainloop()

    def show_gestion(self):
        self.validation_view.pack_forget()
        self.main_area.pack(fill="both", expand=True)

    def open_validation_page(self):
        self.main_area.pack_forget()
        self.validation_view.pack(fill="both", expand=True)

    def add_user_row(self, user_data):
        username, email, dob, role, warns = user_data
        state = {"ban": 0, "mute": 0}
        row = ctk.CTkFrame(self.scroll_frame, fg_color="#86c49c", corner_radius=5)
        row.pack(fill="x", pady=5)

        for i, (_, weight) in enumerate(self.columns_config):
            row.grid_columnconfigure(i, weight=int(weight * 10))

        text_style = {"text_color": "white", "font": ("Arial", 12)}
        ctk.CTkLabel(row, text=username, **text_style).grid(row=0, column=0, pady=10)
        ctk.CTkLabel(row, text=email, **text_style).grid(row=0, column=1, pady=10)
        ctk.CTkLabel(row, text=dob, **text_style).grid(row=0, column=2, pady=10)
        ctk.CTkLabel(row, text=role, **text_style).grid(row=0, column=3, pady=10)

        actions_frame = ctk.CTkFrame(row, fg_color="transparent")
        actions_frame.grid(row=0, column=5, pady=5, padx=5)

        btn_ban = ctk.CTkButton(actions_frame, width=60)
        btn_ban.pack(side="left", padx=2)
        btn_mute = ctk.CTkButton(actions_frame, width=60)
        btn_mute.pack(side="left", padx=2)

        def refresh_buttons():
            if state["ban"] == 1:
                btn_ban.configure(
                    text="Unban",
                    fg_color="#A20909",
                    command=lambda: (
                        set_user_ban(username, False),
                        state.update({"ban": 0}),
                        refresh_buttons()
                    )
                )
            else:
                btn_ban.configure(
                    text="Ban",
                    fg_color="#019136",
                    command=lambda: (
                        set_user_ban(username, True),
                        state.update({"ban": 1}),
                        refresh_buttons()
                    )
                )

            if state["mute"] == 1:
                btn_mute.configure(
                    text="Unmute",
                    fg_color="#A20909",
                    command=lambda: ActionPopup(
                        self, "Unmute", username, state, "mute", refresh_buttons
                    )
                )
            else:
                btn_mute.configure(
                    text="Mute",
                    fg_color="#019136",
                    command=lambda: ActionPopup(
                        self, "Mute", username, state, "mute", refresh_buttons
                    )
                )

        refresh_buttons()

if __name__ == "__main__":
    app = AdminDashboard()
    app.mainloop()