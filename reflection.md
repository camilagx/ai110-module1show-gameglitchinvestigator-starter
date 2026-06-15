# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

When I first ran the game, I noticed a few issues with how it was working. Sometimes the user’s attempts were not being tracked or recorded in the attempt history. I also found that pressing Enter did not submit a guess as expected, so users had to click the “Submit Guess” button instead. Even then, attempts were not always counted correctly. In addition, the score displayed on the scoreboard did not always match the final score shown when the game was completed, which made the results inconsistent.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess of "9" | The number 9 should be logged in the attempt history. | The number 9 is not logged, and the program waits for another number to be entered. | None |
| Guess of 1 | The secret number is 59. I expect the hint to tell me to guess higher. | The hint incorrectly says "Lower." | None |
| Guess of 89 | The secret number is 86. I expect the hint to tell me to guess lower. | The hint incorrectly says "Higher." | None |
| Guess of 100 on "Easy" level | The guess is outside the valid range and should be rejected. | The game tells me to guess lower. | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude Code to walk me thru different code blocks as well as identify logical errors.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

Claude Code identified that "st.session_state.attempts" was being initialized to "1" instead of "0", which caused the game to behave as though one attempt had already been used before the player made any guess. I applied the fix by changing the initial value to "0" in app.py/ To verify it, I ran the game, started a new session, and confirmed that the attempts counter correctly began at 0 and only incremented after I submitted my first guess.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I did not encounter an issue where the AI provided an incorrect suggestion. Instead, the issue was that it performed a task incorrectly. I asked the AI to create a test file and place it in "test/test_game_logic.py". However, it created the file in a directory named "tests" (with an "s") instead of the directory I specified.

I then told Claude that I specifically asked it to be create a directory name "test." Later, when I asked the AI how to run the test file, it provided the command "python3 -m pytest tests/test_game_logic.py -v", which referenced the "tests" directory again. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---
Before allowing Claude to apply the changes, I read the code line by line. After feeling confident that the bug was fixed in the new code, I ran the program and tested the game by entering guesses to ensure it was returning the correct hint and also correctly starting a new game with attempts set to zero.

AI generated 7 tests for me and i used the command "python3 -m  pytest test/test_game_logic.py -v" to run all tests which all PASSED. One tests it created checks if the correct string is returned when a guess is higher than the secret number. After running the test, this is what's outputted in the terminal:
test/test_game_logic.py::test_check_guess_win_with_string_secret PASSED


## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

“Reruns” in Streamlit basically explain how a Streamlit app runs. Every time a user interacts with the UI, Streamlit executes the entire Python script from top to bottom. Because of this, variables don’t behave the same way they do in a normal Python program. For example, if you have a counter variable, it will reset back to its original value every time the app reruns unless you store it in st.session_state.


## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  One strategy I want to reuse in future labs or projects is writing comments about the code I want the AI to debug. It helps me focus on debugging the problem myself first and spotting logical errors before fully relying on AI to fix everything for me. This also makes it easier to clearly explain the issue when I do ask for help, since I’ve already thought through what the code is supposed to be doing.

- What is one thing you would do differently next time you work with AI on a coding task?

One thing I would do differently next time I work with AI on a coding task is to provide more specific guidance, such as the expected output and any edge cases to watch out for when debugging. AI is only as good as the prompts you give it, so if you’re not clear about the specs or requirements, it can sometimes go beyond what you asked for—sometimes in a good way, sometimes not. It can also start to feel a bit out of control if you don’t set clear boundaries. For example, in one prompt, I moved the check_guess function out of app.py into logic_utils.py, and then a couple prompts later, I noticed that Claude had kept the check_guess function in logic_utils.py, but its logic had somehow ended up back in app.py.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

This project changed the way I think about AI-generated code by showing me that there is still a real need for software engineers. Even though AI can do a lot of the heavy lifting, we can’t fully trust everything it produces without checking it carefully. I found that I still had to read through the code, test it, and make sure the logic actually made sense, because AI can sometimes introduce subtle bugs or structure things in a confusing way. 