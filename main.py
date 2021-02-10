import pygame
import sys
import gradients

def load_fonts():
    pygame.font.init()
    return (
            pygame.font.Font("font/Regular.ttf", 12),
            pygame.font.Font("font/Medium.ttf", 12),
            pygame.font.Font("font/SemiBold.ttf", 12)
            )

def percentage_between(value, smallest, largest):
    return (value - smallest) / (largest - smallest)

class steam_message:
    def __init__(self, author, message, avatar, frame, fonts):
        self.author = author
        self.message = message
        self.avatar = avatar
        self.fonts = fonts
        self.starting_frame = frame
        self.width = 240
        self.height = 74
        self.position = (0, 0)

    def draw_box(self, window):
        window.blit(gradients.vertical((self.width, self.height), (18, 26, 42, 255), (24, 53, 82, 255)), self.position)
        window.blit(gradients.vertical((self.width-2, self.height-2), (42, 46, 51, 255), (20, 28, 43, 255)), [p+1 for p in self.position])

    def draw_avatar(self, window):
        window.blit(gradients.vertical((36, 36), (144, 186, 60, 255), (112, 144, 56, 255)), [p+19 for p in self.position])
        window.blit(gradients.vertical((34, 34), (108, 137, 56, 255), (91, 118, 53, 255)), [p+20 for p in self.position])
        window.blit(pygame.transform.scale(self.avatar, (32, 32)), (self.position[0] + 21, self.position[1] + 21))

    def animation_interpolation(self, frame, framerate):
        relative_frame = frame - self.starting_frame
        keyframe_1 = int(framerate * 0.2)
        keyframe_2 = keyframe_1 + int(framerate * 6.0)
        keyframe_3 = keyframe_2 + int(framerate * 0.2)

        if relative_frame in range(0, keyframe_1):
            return percentage_between(relative_frame, 0, keyframe_1)
        elif relative_frame in range(keyframe_1, keyframe_2):
            return 1
        elif relative_frame in range(keyframe_2, keyframe_3):
            return percentage_between(relative_frame, keyframe_3, keyframe_2)
        else:
            return 0

    def move(self, window, frame, framerate):
        window_size = window.get_size()
        x = window_size[0] - self.width
        y = window_size[1] - self.height * self.animation_interpolation(frame, framerate)
        self.position = (x, y)

    def render(self, window, frame, framerate):
        self.move(window, frame, framerate)
        self.draw_box(window)
        self.draw_avatar(window)
        window.blit(self.fonts[2].render(self.author, True, (138, 177, 59)), (self.position[0] + 64, self.position[1] + 16))
        window.blit(self.fonts[1].render("says: ", True, (126, 126, 126)), (self.position[0] + 64, self.position[1] + 30))
        window.blit(self.fonts[0].render(self.message, True, (166, 170, 177)), (self.position[0] + 64, self.position[1] + 44))

def main():
    pygame.init()
    window = pygame.display.set_mode((1280, 720))

    frame = 0
    framerate = 30
    clock = pygame.time.Clock()

    font = load_fonts()

    avatar = pygame.image.load("avatar.png").convert()

    msg = steam_message("Loekaars", "Gert komt je moeder halen", avatar, frame, font)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        window.fill((0, 0, 0))
        msElapsed = clock.tick(framerate)

        text = font[0].render(f"frame#{frame}", True, (255, 0, 255))
        window.blit(text, (0, 0))

        is_mouse_pressed = pygame.mouse.get_pressed()[0]
        if is_mouse_pressed:
            msg.starting_frame = frame

        msg.render(window, frame, framerate)

        frame += 1
        pygame.display.flip()


if __name__ == "__main__":
    main()
