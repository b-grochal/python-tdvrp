import sys
from controllers import AppController


def main(arguments):
    app_controller = AppController()
    #app_controller.simulate(arguments[1])
    app_controller.simulate("nodes.json")


if __name__ == '__main__':
    print(sys.argv)
    main(sys.argv)
