# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

> When I first started I noticed that the hints were incorrectly and unreliabily suggesting the player to guess higher or lower, according to the secret number. Another bug is that the warning "Out of attempts!" popped out when there is one more attempt left. There is a minor bug on the side bar on the number of attempts allowed, where the number is one value bigger than the number of attempts proposed on the main page. A major bug with the secret number is that it may not fall within the range of the difficulty level mentioned in the settings side bar. After we fail to guess a secret number and go over the threshold of attempts, the warning "Game over. Start a new game to try again" remains on screen even if we click 'New Game'. New attempts are not allowed nor accepted, the game fails to rerun. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

> I used Claude Code as my debug partner for this project. One of the issues I used Claude to solve was the inaccurate hints issue. Claude pointed two different parts of the code that were causing the issue: one portion was in the 'check_guess' function and the other was in the 'if submit:' logic. It concluded that there were two independently problems causing the wrong hints: 1) hints were reversed in comparing guess and secret nums; 2) on even tries, the logic was comparing int vs. str, causing TypeError, leading us into the except block where we are comparing the nums as str, making inaccurate comparisons. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

> I decided a bug is really fixed if it performs the behavior as expected through manual testing and assertion test cases (with possible edge cases). For example, when I was fixing the bug with incorrect hint according to the secret number, after I made my first fix, I went for the manual test by playing several games to see if the logic is fixed. I noticed, however, there were still times when the hints are wrong. Therefore, I used AI to run through the logic, and it pointed out the fact that the numbers are being compared as strings, also what is causing the inconsistent hints. After the second fix, I asked Claude to generate the pytest for this feature. 
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

> The secret number changes when new games are started because we call for the change in secret number, with the number range based on game difficulty. Streamlit is the tool used to build functioning web pages with just Python. The way Streamlit works is that every time a button is clicked, the entire script gets reruned. Therefore, if we want to keep data from a previous run, we need something called, 'session state'. There was this one line that starts the game by setting the secret number, randint(1,100), ignoring the game difficulty. The change made was to set it to 'randint(low, high)' to match the game difficulty, as we already have a function returning the range for secret number.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

>  One habit I want to reuse from this project is to, first, explore the files and use AI to understand the structure of the project, and then, if debugging, use AI to pinpoint the sections of code that may be causing the error. With this, I can quickly focus on exploring solutions to fix the issue. As for prompting technique, something I would keep in mind is to be specific in what I want to accomplish and be detailed to ensure the response is as intended. One thing I would do differently next time is to read/understand more carefully of the solutions AI provides, so that I fully understand how the issue is resolved with the solution provided and whether there can be a better solution. Overall, I think AI can provide good templates of projects but they need manual refinements to match the requirements we have designed.