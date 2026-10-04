# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

The game looked great visually. It allowed users to choose a difficulty and, for testing purposes, let me see whether it worked. When I ran the first test I guessed a lower number, and the hint told me to go lower. The same happened when I chose a number above the secret number: it told me to go higher. When I picked the correct number it said I won, but when I tried to start a second game, the values had not reset except for the score and the secret number, meaning the history stayed. When I tried to submit a new guess for the new game, nothing happened, as if the program was not accepting any new input.

- List at least two concrete bugs you noticed at the start  

The hints did not match the guess entered. For example, when entering a lower number the hint said to go lower, and vice versa.
The New Game button did not actually restart the game, meaning I had to refresh the page in order to play again.
While each mode of the game has different parameters, it does not throw an error when users input numbers outside of the range, such as negative numbers or numbers over 100.

  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|   0   |Error- out of range|    go lower     |         none           |
|   26  |    Go higher      |    go lower     |         none           |   
|   93  |     Correct!      |    Correct!     |Game doesn't allow reset|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Claude for this assignment, as it is the AI assigned for this course. Since Claude can access my code, it was easier for me to explain what might be wrong and for Claude to pinpoint specific sections of code that might be incorrect. I planned to use it to verify and check the fixes I intended to implement, and to spot sections I may have overlooked.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

When I attempted to fix the higher/lower bug, the AI immediately recognized that the logic was in the wrong .py file. It pointed out every mistake in the file, including some I hadn't noticed, such as the secret sometimes turning into a string. When I asked it to fix the first bug, it explained clearly what changes it made to fix the issue.

- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

The AI originally wanted to change multiple things in the code, mainly because it had noticed a lot more mistakes than I had. While this was somewhat helpful, it wanted to apply all the changes in the first iteration. That approach had the potential to cause a lot more problems, as it might have overcomplicated parts that already worked well or added "fixes" that could break other portions of the code.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I asked the AI to create a pytest and ran it to see if it passed. Afterwards, I ran the app itself to test the error I had been experiencing. Doing this allowed me to check both that the behind-the-scenes logic worked and that the user's view worked.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

For the new game fix, I asked the AI to make a pytest that checks what happens after someone loses. Then I ran the app in my browser and entered the right number (though it was outside the difficulty's range, a bug I didn't choose to fix), and it told me I won, the same as before the fix. When I pressed New Game, it reset the secret number within the correct range for the difficulty, and it tracked my new guesses.


- Did AI help you design or understand any tests? How?

Yes, I allowed the AI to design the pytests for the two bug fixes I focused on. It explained what each pytest was doing and the intended result, and showed how the fix addressed the original bug. It also made tests for checking the range, which was not a bug I originally intended to fix. As a result, when I ran the program I already understood exactly how to test it from the user's side.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns restart the code from the top every time you interact with something on the page, such as clicking a button or changing a text box. Session state is how Streamlit remembers information between reruns. A simple way to remember it: a rerun starts the script over, and session state keeps important information when it does.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

I would like to continue using AI to verify and double-check my work rather than to create everything from scratch. It also helped explain code that was new to me. I also really liked running the AI-written pytests and then testing the fix from the user's end.

- What is one thing you would do differently next time you work with AI on a coding task?

I would be more specific in my prompts, because when I first asked for help it tried to fix every single bug in the code without telling me what it did. Since this entire project is based on AI-generated code, each addition should be reviewed before being accepted as working. I would also leave comments about what needs fixing and why, such as a guess below the secret number should prompt the "go higher" hint.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

While AI can make a program that looks usable on the surface, it still needs human verification to confirm that it works.