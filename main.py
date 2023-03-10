import pygame
import os
import sys
import random

FPS = 50


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)

    return image


def terminate():
    pygame.quit()
    sys.exit()


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)


# class Tile(pygame.sprite.Sprite):
#     def __init__(self, tile_type, pos_x, pos_y):
#         super().__init__(all_sprites, tiles_group)
#         self.image = tile_images[tile_type]
#         self.rect = self.image.get_rect().move(
#             tile_width * pos_x, tile_height * pos_y)
#
#     def repait(self, img, y, x):
#         self.image = img
#         self.rect.x, self.rect.y = x, y


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites, player_group)
        self.radius = 5
        self.speed = 5
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("blue"),
                           (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect().move(10, 10)

    # def move(self, filename, pos):
    #
    #     for y in range(len(level_map)):
    #         if '@' in level_map[y]:
    #             x = level_map[y].find('@')
    #             break
    #     if (0 <= y + pos[1] < 11 and 0 <= x + pos[0] < 11) and \
    #             level_map[y + pos[1]][x + pos[0]] != '#':
    #         list_map = list(map(lambda z: z, level_map[y]))
    #         list_map[x] = '.'
    #         level_map[y] = ''.join(list_map)
    #         list_map_new = list(map(lambda z: z, level_map[y + pos[1]]))
    #         list_map_new[x + pos[0]] = '@'
    #         level_map[y + pos[1]] = ''.join(list_map_new)
    #
    #         out = (tile_width * pos[0], tile_height * pos[1])
    #         self.moves.append(out)
    #
    #         if pos[1] > 0:
    #             level_map.append(level_map[0])
    #             del level_map[0]
    #         elif pos[1] < 0:
    #             level_map.insert(0, level_map[-1])
    #             del level_map[-1]
    #         elif pos[0] > 0:
    #             for i in range(len(level_map)):
    #                 exm = list(map(str, level_map[i]))
    #                 level_map[i] = level_map[i][1:] + level_map[i][0]
    #         elif pos[0] < 0:
    #             for i in range(len(level_map)):
    #                 exm = list(map(str, level_map[i]))
    #                 level_map[i] = exm[-1] + level_map[i][:-1]
    #
    #     with open(filename, 'w') as mapFile:
    #         mapFile.write('\n'.join(level_map))

    def update(self, pos):
        print(pos)
        self.rect = self.rect.move((pos[0], pos[1]))
        print(self.rect)
        if pygame.sprite.spritecollideany(self, horizontal_borders) and pos[1] != 0:
            self.rect.y += (pos[1] * -1)
            print('-----------------------------------')

        if pygame.sprite.spritecollideany(self, vertical_borders) and pos[0] != 0:
            self.rect.x += (pos[0] * -1)
            print('===============================')
        print(self.rect)





# def generate_level(level, *args):
#     render_list = list() if not args else args[0]
#     new_player, x, y = None, None, None
#     for i in tiles_group:
#         tiles_group.remove(i)
#         all_sprites.remove(i)
#
#     for y in range(len(level)):
#         if not args:
#             render_list.append([])
#         for x in range(len(level[y])):
#             if level[y][x] == '.':
#                 render_list[y].append(Tile('empty', x, y))
#             elif level[y][x] == '#':
#                 render_list[y].append(Tile('wall', x, y))
#             elif not args and level[y][x] == '@':
#                 render_list[y].append(Tile('empty', x, y))
#                 new_player = Player(x, y)
#             elif args and level[y][x] == '@':
#                 args[1].rect.x = x * 50 + 15
#                 args[1].rect.y = y * 50 + 5
#                 render_list[y].append(Tile('empty', x, y))

    # return new_player, render_list


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.image.fill('red')
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.image.fill('red')
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


class Point(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites, point_group)
        self.radius = random.randint(3, 6)
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, (random.randint(20, 255), random.randint(20, 255), random.randint(20, 255)),
                           (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect().move(random.randint(10, SIZE_FIELD - 10), random.randint(10, SIZE_FIELD - 10))


def start_screen():
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры",
                  ""]

    screen2 = pygame.Surface(screen.get_size())

    fon = pygame.transform.scale(load_image('fon.jpg'), (width, height))
    screen2.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, True, 'black')
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen2.blit(string_rendered, intro_rect)

    player = None
    K_RIGHT = K_LEFT = K_UP = K_DOWN = False
    camera = Camera()

    starting = False
    BRAKING = None

    while True:
        pos = [0, 0]

        if starting:
            player = Player()
            Border(0, 0, SIZE_FIELD - 1, 0)
            Border(0, SIZE_FIELD - 1, SIZE_FIELD - 1, SIZE_FIELD - 1)
            Border(0, 0, 0, SIZE_FIELD - 1)
            Border(SIZE_FIELD - 1, 0, SIZE_FIELD - 1, SIZE_FIELD - 1)
            starting = False

            screen.fill('black')
            screen2 = pygame.Surface((SIZE_FIELD, SIZE_FIELD))

            screen2.fill('white', (10, 10, 1, 1))

            point_count = random.randint(100, 150)
            while point_count:
                Point()
                point_count -= 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if player:
                    if event.key == pygame.K_RIGHT:
                        K_RIGHT = True
                    elif event.key == pygame.K_LEFT:
                        K_LEFT = True
                    elif event.key == pygame.K_UP:
                        K_UP = True
                    elif event.key == pygame.K_DOWN:
                        K_DOWN = True

                if player is None:
                    starting = True
            elif event.type == pygame.KEYUP:
                if player:
                    if event.key == pygame.K_RIGHT:
                        K_RIGHT = False
                        BRAKING = [player.speed + player.radius, BRAKING[1] if BRAKING else 0]
                        print(BRAKING)
                    elif event.key == pygame.K_LEFT:
                        K_LEFT = False
                        BRAKING = [-1 * (player.speed + player.radius), BRAKING[1] if BRAKING else 0]
                    elif event.key == pygame.K_UP:
                        K_UP = False
                        BRAKING = [BRAKING[0] if BRAKING else 0, -1 * (player.speed + player.radius)]
                    elif event.key == pygame.K_DOWN:
                        K_DOWN = False
                        BRAKING = [BRAKING[0] if BRAKING else 0, player.speed + player.radius]
            elif event.type == pygame.MOUSEBUTTONUP:
                if player is None:
                    starting = True

        if K_UP:
            pos[1] = player.speed * -1
        elif K_DOWN:
            pos[1] = player.speed * 1
        if K_LEFT:
            pos[0] = player.speed * -1
        elif K_RIGHT:
            pos[0] = player.speed * 1

        if BRAKING:
            if BRAKING[0]:
                if BRAKING[0] > 0:
                    BRAKING[0] -= 1
                else:
                    BRAKING[0] += 1
            x = BRAKING[0]
            if BRAKING[1]:
                if BRAKING[1] > 0:
                    BRAKING[1] -= 1
                else:
                    BRAKING[1] += 1
            y = BRAKING[1]
            pos = [x, y]
            print(pos)
            if BRAKING == [0, 0]:
                BRAKING = None
        #
        if player:
            camera.update(player)
            for sprite in all_sprites:
                camera.apply(sprite)
            print(player.rect.x, player.rect.y)

        # tiles_group.draw(screen2)
        screen.blit(screen2, (0, 0))
        all_sprites.draw(screen)

        all_sprites.update(pos)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Перемещение героя. Новый уровень')
    size = width, height = 1000, 700
    screen = pygame.display.set_mode(size)

    clock = pygame.time.Clock()

    SIZE_FIELD = 1700

    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    vertical_borders = pygame.sprite.Group()
    horizontal_borders = pygame.sprite.Group()
    point_group = pygame.sprite.Group()

    start_screen()