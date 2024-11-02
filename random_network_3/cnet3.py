import networkx as nx
import matplotlib.pyplot as plt

g_1 = nx.erdos_renyi_graph(2000, 0.25)

nx.draw(g_1, node_size=100, alpha=0.5, node_color="yellow", with_labels=False)

plt.savefig("cnet3.png")

nx.write_gexf(g_1, "cnet3.gexf", version="1.2draft")


