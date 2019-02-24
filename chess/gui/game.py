from pyngine import *

class GameController(Controller):

    def __init__(self, interface, white_pieces, black_pieces):
        Controller.__init__(self, interface)

        self.white_pieces = white_pieces
        self.black_pieces = black_pieces

        # width of board image's border relative to its size
        self.border = 0.055
        # chess board is 8x8
        self.chess_grid = 8
        # z index of board/pieces
        self.game_z = 5000
        # options grid height
        self.options_gheight = 10

        # go back to menu
        self.to_menu = False

    def initialize_components(self):
        """Board Area"""
        # area where the game board is drawn
        self.game_panel = Panel(self)
        self.game_panel.width = self.interface.resolution[1]
        self.game_panel.height = self.interface.resolution[1]
        # image of the board
        self.board_box = Imagebox(self, 'chess/assets/board.jpeg', z=self.game_z)
        self.game_z += 1
        self.board_box.scale_to(self.game_panel.width, self.game_panel.height)

        # grid for the pieces on the board
        self.board_grid_panel = Panel(self)
        self.board_grid_panel.loc = (self.game_panel.width * self.border, self.game_panel.height * self.border)
        self.board_grid_panel.width = self.game_panel.width - 2 * (self.game_panel.width * self.border)
        self.board_grid_panel.height = self.game_panel.height - 2 * (self.game_panel.height * self.border)
        #self.board_grid_panel.background = Color['black']

        # grid itself for the pieces
        self.game_grid = Grid(self.board_grid_panel, self.chess_grid, self.chess_grid)

        """Options Area"""
        self.options_panel = Panel(self)
        self.options_panel.loc = (self.interface.resolution[1], self.game_panel.loc[0])
        self.options_panel.width = self.interface.resolution[0] - self.interface.resolution[1]
        self.options_panel.height = self.interface.resolution[1]
        #self.options_panel.background = Color['green']

        # grid for items in the options panel
        self.options_listbox = Listbox(self, self.options_panel)
        self.options_listbox.loc = (self.interface.resolution[0], 0)
        self.options_listbox.width = self.options_panel.width
        self.options_listbox.height = self.options_panel.height

        # buttons for options
        self.undo_button = Button(self, 'Undo', self.options_panel)
        self.new_button = Button(self, 'New', self.options_panel)
        self.exit_button = Button(self, 'Exit', self.options_panel)
        # set actions
        self.undo_button.action = None
        self.new_button.action = None
        self.exit_button.action = self.open_menu
        # put in the listbox
        self.options_listbox.add(self.undo_button)
        self.options_listbox.add(self.new_button)
        self.options_listbox.add(self.exit_button)

    def open_menu(self):
        self.open_menu = True
        self.stop_loop()

    def open_on_close(self):
        if self.open_menu:
            from chess.gui.menu import MenuController
            m = MenuController(self.interface)
            m.run()
