import json

from models import Link, Node


class InputService:
    def load_nodes_form_file(self, file_path):
        with open(file_path) as file:
            return json.load(file)


def parse_nodes(nodes_json):
    nodes = []
    for node in nodes_json["nodes"]:
        node_links = parse_links((node["links"]))
        nodes.append(Node(node["name"], node_links))
    return nodes


def parse_links(links_json):
    links = []
    for link in links_json:
        links.append(Link(link["target_node"], link["costs"]))
    return links
