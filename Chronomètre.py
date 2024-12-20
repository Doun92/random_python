import tkinter as tk
from pygame import mixer

class Chronomètre:
    def __init__(self, root):
        self.root = root
        self.root.title("Chronomètre")
        self.tool = "Chronomètre"

        # Variables
        self.running = False
        self.temps_écoulé = 0

        # Interface graphique

        # Affichage du temps
        if self.tool == "Chronomètre":
            self.label_temps = tk.Label(root, text="00:00:00", font=("Arial", 40))
            self.label_temps.grid(
                row=0,
                column=0,
                columnspan=3,
                pady=20
            )
        self.label_minuteur_en_cours = tk.Label(root, text="", font=("Arial", 40))

        # Bouton Démarrer le Chronomètre
        self.start_button_chronomètre = tk.Button(root, text="Démarrer", command=self.start_chronomètre, width=25)
        self.start_button_chronomètre.grid(
            row=1,
            column=1,
            pady=5
        )

        # Bouton Démarrer le Minuteur
        self.start_button_minuteur = tk.Button(root, text="Démarrer", command=self.start_minuteur, width=25)

        # Bouton Arrêter le Chronomètre
        self.stop_button_temps = tk.Button(root, text="Arrêter", command=self.stop_temps, width=25)
        self.stop_button_temps.grid(
            row=2,
            column=1,
            pady=5
        )

        # Bouton Reset le Chronomètre
        self.reset_button_chronomètre = tk.Button(root, text="Remettre à zéro", command=self.reset_chronomètre, width=25)
        self.reset_button_chronomètre.grid(
            row=3,
            column=1,
            pady=5
        )

        # Bouton modifier Minuteur
        self.modifier_button_minuteur = tk.Button(root, text="Modifier le minuteur", command=self.modifier_minuteur, width=25)

        # Bouton Switch Minuteur
        self.switch_to_minuteur_button = tk.Button(root, text="Aller vers le Minuteur", command=self.switch_to_minuteur, width=25)
        self.switch_to_minuteur_button.grid(
            row=4,
            column=1,
            pady=5
        )

        # Écran minuteur
        # Declaration of variables
        self.heure_nb=tk.StringVar()
        self.minute_nb=tk.StringVar()
        self.seconde_nb=tk.StringVar()
        
        # setting the default value as 0
        self.heure_nb.set("00")
        self.minute_nb.set("00")
        self.seconde_nb.set("00")

        self.écran_minuteur = tk.Frame(root)
        
        # Pop up window pour arrêter la musique
        self.pop_up_window_stop_music = tk.Frame(root)
        # Bouton arrêter musique
        self.arrêter_musique_bouton = tk.Button(self.pop_up_window_stop_music, text="Arrêter la musique", command=self.stop_music, width=25)


         # Configurer la validation pour les champs Entry
        validate_cmd = root.register(self.valider_entrée_minuteur)
        # Heures
        self.label_heures = tk.Label(self.écran_minuteur, text="Heures")
        self.heures=tk.Entry(
            self.écran_minuteur,
            width=5,
            justify=tk.CENTER,
            textvariable = self.heure_nb,
            validate="key",
            validatecommand=(validate_cmd, '%P')
        )
        # Écran minutes
        self.label_minutes = tk.Label(self.écran_minuteur, text="Minutes")
        self.minutes = tk.Entry(
            self.écran_minuteur,
            width=5,
            justify=tk.CENTER,
            textvariable = self.minute_nb,
            validate="key",
            validatecommand=(validate_cmd, '%P')
        )
        # Écran secondes
        self.label_secondes = tk.Label(self.écran_minuteur, text="Secondes")
        self.secondes = tk.Entry(
            self.écran_minuteur,
            width=5,
            justify=tk.CENTER,
            textvariable = self.seconde_nb,
            validate="key",
            validatecommand=(validate_cmd, '%P')
        )

        # Bouton Switch Chronomètre
        self.switch_to_chronomètre_button = tk.Button(root, text="Aller vers le Chronomètre", command=self.switch_to_chronomètre, width=25)

        # Bouton Fermer l'application
        self.close_app_button = tk.Button(root, text="Fermer l'application", command=self.close_app, width=25)
        self.close_app_button.grid(
            row=5,
            column=1,
            pady=5
        )

    """
    Fonctions spécifiques au minuteur
    """
    def valider_entrée_minuteur(self, valeur):
        """
        Valide que l'entrée utilisateur est valide :
        - Deux caractères maximum.
        - Contient uniquement des chiffres.
        - Inférieur à 60.
        """
        if valeur == "": #Permet la suppression complète
            return True
        if len(valeur) <= 2 and valeur.isdigit():
            return int(valeur) < 60
        else:
            return False

    def switch_to_minuteur(self):
        self.running = False
        self.temps_écoulé = 0
        self.label_temps.config(text="00:00:00")
        self.start_button_chronomètre.grid_forget()
        self.reset_button_chronomètre.grid_forget()
        self.switch_to_minuteur_button.grid_forget()
        self.close_app_button.grid_forget()
        self.label_temps.grid_forget()
        self.écran_minuteur.grid(
            row=0,
            column=0,
            columnspan=3,
            pady=20
        )
        self.label_heures.grid(
            row=0,
            column=0
        )
        self.heures.grid(
            row=1,
            column=0
        )
        self.label_minutes.grid(
            row=0,
            column=1
        )
        self.minutes.grid(
            row=1,
            column=1
        )
        self.label_secondes.grid(
            row=0,
            column=2
        )
        self.secondes.grid(
            row=1,
            column=2
        )
        self.start_button_minuteur.grid(
            row=1,
            column=1,
            pady=5
        )
        self.modifier_button_minuteur.grid(
            row=2,
            column=1,
            pady=5
        )
        self.stop_button_temps.grid(
            row=3,
            column=1,
            pady=5
        )
        self.switch_to_chronomètre_button.grid(
            row=4,
            column=1,
            pady=5
        )
        self.close_app_button.grid(
            row=5,
            column=1,
            pady=5
        )
        self.heure_nb.set("00")
        self.minute_nb.set("00")
        self.seconde_nb.set("00")

    def start_minuteur(self):
        """
        Démarre le minuteur en décroissant le temps.
        """
        try:
            # Récupérer les heures, minutes et secondes
            heures = int(self.heure_nb.get())
            minutes = int(self.minute_nb.get())
            secondes = int(self.seconde_nb.get())

            # Convertir le tout en secondes
            total_seconds = heures * 3600 + minutes * 60 + secondes

            # Lancer le décompte
            if not self.running:
                self.running = True
                self.décompte(total_seconds)
        except ValueError:
            # Si une valeur est invalide
            print("Les champs doivent contenir uniquement des nombres valides.")

    def décompte(self, total_seconds):
        """
        Décompte les secondes et met à jour les champs.
        """
        if total_seconds > 0 and self.running:
                # print(total_seconds)
                self.changer_affichage(total_seconds)
                # Calculer les heures, minutes, secondes restantes
                heures, reste = divmod(total_seconds, 3600)
                minutes, secondes = divmod(reste, 60)

                # Mettre à jour les champs
                self.heure_nb.set(f"{heures:02}")
                self.minute_nb.set(f"{minutes:02}")
                self.seconde_nb.set(f"{secondes:02}")

                # Appeler à nouveau la fonction après 1 seconde
                self.label_minuteur_en_cours.after(1000, self.décompte, total_seconds - 1)
        elif total_seconds == 0 and self.running:
            self.running = False
            self.changer_affichage()
            # Quand le décompte est terminé
            self.heure_nb.set("00")
            self.minute_nb.set("00")
            self.seconde_nb.set("00")
            print("Minuteur terminé !")
            self.play_music()

    def changer_affichage(self,secondes ="0"):
        """
        Changer l'affichage d'un input vers un label.
        """
        if self.running:
            self.écran_minuteur.grid_forget()
            self.label_minuteur_en_cours.grid(
                row=0,
                column=0,
                columnspan=3,
                pady=20
            )
            self.label_minuteur_en_cours.config(text=self.format_time_chronomètre(secondes))
        else:
            self.écran_minuteur.grid(
                row=0,
                column=0,
                columnspan=3,
                pady=20
            )
            self.label_minuteur_en_cours.config(text="0")
            self.label_minuteur_en_cours.grid_forget()

    def modifier_minuteur(self):
        self.running = False
        self.écran_minuteur.grid(
            row=0,
            column=0,
            columnspan=3,
            pady=20
        )
        self.label_minuteur_en_cours.grid_forget()

    def play_music(self):
        mixer.init()
        mixer.music.load("Gymnopédie No.1 - Erik Satie.mp3")
        mixer.music.play(loops=0)
        self.pop_up_window_stop_music.grid(
            row=1,
            column=0,
            pady=20
        )
        self.arrêter_musique_bouton.grid(
            row=0,
            column=0,
            pady=20
        )

    def stop_music(self):
        mixer.music.stop()
        self.pop_up_window_stop_music.grid_forget()

    """
    Fonctions spécifiques au chronomètres
    """
    def switch_to_chronomètre(self):
        self.running = False
        self.temps_écoulé = 0
        self.label_temps.config(text="00:00:00")
        self.close_app_button.grid_forget()
        self.écran_minuteur.grid_forget()
        self.start_button_minuteur.grid_forget()
        self.label_minuteur_en_cours.grid_forget()
        self.modifier_button_minuteur.grid_forget()
        self.label_temps.grid(
                row=0,
                column=0,
                columnspan=3,
                pady=20
            )
        self.start_button_chronomètre.grid(
            row=1,
            column=1,
            pady=5
        )
        self.stop_button_temps.grid(
            row=2,
            column=1,
            pady=5
        )
        self.reset_button_chronomètre.grid(
            row=3,
            column=1,
            pady=5
        )
        self.switch_to_minuteur_button.grid(
            row=4,
            column=1,
            pady=5
        )
        self.switch_to_chronomètre_button.grid_forget()
        self.close_app_button.grid(
            row=5,
            column=1,
            pady=5
        )

    def start_chronomètre(self):
        if not self.running:
            self.running = True
            self.update_temps()

    def reset_chronomètre(self):
        self.running = False
        self.temps_écoulé = 0
        self.label_temps.config(text="00:00:00")

    def update_temps(self):
        if self.running:
            self.temps_écoulé += 1
            temps_affiché = self.format_time_chronomètre(self.temps_écoulé)
            self.label_temps.config(text=temps_affiché)
            # Après toutes les 1000 millisecondes (secondes), on relance la même fonction 
            self.root.after(1000, self.update_temps)

    """
    Fonctions pour les deux
    """
    # Pour toujours afficher les heures:minutes:secondes
    def format_time_chronomètre(self, seconds):
        hrs = seconds // 3600
        mins = (seconds % 3600) // 60
        secs = seconds % 60
        return f"{hrs:02}:{mins:02}:{secs:02}"
    
    def stop_temps(self):
        self.running = False

    def close_app(self):
        root.quit()
# Lancement de l'application
if __name__ == "__main__":
    root = tk.Tk()
    chronometer = Chronomètre(root)
    root.mainloop()
