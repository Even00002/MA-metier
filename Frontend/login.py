"""
Nom du fichier   : login.py
Auteur           : Joel Cunha Faria
Date de création : 15.01.2026
Date de modification : 23.01.2026

"""

import customtkinter as ctk
import os
from PIL import Image
from Frontend.signup import *
from CTkMessagebox import CTkMessagebox
import Backend.session as session
from Backend.Services.auth_service import AuthService


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
ctk.set_appearance_mode("light")

class LoginApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CPNV HUB - Login")
        self.geometry("1100x700+400+150")
        self.minsize(900, 600)

        # === Layout principal ===
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # === GAUCHE : IMAGE ===
        self.left = ctk.CTkFrame(self, corner_radius=0)
        self.left.grid(row=0, column=0, sticky="nsew")

        self.bg_path = os.path.join(ASSETS_DIR, "left_background.jpg")
        self._bg_pil = Image.open(self.bg_path)

        self.bg_label = ctk.CTkLabel(
            self.left,
            text="",
            fg_color="transparent",
            corner_radius=0
        )
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.after(10, lambda: self._resize_bg(
            type("E", (), {"width": self.left.winfo_width(), "height": self.left.winfo_height()})()
        ))

        # === LOGO ===
        logo = Image.open(os.path.join(ASSETS_DIR, "Logo.jpg")).convert("RGBA")
        self.logo_ctk = ctk.CTkImage(
            light_image=logo,
            dark_image=logo,
            size=(100, 50),

        )

        self.logo_label = ctk.CTkLabel(
            self.bg_label,
            image=self.logo_ctk,
            text="",
            bg_color="white",
            fg_color="white",
        )
        self.logo_label.place(relx=0.05, rely=0.05, anchor="nw")

        self.left_title = ctk.CTkLabel(
            self.bg_label,
            text="Bienvenue sur CPNV HUB",
            font=ctk.CTkFont(size=32, weight="bold"),
            text_color="white",
            fg_color="#359859"
        )
        self.left_title.place(relx=0.03, rely=0.42, anchor="w")

        self.left_desc = ctk.CTkLabel(
            self.bg_label,
            text=("L'application d'entraide pour partager vos connaissances\n"
                  "et demander de l'aide au sein du CPNV."),
            font=ctk.CTkFont(size=13),
            justify="left",
            text_color="white",
            fg_color="#359859"
        )
        self.left_desc.place(relx=0.05, rely=0.52, anchor="w")

        self.left.bind("<Configure>", self._resize_bg)

        # === DROITE : FORM ===
        self.right = ctk.CTkFrame(self, corner_radius=0, fg_color="white")
        self.right.grid(row=0, column=1, sticky="nsew")

        # Appel de la fonction pour afficher le login par défaut
        self.show_login_page()

    # === LOGIQUE DE NAVIGATION ===
    def clear_right_side(self):
        for widget in self.right.winfo_children():
            widget.destroy()

    def show_login_page(self):
        global show_login_page


        self.right.grid_columnconfigure(0, weight=1)
        self.right.grid_rowconfigure(0, weight=1)
        self.right.grid_rowconfigure(1, weight=0)
        self.right.grid_rowconfigure(2, weight=0)
        self.right.grid_rowconfigure(3, weight=0)
        self.right.grid_rowconfigure(4, weight=1)

        # Bouton quitter
        self.btn_quit = ctk.CTkButton(self.right, text="Quitter", width=110, fg_color="#019136",
                                     hover_color="#017A5C", command=self.destroy)
        self.btn_quit.place(relx=0.95, rely=0.05, anchor="ne")

        # LOGIN CARD
        self.login_card = ctk.CTkFrame(self.right, corner_radius=12, fg_color="#7AC596", width=420)
        self.login_card.grid(row=1, column=0)
        self.login_card.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(self.login_card, text="Login", font=ctk.CTkFont(size=28, weight="bold"),
                     text_color="white").grid(row=0, column=0, sticky="w", padx=20, pady=(18, 4))

        ctk.CTkLabel(self.login_card, text="Connectez vous pour profiter de CPNV HUB",
                     text_color="white").grid(row=1, column=0, sticky="w", padx=20, pady=(0, 14))

        ctk.CTkLabel(
            self.login_card,
            text="Nom d'utilisateur / Adresse email",
            font=ctk.CTkFont(size=12),
            text_color="white"
        ).grid(row=2, column=0, sticky="w", padx=20, pady=(4, 0))

        self.entry_user = ctk.CTkEntry(self.login_card, height=38, fg_color="white")
        self.entry_user.grid(row=3, column=0, padx=20, pady=(0, 10), sticky="ew")


        ctk.CTkLabel(
            self.login_card,
            text="Mot de passe",
            font=ctk.CTkFont(size=12),
            text_color="white"
        ).grid(row=4, column=0, sticky="w", padx=20, pady=(4, 0))

        self.entry_pass = ctk.CTkEntry(self.login_card, height=38, show="*", fg_color="white")
        self.entry_pass.grid(row=5, column=0, padx=20, pady=(0, 14), sticky="ew")


        ctk.CTkButton(self.login_card, text="LOGIN", height=42, fg_color="#019136",
                      command=self.on_login).grid(row=6, column=0, padx=20, pady=(0, 18), sticky="ew")

        # SIGNUP CARD
        self.signup_card = ctk.CTkFrame(self.right, corner_radius=12, fg_color="#7AC596", width=420)
        self.signup_card.grid(row=3, column=0, pady=20)
        self.signup_card.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(self.signup_card, text="Pas encore de compte ?", text_color="white").grid(row=0, padx=20, pady=5)
        ctk.CTkButton(self.signup_card, text="SIGN UP", height=42, fg_color="#019136",
                      command=self.on_signup).grid(row=1, padx=20, pady=(0, 14), sticky="ew")



    # === RESIZE IMAGE ===
    def _resize_bg(self, event):
        w, h = event.width, event.height
        if w < 2 or h < 2: return
        img = self._bg_pil.copy()
        img_ratio = img.width / img.height
        frame_ratio = w / h
        if frame_ratio > img_ratio:
            new_w, new_h = w, int(w / img_ratio)
        else:
            new_h, new_w = h, int(h * img_ratio)
        img = img.resize((new_w, new_h), Image.LANCZOS)
        left, top = (new_w - w) // 2, (new_h - h) // 2
        img = img.crop((left, top, left + w, top + h))
        self.bg_ctk = ctk.CTkImage(light_image=img, dark_image=img, size=(w, h))
        self.bg_label.configure(image=self.bg_ctk)

    def on_login(self):
        login = self.entry_user.get()
        password = self.entry_pass.get()


        success, result = AuthService.login(login, password)

        if success:
            session.current_user = result

            self.destroy()  # Ferme la fenêtre Signup
            from Frontend.Choix_du_domaine import ChoixDomaineApp  # Import local
            app = ChoixDomaineApp()
            app.mainloop()
        else:
            CTkMessagebox(
                title="Erreur",
                message=result,
                icon="cancel"
            )

    def on_signup(self):
        self.destroy()  # Ferme la fenêtre Login
        from Frontend.signup import SignupApp  # Import local pour éviter la boucle
        app = SignupApp()
        app.mainloop()


if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()