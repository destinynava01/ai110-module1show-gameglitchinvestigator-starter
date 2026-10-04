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

- [x] Describe the game's purpose.

  Game Glitch Investigator is a Streamlit number-guessing game. The player picks a difficulty (Easy, Normal or Hard), then tries to guess a secret number within a limited number of attempts. After each guess the game gives a Higher/Lower hint and tracks a score and guess history. The starter code was AI-generated and full of bugs, and the goal of this project was to find, fix and test them.

- [x] Detail which bugs you found.

  - **Backwards hints:** guessing a number below the secret told me to go lower, and guessing above told me to go higher (for example, a guess of 26 returned "Go Lower" when it should have said "Go Higher").
  - **New Game did not restart the game:** after winning, pressing New Game reset only the score and secret number. The guess history stayed and new guesses were not accepted, so the page had to be refreshed to play again.
  - **No input range validation:** each difficulty has a range, but guesses outside it (such as 0, negative numbers or numbers over 100) were accepted and still got a hint instead of an error.
  - **Secret number turning into a string:** on some attempts the secret was converted to a string, which broke the comparison logic. The AI also spotted this when it reviewed the file; I had not noticed it myself.

- [x] Explain what fixes you applied.

  - **Hint logic:** moved `check_guess` out of `app.py` into `logic_utils.py` and corrected it so "Too High" returns "Go LOWER!" and "Too Low" returns "Go HIGHER!".
  - **New Game:** the New Game button now resets attempts, the secret number (within the selected difficulty's range), score, status and history, then calls `st.rerun()` to refresh the app so new guesses are accepted.
  - **Testing:** I had Claude write pytest tests for the two bugs I focused on (the hints and the new game reset), plus tests for the difficulty range. I read through what each test checked, ran `pytest`, and then replayed the same scenarios in the browser to confirm the app behaved correctly for a real user.
  - **Approach:** Claude wanted to apply every fix it found in one pass. I rejected that and fixed one bug at a time, so that a change could not break parts of the code that already worked. The range validation and string-secret issues are not fully fixed yet.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Run `python -m streamlit run app.py` and open the app in your browser. Pick a difficulty in the sidebar (Easy, Normal or Hard). The sidebar shows the number range and how many attempts you get.
2. Open the "Developer Debug Info" expander to see the secret number, so you can check the hints are correct.
3. Type a guess below the secret number and click **Submit Guess**. The hint now correctly says "Go HIGHER!". A guess above the secret says "Go LOWER!".
4. Keep guessing until you enter the secret number. The game shows "Correct!" and marks the game as won.
5. Click **New Game**. The attempts, score and guess history reset and a new secret number is picked within the difficulty's range.
6. Enter a new guess and submit it. The game accepts it and tracks it in the fresh history, with no page refresh needed.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
C:\Users\Navad\Downloads\CodePath\AI110\Project\ai110-module1show-gameglitchinvestigator-starter>python -m pytest
================================================= test session starts =================================================
platform win32 -- Python 3.14.7, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\Navad\Downloads\CodePath\AI110\Project\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.15.1
collected 8 items

tests\test_game_logic.py ........                                                                                [100%]

================================================== 8 passed in 1.83s ==================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
