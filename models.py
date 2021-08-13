class Node:
    def __init__(self, name, load, links, is_visited):
        self.name = name
        self.load = load
        self.links = links
        self.is_visited = is_visited


class Link:
    def __init__(self, target_node, travel_time):
        self.target_node = target_node
        self.travel_time = travel_time


class Vehicle:
    def __init__(self, name, max_capacity):
        self.name = name
        self.max_capacity = max_capacity
        self.current_load = 0
        self.tour = []


class TourPoint:
    def __init__(self, node_name, collected_load, arrival_time, vehicle_load=0):
        self.node_name = node_name
        self.collected_load = collected_load
        self.arrival_time = arrival_time
        self.vehicle_load = vehicle_load
