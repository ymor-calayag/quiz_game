# Quiz Game

This project is a simple quiz application built using object-oriented programming principles. Questions are loaded from a data source, presented one at a time, and evaluated based on the user’s input. The game provides immediate feedback and keeps track of the player’s score throughout the session.

**Technologies Used**

+ ```Python```
+ Object-Oriented Programming (OOP)
+ Classes and methods

**Features**

+ True/False question format
+ Score tracking across multiple questions
+ Immediate feedback after each answer
+ Final score summary at the end of the quiz
+ Clean separation of logic using classes

**What Users Can Do**

+ Answer a series of True/False questions
+ Receive instant feedback on each answer
+ Track their current score during gameplay
+ View their final score after completing the quiz

**The Process / How It’s Built**

+ Question data is stored in a separate file as a list of dictionaries.
+ Each question is converted into a Question object.
+ The ```QuizBrain``` class manages quiz flow, scoring, and question progression.
+ The main program initializes the quiz and loops through questions until finished.
+ Results are displayed when no questions remain.
