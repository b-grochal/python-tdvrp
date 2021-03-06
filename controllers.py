from models import TourPoint
from services import load_json_data_from_file, parse_nodes, load_nodes, load_vehicles, show_routes, show_message


class AppController:
    def __init__(self):
        self.nodes = None
        self.vehicles = None

    def simulate(self, nodes_file_path, vehicles_file_path):
        self.load_data(nodes_file_path, vehicles_file_path)
        self.determine_tours_for_vehicles("Depot", 8)
        if self.check_if_all_nodes_are_visited():
            show_message("All routes has been visited!")
        else:
            show_message("Insufficient capacity!")
        self.show_routes()

    def load_data(self, nodes_file_path, vehicles_file_path):
        self.nodes = load_nodes(nodes_file_path)
        self.vehicles = load_vehicles(vehicles_file_path)

    def determine_tours_for_vehicles(self, starting_node, starting_time):
        self.set_starting_node_as_visited(starting_node)
        for vehicle in self.vehicles:
            current_time = starting_time
            tour_point = self.find_tour_point(starting_node, current_time, vehicle.max_capacity - vehicle.current_load)
            while tour_point is not None:
                vehicle.current_load += tour_point.collected_load
                tour_point.vehicle_load = vehicle.current_load
                vehicle.tour.append(tour_point)
                current_time = tour_point.arrival_time
                self.nodes[tour_point.node_name].is_visited = True
                tour_point = self.find_tour_point(tour_point.node_name, current_time, vehicle.max_capacity - vehicle.current_load)
            vehicle.tour.append(TourPoint("Depot", 0, current_time))

    def find_tour_point(self, current_node_name, time, available_vehicle_load):
        node = self.nodes[current_node_name]
        route_points = []
        for link in node.links:
            if not self.nodes[link.target_node].is_visited:
                route_points.append(TourPoint(link.target_node, self.nodes[link.target_node].load, time + link.travel_time[time % 24]))
        if len(route_points) == 0:
            return None

        route_points.sort(key=lambda x: x.arrival_time, reverse=False)
        for route_point in route_points:
            if route_point.collected_load <= available_vehicle_load:
                return route_point

        return None

    def show_routes(self):
        show_routes(self.vehicles)

    def check_if_all_nodes_are_visited(self):
        return all(node.is_visited is True for node in self.nodes.values())

    def set_starting_node_as_visited(self, starting_node):
        self.nodes[starting_node].is_visited = True
