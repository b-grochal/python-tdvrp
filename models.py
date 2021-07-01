class Node:
    def __init__(self, name, links):
        self.name = name
        self.links = links


class Link:
    def __init__(self, target_node, costs):
        self.target_node = target_node
        self.costs = costs
