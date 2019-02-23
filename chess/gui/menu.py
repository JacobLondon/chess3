from pyngine import *

class MenuController(Controller):

    def __init__(self, interface):
        Controller.__init__(self, interface)

    def initialize_components(self):

        self.play_button = Button(self, 'Play')
        self.deck_button = Button(self, 'Deck Builder')
        self.options_button = Button(self, 'Options')
        self.exit_button = Button(self, 'Exit')

        self.play_button.loc = self.screen_grid.get_pixel(0, 0)
        self.deck_button.loc = self.screen_grid.get_pixel(0, 3)
        self.options_button.loc = self.screen_grid.get_pixel(0, 6)
        self.exit_button.loc = self.screen_grid.get_pixel(0, 9)