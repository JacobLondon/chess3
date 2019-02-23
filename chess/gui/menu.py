from pyngine import *

class MenuController(Controller):

    def __init__(self, interface):
        Controller.__init__(self, interface)

        self.to_lobby = False
        self.to_deck = False
        self.to_options = False

    def initialize_components(self):

        # init components
        self.play_button = Button(self, 'Play')
        self.deck_button = Button(self, 'Deck Builder')
        self.options_button = Button(self, 'Options')
        self.exit_button = Button(self, 'Exit')
        # set locations
        self.play_button.loc = self.screen_grid.get_pixel(0, 0)
        self.deck_button.loc = self.screen_grid.get_pixel(0, 5)
        self.options_button.loc = self.screen_grid.get_pixel(0, 10)
        self.exit_button.loc = self.screen_grid.get_pixel(0, 15)
        # define actions
        self.play_button.action = self.open_lobby
        self.deck_button.action = self.open_deck
        self.options_button.action = None
        self.exit_button.action = self.stop_program

    def open_lobby(self):
        self.to_lobby = True
        self.stop_loop()

    def open_deck(self):
        self.to_deck = True
        self.stop_loop()

    def open_on_close(self):

        if self.to_lobby:
            from chess.gui.lobby import LobbyController
            l = LobbyController(self.interface)
            l.run()
        elif self.to_deck:
            from chess.gui.deck import DeckController
            d = DeckController(self.interface)
            d.run()
