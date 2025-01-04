"""
The model gives us space to define two classes:
    1. the agent class
    2. the manager class (object that manages the agents)
"""

import matplotlib.pyplot as plt
import mesa
import numpy as np
import pandas as pd

from agents import MoneyAgent

"""Creating a model object to measure the gini coefficient.
This gives us a metric for measuring wealth inequality across the model."""
def compute_gini(model):
    # Determining agent_wealths over steps
    agent_wealths = [agent.wealth for agent in model.agents]
    # Sorting agent_wealths in increasing value
    x = sorted(agent_wealths)
    n = model.num_agents
    # B in the Gini coefficient
    B = sum(xi * (n - i) for i, xi in enumerate(x)) / (n * sum(x))
    value = 1 + (1 / n) - 2 * B
    return value

"""Creating a new object associated with the model,
that is, a subclass of the model that defines how many agents we initiate."""
class MoneyModel(mesa.Model):
    """A model with some number of agents."""

    def __init__(self, n, width, height):
        super().__init__()
        """Setting up the agent properties (num_agents and grid)"""
        # Set number of agents
        self.num_agents = n
        # Create a multigrid for the agents to interact and exchange wealth
        self.grid = mesa.space.MultiGrid(width, height, True)
        # Collect the output to for the gini coefficient
        self.datacollector = mesa.DataCollector(
            model_reporters={"Gini": compute_gini}, 
            agent_reporters={"Wealth": "wealth"}
        )
        
        """Create the agents"""
        agents = MoneyAgent.create_agents(model=self, n=n)
        # Create x and y positions for agents
        x = self.rng.integers(0, self.grid.width, size=(n,))
        y = self.rng.integers(0, self.grid.height, size=(n,))
        for a, i, j in zip(agents, x, y):
            # Add the agent to a random grid cell
            # 'a' denoates the agent
            # the pair, (i, j), denote the coordinates of the agent
            self.grid.place_agent(a, (i, j))

    def step(self):
        """Advance the model by one step."""

        # This function runs data collection over the duration
        # of the model to determine the gini coefficient (wealth inequality)
        self.datacollector.collect(self)
        self.agents.shuffle_do("move_agents")

        # This function randomly reorders the list of agent objects
        # and then iterates through calling the function passed in as 
        # a parameter ("say_hi", in this case).
        self.agents.do("give_money")
