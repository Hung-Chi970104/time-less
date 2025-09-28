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
           1, 100, "None", [
            {
                'name': "2",
                'path': "5e36ca559a61ab1b7429aded59660276.svg",
                'center': (241, 239),
                'scale': 1
            },
            {
                'name': "",
                'path': "aa0fc50a5fdcb84576e92413d908e8ba.svg",
                'center': (358, 269),
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

        self.var_directionwhite = 90
        self.var_directionblack = -90
        self.var_lifewhite = 24
        self.var_lifeblack = 24
        self.var_processwhite = 1
        self.var_processblack = 1
        self.var_is_white_healing = "true"
        self.var_is_black_healing = "true"
        self.var_earth_health = 12
        self.var_game_start = "false"
        self.var_timer = 0



        self.sprite.layer = 0

    @on_green_flag
    async def green_flag(self, util):
        self.var_earth_health = 12
        while True:
            if ((lt(self.var_lifeblack, 1) or lt(self.var_lifewhite, 1)) or lt(self.var_earth_health, 1)):
                util.send_broadcast("game_over")
                util.stop_all()
                return None
            if gt(util.timer(), 67):
                util.send_broadcast("victory")
                util.stop_all()
                return None

            await self.yield_()


@sprite('rabbit-white')
class Spriterabbitwhite(Target):
    """Sprite rabbit-white"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 10
        self._ypos = 0
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           9, 200, "left-right", [
            {
                'name': "front_stand",
                'path': "b54bd7c0e26b62e990949a163eb2901f.png",
                'center': (48, 48),
                'scale': 2
            },
            {
                'name': "front_walk1",
                'path': "4bdb11b2529bfb1ca861634075214d2c.png",
                'center': (48, 48),
                'scale': 2
            },
            {
                'name': "front_walk2",
                'path': "ca47b10c00b0872121dabf81adb03233.png",
                'center': (48, 48),
                'scale': 2
            },
            {
                'name': "back_stand",
                'path': "d74da4d93f6307cced0828078e105a8b.png",
                'center': (48, 48),
                'scale': 2
            },
            {
                'name': "back_walk1",
                'path': "04c9fe536c38e460d66eb6c0128b716a.png",
                'center': (48, 48),
                'scale': 2
            },
            {
                'name': "back_walk2",
                'path': "03a084c05937eaca1bb9ea370b7bc07a.png",
                'center': (48, 48),
                'scale': 2
            },
            {
                'name': "left_stand",
                'path': "7574fa3b1f43e5fe8a391b97fb9f2ebf.png",
                'center': (48, 48),
                'scale': 2
            },
            {
                'name': "left_walk1",
                'path': "d199986838467420ad75d0677d4c57d8.png",
                'center': (48, 48),
                'scale': 2
            },
            {
                'name': "left_stand2",
                'path': "dc072eab8213402dbe0540fd74bf5ba8.png",
                'center': (48, 48),
                'scale': 2
            },
            {
                'name': "right_stand",
                'path': "67b2ba9cad3056cbf3ea9a09483ec65d.png",
                'center': (48, 48),
                'scale': 2
            },
            {
                'name': "right_walk1",
                'path': "37efbc86f1bf025fc5a24b3f7579f8ba.png",
                'center': (48, 48),
                'scale': 2
            },
            {
                'name': "right_walk2",
                'path': "4466120b01e7c98f1acad5b1c3fef21f.png",
                'center': (48, 48),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [

        ])





        self.sprite.layer = 15

    @on_green_flag
    async def green_flag(self, util):
        while True:
            if (eq(util.sprites.stage.var_directionwhite, 90) or eq(util.sprites.stage.var_directionwhite, -90)):
                if (util.inputs["left arrow"] or util.inputs["right arrow"]):
                    self.costume.switch("right_walk1")
                    await self.sleep(0.1)
                    self.costume.switch("right_walk2")
                    await self.sleep(0.1)
                else:
                    self.costume.switch("right_stand")
            else:
                if eq(util.sprites.stage.var_directionwhite, 0):
                    if util.inputs["up arrow"]:
                        self.costume.switch("back_walk1")
                        await self.sleep(0.1)
                        self.costume.switch("back_walk2")
                        await self.sleep(0.1)
                    else:
                        self.costume.switch("back_stand")
                else:
                    if eq(util.sprites.stage.var_directionwhite, 180):
                        if util.inputs["down arrow"]:
                            self.costume.switch("front_walk1")
                            await self.sleep(0.1)
                            self.costume.switch("front_walk2")
                            await self.sleep(0.1)
                        else:
                            self.costume.switch("front_stand")

            await self.yield_()

    @on_green_flag
    async def green_flag1(self, util):
        self.gotoxy(10, 0)
        util.sprites.stage.var_lifewhite = 24
        util.sprites.stage.var_directionwhite = 90
        self.costume.size = 200
        self.costume.rotation_style = 'left-right'
        while True:
            if not util.inputs["space"]:
                if util.inputs["up arrow"]:
                    util.sprites.stage.var_directionwhite = 0
                    self.ypos += 3
                else:
                    if util.inputs["left arrow"]:
                        util.sprites.stage.var_directionwhite = -90
                        self.xpos += -3
                    else:
                        if util.inputs["right arrow"]:
                            util.sprites.stage.var_directionwhite = 90
                            self.xpos += 3
                        else:
                            if util.inputs["down arrow"]:
                                util.sprites.stage.var_directionwhite = 180
                                self.ypos += -3
            self.direction = util.sprites.stage.var_directionwhite

            await self.yield_()

    @on_green_flag
    async def green_flag2(self, util):
        util.sprites.stage.var_is_white_healing = "true"
        while True:
            if self.get_touching(util, "tree"):
                if lt(util.sprites.stage.var_lifewhite, 24):
                    util.sprites.stage.var_lifewhite += 1
                    util.sprites.stage.var_is_white_healing = "true"
                    await self.sleep(1.5)
            else:
                util.sprites.stage.var_lifewhite += -1
                util.sprites.stage.var_is_white_healing = "false"
                await self.sleep(0.7)

            await self.yield_()


@sprite('rabbit-black')
class Spriterabbitblack(Target):
    """Sprite rabbit-black"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -10
        self._ypos = 0
        self._direction = -90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           9, 200, "left-right", [
            {
                'name': "front_stand",
                'path': "5b69d1f1ad95dbc6ce1a744a7c9f08f7.png",
                'center': (14, 16),
                'scale': 2
            },
            {
                'name': "front_walk1",
                'path': "54d50328abb63e7bea5e971fba578775.png",
                'center': (14, 16),
                'scale': 2
            },
            {
                'name': "front_walk2",
                'path': "6789c4cf1afedb3a5bc4efc4f768db43.png",
                'center': (14, 16),
                'scale': 2
            },
            {
                'name': "back_stand",
                'path': "e6ea2cf1e8e85b11318582ffc45cad3c.png",
                'center': (14, 16),
                'scale': 2
            },
            {
                'name': "back_walk1",
                'path': "18a3b971f7267c42b85e67dd064b131b.png",
                'center': (14, 16),
                'scale': 2
            },
            {
                'name': "back_walk2",
                'path': "8d522e041eef5630b0a4f85cfec531ec.png",
                'center': (14, 16),
                'scale': 2
            },
            {
                'name': "left_stand",
                'path': "f2489711f035c0661d10663c3adf2780.png",
                'center': (10, 16),
                'scale': 2
            },
            {
                'name': "left_walk1",
                'path': "873166f436c54929b21fc975651a7692.png",
                'center': (10, 16),
                'scale': 2
            },
            {
                'name': "left_stand2",
                'path': "40f92a5907f70a0dc4c0791e612eb58c.png",
                'center': (10, 16),
                'scale': 2
            },
            {
                'name': "right_stand",
                'path': "924b0d2bf31c6c92c678936fedc84f7e.png",
                'center': (10, 16),
                'scale': 2
            },
            {
                'name': "right_walk1",
                'path': "5d49eeaabac43b123c56b16aa4e4f752.png",
                'center': (10, 16),
                'scale': 2
            },
            {
                'name': "right_walk2",
                'path': "01d1533cc4ee9b5d9d33f95e74d64b13.png",
                'center': (10, 16),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [

        ])





        self.sprite.layer = 14

    @on_green_flag
    async def green_flag(self, util):
        while True:
            if (eq(util.sprites.stage.var_directionblack, 90) or eq(util.sprites.stage.var_directionblack, -90)):
                if (util.inputs["a"] or util.inputs["d"]):
                    self.costume.switch("right_walk1")
                    await self.sleep(0.1)
                    self.costume.switch("right_walk2")
                    await self.sleep(0.1)
                else:
                    self.costume.switch("right_stand")
            else:
                if eq(util.sprites.stage.var_directionblack, 0):
                    if util.inputs["w"]:
                        self.costume.switch("back_walk1")
                        await self.sleep(0.1)
                        self.costume.switch("back_walk2")
                        await self.sleep(0.1)
                    else:
                        self.costume.switch("back_stand")
                else:
                    if eq(util.sprites.stage.var_directionblack, 180):
                        if util.inputs["s"]:
                            self.costume.switch("front_walk1")
                            await self.sleep(0.1)
                            self.costume.switch("front_walk2")
                            await self.sleep(0.1)
                        else:
                            self.costume.switch("front_stand")

            await self.yield_()

    @on_green_flag
    async def green_flag1(self, util):
        self.gotoxy(-10, 0)
        util.sprites.stage.var_directionblack = -90
        util.sprites.stage.var_lifeblack = 24
        self.costume.size = 200
        self.costume.rotation_style = 'left-right'
        while True:
            if not util.inputs["q"]:
                if util.inputs["w"]:
                    util.sprites.stage.var_directionblack = 0
                    self.ypos += 3
                else:
                    if util.inputs["a"]:
                        util.sprites.stage.var_directionblack = -90
                        self.xpos += -3
                    else:
                        if util.inputs["d"]:
                            util.sprites.stage.var_directionblack = 90
                            self.xpos += 3
                        else:
                            if util.inputs["s"]:
                                util.sprites.stage.var_directionblack = 180
                                self.ypos += -3
            self.direction = util.sprites.stage.var_directionblack

            await self.yield_()

    @on_green_flag
    async def green_flag2(self, util):
        util.sprites.stage.var_is_black_healing = "true"
        while True:
            if self.get_touching(util, "tree"):
                if lt(util.sprites.stage.var_lifeblack, 24):
                    util.sprites.stage.var_lifeblack += 1
                    util.sprites.stage.var_is_black_healing = "true"
                    await self.sleep(1.5)
            else:
                util.sprites.stage.var_lifeblack += -1
                util.sprites.stage.var_is_black_healing = "false"
                await self.sleep(0.7)

            await self.yield_()


@sprite('rain')
class Spriterain(Target):
    """Sprite rain"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 8
        self._ypos = 0
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 250, "all around", [
            {
                'name': "1",
                'path': "3887928583bc5686ea6c3d395e60ddc4.png",
                'center': (1, 7),
                'scale': 2
            },
            {
                'name': "2",
                'path': "19cbf39aa7479f3345a382926d3a2dfa.png",
                'center': (10, 7),
                'scale': 2
            },
            {
                'name': "3",
                'path': "fafd35bc38bbc9375244ec78e198994a.png",
                'center': (12, -1),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [

        ])





        self.sprite.layer = 5

    @on_green_flag
    async def green_flag(self, util):
        self.shown = False
        while True:
            for _ in range(toint(pick_rand(5, 20))):
                self.create_clone_of(util, "_myself_")

                await self.yield_()
            await self.sleep(0.1)

            await self.yield_()

    @on_clone_start
    async def clone_start(self, util):
        self.shown = True
        self.ypos = 240
        self.xpos = pick_rand(-240, 240)
        self.costume.switch(1)
        for _ in range(toint(pick_rand(5, 40))):
            self.ypos += -10

            await self.yield_()
        self.costume.switch(2)
        await self.sleep(0.1)
        self.costume.switch(3)
        await self.sleep(0.1)
        self.delete_clone(util)


@sprite('dirt-white')
class Spritedirtwhite(Target):
    """Sprite dirt-white"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 30
        self._ypos = -10
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 150, "don't rotate", [
            {
                'name': "1",
                'path': "e81d7670868792b7b539dcfd11c7133a.png",
                'center': (6, 5),
                'scale': 2
            },
            {
                'name': "2",
                'path': "c580b487d3768b5ebe24ab5308faaf6a.png",
                'center': (6, 4),
                'scale': 2
            },
            {
                'name': "3",
                'path': "493d35c2f83bb4fb0149115b086c235f.png",
                'center': (11, 6),
                'scale': 2
            },
            {
                'name': "4",
                'path': "f1a1d08d62da9cc6274ea0c37ca5be57.png",
                'center': (12, 8),
                'scale': 2
            },
            {
                'name': "5",
                'path': "8e6db4c56049e07066809b01f772e83f.png",
                'center': (15, 10),
                'scale': 2
            },
            {
                'name': "6",
                'path': "cbd2aabb2ede40e96c92bbe86a0be6ac.png",
                'center': (15, 10),
                'scale': 2
            },
            {
                'name': "7",
                'path': "09584bd5cad8a8470095e44d93821c3c.png",
                'center': (14, 16),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [

        ])





        self.sprite.layer = 13

    @on_green_flag
    async def green_flag(self, util):
        self.costume.size = 150
        self.costume.rotation_style = 'don\'t rotate'
        while True:
            self.goto(util, "rabbit-white")
            if (eq(util.sprites.stage.var_directionwhite, 0) or eq(util.sprites.stage.var_directionwhite, 180)):
                self.direction = util.sprites.stage.var_directionwhite
                self.move(20)
            if (eq(util.sprites.stage.var_directionwhite, 90) or eq(util.sprites.stage.var_directionwhite, -90)):
                self.direction = util.sprites.stage.var_directionwhite
                self.move(20)
                self.ypos += -10

            await self.yield_()

    @on_green_flag
    async def green_flag1(self, util):
        util.sprites.stage.var_processwhite = 1
        while True:
            if util.inputs["space"]:
                if ((not eq(self.costume.number, 7) and eq(util.sprites.stage.var_is_white_healing, "false")) and not self.get_touching(util, "seed-white")):
                    util.sprites.stage.var_processwhite += 1
                    await self.sleep(0.5)
            else:
                util.sprites.stage.var_processwhite = 1
            self.costume.switch(util.sprites.stage.var_processwhite)

            await self.yield_()

    @on_clone_start
    async def clone_start(self, util):
        self.costume.switch(7)
        self.shown = True

    @on_green_flag
    async def green_flag2(self, util):
        while True:
            if eq(self.costume.number, 7):
                self.create_clone_of(util, "_myself_")
                while not not eq(self.costume.number, 7):
                    await self.yield_()

            await self.yield_()


@sprite('dirt-black')
class Spritedirtblack(Target):
    """Sprite dirt-black"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -30
        self._ypos = -9.999999999999998
        self._direction = -90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 150, "don't rotate", [
            {
                'name': "1",
                'path': "e81d7670868792b7b539dcfd11c7133a.png",
                'center': (6, 5),
                'scale': 2
            },
            {
                'name': "2",
                'path': "c580b487d3768b5ebe24ab5308faaf6a.png",
                'center': (6, 4),
                'scale': 2
            },
            {
                'name': "3",
                'path': "493d35c2f83bb4fb0149115b086c235f.png",
                'center': (11, 6),
                'scale': 2
            },
            {
                'name': "4",
                'path': "f1a1d08d62da9cc6274ea0c37ca5be57.png",
                'center': (12, 8),
                'scale': 2
            },
            {
                'name': "5",
                'path': "8e6db4c56049e07066809b01f772e83f.png",
                'center': (15, 10),
                'scale': 2
            },
            {
                'name': "6",
                'path': "cbd2aabb2ede40e96c92bbe86a0be6ac.png",
                'center': (15, 10),
                'scale': 2
            },
            {
                'name': "7",
                'path': "09584bd5cad8a8470095e44d93821c3c.png",
                'center': (14, 16),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [

        ])





        self.sprite.layer = 4

    @on_green_flag
    async def green_flag(self, util):
        util.sprites.stage.var_processblack = 1
        while True:
            if util.inputs["q"]:
                if (not eq(self.costume.number, 7) and eq(util.sprites.stage.var_is_black_healing, "false")):
                    util.sprites.stage.var_processblack += 1
                    await self.sleep(0.5)
            else:
                util.sprites.stage.var_processblack = 1
            self.costume.switch(util.sprites.stage.var_processblack)

            await self.yield_()

    @on_green_flag
    async def green_flag1(self, util):
        self.costume.rotation_style = 'don\'t rotate'
        self.costume.size = 150
        while True:
            self.goto(util, "rabbit-black")
            if (eq(util.sprites.stage.var_directionblack, 0) or eq(util.sprites.stage.var_directionblack, 180)):
                self.direction = util.sprites.stage.var_directionblack
                self.move(20)
            if (eq(util.sprites.stage.var_directionblack, 90) or eq(util.sprites.stage.var_directionblack, -90)):
                self.direction = util.sprites.stage.var_directionblack
                self.move(20)
                self.ypos += -10

            await self.yield_()

    @on_green_flag
    async def green_flag2(self, util):
        while True:
            if eq(self.costume.number, 7):
                self.create_clone_of(util, "_myself_")
                while not not eq(self.costume.number, 7):
                    await self.yield_()

            await self.yield_()

    @on_clone_start
    async def clone_start(self, util):
        self.costume.switch(7)
        self.shown = True


@sprite('seed-white')
class Spriteseedwhite(Target):
    """Sprite seed-white"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 30
        self._ypos = -10
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "tree-0",
                'path': "19987dee170644f365628cf1f6910d48.png",
                'center': (7, 5),
                'scale': 2
            },
            {
                'name': "tree-1",
                'path': "d2c6c6f7bb46f4c85cb273d3f4073071.png",
                'center': (12, 4),
                'scale': 2
            },
            {
                'name': "tree-3",
                'path': "bda46b82ec858ca5214599683e68c9c4.png",
                'center': (14, 5),
                'scale': 2
            },
            {
                'name': "tree-2",
                'path': "0dbcbdb87df7e1583573d53f8645f2db.png",
                'center': (8, 14),
                'scale': 2
            },
            {
                'name': "tree-4",
                'path': "d1493e63f26778acb78a4496ec54ca40.png",
                'center': (8, 25),
                'scale': 2
            },
            {
                'name': "tree-5",
                'path': "e244083f34f10cdf1163f94bd6e8fde3.png",
                'center': (11, 44),
                'scale': 2
            },
            {
                'name': "tree-6",
                'path': "b3ca1b70da7bccfbbbce28c57144ee2c.png",
                'center': (18, 55),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [

        ])





        self.sprite.layer = 2

    @on_green_flag
    async def green_flag(self, util):
        self.costume.switch("tree-0")
        self.shown = False
        self.costume.size = 100
        while True:
            self.goto(util, "dirt-white")
            if eq(util.sprites.stage.var_processwhite, 7):
                self.create_clone_of(util, "_myself_")
                while not not eq(util.sprites.stage.var_processwhite, 7):
                    await self.yield_()

            await self.yield_()

    @on_clone_start
    async def clone_start(self, util):
        util.sprites.stage.var_earth_health += 1
        self.shown = True
        self.ypos += -1
        while not eq(self.costume.number, 7):
            await self.sleep(5)
            self.costume.next()
            if (lt(util.sprites.stage.var_earth_health, 12) and gt(pick_rand(0, 2), 1)):
                util.sprites.stage.var_earth_health += 1

            await self.yield_()


@sprite('seed-black')
class Spriteseedblack(Target):
    """Sprite seed-black"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -30
        self._ypos = -9.999999999999998
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "tree-0",
                'path': "19987dee170644f365628cf1f6910d48.png",
                'center': (7, 5),
                'scale': 2
            },
            {
                'name': "tree-1",
                'path': "d2c6c6f7bb46f4c85cb273d3f4073071.png",
                'center': (12, 4),
                'scale': 2
            },
            {
                'name': "tree-3",
                'path': "bda46b82ec858ca5214599683e68c9c4.png",
                'center': (14, 5),
                'scale': 2
            },
            {
                'name': "tree-2",
                'path': "0dbcbdb87df7e1583573d53f8645f2db.png",
                'center': (8, 14),
                'scale': 2
            },
            {
                'name': "tree-4",
                'path': "d1493e63f26778acb78a4496ec54ca40.png",
                'center': (8, 25),
                'scale': 2
            },
            {
                'name': "tree-5",
                'path': "e244083f34f10cdf1163f94bd6e8fde3.png",
                'center': (11, 44),
                'scale': 2
            },
            {
                'name': "tree-6",
                'path': "b3ca1b70da7bccfbbbce28c57144ee2c.png",
                'center': (18, 55),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [

        ])





        self.sprite.layer = 3

    @on_green_flag
    async def green_flag(self, util):
        self.costume.switch("tree-0")
        self.shown = False
        self.costume.size = 100
        while True:
            self.goto(util, "dirt-black")
            if eq(util.sprites.stage.var_processblack, 7):
                self.create_clone_of(util, "_myself_")
                while not not eq(util.sprites.stage.var_processblack, 7):
                    await self.yield_()

            await self.yield_()

    @on_clone_start
    async def clone_start(self, util):
        util.sprites.stage.var_earth_health += 1
        self.shown = True
        self.ypos += -1
        while not eq(self.costume.number, 7):
            await self.sleep(7)
            self.costume.next()
            if (lt(util.sprites.stage.var_earth_health, 12) and gt(pick_rand(0, 2), 1)):
                util.sprites.stage.var_earth_health += 1

            await self.yield_()


@sprite('tree')
class Spritetree(Target):
    """Sprite tree"""

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
           9, 100, "all around", [
            {
                'name': "tree-4",
                'path': "1c8af19fb86670883b927d96cb563841.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "tree-3",
                'path': "5ac697fdb615e9ffbbc9b8ef4394ef1e.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "tree-2",
                'path': "d6905a21a02e5b2d5f179f0f9184e3e5.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "tree-1",
                'path': "cb9179e5564cee1741474691a7d20ea4.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "tree-5",
                'path': "1145ef405af6bddcf20182b4cba7631e.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "tree-6b",
                'path': "5e7e318096f194d517fb0c06f0c1d05e.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "tree-6a",
                'path': "b88859d5b82c80211771bd3b3128bc5b.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "tree-6c",
                'path': "5052fb40ef0ec1c5b067eff8210a89ba.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "tree-6d",
                'path': "46c8e011240977f1b0ef3707240f48e1.png",
                'center': (32, 32),
                'scale': 2
            },
            {
                'name': "tree-7",
                'path': "cacd0864fe259146bb6518f54a1b7df2.png",
                'center': (62, 58),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [

        ])





        self.sprite.layer = 1

    @on_green_flag
    async def green_flag(self, util):
        self.back_layer(util)


@sprite('timer-white')
class Spritetimerwhite(Target):
    """Sprite timer-white"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 210
        self._ypos = 150
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           24, 60, "all around", [
            {
                'name': "0",
                'path': "ef08241af4ba26d3c04c3e19fa2c832d.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "1",
                'path': "a178282d3207c5851d666d9c8828122c.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "2",
                'path': "8cfbeb0082ebb5558161d36a5da90cb4.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "3",
                'path': "21022bbe41dc736dd7bb7dc80cf3b754.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "4",
                'path': "59318574304f49c2158f18e58105974d.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "5",
                'path': "d5a113cb9858e25bcd86d1e79b3de3dc.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "6",
                'path': "b65d367ab0f5d4bb2458cb44d1301055.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "7",
                'path': "d403235400db3d735d99162ae5397946.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "8",
                'path': "5d58c6fdcb875fab4563531030eab98f.png",
                'center': (64, 81),
                'scale': 2
            },
            {
                'name': "9",
                'path': "04ddadf7b4b0678d4f159e1369bb2844.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "10",
                'path': "3ec7ea73f1411d8410b50c00af94d249.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "11",
                'path': "f7067ac612a47710e13c5286947f6f7f.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "12",
                'path': "8e021ea2450df1ed786833f7db553a9c.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "13",
                'path': "ed55e4a5d9827bf4da9dc92b3076e10b.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "14",
                'path': "7c4f8540391e9f765f7b13dae430497f.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "15",
                'path': "682b1a6c08c1c8b965960d33c5159ed4.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "16",
                'path': "eff0b4a6f29aced6d67f3b776e5adf08.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "17",
                'path': "4142761ef5de555dcf19538bb9e736ae.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "18",
                'path': "5b5339e2e83bf7b7d55c1dd3c1ca5e25.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "19",
                'path': "80bf266db687e5f4ebc0bcde395baa8e.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "20",
                'path': "89c480437799143bfb9adad4034475bb.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "21",
                'path': "c0b0e7c90fdca7f56e91aba64cba7a9c.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "22",
                'path': "1d8e150fd41f069981b4962a8635493e.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "23",
                'path': "4d6c0e2ae6160710ce0999e7813ac91a.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "24",
                'path': "1bb35468c2dd0595f6c8e52f60235f4e.png",
                'center': (64, 80),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [

        ])





        self.sprite.layer = 7

    @on_green_flag
    async def green_flag(self, util):
        self.gotoxy(210, 150)
        self.costume.switch(24)
        while True:
            self.costume.switch(util.sprites.stage.var_lifewhite)

            await self.yield_()


@sprite('timer-black')
class Spritetimerblack(Target):
    """Sprite timer-black"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -210
        self._ypos = 150
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           24, 60, "all around", [
            {
                'name': "0",
                'path': "ef08241af4ba26d3c04c3e19fa2c832d.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "1",
                'path': "a178282d3207c5851d666d9c8828122c.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "2",
                'path': "8cfbeb0082ebb5558161d36a5da90cb4.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "3",
                'path': "21022bbe41dc736dd7bb7dc80cf3b754.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "4",
                'path': "59318574304f49c2158f18e58105974d.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "5",
                'path': "d5a113cb9858e25bcd86d1e79b3de3dc.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "6",
                'path': "b65d367ab0f5d4bb2458cb44d1301055.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "7",
                'path': "d403235400db3d735d99162ae5397946.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "8",
                'path': "5d58c6fdcb875fab4563531030eab98f.png",
                'center': (64, 81),
                'scale': 2
            },
            {
                'name': "9",
                'path': "04ddadf7b4b0678d4f159e1369bb2844.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "10",
                'path': "3ec7ea73f1411d8410b50c00af94d249.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "11",
                'path': "f7067ac612a47710e13c5286947f6f7f.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "12",
                'path': "8e021ea2450df1ed786833f7db553a9c.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "13",
                'path': "ed55e4a5d9827bf4da9dc92b3076e10b.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "14",
                'path': "7c4f8540391e9f765f7b13dae430497f.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "15",
                'path': "682b1a6c08c1c8b965960d33c5159ed4.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "16",
                'path': "eff0b4a6f29aced6d67f3b776e5adf08.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "17",
                'path': "4142761ef5de555dcf19538bb9e736ae.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "18",
                'path': "5b5339e2e83bf7b7d55c1dd3c1ca5e25.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "19",
                'path': "80bf266db687e5f4ebc0bcde395baa8e.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "20",
                'path': "89c480437799143bfb9adad4034475bb.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "21",
                'path': "c0b0e7c90fdca7f56e91aba64cba7a9c.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "22",
                'path': "1d8e150fd41f069981b4962a8635493e.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "23",
                'path': "4d6c0e2ae6160710ce0999e7813ac91a.png",
                'center': (64, 80),
                'scale': 2
            },
            {
                'name': "24",
                'path': "1bb35468c2dd0595f6c8e52f60235f4e.png",
                'center': (64, 80),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [

        ])





        self.sprite.layer = 6

    @on_green_flag
    async def green_flag(self, util):
        self.gotoxy(-210, 150)
        self.costume.switch(24)
        while True:
            self.costume.switch(util.sprites.stage.var_lifeblack)

            await self.yield_()


@sprite('earth_health')
class Spriteearth_health(Target):
    """Sprite earth_health"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = -140
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "0",
                'path': "e3359454d56f388e78222417b3ceea6a.png",
                'center': (100, 29),
                'scale': 2
            },
            {
                'name': "1",
                'path': "f7911957c2bf52dff954b72dd42c325d.png",
                'center': (100, 29),
                'scale': 2
            },
            {
                'name': "2",
                'path': "5de0ff3538695215163747c312ebd4a4.png",
                'center': (100, 29),
                'scale': 2
            },
            {
                'name': "3",
                'path': "3398d0421d2abce0da0c222d744fb62e.png",
                'center': (100, 29),
                'scale': 2
            },
            {
                'name': "4",
                'path': "8008e744c31db2f45b583a8b5657f857.png",
                'center': (100, 29),
                'scale': 2
            },
            {
                'name': "5",
                'path': "e743a03086b3ea5c99098ee38dc1f0cb.png",
                'center': (100, 29),
                'scale': 2
            },
            {
                'name': "6",
                'path': "7ac019720beb3078dad409d735233bfe.png",
                'center': (100, 29),
                'scale': 2
            },
            {
                'name': "7",
                'path': "68f90200187ddf955f4e53b1ac853eab.png",
                'center': (100, 29),
                'scale': 2
            },
            {
                'name': "8",
                'path': "855d8c27880a77035beb3d9a2f3b8041.png",
                'center': (100, 29),
                'scale': 2
            },
            {
                'name': "10",
                'path': "fb18d2c42a228074e5f97c52939ef361.png",
                'center': (100, 29),
                'scale': 2
            },
            {
                'name': "11",
                'path': "11bff0132fec89b03e4777fa95b7edc2.png",
                'center': (100, 29),
                'scale': 2
            },
            {
                'name': "12",
                'path': "d6fed69b67d8758eb57704aee58ca064.png",
                'center': (100, 29),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [

        ])





        self.sprite.layer = 10

    @on_green_flag
    async def green_flag(self, util):
        while not eq(util.sprites.stage.var_game_start, "true"):
            await self.yield_()
        util.sprites.stage.var_earth_health = 12
        self.costume.switch(12)
        self.gotoxy(0, -140)
        while True:
            self.costume.switch(util.sprites.stage.var_earth_health)
            await self.sleep(1.5)
            util.sprites.stage.var_earth_health += -1

            await self.yield_()


@sprite('black')
class Spriteblack(Target):
    """Sprite black"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -8
        self._ypos = 25
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 80, "all around", [
            {
                'name': "costume1",
                'path': "5fdf66d26cd611c00ebae06c9965e4e8.svg",
                'center': (11, 19),
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





        self.sprite.layer = 9

    @on_green_flag
    async def green_flag(self, util):
        while True:
            self.goto(util, "rabbit-black")
            self.ypos += 25
            self.xpos += 2

            await self.yield_()

    @on_green_flag
    async def green_flag1(self, util):
        while True:
            if eq(util.sprites.stage.var_is_black_healing, "true"):
                self.shown = False
            else:
                self.shown = True

            await self.yield_()


@sprite('white')
class Spritewhite(Target):
    """Sprite white"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 12
        self._ypos = 25
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 80, "all around", [
            {
                'name': "costume1",
                'path': "d3fa6cad803083452cbda48d455c27e8.svg",
                'center': (15, 19),
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





        self.sprite.layer = 12

    @on_green_flag
    async def green_flag(self, util):
        while True:
            self.goto(util, "rabbit-white")
            self.ypos += 25
            self.xpos += 2

            await self.yield_()

    @on_green_flag
    async def green_flag1(self, util):
        while True:
            if eq(util.sprites.stage.var_is_white_healing, "true"):
                self.shown = False
            else:
                self.shown = True

            await self.yield_()


@sprite('intro')
class Spriteintro(Target):
    """Sprite intro"""

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
                'name': "intro (2)",
                'path': "1d96a91329d02ab93964be615888cde6.png",
                'center': (480, 360),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [

        ])





        self.sprite.layer = 20

    @on_green_flag
    async def green_flag(self, util):
        self.shown = True
        util.sprites.stage.var_game_start = "false"
        util.sprites.stage.var_timer = 0
        self.front_layer(util)
        self.gotoxy(0, 0)
        while True:
            if util.inputs.mouse_down:
                self.shown = False
                util.sprites.stage.var_game_start = "true"
                await self.sleep(1)
                while True:
                    if eq(util.sprites.stage.var_game_start, "true"):
                        util.sprites.stage.var_timer += 1
                        await self.sleep(1)

                    await self.yield_()

            await self.yield_()


@sprite('second (first)')
class Spritesecondfirst(Target):
    """Sprite second (first)"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 20
        self._ypos = 140
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           2, 200, "all around", [
            {
                'name': "0",
                'path': "71557be3e2642b4f90bfed41f517ec7e.svg",
                'center': (8, 19),
                'scale': 1
            },
            {
                'name': "1",
                'path': "9e6e7b0f321c327abf4700f60804d3f0.svg",
                'center': (4, 19),
                'scale': 1
            },
            {
                'name': "2",
                'path': "04efdce1b5cd4f69a4d0aff20aa44a9c.svg",
                'center': (8, 19),
                'scale': 1
            },
            {
                'name': "3",
                'path': "29fd0cae881311db4a7f0a034bc87791.svg",
                'center': (6, 19),
                'scale': 1
            },
            {
                'name': "4",
                'path': "f457734f85ac0129e1ca141a999d54d5.svg",
                'center': (8, 19),
                'scale': 1
            },
            {
                'name': "5",
                'path': "311f247658961ddf8d27dac83a4b5dfa.svg",
                'center': (8, 19),
                'scale': 1
            },
            {
                'name': "6",
                'path': "0bf009576c1a8d83b09359789304d460.svg",
                'center': (8, 19),
                'scale': 1
            },
            {
                'name': "7",
                'path': "7140a42f1d682b02537885325a487d39.svg",
                'center': (8, 19),
                'scale': 1
            },
            {
                'name': "8",
                'path': "20fd310e93d6df888f1568f1092534a5.svg",
                'center': (8, 19),
                'scale': 1
            },
            {
                'name': "9",
                'path': "f2d3f91670c8cb984c65a628a62e35bf.svg",
                'center': (8, 19),
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





        self.sprite.layer = 17

    @on_green_flag
    async def green_flag(self, util):
        self.gotoxy(20, 140)
        self.costume.switch(0)
        while True:
            self.costume.switch((((util.timer() % 10) - (util.timer() % 1)) + 1))

            await self.yield_()


@sprite('second (second)')
class Spritesecondsecond(Target):
    """Sprite second (second)"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -15
        self._ypos = 140
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 200, "all around", [
            {
                'name': "0",
                'path': "71557be3e2642b4f90bfed41f517ec7e.svg",
                'center': (8, 19),
                'scale': 1
            },
            {
                'name': "1",
                'path': "9e6e7b0f321c327abf4700f60804d3f0.svg",
                'center': (4, 19),
                'scale': 1
            },
            {
                'name': "2",
                'path': "04efdce1b5cd4f69a4d0aff20aa44a9c.svg",
                'center': (8, 19),
                'scale': 1
            },
            {
                'name': "3",
                'path': "29fd0cae881311db4a7f0a034bc87791.svg",
                'center': (6, 19),
                'scale': 1
            },
            {
                'name': "4",
                'path': "f457734f85ac0129e1ca141a999d54d5.svg",
                'center': (8, 19),
                'scale': 1
            },
            {
                'name': "5",
                'path': "311f247658961ddf8d27dac83a4b5dfa.svg",
                'center': (8, 19),
                'scale': 1
            },
            {
                'name': "6",
                'path': "0bf009576c1a8d83b09359789304d460.svg",
                'center': (8, 19),
                'scale': 1
            },
            {
                'name': "7",
                'path': "7140a42f1d682b02537885325a487d39.svg",
                'center': (8, 19),
                'scale': 1
            },
            {
                'name': "8",
                'path': "20fd310e93d6df888f1568f1092534a5.svg",
                'center': (8, 19),
                'scale': 1
            },
            {
                'name': "9",
                'path': "f2d3f91670c8cb984c65a628a62e35bf.svg",
                'center': (8, 19),
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





        self.sprite.layer = 16

    @on_green_flag
    async def green_flag(self, util):
        self.gotoxy(-15, 140)
        self.costume.switch(0)
        while True:
            self.costume.switch((div((util.timer() - (util.timer() % 10)), 10) + 1))

            await self.yield_()


@sprite('gameover')
class Spritegameover(Target):
    """Sprite gameover"""

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
                'name': "gameover",
                'path': "0df1f915d79801d8c0d9ab57dd422ebc.png",
                'center': (480, 360),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [

        ])





        self.sprite.layer = 19

    @on_broadcast('game_over')
    async def broadcast_game_over(self, util):
        self.shown = True
        self.front_layer(util)

    @on_green_flag
    async def green_flag(self, util):
        self.shown = False


@sprite('victory')
class Spritevictory(Target):
    """Sprite victory"""

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
                'name': "victory",
                'path': "f733925211ab7f358a1ceb1adbd78482.png",
                'center': (480, 360),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [

        ])





        self.sprite.layer = 18

    @on_green_flag
    async def green_flag(self, util):
        self.shown = False

    @on_broadcast('victory')
    async def broadcast_victory(self, util):
        self.shown = True
        self.front_layer(util)


@sprite('black2')
class Spriteblack2(Target):
    """Sprite black2"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -165
        self._ypos = 150
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "costume1",
                'path': "5fdf66d26cd611c00ebae06c9965e4e8.svg",
                'center': (11, 19),
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





        self.sprite.layer = 8

    @on_green_flag
    async def green_flag(self, util):
        self.gotoxy(-165, 150)
        self.shown = True
        self.costume.size = 100


@sprite('white2')
class Spritewhite2(Target):
    """Sprite white2"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 165
        self._ypos = 150
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "costume1",
                'path': "9c8400e883b39ca92343d52897f7021f.svg",
                'center': (15, 19),
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





        self.sprite.layer = 11

    @on_green_flag
    async def green_flag(self, util):
        self.gotoxy(165, 150)
        self.shown = True
        self.costume.size = 100




if __name__ == '__main__':
    engine.start_program()
