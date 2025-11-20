from tkinter import *
import random

def play(player_choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    if player_choice == computer_choice:
        result = "It's a Tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or (player_choice == "Paper" and computer_choice == "Rock") or (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "You Lose!"
    result_label.config(text=f"You: {player_choice}\nComputer: {computer_choice}\n\n{result}")

window = Tk()
window.title('Rock Paper Scissors')
window.geometry('300x300')

Label(window, text="Choose your move:", font=("Arial", 14)).pack(pady=10)

button1 = Button(text="Rock", width=12, command=lambda: play("Rock"))
button2 = Button(text="Paper", width=12, command=lambda: play("Paper"))
button3 = Button(text="Scissors", width=12, command=lambda: play("Scissors"))

button1.pack(pady=5)
button2.pack(pady=5)
button3.pack(pady=5)

result_label = Label(window, text="", font=("Arial", 12))
result_label.pack(pady=20)

window.mainloop()
