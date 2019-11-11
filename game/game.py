from level import Level
from game.gameio import Control
from game.gameui import MainUI
from game.gameui import StartUI
from game.gameui import StoryUI
from game.gameui import GameCompleteUI
from game.gameui import PlayerDeadUI
from game.gameui import LevelsUI
from character.player import Player
from config import level_config


class Game(object):
    """Game class that contains all the game mechanics."""

    def __init__(self, debug=False):
        self.debug = debug
        self.control = Control(self)
        self.level = Level(self)
        self.player = Player(self)
        self.gameui = StartUI(self)
        self.setup()

    def setup_level(self, level_number):
        """Setup the game level."""

        level = Level(self)
        level.build(level_number)
        self.level = level

    def setup_player(self):
        """Setup the player based on the game level"""

        map_config = level_config['level'][self.level.number]['map']
        enter_coords = map_config['coord_enter']
        enter_orientation = map_config['orientation_enter']

        self.player.move_to(*enter_coords)
        self.player.orientation = enter_orientation
        self.player.inventory.clear_items()

    def setup(self, level_number=0):
        """Setup game elements."""

        # setup level before player
        self.setup_level(level_number)
        self.setup_player()

    def mainloop(self):
        """The main game loop."""

        while True:

            if isinstance(self.gameui, StartUI):
                if self.debug is True:
                    self.gameui = LevelsUI(game=self)

            if isinstance(self.gameui, MainUI):
                if self.player.cell.has_story_text() and not self.player.cell.story_seen:
                    self.gameui = StoryUI(game=self)
                if self.level.system.kills_player():
                    death = self.level.system.get_death()
                    self.gameui = PlayerDeadUI(game=self, message=death['description'])
                if self.level.is_complete():
                    if not self.level.has_next_level():
                        self.gameui = GameCompleteUI(game=self)
                    else:
                        self.gameui.next_level()
                        continue

            self.gameui.process_input(self.gameui.prompt())