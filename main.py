import pygame
import os
import sys
import requests


API_KEY = '2854f8b4-6b52-4eed-a5f0-80ce99c60326'
SIZE = WIDTH, HEIGHT = 1000, 700


def get_image(longitude, lattitude, delta):
    # Собираем параметры для запроса к StaticMapsAPI:
    map_params = {
        "ll": ",".join([longitude, lattitude]),
        "spn": ",".join([delta, delta]),
        "l": "map",
        'size': '600,450',
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    # ... и выполняем запрос
    response = requests.get(map_api_server, params=map_params)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)

    return map_file


def draw_img(file, screen):
    img = pygame.image.load(file)
    img = pygame.transform.scale(img, (1000, 700))
    screen.blit(img, (0, 0))
    pygame.display.flip()


def draw_layer_maps(screen):
    button_1 = pygame.Rect(0, 0, 250, 50)
    pygame.draw.rect(screen, (255, 120, 120), button_1)


def main():
    pygame.init()
    pygame.display.set_caption('MAP')
    screen = pygame.display.set_mode(SIZE)

    print('координаты: ', end='')
    longitude, lattitude = '37.530887, 55.703118'.split(', ')
    print('масштаб: ', end='')
    delta = '0.03'

    map_file = get_image(longitude, lattitude, delta)

    running = True
    while running:
        screen.fill((0, 255, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os.remove(map_file)
                running = False

        # draw_img(map_file, screen)
        # draw_layer_maps(screen)
        # pygame.draw.rect(screen, (200, 200, 200), (0, 0, 1000, 20))


if __name__ == '__main__':
    main()
    pygame.quit()