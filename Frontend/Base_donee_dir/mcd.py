"""
Nom du fichier   : Sujets.py
Auteur           : Even
Date de création : 21.01.2026
Date de modification : 29.01.2026
"""

from Frontend.Base_donee import ChoixBase
import customtkinter as ctk
import os
from PIL import Image
from Backend.Services.subdomain_service import get_sujet_text

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "..", "assets")
ctk.set_appearance_mode("light")

def retour(parent):
    parent.destroy()        # ferme la fenêtre du sujet
    app = ChoixBase()        # lance la page Choix du sujet
    app.mainloop()

class SujetsMCD(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CPNV HUB - MCD")
        self.geometry("1100x700+400+150")
        self.minsize(900, 600)

        # === Layout principal ===
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # ================= GAUCHE =================
        self.left = ctk.CTkFrame(self, corner_radius=0)
        self.left.grid(row=0, column=0, sticky="nsew")

        self.bg_path = os.path.join(ASSETS_DIR, "left_background.jpg")
        self._bg_pil = Image.open(self.bg_path)

        self.bg_label = ctk.CTkLabel(self.left, text="")
        self.bg_label.place(relwidth=1, relheight=1)

        self.left.bind("<Configure>", self._resize_bg)

        # Logo
        logo = Image.open(os.path.join(ASSETS_DIR, "Logo.jpg")).convert("RGBA")
        self.logo_img = ctk.CTkImage(logo, logo, size=(100, 50))
        ctk.CTkLabel(self.bg_label, image=self.logo_img, text="").place(
            relx=0.05, rely=0.05, anchor="nw"
        )

        # Titre gauche
        ctk.CTkLabel(
            self.bg_label,
            text="Forum Base de données",
            font=ctk.CTkFont(size=34, weight="bold"),
            text_color="white",
            fg_color="#2f8f5b",
            corner_radius=0,
            padx=20,
            pady=10,
        ).place(relx=0.05, rely=0.20, anchor="w")

        # Texte explicatif
        self.left_text = ctk.CTkFrame(
            self.bg_label, fg_color="#2f8f5b", corner_radius=0, border_color="black", border_width=2
        )
        self.left_text.place(relx=0.05, rely=0.30, relwidth=0.80, relheight=0.60)

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
        ).pack(anchor="w", padx=2, pady=2)

        # ================= DROITE =================
        self.right = ctk.CTkFrame(self, fg_color="white", corner_radius=0)
        self.right.grid(row=0, column=1, sticky="nsew")

        # Boutons retour
        ctk.CTkButton(
            self.right,
            text="← Retour",
            width=100,
            fg_color="#019136",
            hover_color="#017a5c",
            cursor = "hand2",
            command=lambda: retour(self),
        ).place(relx=0.05, rely=0.05, anchor="nw")

        # Boutons quitter
        ctk.CTkButton(
            self.right,
            text="Quitter",
            width=100,
            fg_color="#019136",
            hover_color="#017a5c",
            command=self.destroy
        ).place(relx=0.95, rely=0.05, anchor="ne")

        # Carte sujet
        self.card = ctk.CTkFrame(
            self.right,
            fg_color="#7ac596",
            corner_radius=12
        )
        self.card.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.75, relheight=0.75)

        # Titre sujet
        ctk.CTkLabel(
            self.card,
            text="MCD",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="white"
        ).pack(pady=(30, 20))

        # Texte sujet
        sujet_texte = get_sujet_text("MCD")

        self.text_box = ctk.CTkTextbox(self.card, font=ctk.CTkFont(size=13), fg_color="#7ac596", text_color="white")
        self.text_box.insert("0.0", sujet_texte)
        self.text_box.configure(state="disabled")  # empêche l'édition
        self.text_box.pack(fill="both", expand=True, padx=20, pady=20)

        # Bouton modifier
        ctk.CTkButton(
            self.right,
            text="Modifier",
            fg_color="#019136",
            hover_color="#017a5c",
            width=100,
            cursor = "hand2"
        ).place(relx=0.95, rely=0.95, anchor="se")

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
    app = SujetsMCD()
    app.mainloop()
