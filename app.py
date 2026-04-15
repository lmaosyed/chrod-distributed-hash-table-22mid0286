import streamlit as st
import random
import matplotlib.pyplot as plt
from chord import build_ring, lookup

st.title("Chord Protocol Simulation")

num_nodes = st.slider("Number of Nodes", 5, 30, 10)

node_ids = sorted(random.sample(range(64), num_nodes))
nodes = build_ring(node_ids)

st.write("### Nodes in Ring")
st.write(node_ids)

# Select node
selected_id = st.selectbox("Select Node", node_ids)
selected_node = [n for n in nodes if n.id == selected_id][0]

# Show finger table
st.write("### Finger Table")
for i, finger in enumerate(selected_node.finger_table):
    st.write(f"Entry {i}: Node {finger.id}")

# Lookup
key = st.slider("Lookup Key", 0, 63, 10)

if st.button("Run Lookup"):
    hops = lookup(selected_node, key)
    st.write("### Lookup Path")
    st.write(hops)
    st.write(f"Total hops: {len(hops)}")

    # Plot ring
    fig, ax = plt.subplots()
    ax.scatter(node_ids, [1]*len(node_ids))
    ax.set_title("Chord Ring (Linear View)")
    st.pyplot(fig)