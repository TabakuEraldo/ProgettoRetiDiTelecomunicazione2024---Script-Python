import copy

class Node:
    def __init__(self, name):
        self.name = name
        self.routing_table = {name: 0}
        self.neighbors = {}
    
    def add_neighbor(self, neighbor, distance):
        self.neighbors[neighbor] = distance
        self.routing_table[neighbor.name] = distance
    def update_routing_table(self):
        updated = False
        for neighbor, dist in self.neighbors.items():
            for destination, neighbor_dist in neighbor.routing_table.items():
                alt_distance = dist + neighbor_dist
                if destination not in self.routing_table or self.routing_table[destination] > alt_distance:
                    self.routing_table[destination] = alt_distance
                    updated = True
        return updated


def create_network():
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    
    A.add_neighbor(B, 1)
    A.add_neighbor(C, 4)
    B.add_neighbor(A, 1)
    B.add_neighbor(C, 2)
    B.add_neighbor(D, 5)
    C.add_neighbor(A, 4)
    C.add_neighbor(B, 2)
    C.add_neighbor(D, 1)
    D.add_neighbor(B, 5)
    D.add_neighbor(C, 1)
    
    return [A, B, C, D]


def simulate_routing(network):
    converged = False
    iteration = 0
    
    while not converged:
        converged = True
        print(f"\nIterazione {iteration}:")
        for node in network:
            if node.update_routing_table():
                converged = False
        for node in network:
            print(f"Tabella di routing per il nodo {node.name}: {node.routing_table}")
        
        iteration += 1

if __name__ == "__main__":
    network = create_network()
    simulate_routing(network)

