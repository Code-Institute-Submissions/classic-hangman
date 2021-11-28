# Classic Hangman
Hangman is a Python terminal game, which runs in the Code Institue mock terminal on Heroku.

Players try to guess the letters of the hidden word before they ran out of lives.

![responsive.png](documentation/images/responsive.png)

---

## How to play

Classic hangman is very intuitive and fun game. In this game user will easily start a game by just typing first letter. If user guesses a letter thats in the word it will display in terminal on the line, if user doesn't guess a word terminal will show a head of hangman as a first sign of wrong letter guessing. At the end of the game user can choose to play again or not.

---



## UX User Experience

**User Goals**
* As a user i want to have fun with game.
* As a user i want the game to be challenging.

**User Stories**

**As a user, I want the game to be intuitive.**
* The user should be able to understand easy game steps by just typing guessing letters.

**As a user, I want to quickly start the game.**
* The user should be able to see message "Guess ahidden letter or word:" and easily start the game.

**As a user, I would like to be able to choose if i want to play a new game or not.**
* The user should be able to see at the end of game option Play Again? (Y/N).


**Project Goal**

* The main goal of this project is to make minimum design game that will be easy, simple and quick to play for all age groups.
---

## Features

**Existing features**

* Welcome screen
* Accept user inputs

![feature1.png](documentation/images/feature1.png)

* Shows when user didn't guess letter

![feature2.png](documentation/images/feature2.png)

* Shows when user already guessed same letter

![feature3.png](documentation/images/feature3.png)

* Game shows to user new parts of hangman each time user doesn't guess a letter

![feature4.png](documentation/images/feature4.png)

* In case the user lost, game will show actual hidden word, wish user "Good luck next time and it will offer user with option to play game again

![feature5.png](documentation/images/feature5.png)

---

**Future Features**

* Different levels of difficulty
* Add scoring system
* Add option for player name input

---

## Technologies Used

**Languages used**
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

**Programs used**
* [GitHub](https://github.com/) Github was used to store the project.
* [GitPod](https://www.gitpod.io/) GitPod was used for writing code.
* [Heroku](https://www.heroku.com/) Heroku was used to deploy project.
* [PEP8online](http://pep8online.com/) PEP8online Validator was used to check for errors in code.

**Libraries**
* random was used to select a random word.

---
## Testing

* I completed testing of the website page in multiple browsers: Brave, Chrome, Firefox and also used DevTools to confirm that the project is responsive and functional.
* I tested the website on different devices and operating systems Laptop (Windows), Tablet Samsung Galaxy Tab A (Android), and Galaxy Note 20 Ultra 5G (Android). The website worked perfectly on all devices.
* The Website was successfuly tested on [ResponsiveDesign](http://ami.responsivedesign.is/#)

**Validator Testing**

**No errors were returned when passing through the** [W3C HTML Validator](https://validator.w3.org/nu/)

![19html-validator.png](assets/images/19html-validator.png)

**No errors were returned when passing through the** [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

![18css-validator.png](assets/images/18css-validator.png)

**No errors were returned when passing through the** [JSHINT Validator](https://jshint.com/)

![20js-validator.png](assets/images/20js-validator.png)

---

**Lighthouse Reports**

**Lighthouse report for mobile**

![16lighthouse-mobile.png](assets/images/16lighthouse-mobile.png)

**Lighthouse report for desktop**

![17lighthouse-desktop.png](assets/images/17lighthouse-desktop.png)

---

## Unresolved bugs

**Google chrome dev tools shows 1 error in console**

* Error with Permissions-Policy header: Unrecognized feature: 'interest-cohort'.



---
---
## Deployment


**GitHub Pages**

The live deployed site can be viewed here [rock-paper-scissors](https://sirjarvis.github.io/rock-paper-scissors/)

**The site was deployed to Github pages** 
> These are the steps to deploy this project:
* Login to Github and go into repository [SirJarvis/rock-paper-scissors](https://github.com/SirJarvis/rock-paper-scissors)
* Click on settings and scroll down to Pages section on the page
* Under the source heading select the master branch option and click save
* The project has now been deployed and wait for approximate 10 minutes for the link to become active
* Refresh the page and click on the link to view the live site.
**Forking The Github Repository**

> By forking the GitHub repository, we create a clone of the original repository in our Github account. This allows us to make modifications to the files without affecting the original repository.
These are the steps:
* Please sign in to your GitHub account.
* Locate the repository to be duplicated, in this case [SirJarvis/rock-paper-scissors](https://github.com/SirJarvis/rock-paper-scissors).
* Locate and click the “Fork” button at the top of the [SirJarvis/rock-paper-scissors](https://github.com/SirJarvis/rock-paper-scissors) repository page.
* This creates a copy of the repository in our account, allowing us to make modifications.
**Making A Local Clone**

* Please sign in to your GitHub account.
* Locate the desired repository in this case [SirJarvis/rock-paper-scissors](https://github.com/SirJarvis/rock-paper-scissors).
* Locate the “Code” button at the top of the [SirJarvis/rock-paper-scissors](https://github.com/SirJarvis/rock-paper-scissors)   repository page. Click it and copy the HTTPS link that appears.
* Activate your local IDE terminal.
* Change the current working directory to the location where you wish the cloned file to be saved.
* In the terminal, type “git clone” and then paste the link copied from HTTPS.
* e.g "git clone [SirJarvis/rock-paper-scissors](https://github.com/SirJarvis/rock-paper-scissors)
* Clone has been made once you press enter.

---
---
## Credits

**Media**
* The site fonts were taken from [GoogleFonts](https://fonts.google.com/)
* Footer Icons were sourced from [FontAwesome](https://fontawesome.com/)
* Footer Icon colors was sourced from [Materialui](https://materialui.co/)
* Website colors were sourced from [Coolors](https://coolors.co/)
* Main control button icons were sourced from [Icons8](https://icons8.com/)
* Favicon icon was sourced from [Flaticon](https://www.flaticon.com/)


**Content**

**Code**
* [MDN](https://developer.mozilla.org/en-US/), [W3SCHOOLS](https://www.w3schools.com/), [STACKOVERFLOW](https://stackoverflow.com/), [TRAVERSY MEDIA](https://www.youtube.com/channel/UC29ju8bIPH5as8OGnQzwJyA), [FREECODECAMP](https://www.youtube.com/c/Freecodecamp/videos), [PYTHONTUTOR](https://pythontutor.com/visualize.html#mode=edit)
   were all used on daily basis, to better understand and write the code and it's structure.

* This readme document was based on research on several readme documents such as the Code Institute's readme [Sample](https://github.com/Code-Institute-Solutions/SampleREADME).

* I used the lessons learned during the Code Institute "Love Running" project to help with the structure of contact form.

* I used tutorial lesson for creating special hover/color effect on footer icons from [Easy WebCode](https://www.youtube.com/c/EasyWebCode/featured)

* I used tutorial lesson to create Modal from [Traversy Media](https://www.youtube.com/channel/UC29ju8bIPH5as8OGnQzwJyA)



**Acknowledgements**

* My partner, for her time, patience, effort and infinite support.
* My mentor, Chris Quinn, for all valuable sessions, all advices and guidance.
* Code Institute and Slack community for their help and support at any time.