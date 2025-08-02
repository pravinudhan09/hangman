import streamlit as st
import random


words = ['apple', 'tiger', 'plane', 'snake', 'grape', 'pavan', 'pravin']

if 'word' not in st.session_state:
    st.session_state.word = random.choice(words)
    st.session_state.guessed = ['_'] * len(st.session_state.word)
    st.session_state.attempts_left = 6
    st.session_state.guessed_letters = []


st.title("🕹️ Hangman Game")


st.write("Word: ", ' '.join(st.session_state.guessed))


guess = st.text_input("Enter a letter:", max_chars=1).lower()

if st.button("Guess"):
    if guess and guess.isalpha() and guess not in st.session_state.guessed_letters:
        st.session_state.guessed_letters.append(guess)
        if guess in st.session_state.word:
            for idx, char in enumerate(st.session_state.word):
                if char == guess:
                    st.session_state.guessed[idx] = guess
        else:
            st.session_state.attempts_left -= 1

st.write(f"Attempts Left: {st.session_state.attempts_left}")
st.write("Guessed Letters: ", ', '.join(st.session_state.guessed_letters))


if '_' not in st.session_state.guessed:
    st.success("🎉 You won!")
elif st.session_state.attempts_left == 0:
    st.error(f"💀 Game Over! The word was: {st.session_state.word}")


if st.button("Restart Game"):
    st.session_state.word = random.choice(words)
    st.session_state.guessed = ['_'] * len(st.session_state.word)
    st.session_state.attempts_left = 6
    st.session_state.guessed_letters = []

