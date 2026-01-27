"""
Nom du fichier : popups.py
Description : Gestion des popups Ban/Mute et Validation (Ajout/Edit)
Dernier changement : 27.01.2026
"""

import customtkinter as ctk

class ActionPopup(ctk.CTkToplevel):
    def __init__(self, parent, action_type, username, state_dict, key, callback):
        super().__init__(parent)
        self.state_dict = state_dict
        self.key = key
        self.callback = callback

        self.geometry("500x400")
        self.title(f"{action_type} - {username}")
        self.resizable(False, False)
        self.attributes("-topmost", True)
        self.configure(fg_color="white") # Fond de la fenêtre

        # Couleurs originales
        self.green_header = "#019136"
        self.input_bg = "#86c49c"

        # En-tête
        self.header = ctk.CTkFrame(self, fg_color=self.green_header, corner_radius=0, height=60)
        self.header.pack(fill="x")

        ctk.CTkLabel(self.header, text=f"{action_type} - {username}", text_color="white",
                     font=("Arial", 16, "bold")).pack(side="left", padx=15, pady=10)

        ctk.CTkButton(self.header, text="X", width=30, fg_color="transparent", hover_color="#017a2d",
                      command=self.destroy).pack(side="right", padx=10)

        # Contenu
        ctk.CTkLabel(self, text="Raison de l'action :", text_color="black", font=("Arial", 14, "bold")).pack(pady=(20, 5), padx=20, anchor="w")

        self.reason_entry = ctk.CTkTextbox(self, height=100, fg_color=self.input_bg,
                                           text_color="white", corner_radius=10, border_width=0, font=("Arial", 12))
        self.reason_entry.pack(padx=20, pady=5, fill="both", expand=True)

        # Boutons
        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack(side="bottom", fill="x", pady=20, padx=20)

        ctk.CTkButton(self.btn_frame, text="Annuler", fg_color="#A20909", hover_color="#901010",
                      width=120, command=self.destroy).pack(side="left")

        ctk.CTkButton(self.btn_frame, text="Confirmer", fg_color="#019136", hover_color="#017a5c",
                      width=120, command=self.confirmer_action).pack(side="right")

    def confirmer_action(self):
        raison = self.reason_entry.get('0.0', 'end').strip()
        self.state_dict[self.key] = 1 if self.state_dict[self.key] == 0 else 0
        self.callback()
        self.destroy()

class ValidationPopup(ctk.CTkToplevel):
    def __init__(self, parent, data):
        super().__init__(parent)
        titre, user, date, type_v = data

        # Config fenêtre
        self.geometry("700x800")
        self.title(f"Validation {type_v}")
        self.configure(fg_color="#019136") # Le vert en fond comme sur ta maquette
        self.attributes("-topmost", True)

        # --- HEADER ---
        header_frame = ctk.CTkFrame(self, fg_color="transparent")
        header_frame.pack(fill="x", padx=30, pady=(20, 10))

        # Titre et Badge
        title_row = ctk.CTkFrame(header_frame, fg_color="transparent")
        title_row.pack(fill="x")

        lbl_titre = ctk.CTkLabel(title_row, text=titre, font=("Arial", 22, "bold"), text_color="white")
        lbl_titre.pack(side="left")

        badge_txt = "Ajout" if type_v == "Ajout" else "Edit"
        ctk.CTkLabel(title_row, text=badge_txt, fg_color="white", text_color="black",
                     corner_radius=5, width=60, font=("Arial", 12, "bold")).pack(side="left", padx=15)

        # Infos utilisateur
        ctk.CTkLabel(header_frame, text=f"Par : {user}\nSoumis le : {date}",
                     text_color="white", justify="left", font=("Arial", 13)).pack(anchor="w", pady=5)

        # Bouton fermer en haut à droite
        ctk.CTkButton(self, text="✕", width=30, fg_color="transparent", text_color="white",
                      font=("Arial", 20), command=self.destroy).place(relx=0.95, rely=0.02)

        # --- ZONE DE CONTENU (GRIS) ---
        main_box = ctk.CTkFrame(self, fg_color="#E0E0E0", corner_radius=15)
        main_box.pack(fill="both", expand=True, padx=25, pady=10)

        # Conteneur scrollable ou frame interne pour les textboxes
        content_inner = ctk.CTkFrame(main_box, fg_color="transparent")
        content_inner.pack(fill="both", expand=True, padx=20, pady=20)

        if type_v == "Edit":
            # Section Ancien
            ctk.CTkLabel(content_inner, text="Ancien contenu :", text_color="black", font=("Arial", 13, "bold")).pack(anchor="w", pady=(0, 5))
            self.old_txt = ctk.CTkTextbox(content_inner, corner_radius=10, border_width=0, fg_color="white", text_color="black")
            self.old_txt.pack(fill="both", expand=True, pady=(0, 15))
            self.old_txt.insert("0.0", "Contenu précédent récupéré de la DB...")
            self.old_txt.configure(state="disabled") # Lecture seule pour l'ancien

            # Section Nouveau
            ctk.CTkLabel(content_inner, text="Nouveau contenu :", text_color="black", font=("Arial", 13, "bold")).pack(anchor="w", pady=(0, 5))
            self.new_txt = ctk.CTkTextbox(content_inner, corner_radius=10, border_width=0, fg_color="white", text_color="black")
            self.new_txt.pack(fill="both", expand=True)
            self.new_txt.insert("0.0", "Nouveau contenu soumis par l'utilisateur...")
        else:
            # Mode Ajout (Une seule grande zone)
            ctk.CTkLabel(content_inner, text="Contenu de la publication :", text_color="black", font=("Arial", 13, "bold")).pack(anchor="w", pady=(0, 5))
            self.add_txt = ctk.CTkTextbox(content_inner, corner_radius=10, border_width=0, fg_color="white", text_color="black")
            self.add_txt.pack(fill="both", expand=True)
            self.add_txt.insert("0.0", "Détails de l'ajout...")

        # --- BOUTONS ACTIONS ---
        btn_container = ctk.CTkFrame(self, fg_color="transparent")
        btn_container.pack(fill="x", side="bottom", pady=25, padx=25)

        self.btn_refuser = ctk.CTkButton(btn_container, text="Refuser", fg_color="#bd0000", hover_color="#900000",
                                         height=45, font=("Arial", 14, "bold"), command=self.destroy)
        self.btn_refuser.pack(side="left", fill="x", expand=True, padx=(0, 10))

        self.btn_valider = ctk.CTkButton(btn_container, text="Valider", fg_color="#00a335", hover_color="#00802a",
                                         height=45, font=("Arial", 14, "bold"), command=self.valider_publication)
        self.btn_valider.pack(side="left", fill="x", expand=True, padx=(10, 0))

    def valider_publication(self):
        # Logique de validation ici
        print("Publication validée")
        self.destroy()

class HistoryPopup(ctk.CTkToplevel):
    def __init__(self, parent, username, history_data):
        super().__init__(parent)
        self.geometry("550x450")
        self.title(f"Historique - {username}")
        self.attributes("-topmost", True)
        self.configure(fg_color="white")

        self.header = ctk.CTkFrame(self, fg_color="#019136", corner_radius=0, height=60)
        self.header.pack(fill="x")

        ctk.CTkLabel(self.header, text=f"Historique de sanction - {username}", text_color="white",
                     font=("Arial", 16, "bold")).pack(side="left", padx=15, pady=10)

        ctk.CTkButton(self.header, text="✕", width=30, fg_color="transparent", hover_color="#017a2d",
                      command=self.destroy).pack(side="right", padx=10)

        self.scroll_area = ctk.CTkScrollableFrame(self, fg_color="transparent", corner_radius=0)
        self.scroll_area.pack(fill="both", expand=True, padx=10, pady=10)

        if not history_data:
            ctk.CTkLabel(self.scroll_area, text="Aucun historique pour cet utilisateur.",
                         text_color="gray", font=("Arial", 13, "italic")).pack(pady=50)