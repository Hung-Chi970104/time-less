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
           2, 100, "None", [
            {
                'name': "backdrop1",
                'path': "cd21514d0531fdffb22204e0ec5ed84a.svg",
                'center': (240, 180),
                'scale': 2
            },
            {
                'name': "3",
                'path': "903d1c68c0bb3b143165ac0ceb0d8779.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "",
                'path': "bdfb2ac558f5684ac798f3638c09f932.svg",
                'center': (268, 180),
                'scale': 1
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
        self.var_speed = 0
        self.var_acceleration = 0.3
        self.var_friction = 0.95
        self.var_walkingFrame = 0
        self.var_gravitationalacceleration = 0
        self.var_downwardspeed = 0



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
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           14, 125, "all around", [
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
            },
            {
                'name': "",
                'path': "c6756be332b7e5d6c558af3beed62b09.png",
                'center': (16, 20),
                'scale': 2
            },
            {
                'name': "2",
                'path': "f60a099726199ee5bf73f698bbc3d3c1.png",
                'center': (16, 20),
                'scale': 2
            },
            {
                'name': "3",
                'path': "f8c764261e1c75e9b173b1abdc022015.png",
                'center': (16, 20),
                'scale': 2
            },
            {
                'name': "4",
                'path': "65abb7c836e84f0dbb2152f620f05eb9.png",
                'center': (16, 20),
                'scale': 2
            },
            {
                'name': "5",
                'path': "86a1422fb87bf331a14d6f345d54b23b.png",
                'center': (16, 20),
                'scale': 2
            },
            {
                'name': "6",
                'path': "ca5de5245e030bb44c6e2f8cd12db393.png",
                'center': (16, 20),
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

        self._xpos = 111.63701412680314
        self._ypos = 51
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           9, 125, "left-right", [
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
            },
            {
                'name': "",
                'path': "19e26bdd3d058067798e5163b4b75c6b.png",
                'center': (17, 21),
                'scale': 2
            },
            {
                'name': "2",
                'path': "d77749c16e7acc699f7f256705b37e8f.png",
                'center': (17, 21),
                'scale': 2
            },
            {
                'name': "3",
                'path': "c1a0bedd21353858d1de76325e60986e.png",
                'center': (16, 20),
                'scale': 2
            },
            {
                'name': "4",
                'path': "0a447791758a6840f21df275d8fbd906.png",
                'center': (16, 20),
                'scale': 2
            },
            {
                'name': "5",
                'path': "8e7cb5fa8b5fa62101eb86fd47705422.png",
                'center': (16, 20),
                'scale': 2
            },
            {
                'name': "6",
                'path': "fa4d35ef341519280f785b73ba0600a1.png",
                'center': (16, 20),
                'scale': 2
            },
            {
                'name': "7",
                'path': "3522bbc838d1eeb42c373976a9d1970b.png",
                'center': (16, 20),
                'scale': 2
            },
            {
                'name': "8",
                'path': "aae78f43a71b994c3b3829851f07ed37.png",
                'center': (16, 20),
                'scale': 2
            },
            {
                'name': "9",
                'path': "401dd966e283a4ea7b2e5322091a73db.png",
                'center': (16, 20),
                'scale': 2
            },
            {
                'name': "10",
                'path': "ef148eda63aa09827efb1a24e7c98f70.png",
                'center': (16, 20),
                'scale': 2
            },
            {
                'name': "11",
                'path': "a0611caee4bbc37ced4240dbf0bb7c86.png",
                'center': (16, 20),
                'scale': 2
            },
            {
                'name': "12",
                'path': "57ede8d2ab9eba7a316afd6101faba88.png",
                'center': (16, 20),
                'scale': 2
            },
            {
                'name': "13",
                'path': "9da003d467d96a5f6f9472c0b76e1177.png",
                'center': (16, 20),
                'scale': 2
            },
            {
                'name': "14",
                'path': "040536dce74a3b73b9d9f5c8166ec475.png",
                'center': (16, 20),
                'scale': 2
            },
            {
                'name': "15",
                'path': "554990957f2fdd2abcf01fad2c8e85db.png",
                'center': (16, 20),
                'scale': 2
            },
            {
                'name': "16",
                'path': "95d5c8bf868cfae5288d64dfeea228d9.png",
                'center': (16, 20),
                'scale': 2
            },
            {
                'name': "17",
                'path': "90f1afe4f15e8fa5e9212b5d5a0004b8.png",
                'center': (16, 20),
                'scale': 2
            },
            {
                'name': "18",
                'path': "9300e0fd9074b224e43b7bdcf3595d15.png",
                'center': (16, 20),
                'scale': 2
            },
            {
                'name': "19",
                'path': "d559bc43e3677db73b9f94f7d3bee9c7.png",
                'center': (16, 20),
                'scale': 2
            },
            {
                'name': "20",
                'path': "05af998edd36bb3f9029df104d181d0e.png",
                'center': (16, 20),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [

        ])

        self.var_heading_direction = "up"



        self.sprite.layer = 3

    @on_green_flag
    async def green_flag(self, util):
        self.costume.size = 125
        self.costume.rotation_style = 'left-right'
        while True:
            if util.inputs["w"]:
                self.var_heading_direction = "up"
                self.ypos += 3
            else:
                if util.inputs["a"]:
                    self.direction = -90
                    self.xpos += -3
                else:
                    if util.inputs["d"]:
                        self.direction = 90
                        self.xpos += 3
                    else:
                        if util.inputs["s"]:
                            self.ypos += -3

            await self.yield_()

    @on_green_flag
    async def green_flag1(self, util):
        while True:
            if (util.inputs["a"] or util.inputs["d"]):
                self.costume.switch("right_walk1")
            else:
                if util.inputs["w"]:
                    self.costume.switch("back_walk1")
                else:
                    if util.inputs["s"]:
                        self.costume.switch("front_walk1")

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
        self.shown = False
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
