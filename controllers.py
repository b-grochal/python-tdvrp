from models import RoutePoint
from services import load_json_data_from_file, parse_nodes, load_nodes, load_vehicles, show_routes


class AppController:
    def __init__(self):
        self.nodes = None
        self.vehicles = None

    def simulate(self, nodes_file_path, vehicles_file_path):
        self.load_data(nodes_file_path, vehicles_file_path)
        self.determine_routes_for_vehicles("Depot", 8)
        self.show_routes()
        print("END")

    def load_data(self, nodes_file_path, vehicles_file_path):
        self.nodes = load_nodes(nodes_file_path)
        self.vehicles = load_vehicles(vehicles_file_path)

    def determine_routes_for_vehicles(self, starting_node, starting_time):
        for vehicle in self.vehicles:
            current_time = starting_time
            route_point = self.find_route_point(starting_node, current_time, vehicle.max_capacity - vehicle.current_load)
            while route_point is not None:
                if vehicle.current_load + route_point.load > vehicle.max_capacity:
                    break
                vehicle.add_route_point(route_point)
                current_time = route_point.time
                self.nodes[route_point.node_name].is_visited = True
                route_point = self.find_route_point(route_point.node_name, current_time, vehicle.max_capacity - vehicle.current_load)
            vehicle.add_route_point(RoutePoint("Depot", 0, current_time))

    def find_route_point(self, current_node_name, time, available_vehicle_load):
        node = self.nodes[current_node_name]
        route_points = []
        for link in node.links:
            if not self.nodes[link.target_node].is_visited:
                route_points.append(RoutePoint(link.target_node, self.nodes[link.target_node].load, time + link.travel_time[time % 24]))
        if len(route_points) == 0:
            return None

        route_points.sort(key=lambda x: x.load, reverse=False)
        for route_point in route_points:
            if route_point.load <= available_vehicle_load:
                return route_point

        return None

    def show_routes(self):
        show_routes(self.vehicles)
