import networkx as nx
import matplotlib.pyplot as plt

g_1 = nx.erdos_renyi_graph(1000, 0.2)

nx.draw(g_1, node_size=100, alpha=0.5, node_color="red", with_labels=False)

plt.savefig("cnet2.png")

nx.write_gexf(g_1, "cnet2.gexf", version="1.2draft")


