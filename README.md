# Botlzmann Wealth Model #

## Project Description ##
I made this little project to practice simulation tools with Mesa - Python's agent-based modeling and simulation library.

## Project Details ##
As you'll see, there are 4 files in this repo:
1. agents.py: this file defines the agents in this model through the use of a class called 'MoneyAgent' - this is because the agents in this model are characterized as individuals that exchange money with one another.
2. app.py: while at some point, I'd like to create a webpage for this little project, this file is curently empty. Stay tuned for more updates on this but for now, it's empty.
3. model.py: this file defines two classes:
    A. the agent class (that is, how the agents interact)
    B. the manager class (an object that manages the agents)
4. run.py: this file currently threads the model together and creates visualizations for understanding the distribution of wealth over time (leveraging the Gini coefficient) as well as how many agents occupy a cell at the end of the simulation, in addition to exporting the model and agent data into .csv files.

## How to Use ##
1. Clone all files in this project.
2. Make sure to have all your library dependencies installed
3. Run the model from the 'run.py' script and enjoy the output visualizations and data

## NOTE ##
This was a fun project to work on and I'll be updating it as time goes on but for now, I'm happy with what I've learned and probably won't be updating this README anytime soon. Check the commitment history for more updates as that is the most reliable way to keep up-to-date with this project.

As always, ENJOY! =D
