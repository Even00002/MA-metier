"""
Nom du fichier   : login.py
Auteur           : Joel Cunha Faria
Date de création : 15.01.2026
"""
import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("light")


class LoginApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CPNV HUB - Login")
        self.geometry("1100x700")
        self.minsize(900, 600)

        # === Layout principal ===
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # === GAUCHE : IMAGE ===
        self.left = ctk.CTkFrame(self, corner_radius=0)
        self.left.grid(row=0, column=0, sticky="nsew")

        self.bg_path = "assets/left_background.jpg"
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
        logo_pil = Image.open("assets/logo.png").convert("RGBA")

        self.logo_ctk = ctk.CTkImage(
            light_image=logo_pil,
            dark_image=logo_pil,
            size=(90, 90)
        )

        self.logo_label = ctk.CTkLabel(
            self.bg_label,
            image=self.logo_ctk,
            text="",
            fg_color="transparent"
        )
        self.logo_label.place(relx=0.05, rely=0.06, anchor="nw")

        self.left_title = ctk.CTkLabel(
            self.bg_label,
            text="Bienvenue sur CPNV HUB",
            font=ctk.CTkFont(size=34, weight="bold"),
            text_color="white",
            fg_color="#359859"
        )
        self.left_title.place(relx=0.07, rely=0.42, anchor="w")

        self.left_desc = ctk.CTkLabel(
            self.bg_label,
            text=("Lorem ipsum dolor sit amet, consectetur adipisicing elit...\n"
                  "olor sit amet, consectetur"),
            font=ctk.CTkFont(size=13),
            justify="left",
            text_color="white",
            fg_color="#359859"
        )
        self.left_desc.place(relx=0.07, rely=0.52, anchor="w")

        self.left.bind("<Configure>", self._resize_bg)

        # === DROITE : FORM ===
        self.right = ctk.CTkFrame(self, corner_radius=0, fg_color="white")
        self.right.grid(row=0, column=1, sticky="nsew")

        self.right.grid_columnconfigure(0, weight=1)
        self.right.grid_rowconfigure(0, weight=1)
        self.right.grid_rowconfigure(1, weight=0)
        self.right.grid_rowconfigure(2, weight=0)
        self.right.grid_rowconfigure(3, weight=0)
        self.right.grid_rowconfigure(4, weight=1)

        # Bouton quitter
        self.btn_quit = ctk.CTkButton(
            self.right,
            text="Quitter",
            width=110,
            fg_color="#019136",
            hover_color="#017A5C",
            command=self.destroy
        )
        self.btn_quit.place(relx=0.95, rely=0.05, anchor="ne")

        # === LOGIN CARD ===
        self.login_card = ctk.CTkFrame(self.right, corner_radius=12, fg_color="#7AC596", width=420)
        self.login_card.grid(row=1, column=0)
        self.login_card.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            self.login_card,
            text="Login",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="white"
        ).grid(row=0, column=0, sticky="w", padx=20, pady=(18, 4))

        ctk.CTkLabel(
            self.login_card,
            text="Connectez vous pour profiter pleinement de CPNV HUB",
            font=ctk.CTkFont(size=12),
            text_color="white"
        ).grid(row=1, column=0, sticky="w", padx=20, pady=(0, 14))

        ctk.CTkLabel(
            self.login_card,
            text="Nom d'utilisateur / Adresse email",
            font=ctk.CTkFont(size=12),
            text_color="white"
        ).grid(row=2, column=0, sticky="w", padx=20, pady=(0, 4))

        self.entry_user = ctk.CTkEntry(
            self.login_card,
            height=38,
            fg_color="white",
            text_color="#1f1f1f",
            border_color="white"
        )
        self.entry_user.grid(row=3, column=0, padx=20, pady=(0, 10), sticky="ew")

        ctk.CTkLabel(
            self.login_card,
            text="Mot de passe",
            font=ctk.CTkFont(size=12),
            text_color="white"
        ).grid(row=4, column=0, sticky="w", padx=20, pady=(0, 4))

        self.entry_pass = ctk.CTkEntry(
            self.login_card,
            height=38,
            show="•",
            fg_color="white",
            text_color="#1f1f1f",
            border_color="white"
        )
        self.entry_pass.grid(row=5, column=0, padx=20, pady=(0, 14), sticky="ew")

        self.btn_login = ctk.CTkButton(
            self.login_card,
            text="LOGIN",
            height=42,
            fg_color="#019136",
            hover_color="#017A5C",
            text_color="white",
            command=self.on_login
        )
        self.btn_login.grid(row=6, column=0, padx=20, pady=(0, 18), sticky="ew")

        # ESPACE
        ctk.CTkFrame(self.right, height=30, fg_color="transparent").grid(row=2, column=0)

        # === SIGNUP CARD ===
        self.signup_card = ctk.CTkFrame(self.right, corner_radius=12, fg_color="#7AC596", width=420)
        self.signup_card.grid(row=3, column=0)
        self.signup_card.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            self.signup_card,
            text="Pas encore de compte ?",
            font=ctk.CTkFont(size=12),
            text_color="white"
        ).grid(row=0, column=0, sticky="w", padx=20, pady=(14, 8))

        self.btn_signup = ctk.CTkButton(
            self.signup_card,
            text="SIGN UP",
            height=42,
            fg_color="#019136",
            hover_color="#017A5C",
            text_color="white",
            command=self.on_signup
        )
        self.btn_signup.grid(row=1, column=0, padx=20, pady=(0, 14), sticky="ew")

    # === BG RESIZE ===
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

        self.bg_ctk = ctk.CTkImage(light_image=img, dark_image=img, size=(w, h))
        self.bg_label.configure(image=self.bg_ctk)

    def on_login(self):
        print("LOGIN:", self.entry_user.get(), self.entry_pass.get())

    def on_signup(self):
        print("SIGN UP")


if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()