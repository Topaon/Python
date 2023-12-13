import pygame

def run():
    pygame.init()

    screen = pygame.display.set_mode([400, 400])

    launched = True
    while launched:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                launched = False

        screen.fill((12, 25, 38))
        pygame.draw.line(screen, (128, 25, 240), [10, 10], [280, 310], 3)
        pygame.display.flip()

    pygame.quit()

run()
