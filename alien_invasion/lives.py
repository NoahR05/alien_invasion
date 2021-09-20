import pygame.font


class Lives:
    """class to display the number of lives left"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (100, 100, 100)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_lives()

    def prep_lives(self):
        lives_str = str(self.stats.ships_left)
        lives_remaining = "lives remaining: " + lives_str
        self.lives_image = self.font.render(lives_remaining, True,
                                            self.text_color, self.settings.bg_color)

        # display the remaining lives at the top left of the screen
        self.lives_rect = self.lives_image.get_rect()
        self.lives_rect.right = self.screen_rect.left + 20
        self.lives_rect.top = 20

    def show_lives(self):
        """draw lives to the screen"""
        self.screen.blit(self.lives_image, self.lives_rect)
