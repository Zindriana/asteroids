# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from asteroid import *
from constants import *
from player import *
from asteroidfield import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while 1 > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for drawable_object in drawable:
            drawable_object.draw(screen)
        for updatable_object in updatable:
            updatable_object.update(dt)
        pygame.display.flip()
        dt = clock.tick(60)/1000
if __name__ == "__main__":
    main()
