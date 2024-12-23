import os
import networkx as nx
import matplotlib.pyplot as plt

directory = 'venv/Lib/site-packages/numpy'

dot = nx.Graph()

for fileName in os.listdir(directory):
    f = os.path.join(directory, fileName)
    if os.path.isdir(f):
        for subFile in os.listdir(f):
            dot.add_edge(fileName, subFile)

nx.draw(dot, with_labels=True, font_weight='bold')
plt.show()
plt.savefig('Graph.png', format='png')