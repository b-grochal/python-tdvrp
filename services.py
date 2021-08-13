import json
from models import Link, Node, Vehicle


# Input
def load_json_data_from_file(file_path):
    with open(file_path) as file:
        return json.load(file)


# Output
def show_routes(vehicles):
    for vehicle in vehicles:
        print("Vehicle: {} - Max Capacity: {}".format(vehicle.name, vehicle.max_capacity))
        for tour_point in vehicle.tour:
            print("Node: {} - Time: {} - Collected load: {} - Vehicle load: {}/{}".format(tour_point.node_name, tour_point.arrival_time, tour_point.collected_load, tour_point.vehicle_load, vehicle.max_capacity))
        print("\n")


def show_message(message):
    print(message + "\n")


# Parser
def parse_nodes(nodes_json):
    nodes = {}
    for node in nodes_json["nodes"]:
        node_links = parse_links((node["links"]))
        nodes[node["name"]] = Node(node["name"], node["load"], node_links, False)
    return nodes


# Parser
def parse_links(links_json):
    links = []
    for link in links_json:
        links.append(Link(link["target_node"], link["travel_times"]))
    return links


# Parser
def parse_vehicles(vehicles_json):
    vehicles = []
    for vehicle in vehicles_json["vehicles"]:
        vehicles.append(Vehicle(vehicle["name"], vehicle["max_capacity"]))
    return vehicles


# Helper
def load_nodes(nodes_file_path):
    json_data = load_json_data_from_file(nodes_file_path)
    return parse_nodes(json_data)


# Helper
def load_vehicles(vehicles_file_path):
    json_data = load_json_data_from_file(vehicles_file_path)
    return parse_vehicles(json_data)
