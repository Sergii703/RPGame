from Character import *


class Mob(Character):

    def __init__(self, game, name, x_start, y_start, dir, image_pack, speed):
        Character.__init__(self, game, name, x_start, y_start, dir, image_pack, speed)


class Demon(Mob):
    def __init__(self, game, x_start, y_start, dir):
        self.image_pack = ['pic/demonr.png', 'pic/demond.png', 'pic/demonl.png', 'pic/demonu.png']
        Mob.__init__(self, game, 'Demon', x_start, y_start, dir, self.image_pack, speed=2)
