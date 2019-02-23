from pyngine import *

class GameController(Controller):

    def __init__(self, interface):
        Controller.__init__(self, interface)

    def initialize_components(self):
        self.board_box = Imagebox(self, 'chess/assets/board.jpeg')
        self.board_box.scale_to(self.interface.resolution[0], self.interface.resolution[1])