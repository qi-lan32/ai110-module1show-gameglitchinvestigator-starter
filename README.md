# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- The purpose of this game is to explore debugging with the help of AI, experiment and understand the reliability of AI in providing solutions and tips in debugging, and learn how we can utilize this tool to help us with debug.
- Most of the bugs found were logical bugs in the game: inaccurate hints according to secret number, out of attempts warning message showing beforehand, secret number is out of range from game difficulty, or new game button fail to refresh.
- The fixes were mainly correctly the structure of the if-conditions checks (for inaccurate hints), wrong initial value, wrong variable assignment (out of range secret number), and missing line to reset the game status (new game fail to refresh).

## 📸 Demo

-  [![alt text](image.png)]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
