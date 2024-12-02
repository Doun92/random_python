import tkinter as tk

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
            self.label_temps.pack(pady=20)

        # Bouton Démarrer
        self.start_button = tk.Button(root, text="Démarrer", command=self.start, width=15)
        self.start_button.pack(pady=5)

        # Bouton Arrêter
        self.stop_button = tk.Button(root, text="Arrêter", command=self.stop, width=15)
        self.stop_button.pack(pady=5)

        # Bouton Reset
        self.reset_button = tk.Button(root, text="Remettre à zéro", command=self.reset, width=15)
        self.reset_button.pack(pady=5)

        # Bouton Switch Minuteur
        self.switch_to_minuteur_button = tk.Button(root, text="Aller vers le Minuteur", command=self.switch_to_minuteur, width=15)
        self.switch_to_minuteur_button.pack(pady=5)

        # Bouton Switch Chronomètre
        self.switch_to_chronomètre_button = tk.Button(root, text="Aller vers le Chronomètre", command=self.switch_to_chronomètre, width=15)
        self.switch_to_chronomètre_button.pack(pady=5)

    # Pour toujours afficher les heures:minutes:secondes
    def format_time(self, seconds):
        hrs = seconds // 3600
        mins = (seconds % 3600) // 60
        secs = seconds % 60
        return f"{hrs:02}:{mins:02}:{secs:02}"

    def update_temps(self):
        if self.running:
            self.temps_écoulé += 1
            temps_affiché = self.format_time(self.temps_écoulé)
            self.label_temps.config(text=temps_affiché)
            # Après toutes les 1000 millisecondes (secondes), on relance la même fonction 
            self.root.after(1000, self.update_temps)
    
    def switch_to_minuteur(self):
        self.running = False
        self.temps_écoulé = 0
        self.label_temps.config(text="00:00:00")

    def switch_to_chronomètre(self):
        self.running = False
        self.temps_écoulé = 0
        self.label_temps.config(text="00:00:00")

    def start(self):
        if not self.running:
            self.running = True
            self.update_temps()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.temps_écoulé = 0
        self.label_temps.config(text="00:00:00")

# Lancement de l'application
if __name__ == "__main__":
    root = tk.Tk()
    chronometer = Chronomètre(root)
    root.mainloop()