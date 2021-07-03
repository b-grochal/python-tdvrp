class Node:
    def __init__(self, name, links):
        self.name = name
        self.links = links


class Link:
    def __init__(self, target_node, costs):
        self.target_node = target_node
        self.costs = costs


class Vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.route = []


class RoutePoint:
    def __init__(self, node_name, time, cost):
        self.node_name = node_name
        self.time = time
        self.cost = cost
