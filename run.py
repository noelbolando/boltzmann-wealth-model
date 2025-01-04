import matplotlib.pyplot as plt
import numpy as np

from model import MoneyModel, compute_gini

all_wealth = []

# This runs the model model_run times where each model has steps
model_runs = 100
for _ in range(model_runs):
    x_size = 10
    y_size = 10
    num_agents = 100
    steps = 100
    # Run the model with 100 agents on a 10x10 grid
    model = MoneyModel(num_agents, x_size, y_size)
    for _ in range(steps):
        model.step()

    # Store the results
    for agent in model.agents:
        all_wealth.append(agent.wealth)

# Create a histogram with matplotlib
bins = np.arange(0, 10, 1)
plt.hist(all_wealth, bins=bins, edgecolor="black", histtype="bar")
plt.title("Wealth Ditribution")
plt.xlabel("Wealth [USD]")
plt.ylabel("Number of Agents")
plt.show()

"""Create a heatmap to visualize the number of agents residing in each cell"""
agent_counts = np.zeros((model.grid.width, model.grid.height))
for cell_content, (x,y) in model.grid.coord_iter():
    agent_count = len(cell_content)
    agent_counts[x][y] = agent_count

# Plot a heatmap with matplotlib
fig, ax = plt.subplots()
im = ax.imshow(agent_counts)
# Iterate through each agent_counts value to plot the agent_counts in each
# grid of the heatmap
for i in range(len(agent_counts)):
    for j in range (len(agent_counts)):
        text = ax.text(j, i, agent_counts[i, j], ha="center", va="center")
ax.set_title("Number of Agents on Each Cell of the Grid")
plt.show()

"""Plot the Gini coefficient (wealth inequality) over time."""
gini_coeff = model.datacollector.get_model_vars_dataframe()
# Plot the Gini coefficient over times
gini_coeff.plot()
plt.title("Gini Coefficient over Time")
plt.xlabel("Steps")
plt.ylabel("Gini Coefficient")
plt.show()

"""Printing Agent Data"""
agent_wealth = model.datacollector.get_agent_vars_dataframe()
print(agent_wealth.head())

"""Plot the wealth distribution at the end of the simulation"""
last_step = agent_wealth.index.get_level_values("Step").max()
end_wealth = agent_wealth.xs(last_step, level="Step")["Wealth"]
# Create a histogram of wealth at the last step
plt.hist(end_wealth, edgecolor="black", histtype="bar")
plt.title("Wealth Ditribution at the End of the Simulation")
plt.xlabel("Wealth [USD]")
plt.ylabel("Number of Agents")
plt.show()

"""Plot the average wealth of all agents over time"""
# Transform the data to a long format
agent_wealth_long = agent_wealth.T.unstack().reset_index()
agent_wealth_long.columns = ["Step", "AgentID", "Variable", "Value"]
agent_wealth_long.head(3)
# Plot the average wealth over time
agent_wealth_long.plot(x="Step", y="Value")
plt.title("Average Wealth for All Agents over Time")
plt.xlabel("Step")
plt.ylabel("Value")
plt.show()

"""Export model data"""
# Save the model data to a csv
gini_coeff.to_csv("model_data.csv")
# Save the agent data to a csv
agent_wealth.to_csv("agent_data.csv")
