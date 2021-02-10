import pygame
import os
import sys
import requests


API_KEY = '2854f8b4-6b52-4eed-a5f0-80ce99c60326'
SIZE = WIDTH, HEIGHT = 600, 450


def image(longitude, lattitude, delta):
    # Собираем параметры для запроса к StaticMapsAPI:
    map_params = {
        "ll": ",".join([longitude, lattitude]),
        "spn": ",".join([delta, delta]),
        "l": "map"
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    # ... и выполняем запрос
    response = requests.get(map_api_server, params=map_params)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)

    return map_file


def main():
    pygame.init()
    pygame.display.set_caption('MAP')
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    print('координаты: ', end='')
    longitude, lattitude = input().split(', ')
    print('масштаб: ', end='')
    delta = input()

    map_file = image(longitude, lattitude, delta)
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os.remove(map_file)
                running = False
                pygame.quit()


if __name__ == '__main__':
    main()