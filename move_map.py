import pygame

"""
3. Добавить обработку клавиш вверх/вниз/вправо/влево, по нажатию на которые перемещать центр карты
в соответствующую сторону на размер экрана. Также необходимо отслеживать предельные значения координат.
"""


if __name__ == '__main__':
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            key = pygame.key.get_pressed()
            if key[pygame.K_DOWN]:
                pass
            #    sprite.rect.top += 10
            elif key[pygame.K_UP]:
                pass
            #    sprite.rect.top -= 10
            if key[pygame.K_RIGHT]:
                pass
            #    sprite.rect.left += 10
            elif key[pygame.K_LEFT]:
                pass
            #    sprite.rect.left -= 10
