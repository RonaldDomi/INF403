Database simulator with Python/SQL on the command line.

To execute the program, run 'py main.py' or 'python3 main.py' 
depending if you're using windows or linux.


# Folder description
The UML part of the project is described on /Modelization.docx

Inside the /db folder we can find different sql files, which are the 
files used to create our database with correct data.

Inside /utils there is the main code, which will be described bellow.
This code is the implementation of how we would interact with our database.

Inside /model there is the UML formalization docx and the image of the automata

# Program 

Once the main program is launched, the user is asked to enter a command. 
The list of commands the user can enter is predefined and it follows strictly 
the automata. 

While executing the program, we can see the different operation which we can 
do to communicate with the database. At every point we can check if the db is
updated correctly.



![Image of automaton used on this project](/model/automaton.jpg "Automaton")