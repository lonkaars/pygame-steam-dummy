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

class steam_message:
    def __init__(self, **kwargs):
        self.author = kwargs["author"]
        self.message = kwargs["message"]
        self.avatar = kwargs["avatar"]
        self.fonts = kwargs["fonts"]
        self.starting_frame = kwargs["frame"]
        self.window = kwargs["window"]
        self.framerate = kwargs["framerate"]
        self.width = 240
        self.height = 74
        self.position = (0, 0)

    def draw_box(self):
        self.window.blit(gradients.vertical((self.width, self.height), (18, 26, 42, 255), (24, 53, 82, 255)), self.position)
        self.window.blit(gradients.vertical((self.width-2, self.height-2), (42, 46, 51, 255), (20, 28, 43, 255)), [p+1 for p in self.position])

    def draw_avatar(self):
        self.window.blit(gradients.vertical((36, 36), (144, 186, 60, 255), (112, 144, 56, 255)), [p+19 for p in self.position])
        self.window.blit(gradients.vertical((34, 34), (108, 137, 56, 255), (91, 118, 53, 255)), [p+20 for p in self.position])
        self.window.blit(pygame.transform.scale(self.avatar, (32, 32)), (self.position[0] + 21, self.position[1] + 21))

    def linear_interpolate(self, value, smallest, largest):
        return (value - smallest) / (largest - smallest)

    def animation_interpolation(self, frame):
        relative_frame = frame - self.starting_frame
        keyframe_1 = int(self.framerate * 0.2)
        keyframe_2 = keyframe_1 + int(self.framerate * 6.0)
        keyframe_3 = keyframe_2 + int(self.framerate * 0.2)

        if relative_frame in range(0, keyframe_1):
            return self.linear_interpolate(relative_frame, 0, keyframe_1)
        elif relative_frame in range(keyframe_1, keyframe_2):
            return 1
        elif relative_frame in range(keyframe_2, keyframe_3):
            return self.linear_interpolate(relative_frame, keyframe_3, keyframe_2)
        else:
            return 0

    def move(self, frame):
        window_size = self.window.get_size()
        x = window_size[0] - self.width
        y = window_size[1] - self.height * self.animation_interpolation(frame)
        self.position = (x, y)

    def render(self, frame):
        self.move(frame)
        self.draw_box()
        self.draw_avatar()
        self.window.blit(self.fonts[2].render(self.author, True, (138, 177, 59)), (self.position[0] + 64, self.position[1] + 16))
        self.window.blit(self.fonts[1].render("says: ", True, (126, 126, 126)), (self.position[0] + 64, self.position[1] + 30))
        self.window.blit(self.fonts[0].render(self.message, True, (166, 170, 177)), (self.position[0] + 64, self.position[1] + 44))

def main():
    pygame.init()
    window = pygame.display.set_mode((1280, 720))

    frame = 0
    framerate = 30
    clock = pygame.time.Clock()

    font = load_fonts()

    msg = steam_message(
            author="Loekaars",
            message="Gert komt je moeder halen",
            avatar=pygame.image.load("avatar.png").convert(),
            fonts=font,
            frame=frame,
            framerate=framerate,
            window=window
            )

    while True:
        # check if window wants to be closed by user instead of stopping process in tty
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        window.fill((0, 0, 0)) # clear the window

        msElapsed = clock.tick(framerate) # wait for next frame

        # render frame count in top left
        window.blit(font[0].render(f"frame#{frame}", True, (255, 0, 255)), (0, 0))

        # reset animation starting frame when left mouse button is pressed (restart animation)
        if pygame.mouse.get_pressed()[0]:
            msg.starting_frame = frame

        msg.render(frame) # render the steam message popup

        frame += 1 # increment the frame counter
        pygame.display.flip() # push all drawing operations to the window


if __name__ == "__main__":
    main()
