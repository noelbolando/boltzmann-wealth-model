# Botlzmann Wealth Model #
This model is drawn from econophysics and presents a statistical mechanics approach to wealth distribution.

Refererences and further reading can be found below.

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

## References ##
Check out [this](https://mesa.readthedocs.io/stable/examples/basic/boltzmann_wealth_model.html) tutorial on how to build this model, using a similar approach to the one I used.

Other light readings:
1. [A Statistical Equilibrium Model of Wealth and Distribution](https://editorialexpress.com/cgi-bin/conference/download.cgi?db_name=SCE2001&amp;paper_id=214)
2. [Statistical Mechanics of Money, Income, and Wealth: A Short Survey](https://arxiv.org/pdf/cond-mat/0211175v1)

## NOTE ##
This was a fun project to work on and I'll be updating it as time goes on but for now, I'm happy with what I've learned and probably won't be updating this README anytime soon. Check the commitment history for more updates as that is the most reliable way to keep up-to-date with this project.

As always, ENJOY! =D
