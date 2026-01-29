import os
from PIL import Image
import customtkinter as ctk
from Backend.Services.chat_service import ChatService
import Backend.session as session
from Frontend.Choix_du_domaine import ChoixDomaineApp

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
ctk.set_appearance_mode("light")

DOMAIN_ID = 1  # Domaine Programmation

def retour(parent):
    parent.destroy()
    app = ChoixDomaineApp()
    app.mainloop()


class ChoixProg(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CPNV HUB - Programmation")
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
        logo = Image.open(os.path.join(ASSETS_DIR, "Logo.jpg")).convert("RGBA")
        self.logo_img = ctk.CTkImage(logo, logo, size=(100, 50))
        ctk.CTkLabel(self.bg_label, image=self.logo_img, text="").place(
            relx=0.05, rely=0.05, anchor="nw"
        )

        # Titre gauche
        ctk.CTkLabel(
            self.bg_label,
            text="Forum Programmation",
            font=ctk.CTkFont(size=34, weight="bold"),
            text_color="white",
            fg_color="#2f8f5b",
            corner_radius=0,
            padx=20,
            pady=10,
        ).place(relx=0.05, rely=0.20, anchor="w")

        # ======== CHAT ========
        # ======== CHAT ========
        # Frame pour le chat
        self.left_text = ctk.CTkFrame(
            self.bg_label,
            fg_color="#2f8f5b",
            corner_radius=0,  # coins carrés
            border_color="black",
            border_width=2
        )
        self.left_text.place(relx=0.05, rely=0.25, relwidth=0.80,
                             relheight=0.60)  # plus bas pour ne pas chevaucher le titre

        # Canvas + Scrollbar
        self.chat_canvas = ctk.CTkCanvas(self.left_text, bg="#2f8f5b", highlightthickness=0)
        self.chat_scrollbar = ctk.CTkScrollbar(self.left_text, orientation="vertical", command=self.chat_canvas.yview)
        self.chat_canvas.configure(yscrollcommand=self.chat_scrollbar.set)
        self.chat_scrollbar.pack(side="right", fill="y")
        self.chat_canvas.pack(side="left", fill="both", expand=True)

        # Frame interne pour les messages
        self.chat_inner_frame = ctk.CTkFrame(self.chat_canvas, fg_color="#2f8f5b", corner_radius=0)
        self.chat_canvas.create_window((0, 0), window=self.chat_inner_frame, anchor="nw")

        def on_configure(event):
            self.chat_canvas.configure(scrollregion=self.chat_canvas.bbox("all"))

        self.chat_inner_frame.bind("<Configure>", on_configure)

        # ======== Zone d'envoi sous le chat ========
        # Frame du champ + bouton
        self.entry_frame = ctk.CTkFrame(
            self.bg_label,
            fg_color="#2f8f5b",
            corner_radius=0,
            height=40
        )
        # Positionnement : relwidth = largeur proportionnelle à la fenêtre
        self.entry_frame.place(relx=0.05, rely=0.87, relwidth=0.80)

        # Champ de saisie
        self.message_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="Écrire un message...")
        self.message_entry.pack(side="left", fill="x", expand=True, padx=(0, 5), pady=5)

        # Bouton Envoyer
        self.send_button = ctk.CTkButton(
            self.entry_frame,
            text="Envoyer",
            width=80,
            fg_color="#019136",
            hover_color="#017a5c",
            corner_radius=0,
            command=self.send_message
        )
        self.send_button.pack(side="right", padx=(5, 0), pady=5)

        # ======== Messages ========
        def load_chat(self):
            for widget in self.chat_inner_frame.winfo_children():
                widget.destroy()

            success, messages = ChatService.get_messages_by_domain(DOMAIN_ID)
            if success:
                for msg in messages:
                    is_user = msg['username'] == session.current_user.username
                    anchor = "e" if is_user else "w"

                    ctk.CTkLabel(
                        self.chat_inner_frame,
                        text=f"{msg['username']} : {msg['content']}",
                        fg_color="transparent",
                        corner_radius=0,
                        text_color="white",
                        padx=5,
                        pady=2
                    ).pack(side="top", anchor=anchor, pady=2, padx=5)

                # Scroll automatique en bas
                self.chat_canvas.update_idletasks()
                self.chat_canvas.yview_moveto(1.0)

        # ================= DROITE =================
        self.right = ctk.CTkFrame(self, fg_color="white", corner_radius=0)
        self.right.grid(row=0, column=1, sticky="nsew")

        # Boutons retour / quitter
        ctk.CTkButton(
            self.right,
            text="← Retour",
            width=100,
            fg_color="#019136",
            hover_color="#017a5c",
            cursor="hand2",
            command=lambda: retour(self),
        ).place(relx=0.05, rely=0.05, anchor="nw")

        ctk.CTkButton(
            self.right,
            text="Quitter",
            width=100,
            fg_color="#019136",
            hover_color="#017a5c",
            command=self.destroy
        ).place(relx=0.95, rely=0.05, anchor="ne")

        # Carte choix des sujets
        self.card = ctk.CTkFrame(self.right, fg_color="#7ac596", corner_radius=12)
        self.card.place(relx=0.5, rely=0.53, anchor="center", relwidth=0.75, relheight=0.75)

        ctk.CTkLabel(
            self.card,
            text="Veuillez choisir un sujet du\n"
                 "domaine Programmation",
            font=ctk.CTkFont(size=26, weight="bold"),
            text_color="white",
            justify="center"
        ).pack(pady=(30, 20))

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
            ("Python", 0, 0),
            ("C#", 0, 1),
            ("Javascript", 1, 0),
            ("C++", 1, 1),
            ("Java", 2, 0)
        ]

        for text, r, c in subjects:
            ctk.CTkButton(
                self.buttons_frame,
                text=text,
                command=lambda t=text: self.ouvrir_sujet(t),
                **btn_style
            ).grid(row=r, column=c, padx=20, pady=15)

        self.buttons_frame.grid_columnconfigure(0, weight=1)
        self.buttons_frame.grid_columnconfigure(1, weight=1)

        # ===== Charger l'historique =====
        self.load_chat()

    # === Méthode pour gérer le clic sur un sujet ===
    def ouvrir_sujet(self, sujet):
        print(f"Sujet choisi : {sujet}")
        self.destroy()
        if sujet == "Python":
            from Frontend.Programmation_dir.Python import SujetsPython
            app = SujetsPython()
        elif sujet == "C#":
            from Frontend.Programmation_dir.Ctag import SujetsCtag
            app = SujetsCtag()
        elif sujet == "Javascript":
            from Frontend.Programmation_dir.Javascript import SujetsJavascript
            app = SujetsJavascript()
        elif sujet == "C++":
            from Frontend.Programmation_dir.Cplus import SujetsCplus
            app = SujetsCplus()
        elif sujet == "Java":
            from Frontend.Programmation_dir.Java import SujetsJava
            app = SujetsJava()
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

    # ===== Chat lié à la base de données =====
    def send_message(self):
        content = self.message_entry.get().strip()
        if not content:
            return

        ChatService.send_message(
            user_id=session.current_user.id,
            domain_id=DOMAIN_ID,
            content=content
        )

        self.message_entry.delete(0, "end")
        self.load_chat()

    def load_chat(self):
        # Supprime tous les anciens messages
        for widget in self.chat_inner_frame.winfo_children():
            widget.destroy()

        # Récupère les messages depuis la DB
        success, messages = ChatService.get_messages_by_domain(DOMAIN_ID)
        if success:
            for msg in messages:
                # Message simple, aligné à gauche, sans fond
                ctk.CTkLabel(
                    self.chat_inner_frame,
                    text=f"{msg['username']} : {msg['content']}",
                    fg_color="transparent",  # plus de fond
                    corner_radius=0,
                    text_color="white",
                    padx=5,
                    pady=2,
                    anchor="w",
                    justify="left"
                ).pack(anchor="w", pady=2, padx=5)

            # Scroll en bas
            self.chat_canvas.update_idletasks()
            self.chat_canvas.yview_moveto(1.0)


if __name__ == "__main__":
    app = ChoixProg()
    app.mainloop()