import networkx as nx
import matplotlib.pyplot as plt

def create_graph(entities, relationships):
    G = nx.Graph()
    for entity in entities:
        G.add_node(entity.value, type=entity.entity_type, **entity.properties)
    for src, dst, label in relationships:
        G.add_edge(src.value, dst.value, label=label)
    return G

def visualize_graph(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray")
    edge_labels = nx.get_edge_attributes(G, "label")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()
