import instaloader
from textwrap import wrap
import networkx as nx
import matplotlib.pyplot as plt

loader = instaloader.Instaloader()

username = "name"
password = "password"
loader.login(username, password)

profile = instaloader.Profile.from_username(loader.context, username)

graph = nx.Graph()

user_full_names = {username: profile.full_name}

graph.add_node(username, label=user_full_names[username])

for follower in profile.get_followers():
    follower_username = follower.username
    if follower_username not in user_full_names:
        user_full_names[follower_username] = follower.full_name
        graph.add_node(follower_username)
    graph.add_edge(username, follower_username)

avg_degree = sum(dict(graph.degree()).values()) / float(len(graph.nodes()))
print(f"Середня ступінь вершини: {avg_degree:.2f}")

pos = nx.spring_layout(graph)
node_labels = nx.get_node_attributes(graph, 'label')
plt.figure(figsize=(12, 8))
nx.draw(graph, pos, with_labels=True, font_weight='bold', node_color='lightgreen')
label_pos = {k: (v[0], v[1] + 0.05) for k, v in pos.items()}
labels = {k: '\n'.join(wrap(v, 16)) for k, v in node_labels.items()}
nx.draw_networkx_labels(graph, label_pos, labels, font_size=10, font_weight='bold')
plt.axis('off')
nx.write_gexf(graph, "insta_graph.gexf")
plt.show()
