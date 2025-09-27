import math
import time

import engine
from engine.events import *
from engine.operators import *
from engine.types import *


@sprite('Stage')
class Stage(Target):
    """Sprite Stage"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 0
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "None", [
            {
                'name': "backdrop1",
                'path': "cd21514d0531fdffb22204e0ec5ed84a.svg",
                'center': (240, 180),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "pop",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])

        self.var_tableX = 0
        self.var_speed = 288.5000000000007
        self.var_acceleration = 0.3
        self.var_friction = 0



        self.sprite.layer = 0




@sprite('red')
class Spritered(Target):
    """Sprite red"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -65
        self._ypos = -7
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 125, "all around", [
            {
                'name': "front1",
                'path': "574df75638e438128433a157c195bd16.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "front2",
                'path': "798d56864b5546b797aa7fe53b6a7196.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "front3",
                'path': "d4a056d7d1dc738627a32abcb24dbd04.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "back3",
                'path': "f0179af87e086cc427ffddbb1c84d6e7.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "back1",
                'path': "854dda29df1cf3581e1d147a89742676.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "back2",
                'path': "1074f83649e83adcfd18d2503fced006.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "right3",
                'path': "1ed3b45c877d9ddf08948e3c32cf932e.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "right1",
                'path': "dbd8e01c0f6924e79605dccc6af0cb67.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "right2",
                'path': "bc0185cbdb0be5e6a5605d8b10379c25.png",
                'center': (32, 32),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [

        ])





        self.sprite.layer = 1




@sprite('blue')
class Spriteblue(Target):
    """Sprite blue"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 245
        self._ypos = 45
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           6, 125, "don't rotate", [
            {
                'name': "front_walk1",
                'path': "65aba051701c859896ace011e7a35e1d.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "front_stand",
                'path': "310457860e9386ac6f4a0399f1b836fa.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "front_walk2",
                'path': "9875b532b967c64fe3841e0a5806de43.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "back_walk1",
                'path': "833e0461a30031aa0ce27c38ec78b42b.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "back_stand",
                'path': "62d4bed595eb7fdb7ca2e40c6d0ddcc0.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "back_walk2",
                'path': "bb68f37b4488ff9a87f49f2c3f071acc.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "right_walk1",
                'path': "3f3c58e261712b3f3d2fec25b1974338.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "right_walk2",
                'path': "7bafb3fb839b8722392a98054dcf7563.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "right_stand",
                'path': "e2e0bce80d3bd1ec86255172a024f869.png",
                'center': (32, 32),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [

        ])

        self.var_heading_direction = "right"
        self.var_moving = 0



        self.sprite.layer = 3

    @on_green_flag
    async def green_flag(self, util):
        self.costume.rotation_style = 'don\'t rotate'
        self.costume.size = 125
        while True:
            if util.inputs["w"]:
                self.var_heading_direction = "up"
                self.ypos += 3
            else:
                if util.inputs["a"]:
                    self.var_heading_direction = "left"
                    self.direction = -90
                    self.xpos += (util.sprites.stage.var_speed * -1)
                    if lt(util.sprites.stage.var_speed, abs(5)):
                        util.sprites.stage.var_speed += util.sprites.stage.var_acceleration
                else:
                    if util.inputs["d"]:
                        self.var_heading_direction = "right"
                        self.direction = 90
                        self.xpos += util.sprites.stage.var_speed
                        if lt(util.sprites.stage.var_speed, abs(5)):
                            util.sprites.stage.var_speed += util.sprites.stage.var_acceleration
                    else:
                        if util.inputs["s"]:
                            self.var_heading_direction = "down"
                            self.ypos += -3
                        else:
                            util.sprites.stage.var_speed = 0

            await self.yield_()

    @on_green_flag
    async def green_flag1(self, util):
        util.sprites.stage.var_acceleration = 0.3
        util.sprites.stage.var_speed = 0
        while True:
            if self.get_touching(util, "table"):
                self.xpos = (util.sprites.stage.var_tableX - 14)

            await self.yield_()

    @on_green_flag
    async def green_flag2(self, util):
        while True:
            if eq(self.var_heading_direction, "up"):
                pass

            await self.yield_()


@sprite('yellow')
class Spriteyellow(Target):
    """Sprite yellow"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -118
        self._ypos = -10
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 125, "all around", [
            {
                'name': "tile018",
                'path': "55f4a5d6d3542705e9f3b0881d1880fa.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "tile019",
                'path': "34eae7cf1c7e2de784ed3a49aeb7bfe0.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "tile020",
                'path': "2277b446c37ed7737bb4a8171a691fee.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "tile021",
                'path': "8b77d63cfc2485c79531b6fe222d8151.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "tile022",
                'path': "9a4bcd65acc4f548141e6086b4c74832.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "tile023",
                'path': "95a1b258cbba8f5bf479a2b064639c36.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "tile024",
                'path': "44cf3e42df4a96a7253d77acd5229884.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "tile025",
                'path': "05ecf4f13674b84ac7f3d35be4ce4464.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "tile026",
                'path': "6ba596758bd5c2748b9567185a39774d.png",
                'center': (32, 32),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [

        ])





        self.sprite.layer = 2

    @on_green_flag
    async def green_flag(self, util):
        self.costume.size = 125
        while True:
            if util.inputs["up arrow"]:
                self.ypos += 3
            else:
                if util.inputs["left arrow"]:
                    self.xpos += -3
                else:
                    if util.inputs["right arrow"]:
                        self.xpos += 3
                    else:
                        if util.inputs["down arrow"]:
                            self.ypos += -3

            await self.yield_()


@sprite('table')
class Spritetable(Target):
    """Sprite table"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 0
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "table (1)",
                'path': "2765dcf0234a41b6fa449ec90b51c2fb.png",
                'center': (9, 12),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [

        ])





        self.sprite.layer = 4

    @on_green_flag
    async def green_flag(self, util):
        util.sprites.stage.var_friction = 0.95
        self.gotoxy(0, 0)
        while True:
            util.sprites.stage.var_tableX = self.xpos

            await self.yield_()

    @on_green_flag
    async def green_flag1(self, util):
        while True:
            if self.get_touching(util, "blue"):
                self.xpos += util.sprites.stage.var_speed
                util.sprites.stage.var_speed += util.sprites.stage.var_acceleration
                util.sprites.stage.var_speed = (util.sprites.stage.var_speed * util.sprites.stage.var_friction)

            await self.yield_()




if __name__ == '__main__':
    engine.start_program()
