# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip3 install -r requirements.txt`
2. Run the broken app: `python3 -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `python3 -m  pytest test/test_game_logic.py -v` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

The purpose of the game is to guess the secret number. Per game, the user gets 8 attempts. There is 3 level of difficuly: one difficult, medium, or easy. Depending on the level of diffculty will determine the range of the secret number. For example, if the difficulty level is set to diffcult, then the secret number can range from 1 to 100 where as easy is 1 to 20. For each guess, the game will provide a hint to assist you with guessing closer to the secret number til correct. 

I focused on 2 specific bugs:
1. Number of Attempts starting from 1 instead of 0
The attempts counter in app.py was set to 1 at the start of each game session. This meant the game behaved as though the player had already used one attempt before making any guess. The counter was off by one from the very beginning. I fixed this by changing the initial value to 0, so the counter only increments after the player actually submits a guess.

2. Incorrect Hints
When testing the game, I noticed the hints were backwards. For example, guessing 1 when the secret was 59 showed a "Lower" hint, and guessing 89 when the secret was 86 showed a "Higher" hint. The logic for returning outcomes was inverted. I fixed this by correcting the comparison logic in check_guess inside logic_utils.py so that guess > secret correctly returns "Too High" with a "go lower" message, and guess < secret correctly returns "Too Low" with a "go higher" message.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Set your difficulty level by choosing between easy, normal, hard
2. Once the difficulty level is set, you have 8 attempts to guess the secret number
3. Enter a guess in the text field and click "Submit Guess." The game will provide a hint for every guess you enter. 
4. Submit a guess until all attempts have run out.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->
## 🧪 Test Results

```
test/test_game_logic.py::test_winning_guess PASSED                                                                                                                                    [ 14%]
test/test_game_logic.py::test_guess_too_high PASSED                                                                                                                                   [ 28%]
test/test_game_logic.py::test_guess_too_low PASSED                                                                                                                                    [ 42%]
test/test_game_logic.py::test_check_guess_win_with_string_secret PASSED                                                                                                               [ 57%]
test/test_game_logic.py::test_check_guess_too_high_with_string_secret PASSED                                                                                                          [ 71%]
test/test_game_logic.py::test_check_guess_too_low_with_string_secret PASSED                                                                                                           [ 85%]
test/test_game_logic.py::test_attempts_initial_value_is_zero PASSED                                                                                                                   [100%]
===================================================================================== 7 passed in 0.01s =====================================================================================
```
