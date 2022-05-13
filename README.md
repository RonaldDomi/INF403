Database simulator with Python/SQL on the command line.

To execute the program, run 'py main.py' or 'python3 main.py' 
depending if you're using windows or linux.


# Folder description
The UML part of the project is described on /doc/Project403.docx

Inside the /data folder we can find different sql files, which are the 
files used to create our database, with correct or incorrect data.

Inside /utils there is the main code, which will be described bellow.
This code is the implementation of how we would interact with our database.

# Main Program
The best way to showcase the project is an actuall example:
once you exeute the program                                                   **'py main.py'**
there is an introduction paragraph.

Directly the program asks what is our next command so we hit                  **'help'**
the program responds with a list of commands which we could enter

Description is what the database has inside its cover, its UML

Information contains all the data in our database, so we try it out.         **'-i'**
We need to be more specific though, so we decide we want to see our auteurs  **'autuers'**
Likewise, we could see our 4 tables of our database directly into

We don't know what to do in this situation, and we think that we need         **'help'**
In this state of the program, 'help' is not a recognized command. The 
kind program responds always with the acceptable commands in every 
state of the program, so we could never get lost. Lets go back                **'main'**

Attention not to 'quit', or the program will stop at any point. Attention!

Let's see how our autheurs are doing, we will connect with a predefined author  **'connect 201'**
We get the authors name and his id. The list of commands is 
'history, sell, remove and stat'

WE will try them one by one.  **'history'** will give us the works 'oeuvres' created by our autheur.
**'sell'** is when we want to add a new work on the name of this author. Putting it on sale.
It will ask us for some details, and afterwards we could see that our work has been created.
Carefull to enter your primary key unique. I suggest 311, 312 ...
To check wee need to go back to **"main"** and then **"-i"** and finaly **"oeuvres"**.

If in the insert we don't put a correct PK, than the program will just crash, which we don't want :(
In fact the error handeling isn't implemented, being outside the scope and time budget. 

If we return to our **'main' -> 'connect 201'** we can now try to remove his works from the sale.
**'remove' 303'** Will remove one of his works and we can verify with **'--hist'**.

Finaly with our author we could check our complex sql request. **'stat'**
This shows how much we have earned from selling different kinds of audios.


To look at how our clients are doing, we go back and deconect with **"main"** and reconnect 
with a client id: **'connect 101"**. Similarly here we have our bought works with **--hist**
and we can add new ones with **shop 308**. After buying we can double check our history.


# Final Words
There are some unimplemented functionalities but nonetheless the template is a pretty stable template.
It is really scalable and easy to menage, to add and remove transitions and states. There are 
INSERTS, DELETE FROM, SELECT *, GROUP BY, JOIN and all the basic functionalities. All the missing options 
are optimisations which are duplicate functionalities of those already implemented. 