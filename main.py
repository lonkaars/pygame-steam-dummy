import pygame
import sys

def load_fonts():
    pygame.font.init()
    return (
            pygame.font.Font("font/Regular.ttf", 12),
            pygame.font.Font("font/Medium.ttf", 12),
            pygame.font.Font("font/SemiBold.ttf", 12)
            )

def main():
    frame = 0
    pygame.init()
    font = load_fonts()
    window = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        window.fill((0, 0, 0))
        msElapsed = clock.tick(30)

        text = font[0].render(f"frame#{frame}", True, (255, 0, 255))
        window.blit(text, (0, 0))

        frame += 1
        pygame.display.flip()


if __name__ == "__main__":
    main()
