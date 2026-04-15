import simpy
import random
from chord import build_ring, lookup

def lookup_process(env, nodes):
    while True:
        start = random.choice(nodes)
        key = random.randint(0, 63)

        hops = lookup(start, key)

        print(f"[{env.now}] Lookup key {key} from Node {start.id}")
        print(f"Path: {hops} | Hops = {len(hops)}\n")

        yield env.timeout(1)


def run_simulation(num_nodes=10):
    env = simpy.Environment()

    node_ids = random.sample(range(64), num_nodes)
    nodes = build_ring(node_ids)

    env.process(lookup_process(env, nodes))
    env.run(until=10)

    return nodes