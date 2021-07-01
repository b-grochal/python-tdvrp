from services import InputService, parse_nodes


class AppController:
    def __init__(self):
        self.input_service = InputService()

    def simulate(self, nodes_filepath):
        print(nodes_filepath)
        data = self.input_service.load_nodes_form_file(nodes_filepath)
        print(data)
        parse_nodes(data)
