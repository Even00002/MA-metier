import customtkinter as ctk
from PIL import Image
from Frontend.login import *

class SignupApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CPNV HUB - Signup")
        self.geometry("1100x700+400+150")
        self.minsize(900, 600)

        # === Layout principal ===
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # === GAUCHE : IMAGE ===
        self.left = ctk.CTkFrame(self, corner_radius=0)
        self.left.grid(row=0, column=0, sticky="nsew")

        self.bg_path = "Frontend/assets/left_background.jpg"
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
        logo_pil = Image.open("Frontend/assets/Logo.png").convert("RGBA")
        self.logo_ctk = ctk.CTkImage(
            light_image=logo_pil,
            dark_image=logo_pil,
            size=(100, 90),

        )

        self.logo_label = ctk.CTkLabel(
            self.bg_label,
            image=self.logo_ctk,
            text="",
            bg_color="white"
        )
        self.logo_label.place(relx=0.05, rely=0.06, anchor="nw")

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
        self.show_signup_page()

    # === MODIFICATION DE applogin ===
    def applogin(self):
        self.destroy()  # Ferme la fenêtre Signup
        from Frontend.login import LoginApp  # Import local
        app = LoginApp()
        app.mainloop()



    def show_signup_page(self):

        # Bouton retour
        back_btn = ctk.CTkButton(self.right, text="← Retour", fg_color="#019136", width=100, command=self.applogin)
        back_btn.place(relx=0.05, rely=0.05, anchor="nw")

        # Bouton quitter
        self.btn_quit = ctk.CTkButton(self.right, text="Quitter", width=110, fg_color="#019136",
                                     hover_color="#017A5C", command=self.destroy)
        self.btn_quit.place(relx=0.95, rely=0.05, anchor="ne")

        # Formulaire d'inscription
        self.reg_card = ctk.CTkFrame(self.right, corner_radius=12, fg_color="#7AC596", width=420)
        self.reg_card.place(relx=0.5, rely=0.5, anchor="center")
        self.reg_card.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(self.reg_card, text="Inscription", font=ctk.CTkFont(size=28, weight="bold"),
                     text_color="white").grid(row=0, column=0, pady=20)

        ctk.CTkLabel(
            self.reg_card,
            text="Nom d'utilisateur",
            font=ctk.CTkFont(size=12),
            text_color="white"
        ).grid(row=1, column=0, sticky="w", padx=20, pady=(4, 0))

        ctk.CTkEntry(self.reg_card, height=40, width=350,
                     fg_color="white", corner_radius=5).grid(row=2, column=0, pady=3, padx=20)
        ctk.CTkLabel(
            self.reg_card,
            text="Adresse email",
            font=ctk.CTkFont(size=12),
            text_color="white"
        ).grid(row=3, column=0, sticky="w", padx=20, pady=(4, 0))

        ctk.CTkEntry(self.reg_card, height=40, width=350,
                     fg_color="white", corner_radius=5).grid(row=4, column=0, pady=3, padx=20)

        ctk.CTkLabel(
            self.reg_card,
            text="Date de naissance",
            font=ctk.CTkFont(size=12),
            text_color="white"
        ).grid(row=5, column=0, sticky="w", padx=20, pady=(4, 0))

        ctk.CTkEntry(self.reg_card, height=40, width=350,
                     fg_color="white", corner_radius=5).grid(row=6, column=0, pady=3, padx=20)

        ctk.CTkLabel(
            self.reg_card,
            text="Mot de passe",
            font=ctk.CTkFont(size=12),
            text_color="white"
        ).grid(row=7, column=0, sticky="w", padx=20, pady=(4, 0))

        ctk.CTkEntry(self.reg_card, show="*", height=40, width=350,
                     fg_color="white").grid(row=8, column=0, pady=3, padx=20)

        ctk.CTkLabel(
            self.reg_card,
            text="Confirmer le mot de passe",
            font=ctk.CTkFont(size=12),
            text_color="white"
        ).grid(row=9, column=0, sticky="w", padx=20, pady=(4, 0))

        ctk.CTkEntry(self.reg_card, show="*", height=40, width=350,
                     fg_color="white").grid(row=10, column=0, pady=3, padx=20)

        ctk.CTkButton(self.reg_card, text="S'INSCRIRE", fg_color="#019136", height=45,
                      command=self.on_signup).grid(row=11, column=0, pady=25, padx=20, sticky="ew")
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

    def on_signup(self):
        print("Compte créé (simulé)")
        self.destroy()  # Ferme la fenêtre Signup
        from Frontend.Choix_du_domaine import ChoixDomaineApp  # Import local
        app = ChoixDomaineApp()
        app.mainloop()
# --- CORRECTION INDENTATION ---
if __name__ == "__main__":
    app = SignupApp()
    app.mainloop()
