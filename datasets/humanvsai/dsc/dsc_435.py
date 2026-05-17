import pygame
import sys

class Canvas:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))

    def draw_cross(self, position, color=(255, 0, 0), radius=4):
        pygame.draw.line(self.screen, color, (position[0] - radius, position[1] - radius), (position[0] + radius, position[1] + radius), 2)
        pygame.draw.line(self.screen, color, (position[0] + radius, position[1] - radius), (position[0] - radius, position[1] + radius), 2)

    def update(self):
        pygame.display.flip()

def main():
    canvas = Canvas()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        canvas.screen.fill((0, 0, 0))
        canvas.draw_cross((400, 300))
        canvas.update()

if __name__ == "__main__":
    main()