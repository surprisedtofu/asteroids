# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from asteroid import *
from asteroidfield import *
from constants import *
from player import *
from shot import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid_group, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shot_group, updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for item in updatable:
            item.update(dt)
        for asteroid in asteroid_group:
            if player.is_collision(asteroid):
                print("Game over!")
                sys.exit()
            for shot in shot_group:
                if shot.is_collision(asteroid):
                    shot.kill()
                    asteroid.split()
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()