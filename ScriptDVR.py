# Eraldo Tabaku Matricola: 0001089499
# Progetto per il corso di Reti di Telecomunicazione

import random

class Node:
    def __init__(self, name):
        self.name = name
        self.routing_table = {name: 0}
        self.neighbors = {}

    def add_neighbor(self, neighbor, distance):
        self.neighbors[neighbor] = distance
        self.routing_table[neighbor.name] = distance

    def remove_neighbor(self, neighbor):
        if neighbor in self.neighbors:
            del self.neighbors[neighbor]
        if neighbor.name in self.routing_table:
            del self.routing_table[neighbor.name]

    def update_routing_table(self):
        updated = False
        for neighbor, dist in self.neighbors.items():
            for destination, neighbor_dist in neighbor.routing_table.items():
                alt_distance = dist + neighbor_dist
                if destination not in self.routing_table or self.routing_table[destination] > alt_distance:
                    self.routing_table[destination] = alt_distance
                    updated = True
        return updated


def create_random_network(num_nodes, max_distance=10):
    nodes = [Node(chr(65 + i)) for i in range(num_nodes)]
    
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if random.random() < 0.5:
                distance = random.randint(1, max_distance)
                nodes[i].add_neighbor(nodes[j], distance)
                nodes[j].add_neighbor(nodes[i], distance)
    
    return nodes


def simulate_routing(network, max_iterations=10, error_probability=0.2):
    converged = False
    iteration = 0

    while not converged and iteration < max_iterations:
        converged = True
        print(f"\nIterazione {iteration}:")
        
        # Simulazione di errori: rimozione casuale di collegamenti
        for node in network:
            if random.random() < error_probability:
                if node.neighbors:
                    neighbor_to_remove = random.choice(list(node.neighbors.keys()))
                    print(f"Errore: Rimosso il collegamento tra {node.name} e {neighbor_to_remove.name}")
                    node.remove_neighbor(neighbor_to_remove)
                    neighbor_to_remove.remove_neighbor(node)

        for node in network:
            if node.update_routing_table():
                converged = False
        
        for node in network:
            print(f"Tabella di routing per il nodo {node.name}: {node.routing_table}")
        
        iteration += 1
    
    if converged:
        print("\nConvergenza raggiunta.")
    else:
        print("\nTermine simulazione: massimo numero di iterazioni raggiunto.")


if __name__ == "__main__":
    NUM_NODES = 5
    MAX_DISTANCE = 10
    ERROR_PROBABILITY = 0.2

    network = create_random_network(NUM_NODES, MAX_DISTANCE)

    print("Topologia della rete iniziale (collegamenti):")
    for node in network:
        for neighbor, distance in node.neighbors.items():
            print(f"{node.name} --{distance}--> {neighbor.name}")
    

    simulate_routing(network, error_probability=ERROR_PROBABILITY)

