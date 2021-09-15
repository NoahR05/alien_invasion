class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        # start chonko invasion in an active state
        self.game_active = True

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
