import pygame
import spritesheet
import sprite_animations.zoro as z

BG = (50, 50, 50)
BLACK = (0, 0, 0)


def load_animation(input_dict: dict) -> list:
    sprite_sheet_image = pygame.image.load(input_dict["sprite_sheet_image"])
    sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)
    initial_step = input_dict["initial step"]
    animation_frames = []
    for i in range(0, input_dict["frame number"]):
        animation_frames.append(sprite_sheet.get_image(
            initial_step, width=input_dict["frame width"], height=input_dict["frame height"],
            scale=1, colour=BLACK
        ))
        initial_step += input_dict["step jump"]

    return animation_frames


if __name__ == "__main__":
    pygame.init()
    screen_width = 500
    screen_height = 500
    animation_cooldown = 150
    frame = 1
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('SpriteRunner')
    last_update = pygame.time.get_ticks()
    font = pygame.font.Font(None, 36)

    run = True
    while run:

        # update background
        screen.fill(BLACK)
        frame_text = font.render('Frame: ' + str(frame), True, (255, 255, 255))
        animation_list = load_animation(input_dict=z.walking_settings)
        print(len(animation_list))
        # update animation
        current_time = pygame.time.get_ticks()

        if current_time - last_update >= animation_cooldown:
            frame += 1
            last_update = current_time
            if frame >= len(animation_list):
                frame = 1
                initial_step = 0
        # show frame image
        screen.blit(animation_list[frame], (30, 30))
        screen.blit(frame_text, (300, 200))

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()
