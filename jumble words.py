import tkinter as tk
from tkinter import messagebox
import random

def add_user_words():
    add_words_label.pack(pady=10)
    add_words_entry.pack()
    add_words_submit_button.pack(pady=5)

def submit_words():
    words = add_words_entry.get().split(',')
    words = [word.strip().upper() for word in words]
    if len(words) > 10:
        messagebox.showwarning("Warning", "Please enter a maximum of 10 words.")
        return
    global user_words
    user_words = words
    messagebox.showinfo("Success", "Words added successfully.")
    start_game_with_user_words()

def start_game_with_default_words():
    global user_words
    user_words = []
    start_game()

def start_game_with_user_words():
    add_words_label.pack_forget()
    add_words_entry.pack_forget()
    add_words_submit_button.pack_forget()
    start_game()

def start_game():
    global user_words
    global shuffled_words
    if user_words:
        words = user_words
    else:
        words = default_words
    random.shuffle(words)
    shuffled_words = words.copy()
    global current_word_index
    current_word_index = 0
    global score
    score = 0
    display_word(current_word_index, shuffled_words, score)

    # Show guess entry and check button
    user_guess_entry.pack()
    check_button.pack(pady=5)
    final_score_label.pack_forget()
    play_again_button.pack_forget()

def display_word(current_word_index, shuffled_words, score):
    current_word = shuffled_words[current_word_index]
    jumbled_word = ''.join(random.sample(current_word, len(current_word)))
    jumbled_word_label.config(text=jumbled_word)

def check_answer():
    global current_word_index
    global score
    global shuffled_words
    user_guess = user_guess_entry.get().upper()
    if user_guess == shuffled_words[current_word_index]:
        score += 1
        show_message("Correct guess!")
    else:
        show_message("Incorrect guess. Try again.")

    current_word_index += 1

    if current_word_index < len(shuffled_words):
        display_word(current_word_index, shuffled_words, score)
        update_score()
        user_guess_entry.delete(0, tk.END)  # Clear the input bar
    else:
        show_final_score_with_remarks()
        if score > highest_score:
            highest_score = score
        update_highest_score()
        show_end_ui()

def show_message(message):
    messagebox.showinfo("Message", message)

def update_score():
    score_label.config(text=f"Score: {score}")

def update_highest_score():
    highest_score_label.config(text=f"Highest Score: {highest_score}")

def show_end_ui():
    user_guess_entry.pack_forget()
    check_button.pack_forget()
    final_score_label.pack()
    play_again_button.pack()

def show_final_score_with_remarks():
    global score
    global highest_score
    if score >= 8:
        remarks = "Excellent!"
    elif score >= 5:
        remarks = "Good job!"
    elif score >= 3:
        remarks = "Not bad!"
    else:
        remarks = "Better luck next time!"

    final_score_label.config(text=f"Your total score: {score}\nRemarks: {remarks}")
    messagebox.showinfo("Game Over", f"Your total score: {score}\nRemarks: {remarks}")

def play_again():
    final_score_label.pack_forget()
    play_again_button.pack_forget()
    options_label.pack()
    default_words_button.pack()
    user_words_button.pack()

root = tk.Tk()
root.title("Word Jumble Game")
root.geometry("400x400")

# Define colors
background_color = "#87CEEB"  # Sky Blue
label_color = "#333333"  # Dark Gray
button_color = "#FFB6C1"  # Light Pink
entry_color = "#FFFFFF"  # White
text_color = "#000000"  # Black

# Default words
default_words = ["PYTHON", "COMPUTER", "GAMES", "PROGRAMMING", "ALGORITHM", "DEVELOPMENT", "DATA", "SCIENCE", "ARTIFICIAL", "INTELLIGENCE"]
user_words = []
shuffled_words = []

# UI components
options_label = tk.Label(root, text="Choose an option to start the game:", fg=label_color, bg=background_color)
options_label.pack(pady=10)

default_words_button = tk.Button(root, text="Play with Default Words", command=start_game_with_default_words, bg=button_color, fg=text_color)
default_words_button.pack(pady=5)

user_words_button = tk.Button(root, text="Play with Your Words", command=add_user_words, bg=button_color, fg=text_color)
user_words_button.pack(pady=5)

add_words_label = tk.Label(root, text="Enter your words (comma-separated, 10 words maximum):", fg=label_color, bg=background_color)
add_words_entry = tk.Entry(root, bg=entry_color)

add_words_submit_button = tk.Button(root, text="Submit Words", command=submit_words, bg=button_color, fg=text_color)

jumbled_word_label = tk.Label(root, text="", fg=label_color, bg=background_color)
jumbled_word_label.pack(pady=10)

user_guess_entry = tk.Entry(root, bg=entry_color)
check_button = tk.Button(root, text="Check", command=check_answer, bg=button_color, fg=text_color)

score_label = tk.Label(root, text="Score: 0", fg=label_color, bg=background_color)
score_label.pack(pady=5)

highest_score_label = tk.Label(root, text="Highest Score: 0", fg=label_color, bg=background_color)
highest_score_label.pack(pady=5)

final_score_label = tk.Label(root, text="", fg=label_color, bg=background_color)
final_score_label.pack(pady=10)
final_score_label.pack_forget()  # Hide initially

play_again_button = tk.Button(root, text="Play Again", command=play_again, bg=button_color, fg=text_color)
play_again_button.pack(pady=5)
play_again_button.pack_forget()  # Hide initially

root.config(bg=background_color)

root.mainloop()
