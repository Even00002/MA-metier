"""
Nom du fichier   : Choix_du_domaine.py
Auteur           : Even
Date de création : 16.01.2026
"""

import customtkinter as ctk
import os
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
ctk.set_appearance_mode("light")

class ChoixDomaineApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CPNV HUB - Sujet")
        self.geometry("1100x700+400+150")
        self.minsize(900, 600)

        # === Layout principal ===
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # ================= GAUCHE =================
        self.left = ctk.CTkFrame(self, corner_radius=0)
        self.left.grid(row=0, column=0, sticky="nsew")

        # Background
        self.bg_path = os.path.join(ASSETS_DIR, "left_background.jpg")
        self._bg_pil = Image.open(self.bg_path)

        self.bg_label = ctk.CTkLabel(self.left, text="")
        self.bg_label.place(relwidth=1, relheight=1)
        self.left.bind("<Configure>", self._resize_bg)

        # Logo
        logo = Image.open(os.path.join(ASSETS_DIR, "Logo.png")).convert("RGBA")
        self.logo_img = ctk.CTkImage(logo, logo, size=(90, 80))
        ctk.CTkLabel(self.bg_label, image=self.logo_img, text="").place(
            relx=0.05, rely=0.05, anchor="nw"
        )

        # Titre gauche
        ctk.CTkLabel(
            self.bg_label,
            text="Bienvenue sur CPNV HUB",
            font=ctk.CTkFont(size=34, weight="bold"),
            text_color="white",
            fg_color="#2f8f5b",
            corner_radius=0,
            padx=20,
            pady=10,
        ).place(relx=0.07, rely=0.32, anchor="w")

        # Texte explicatif
        self.left_text = ctk.CTkFrame(
            self.bg_label, fg_color="#2f8f5b", corner_radius=0, border_color="#2f8f5b"
        )
        self.left_text.place(relx=0.07, rely=0.53, relwidth=0.80, relheight=0.20)

        ctk.CTkLabel(
            self.left_text,
            text=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod\n"
                "tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,\n"
                "quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo\n"
                "consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum\n"
                "dolore eu fugiat nulla pariatur.\n"
                "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia\n"
                "deserunt mollit anim id est laborum."
            ),
            font=ctk.CTkFont(size=13),
            text_color="white",
            justify="left",
            fg_color="#2f8f5b",
        ).pack(anchor="w")

        # ================= DROITE =================
        self.right = ctk.CTkFrame(self, fg_color="white", corner_radius=0)
        self.right.grid(row=0, column=1, sticky="nsew")

        # Bouton retour
        ctk.CTkButton(
            self.right,
            text="← Retour",
            width=100,
            fg_color="#019136",
            hover_color="#017a5c",
            cursor = "hand2",
            command=self.appchange
        ).place(relx=0.05, rely=0.05, anchor="nw")

        # Bouton quitter
        ctk.CTkButton(
            self.right,
            text="Quitter",
            width=100,
            fg_color="#019136",
            hover_color="#017a5c",
            command=self.destroy
        ).place(relx=0.95, rely=0.05, anchor="ne")

        # Carte de choix des sujets
        self.card = ctk.CTkFrame(self.right, fg_color="#7ac596", corner_radius=12)
        self.card.place(relx=0.5, rely=0.53, anchor="center", relwidth=0.75, relheight=0.75)

        # Titre
        ctk.CTkLabel(
            self.card,
            text="Veuillez choisir le domaine\n"
                 "sur lequel vous souhaitez\n"
                 "être conseillé",
            font=ctk.CTkFont(size=26, weight="bold"),
            text_color="white",
            justify="center"
        ).pack(pady=(30, 20))

        # ========= Boutons de sujets =========
        self.buttons_frame = ctk.CTkFrame(self.card, fg_color="transparent")
        self.buttons_frame.pack(pady=20)

        btn_style = {
            "width": 180,
            "height": 45,
            "corner_radius": 15,
            "fg_color": "#019136",
            "hover_color": "#017a5c",
            "text_color": "white",
            "cursor": "hand2",
            "font": ctk.CTkFont(size=12, weight="bold")
        }

        subjects = [
            ("Programmation", 0, 0),
            ("Web", 0, 1),
            ("Bases de données", 1, 0),
            ("Systèmes & Réseaux", 1, 1),
            ("Outils & Méthode", 2, 0),
            ("Aide scolaire IT", 2, 1)
        ]

        for text, r, c in subjects:
            ctk.CTkButton(
                self.buttons_frame,
                text=text,
                command=lambda t=text: self.ouvrir_sujet(t),
                **btn_style
            ).grid(row=r, column=c, padx=20, pady=15)

        # Aligner Java au centre
        self.buttons_frame.grid_columnconfigure(0, weight=1)
        self.buttons_frame.grid_columnconfigure(1, weight=1)

    # === Méthode pour gérer le clic sur un sujet ===
    def ouvrir_sujet(self, sujet):
        print(f"Sujet choisi : {sujet}")
        # Ici, tu peux ouvrir la fenêtre correspondante
        if sujet == "Programmation":
            self.destroy()
            from Frontend.Programmation import ChoixProg
            app = ChoixProg()
            app.mainloop()
        if sujet == "Web":
            self.destroy()
            from Frontend.Web import ChoixWeb
            app = ChoixWeb()
            app.mainloop()
        if sujet == "Bases de données":
            self.destroy()
            from Frontend.Base_donee import ChoixBase
            app = ChoixBase()
            app.mainloop()
        if sujet == "Systèmes & Réseaux":
            self.destroy()
            from Frontend.Systeme_et_Reseau import ChoixReseau
            app = ChoixReseau()
            app.mainloop()
        if sujet == "Outils & Méthode":
            self.destroy()
            from Frontend.Outil_et_Methode import ChoixOutils
            app = ChoixOutils()
            app.mainloop()
        if sujet == "Aide scolaire IT":
            self.destroy()
            from Frontend.Aide_scolaire_IT import ChoixAide
            app = ChoixAide()
            app.mainloop()

    def appchange(self):
        self.destroy()  # Ferme la fenêtre Login
        from Frontend.login import LoginApp  # Import local pour éviter la boucle
        app = LoginApp()
        app.mainloop()


    # === Resize background ===
    def _resize_bg(self, event):
        w, h = event.width, event.height
        if w < 2 or h < 2:
            return

        img = self._bg_pil.copy()
        img_ratio = img.width / img.height
        frame_ratio = w / h

        if frame_ratio > img_ratio:
            new_w = w
            new_h = int(w / img_ratio)
        else:
            new_h = h
            new_w = int(h * img_ratio)

        img = img.resize((new_w, new_h), Image.LANCZOS)
        left = (new_w - w) // 2
        top = (new_h - h) // 2
        img = img.crop((left, top, left + w, top + h))

        self.bg_ctk = ctk.CTkImage(img, img, size=(w, h))
        self.bg_label.configure(image=self.bg_ctk)


if __name__ == "__main__":
    app = ChoixDomaineApp()
    app.mainloop()
