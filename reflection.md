# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game looks like a normal number guessing game.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. When entering the same guess, the hint jumps from go lower to go higher occasioanlly
  2. If I've used all the attempts, it doesn't let me start a new game

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Secret was 42, I typed 42 on my 2nd guess | I should win | It told me to go higher/lower and never let me win | Checked the terminal and saw `TypeError: '>' not supported between instances of 'int' and 'str'`. Turns out it turns the secret into a string on even guesses |
| Clicked "New Game" after losing | Game restarts so I can play again | Nothing happened, still stuck on the game over screen | No error, it just wouldn't reset |
| Typed "abc" instead of a number | Should warn me and not count it | Showed an error but still used up one of my attempts | No error |
| Picked Hard difficulty | Hard should be harder than Normal | Range was only 1–50, but Normal goes up to 100, so Hard was actually easier | No error |
| Picked Easy difficulty | Prompt should say the range is 1–20 | It still said "between 1 and 100" | No error |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI claimed all three README symptoms — "you can't win," "the hints lie," and "the secret keeps changing" — were really caused by one line, secret = str(...), that ran only on even-numbered attempts. It explained that casting the secret to a string made guess == secret always false (so winning was impossible) and made guess > secret throw a TypeError that the code silently caught. I verified this two ways: first I opened the Developer Debug Info panel and saw the secret number was not actually changing, which contradicted my original assumption; then I deleted that line and played several rounds, winning on both even and odd attempts. Running pytest afterward showed all 3 tests passing, which confirmed the fix didn't break the comparison logic.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
When refactoring, the obvious AI move was to copy check_guess from app.py into logic_utils.py exactly as written. But that version returned a tuple (outcome, message), while the tests call check_guess(50, 50) and expect just the string "Win". I caught this by reading the test file before refactoring, then ran pytest to confirm — the function had to return a single string, so blindly trusting the "just move it" suggestion would have failed all 3 tests.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
Test and review it myself!
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I tested manually by testing out different cases in the game. It showed that with the help of AI, my code has become flawless!
- Did AI help you design or understand any tests? How?
Yes, I also asked AI to help me generate some test cases.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit re-runs the entire script on every click or keystroke (a "rerun"), which resets normal variables, so we use st.session_state as a memory box that survives reruns to keep values like the secret number and score from being lost between interactions.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
I think the ability to use AI to generate test cases
- What is one thing you would do differently next time you work with AI on a coding task?
try another model, not Claude
- In one or two sentences, describe how this project changed the way you think about AI generated code.
It's pretty neat!
