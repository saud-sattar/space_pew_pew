import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    ## game info
    version = pygame.version.ver
    print(f"Starting Asteroids with pygame version: {version}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
   
    ## pygame initialisation
    pygame.init()
    
    ## screen and clock
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    ## sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    ## set containers for sprites
    Player.containers = (updatable, drawable)
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Shot.containers = (shots, updatable, drawable)
    
    ## player initialised
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    ## game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        log_state()
        screen.fill("black")
        
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)
            
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                running = False
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    
    pygame.quit()


if __name__ == "__main__":
    main()
