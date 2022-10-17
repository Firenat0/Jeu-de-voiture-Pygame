import pygame
import pytmx
import pyscroll

from player import Player

class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((1000, 1000))
        pygame.display.set_caption("projet")

        tmx_data = pytmx.util_pygame.load_pygame('maps/Map 1.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 1.25

        player_position = tmx_data.get_object_by_name("spawn 1")
        self.player = Player(player_position.x, player_position.y)

        self.walls = []
        self.finish = []

        for object in tmx_data.objects:
            if object.type == "collision":
                self.walls.append(pygame.Rect(object.x,object.y,object.width,object.height))
            if object.type == "finish":
                self.finish.append(pygame.Rect(object.x,object.y,object.width,object.height))

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.group.add(self.player)

    def handle_input(self):
        pressed=pygame.key.get_pressed()

        if pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation('right')
            self.player.speed_high = 4
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation('left')
            self.player.speed_high = 4
        else:
            self.player.move_high()
            self.player.change_animation('high')
            self.player.speed_high = 2.5

    def update(self):
        self.group.update()
        for sprite in self.group.sprites():
            if sprite.hitbox.collidelist(self.walls) >-1 :
                sprite.move_back()
                self.player.move_down()

            if sprite.hitbox.collidelist(self.finish) >-1 :
                self.__init__()

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            self.player.location()
            self.handle_input()
            self.update()
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)
            pygame.display.flip()
            self.player.move_high()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            clock.tick(60)
        pygame.quit()
