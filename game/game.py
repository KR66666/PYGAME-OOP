from os import name
import pygame
from config import *
from game.player import Player
from game.platform import Platform
from game.coin import Coin
import random

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True

        self.all_sprites = pygame.sprite.Group()
        self.platform = pygame.sprite.Group()

        x = random.randint(50, SCREEN_WIDTH - 50)
        y = random.randint(50, 200)
        self.player = Player(x, y)
        self.all_sprites.add(self.player)

        ground = Platform(0, SCREEN_HEIGHT - 40, SCREEN_WIDTH, 40)
        self.platform.add(ground)
        self.all_sprites.add(ground)

        p1 = Platform(150, 450, 150, 20)
        p2 = Platform(400, 350, 150, 20)
        p3 = Platform(600, 250, 150, 20)
        self.platform.add(p1, p2, p3)
        self.all_sprites.add(p1, p2, p3)

        self.coins = pygame.sprite.Group()
        c1 = Coin(200,420)
        c2 = Coin(450,320)
        c3 = Coin(650,220)
        self.coins.add(c1,c2,c3)
        self.all_sprites.add(c1,c2,c3)

    def handle_events(self):
        for event in pygame.event.get():
            evt_name = pygame.event.event_name(event.type)

            if event.type == pygame.QUIT:
                self.running = False

            if event.type in (pygame.KEYDOWN, pygame.KEYUP):
                evt_key = pygame.key.name(event.key)
                print(f"{evt_name}: {evt_key}")

            elif event.type == pygame.MOUSEMOTION:
                print(f"{evt_name}: {event.pos}")

            elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP):
                print(f"{evt_name}: {event.button} at {event.pos}")
    
    def update(self):
        game_over = self.player.update(self.platform)

        coins_collected = pygame.sprite.spritecollide(self.player, self.coins, True)
        if len(self.coins) == 0:
            print("Vyhrál jsi")
            self.running = False
        if game_over:
            self.running = False

    def draw(self):
        self.screen.fill(SKY_BLUE)
        
        for sprite in self.all_sprites:
            sprite.draw(self.screen)
        
        pygame.display.flip()


    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)