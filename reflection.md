# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

Sometimes user attempts are not tracked or recorded in the attempt history. Additionally, pressing Enter does not submit a guess as expected. Users must click the "Submit Guess" button, but even then, attempts are not always counted correctly.

I also noticed that the score displayed on the scoreboard does not accurately match the final score shown when the game is completed.

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
Claude Code


- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).


- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).



---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
