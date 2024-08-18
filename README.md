# Welcome to my 100 day coding challenge !

As I haven't programmed in object oriented in a while, I figured I'd challenge myself to a 100 days of minimum 20min of coding per day in Python!

What is object-oriented programming (OOP)? [Real Python](https://realpython.com/python3-object-oriented-programming/) describes it better, but it is a way of defining code and functions through specific objects. In my case, I want to recreate a fantasy world I grew up with, the Mercedes Thompson series by Patricia Briggs.

## The world of Mercedes Thompson

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

## New notions

pre-commit
What does pre-commit do ? pre-commit aims to improve the qualities of your commits.

Trigger a GitHub action for CI
I added a Github action to automatically lint my python code. I will try to add a github action to see if pre-commit has been run as well.

## Days

Here i keep track of my days just to hold myself accountable!

- day 3 : Added a linting github action and fixed all linting issues (most notably adding \* definition strings)
- day 4 : Played around with the City class. City contain creatures. A city has a move event, add inhabitant when they move in. A creature can belong to a city so it also has an attribute in its own class.
- day 5 cleaned my code a bit and will look into adding unit tests
- day 6 (18/08) started adding pytests!
