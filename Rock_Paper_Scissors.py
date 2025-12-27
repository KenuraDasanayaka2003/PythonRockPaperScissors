import tkinter as tk #for GUI
import random        #for selecting the choice randomly by computer

#------------------------GUI----------------------------------------
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("400x400")

title = tk.Label(window, text="Rock Paper Scissors", font=("Arial",16))
title.pack(pady=10)

score_label = tk.Label(window, text=" User : 0 | Computer : 0 ", font=("Arial",12))
score_label.pack(pady=5)

computer_label = tk.Label(window, text=" Computer chose - ", font=("Arial",12) )
computer_label.pack(pady=5)

user_label = tk.Label(window, text=" User chose - ", font=("Arial",12) )
user_label.pack(pady=5)

result_label = tk.Label(window, text="Click START to play!" , font=("Arial",12) )
result_label.pack(pady=5)

#------------------------Game Variables-----------------------------------
choices = ['Rock', 'Paper', 'Scissors'] #Store possible choices for the computer
user_score = 0  #initializing the user score as 0
computer_score = 0 #initializing the computer score as 0
game_running = False

#------------------------Game Logic------------------------------------------
def start_game():
    global game_running
    game_running = True
    result_label.config(text="Game Started! Make your move")

def stop_game():
    global game_running, user_score, computer_score
    game_running = False
    user_score =0
    computer_score =0

    score_label.config(text="User: 0 | Computer: 0")
    computer_label.config(text="Computer chose: -")
    user_label.config(text="User chose: -")
    result_label.config(text="Game Stopped. Scores Reset.")

rng = random.SystemRandom()
def play(user_choice):
    global user_score, computer_score

    if not game_running:
        result_label.config(text="Click START to play again")
        return

    computer_choice = rng.choice(choices)
    computer_label.config(text=f"Computer chose : {computer_choice}")
    user_label.config(text=f"User chose : {user_choice}")

    if user_choice == computer_choice:
        result = "It is a draw"

    elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Paper" and computer_choice == "Rock") or
            (user_choice == "Scissors" and computer_choice == "Paper")):
        user_score += 1
        result = "You win!"

    else:
        computer_score += 1
        result = "Computer wins!"

    score_label.config(text=f"User : {user_score} | Computer : {computer_score}")
    result_label.config(text=result)

#-----------------------------Buttons--------------------------------------
btn_frame = tk.Frame(window)
btn_frame.pack(pady=10)

control_frame = tk.Frame(window)
control_frame.pack(pady=20)

tk.Button(btn_frame, text="Rock" ,width=10 , command=lambda:play("Rock")).grid(row=0, column=0,padx=10)
tk.Button(btn_frame, text="Paper",width=10 , command=lambda:play("Paper")).grid(row=0, column=1,padx=10)
tk.Button(btn_frame, text="Scissors", width=10 , command=lambda:play("Scissors")).grid(row=0, column=2,padx=10)

tk.Button(control_frame, text="START", width=10, bg="green", fg="white", command=start_game).grid(row=0, column=0, padx=10)
tk.Button(control_frame, text="STOP", width=10, bg="red", fg="white", command=stop_game).grid(row=0, column=1, padx=10)

window.mainloop()


