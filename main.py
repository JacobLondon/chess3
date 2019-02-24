from chess import MenuController
from pyngine import Interface

def main():
    interface = Interface(window_text='Chess 3', resolution=(1000,800))
    controller = MenuController(interface)
    controller.run()

if __name__ == '__main__':
    main()