# CoffeeMachine
A Coffee Machine which can serve parallely using multithreading.

# Assumptions
* The input JSON will not have duplicate beverage names. (Workaround would be to use custom deserialiser. 
    Considering this out of scope for now.)
* The input JSON contains correct input.

# Algorithm
* A multithreaded system with n threads is started which represent n outlet coffee machine.
* It tries to create all the beverages. Preference served to represent multithreaded system and to ensure two drinks do not use same ingredient.
* Extra Feature include - API for new ingredient addition in our stock, and API for adding new Beverage Requests at any given point of time.
* Used singleton class to simulate a Coffee Machine

# Steps to run
* Run the ```run.py``` script for dry run of the system.
* Change the input file name in ```run.py``` file to run for different test data. 
* All input files are in ```coffee_machine/assets```