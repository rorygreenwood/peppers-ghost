from random import choice

import pygame
import os

BG = (50, 50, 50)
BLACK = (0, 0, 0)


def load_animation(character: str,
                   state: str,
                   flipped: bool) -> list:
    animation_frames = []

    states = ['idle', 'walking', 'punch']
    characters = os.listdir('sprite_frames')

    assert state in states
    assert character in characters

    filestring = 'sprite_frames/{}/{}'.format(character, state)
    # ascertain whether to make the animations invert horizontally
    for image in os.listdir(filestring):
        sprite_image = pygame.image.load(os.path.join(filestring, image))
        if flipped:
            sprite_image = pygame.transform.flip(sprite_image, True, False)
        animation_frames.append(sprite_image)
    return animation_frames


if __name__ == "__main__":
    pygame.init()
    screen_width = 200
    screen_height = 200
    animation_cooldown = 150
    frame = 0
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('SpriteRunner')
    last_update = pygame.time.get_ticks()
    states = ['idle', 'walking', 'punch']
    run = True
    state = choice(states)
    flipped = choice([False])
    while run:
        # update animation list
        animation_list = load_animation(character='sakazuki',
                                        state=state, flipped=flipped)

        # update animation
        current_time = pygame.time.get_ticks()

        # play each frame of the animation
        if current_time - last_update >= animation_cooldown:
            frame += 1
            last_update = current_time

            # once complete, determine new choice and if to flip on x-axis
            if frame >= len(animation_list):
                frame = 0
                state = choice(states)
                flipped = choice([False])

        screen.fill(BLACK)
        animation_frame = animation_list[frame]
        animation_rect = animation_frame.get_rect()

        # show frame image
        screen.blit(animation_frame, (screen_width - animation_rect.right,
                                      screen_height - animation_rect.bottom))
        pygame.display.update()

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.quit()
