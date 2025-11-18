import random
import tkinter as tk

root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("300x200")

random_number = random.randint(1, 10)
attempts = 0  
max_attempts = 3

# Function to check the guess
def check_guess():
    global attempts
    guess = int(guess_entry.get())
    attempts += 1
    if guess == random_number:
        result.set("Congratulations! You guessed it right.")
    elif attempts >= max_attempts:
        result.set(f"Sorry, you've used all attempts. The number was {random_number}.")
    elif guess < random_number:
        result.set("Try a higher number.")
    else:
        result.set("Try a lower number.")

# Function to reset the game
def reset_game():
    global random_number, attempts
    random_number = random.randint(1, 10)  
    attempts = 0                          
    result.set("")                       
    guess_entry.delete(0, tk.END)   
# GUI Components
instruction = tk.Label(root, text="Guess a number between 1 and 10:")
instruction.pack(pady=10)

guess_entry = tk.Entry(root)
guess_entry.pack(pady=5)

submit_button = tk.Button(root, text="Submit Guess", command=check_guess,bg="green", fg="white")
submit_button.pack(pady=5)

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.pack(pady=10)
reset_button = tk.Button(root, text="Reset Game", command=reset_game,bg="gray", fg="white")
reset_button.pack(pady=15)

root.mainloop()
