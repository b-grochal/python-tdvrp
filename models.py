class Node:
    def __init__(self, name, links, is_visited):
        self.name = name
        self.links = links
        self.is_visited = is_visited


class Link:
    def __init__(self, target_node, costs):
        self.target_node = target_node
        self.costs = costs


class Vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.route = []

    def add_route_point(self, route_point):
        self.route.append(route_point)


class RoutePoint:
    def __init__(self, node_name, cost, time):
        self.node_name = node_name
        self.cost = cost
        self.time = time
