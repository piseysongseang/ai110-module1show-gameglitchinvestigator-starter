# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  - The game looks perfect at first because I try to win in first attempt but then I noticed I couldn't start new game. I need to refresh the page to start new game which should be done by just clicking new game button. So, I found out that the button doesn't work.
- List at least two concrete bugs you noticed at the start
  (for example: "the secret number kept changing" or "the hints were backwards").
  - The hints were backwards: when I go low, it told me to go lower and vice versa.
  - The new game button doesn't work.
  - The attempt left count doesn't match the attempt that describe under the settings difficulty level. And when I finish my first attempt, it doesn't change until the next attempt.
  - Enter to apply/submit answer doesn't work.
  - When choosing other level of difficult(Hard and Easy), after two attempts of guessing, it gliches back to Normal level.
  - The score doesn't add up right.
  - When choosing other level of difficulty, the text under changes but doesn't match up with the instruction over the guessing box which confuses the players.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - I asked AI what's wrong with the game logic. And it gave me several issues that I've found.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - Testing using pytest and all the tests are passed.
- Describe at least one test you ran (manual or using pytest)and what it showed you about your code.
  - The code logics are wrong for example, the hints are backward. Therefore, I need to fix it by promting and verify Copilot's code.
- Did AI help you design or understand any tests? How?
  - Yes. It recommended me using pytest and it also did pytest on its own and recommended some solutions and explained what it did to fix the problems.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
