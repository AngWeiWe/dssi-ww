import streamlit as st
import random

# Function to generate a random 4-digit code
def generate_code():
    return [random.randint(0, 9) for _ in range(4)]

# Function to check the guess against the code
def check_guess(code, guess):
    a_count = 0
    b_count = 0
    guess_checked = [False] * 4
    code_checked = [False] * 4

    # First pass: check for correct position (A)
    for i in range(4):
        if guess[i] == code[i]:
            a_count += 1
            guess_checked[i] = True
            code_checked[i] = True

    # Second pass: check for correct number in wrong position (B)
    for i in range(4):
        if not guess_checked[i]:
            for j in range(4):
                if not code_checked[j] and guess[i] == code[j]:
                    b_count += 1
                    code_checked[j] = True
                    break

    return a_count, b_count

# Initialize game state
if 'code' not in st.session_state:
    st.session_state.code = generate_code()
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# Game Title
st.title("Crack the Code Game")

# Game Instructions
st.write("I have generated a random 4-digit code. Try to guess it!")
st.write("For each guess, you'll receive feedback:")
st.write("- `A` for each digit that is correct and in the correct position.")
st.write("- `B` for each digit that is correct but in the wrong position.")

# User Input
guess = st.text_input("Enter your 4-digit guess:")

# Check Guess
if st.button("Submit Guess"):
    if len(guess) == 4 and guess.isdigit():
        guess = [int(digit) for digit in guess]
        st.session_state.attempts += 1
        a_count, b_count = check_guess(st.session_state.code, guess)
        st.write(f"Guess {st.session_state.attempts}: {''.join(map(str, guess))} - {a_count}A{b_count}B")
        if a_count == 4:
            st.write(f"Congratulations! You've cracked the code in {st.session_state.attempts} attempts!")
            st.session_state.game_over = True
    else:
        st.write("Please enter a valid 4-digit number.")

# Restart Game
if st.session_state.game_over and st.button("Play Again"):
    st.session_state.code = generate_code()
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.experimental_rerun()
