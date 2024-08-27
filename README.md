# Welcome to my 100 day coding challenge !

As I haven't programmed in object oriented in a while, I figured I'd challenge myself to a 100 days of a minimum 20min of coding per day in Python!

What is object-oriented programming (OOP)? [Real Python](https://realpython.com/python3-object-oriented-programming/) describes it better, but it is a way of defining code and functions through specific objects. In my case, I want to recreate a fantasy world I grew up with, the Mercedes Thompson series by Patricia Briggs.

## The world of Mercedes Thompson

My mom and I have been reading the Mercedes Thompson books forever (I think I was 13 when we started!). You can find all of the books here : https://www.goodreads.com/series/40932-mercy-thompson

Mercedes Thompson is a mechanic who lives in the Tri State area. She also happens to be a shapeshifter who can turn into a coyote. In her reparation shop, she works with Zee, a grumpy but very powerful old fae. Her nextdoor neighbour is Adam Hauptman, the leader of the werewolf pack.

## Python things I cover in my code

- classes
- classes inheritances
- pre-commit
- the **init**, repr functions
- properties and static functions
- dictionaries
- property functions (defining a setting the user can't modify)
- pre-commit
- linting
- pytest : pytest is designed to automatically discover and run tests based on a few conventions. By default, pytest looks for files that match the pattern test\*_.py or _\_test.py. Within the test files, pytest looks for functions that start with test*. For example, test*correctness_of_attributes\* is a valid test function name.
- data classes : A data class is a class typically containing mainly data, although there aren’t really any restrictions. It is created using the new @dataclass decorator. Here the class Power is a dataclass

## New notions

### pre-commit
pre-commit is a framework that automates code checks and formatting before commits, ensuring consistency and quality across a project. It uses git hooks to run tools like linters, formatters, and security scanners automatically. Configured via a .pre-commit-config.yaml file, it standardizes coding practices by enforcing rules across all contributors. If any checks fail, the commit is blocked until issues are fixed. This helps catch errors early and maintain a clean, consistent codebase.

Trigger a GitHub action for CI
I added a Github action to automatically lint my python code. I will try to add a github action to see if pre-commit has been run as well.

### data classes

Data classes in Python are a concise way to create classes primarily used for storing data with minimal boilerplate code. Introduced in Python 3.7 via the @dataclass decorator, they automatically generate special methods like __init__, __repr__, and __eq__ based on class attributes. Data classes make it easy to define immutable or mutable objects with default values and type annotations. They are ideal for modeling simple data structures without needing to manually write standard methods. This leads to cleaner, more readable, and maintainable code.

## Days

Here i keep track of my days just to hold myself accountable!


| Day   | Notion |
| ------- | --- |
| 3 | Added a linting github action and fixed all linting issues (most notably adding \* definition strings) |
| 4 | Played around with the City class. City contain creatures. A city has a move event, add inhabitant when they move in. A creature can belong to a city so it also has an attribute in its own class.  |
| 5 | cleaned my code a bit and will look into adding unit tests  |
| 6 | started adding pytests and added a Docker container |
| 7 | added the pytest in the github CI, added a pet which is a NamedTuple for shapeshifters |
| 8 | added click functions to create characters from the terminal :)  |
| 9 | added the test werewolf  |
| 10 | fixed the linting, added the cli function in another script, fixed the Werewolf pytest  |
| 11 | Added the function read_letter |
| 12 | Added a function move in Creature, updating the City attribute  |
| 13 | Added the class Vampire accompanied with a data class Power  |
