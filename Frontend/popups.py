"""
Nom du fichier : popups.py
Description : Gestion des popups Ban/Mute et Historique
"""

import customtkinter as ctk

class ActionPopup(ctk.CTkToplevel):
    def __init__(self, parent, action_type, username, state_dict, key, callback):
        super().__init__(parent)
        self.state_dict = state_dict
        self.key = key
        self.callback = callback

        self.geometry("400x300+300+300")
        self.title(f"{action_type} - {username}")
        self.resizable(False, False)
        self.attributes("-topmost", True)

        # Couleurs originales
        self.green_header = "#019136"
        self.input_bg = "#86c49c"

        # En-tête
        self.header = ctk.CTkFrame(self, fg_color=self.green_header, corner_radius=0, height=50)
        self.header.pack(fill="x")

        ctk.CTkLabel(self.header, text=f"{action_type} - {username}", text_color="white",
                     font=("Arial", 16, "bold")).pack(side="left", padx=15, pady=10)

        ctk.CTkButton(self.header, text="X", width=30, fg_color="transparent",
                      command=self.destroy).pack(side="right", padx=10)

        # Contenu
        self.content = ctk.CTkFrame(self, fg_color="white", corner_radius=0)
        self.content.pack(fill="both", expand=True)

        ctk.CTkLabel(self.content, text="Raison:", text_color="black", font=("Arial", 14)).pack(pady=(20, 5))

        self.reason_entry = ctk.CTkTextbox(self.content, height=80, fg_color=self.input_bg,
                                           text_color="white", corner_radius=10, border_width=0)
        self.reason_entry.pack(padx=20, pady=5, fill="x")

        # Boutons
        self.btn_frame = ctk.CTkFrame(self.content, fg_color="transparent")
        self.btn_frame.pack(side="bottom", fill="x", pady=20, padx=20)

        ctk.CTkButton(self.btn_frame, text="Annuler", fg_color="#A20909", hover_color="#901010",
                      command=self.destroy).pack(side="left")

        ctk.CTkButton(self.btn_frame, text="Confirmer", fg_color="#019136", hover_color="#017a5c",
                      command=self.confirmer_action).pack(side="right")

    def confirmer_action(self):
        raison = self.reason_entry.get('0.0', 'end').strip()
        print(f"Action validée pour {self.key} sur l'utilisateur. Raison: {raison}")

        # Alterne l'état (0 -> 1 ou 1 -> 0)
        self.state_dict[self.key] = 1 if self.state_dict[self.key] == 0 else 0

        # Rafraîchit les boutons du dashboard
        self.callback()
        self.destroy()

class HistoryPopup(ctk.CTkToplevel):
    def __init__(self, parent, username, history_data):
        super().__init__(parent)
        self.geometry("500x400")
        self.title(f"Historique - {username}")
        self.attributes("-topmost", True)

        self.header = ctk.CTkFrame(self, fg_color="#019136", corner_radius=0, height=50)
        self.header.pack(fill="x")

        ctk.CTkLabel(self.header, text=f"Historique de sanction - {username}", text_color="white",
                     font=("Arial", 16, "bold")).pack(side="left", padx=15, pady=10)

        ctk.CTkButton(self.header, text="X", width=30, fg_color="transparent",
                      command=self.destroy).pack(side="right", padx=10)

        self.scroll_area = ctk.CTkScrollableFrame(self, fg_color="white", corner_radius=0)
        self.scroll_area.pack(fill="both", expand=True)

        if not history_data:
            ctk.CTkLabel(self.scroll_area, text="Aucun historique.", text_color="black").pack(pady=20)

    import customtkinter as ctk

class ValidationPopup(ctk.CTkToplevel):
    def __init__(self, parent, data):
        super().__init__(parent)
        titre, user, date, type_v = data
        self.geometry("600x550")
        self.config(background="#019136")
        self.attributes("-topmost", True)

        # Header
        lbl_titre = ctk.CTkLabel(self, text=titre, font=("Arial", 20, "bold"), text_color="white")
        lbl_titre.pack(pady=(20, 5), padx=20, anchor="w")

        ctk.CTkLabel(self, text=f"Par : {user}\nSoumis le : {date}", text_color="white", justify="left").pack(
            padx=20, anchor="w")

        # Zone grise
        box = ctk.CTkFrame(self, fg_color="#E0E0E0", corner_radius=15)
        box.pack(fill="both", expand=True, padx=20, pady=20)

        if type_v == "Edit":
            ctk.CTkLabel(box, text="Ancien contenu :", text_color="black").pack(pady=5)
            ctk.CTkTextbox(box, height=100, width=500).pack(pady=5)
            ctk.CTkLabel(box, text="Nouveau contenu :", text_color="black").pack(pady=5)
            ctk.CTkTextbox(box, height=100, width=500).pack(pady=5)
        else:
            ctk.CTkTextbox(box, height=300, width=500).pack(pady=20)

        # Boutons
        btn_f = ctk.CTkFrame(self, fg_color="transparent")
        btn_f.pack(fill="x", side="bottom", pady=20)
        ctk.CTkButton(btn_f, text="Refuser", fg_color="#bd0000", width=200, command=self.destroy).pack(side="left",
                                                                                                       padx=40)
        ctk.CTkButton(btn_f, text="Valider", fg_color="#00a335", width=200).pack(side="right", padx=40)