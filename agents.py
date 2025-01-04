"""
In this model, agents are the individuals that exchange money 
such that the amount of money an individiaul agent has is 
represented as wealth.

Notes:
    - mesa automatically asigns each agent a unique_id
    - the 'do' function calls agent functions to grow in the ABS model 
"""

import mesa

"""Creating a new object associated with each agent, 
that is, a subclass of each agent. MoneyAgent represents wealth."""
class MoneyAgent(mesa.Agent):
    """An agent with fixed initial wealth."""

    def __init__(self, model):
        # Pass the parameters to the parent class
        super().__init__(model)

        # Initiate the agent's variable (wealth) and set the initial values
        self.wealth = 1
    
    def say_hi(self):
        # The agent's step will GO here
        # The agent introduces itself with it's 'unique_id'
        print(f"Hi, I am an agent, you can call me {str(self.unique_id)}.")

    def say_wealth(self):
        # The agent's step will GO here
        # The agent introduces itself with it's 'wealth'
        print(f"Hi, I am an agent named {str(self.unique_id)}, I have this much wealth {str(self.wealth)}.")

    def exchange_wealth(self):
        # The agent's step will GO here
        # First, verify that agent has some wealth
        if self.wealth > 0:
            # If they do, then they random choose another agent to engage with
            other_agent = self.random.choice(self.model.agents)
            # As long as the other agent exists, 
            # the other agent's wealth increaes by 1
            # and the initial agent's wealth decreases by 1
            if other_agent is not None:
                other_agent.wealth += 1
                self.wealth -= 1
    
    def move_agents(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            # Moore method includes all 8 surrounding squares
            moore=True,
            include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def give_money(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        # Ensure agent is not giving money to itself
        cellmates.pop(
            cellmates.index(self)
        )
        if len(cellmates) > 0:
            other = self.random.choice(cellmates)
            other.wealth += 1
            self.wealth -= 1
