from services import load_json_data_from_file, parse_nodes, load_nodes, load_vehicles


class AppController:
    def __init__(self):
        self.nodes = None
        self.vehicles = None

    def simulate(self, nodes_file_path, vehicles_file_path):
        self.load_data(nodes_file_path, vehicles_file_path)

    def load_data(self, nodes_file_path, vehicles_file_path):
        self.nodes = load_nodes(nodes_file_path)
        self.vehicles = load_vehicles(vehicles_file_path)

    # def determine_routes_for_vehicles(self):
    #     for vehicle in self.vehicles:
    #         route_point = None
    #         while true:
    #
    # def find_route_point(self, current_node, time):

