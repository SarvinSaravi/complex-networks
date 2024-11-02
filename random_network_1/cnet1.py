import networkx as nx
import matplotlib.pyplot as plt

g_1 = nx.erdos_renyi_graph(500, 0.1)

nx.draw(g_1, node_size=100, alpha=0.5, node_color="blue", with_labels=False)

plt.savefig("cnet1.png")

nx.write_gexf(g_1, "cnet1.gexf", version="1.2draft")


