"""
Nom du fichier   : Sujets.py
Auteur           : Even
Date de création : 21.01.2026
"""

from Frontend.Aide_scolaire_IT import ChoixAide
import customtkinter as ctk
import os
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "..", "assets")
ctk.set_appearance_mode("light")

def retour(parent):
    parent.destroy()        # ferme la fenêtre du sujet
    app = ChoixAide()        # lance la page Choix du sujet
    app.mainloop()

class SujetsMemento(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CPNV HUB - Memento")
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

        # Titre gauche (bande verte)
        self.left_title = ctk.CTkLabel(
            self.bg_label,
            text="Forum Aide scolaire IT",
            font=ctk.CTkFont(size=34, weight="bold"),
            text_color="white",
            fg_color="#2f8f5b",
            corner_radius=0,
            padx=20,
            pady=8,
        )
        self.left_title.place(relx=0.07, rely=0.40, anchor="w")

        # Texte encadré
        self.left_text = ctk.CTkFrame(
            self.bg_label,
            fg_color="#2f8f5b",
            corner_radius=0,
            border_width=0
        )
        self.left_text.place(relx=0.07, rely=0.48, relwidth=0.8)

        ctk.CTkLabel(
            self.left_text,
            text=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod\n"
                "tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,\n"
                "quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo\n"
                "consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum\n"
                "dolore eu fugiat nulla pariatur."
            ),
            text_color="white",
            font=ctk.CTkFont(size=12),
            justify="left",
            padx=12,
            pady=12
        ).pack()

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
            text="Memento",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="white"
        ).pack(pady=(30, 20))

        # Texte sujet
        ctk.CTkLabel(
            self.card,
            text=(
                "https://www.cpnv.ch/vivre-au-cpnv"
            ),
            font=ctk.CTkFont(size=13),
            text_color="white",
            justify="center",
            wraplength=450
        ).pack(padx=40)

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
    app = SujetsMemento()
    app.mainloop()
