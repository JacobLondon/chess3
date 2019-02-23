from pyngine import *

class LobbyController(Controller):

    def __init__(self, interface):
        Controller.__init__(self, interface)

        self.to_game = False
        self.to_menu = False

    def initialize_components(self):
        
        self.play_button = Button(self, 'Play')
        self.back_button = Button(self, 'Back')

        self.play_button.loc = self.screen_relative.southeast
        self.back_button.loc = self.screen_relative.southwest

        self.play_button.anchor = self.play_button.southeast
        self.back_button.anchor = self.back_button.southwest

        self.play_button.action = self.open_game
        self.back_button.action = self.open_menu

    def open_game(self):
        self.to_game = True
        self.stop_loop()

    def open_menu(self):
        self.to_menu = True
        self.stop_loop()

    def open_on_close(self):

        if self.to_game:
            from chess.gui.game import GameController
            g = GameController(interface)
            g.run()
        elif self.to_menu:
            from chess.gui.menu import MenuController
            m = MenuController(interface)
            m.run()

    
