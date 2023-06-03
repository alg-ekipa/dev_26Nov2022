#make python program which simulates access control with bell button on gui with nice bell picture and bell sound, and access button which trigers another window where keyboard with pin buttons (0-9) input via gui appears and grants access for diferent people and one admin which has pin code 1234 and is able to add, delete and modifiy existing users via another window which opens if pin 1234 is entered


import tkinter as tk
import pygame

class DoorbellSimulator:
    def __init__(self):
        # Initialize pygame mixer
        pygame.mixer.init()

        # Create the main window
        self.root = tk.Tk()
        self.root.title("Doorbell Simulator")
        self.root.geometry("200x100")

        # Doorbell button
        doorbell_button = tk.Button(self.root, text="Ring Doorbell", command=self.ring_doorbell)
        doorbell_button.pack()

    def ring_doorbell(self):
        # Play the doorbell sound
        pygame.mixer.music.load("doorbell_sound.wav")
        pygame.mixer.music.play()

    def run(self):
        # Start the GUI main loop
        self.root.mainloop()


# Run the doorbell simulator
doorbell_simulator = DoorbellSimulator()
doorbell_simulator.run()



