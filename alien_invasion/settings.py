import pygame


class Settings:
    def __init__(self):
        # screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (0, 0, 0)
        self.bg = pygame.image.load('space_background.png')

        # ship settings
        self.ship_speed = 3.0
        self.ship_limit = 3

        # bullet settings
        self.bullet_speed = 2.0

        # 3, 15 original
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3

        # sound settings- bullet, collision, music
        self.bullet_sound = pygame.mixer.Sound('laser.mp3')
        self.hit_sound = pygame.mixer.Sound('mixkit-short-explosion-1694.wav')

        # alien settings
        self.alien_speed = 1.8
        self.fleet_drop_speed = 10

        # how quickly the game speeds up
        self.speedup_scale = 1.1

        # how quickly the score inrements speed up
        self.score_scale = 1.5

        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize settings that change throughout the game."""
        self.ship_speed = 3.0
        self.bullet_speed = 2.0
        self.alien_speed = 2.0

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """increase speed settings and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
