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
                'name': "backdrop1",
                'path': "e7ebc6f8321d543acf0d9a01e5354b38.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "backdrop2",
                'path': "7ad903c656ae37315da2f56243a2a05f.png",
                'center': (480, 360),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            80, [
            {
                'name': "Exit the Premises.mp3",
                'path': "93dfb1b0ecd7f9c3b1fe11c24547fe29.wav"
            },
            {
                'name': "Village Consort.mp3",
                'path': "99bf68f66ff4cdc223c539c9c4e8894a.wav"
            }
        ])

        self.var_Shuriken = 0
        self.var_Hurt = 1
        self.var_Lives = 3
        self.var_Knives = 3
        self.var_ShurLevel = 1
        self.var_ShurikenS = 1
        self.var_KnivesLevel = 1
        self.var_KnivesS = 1
        self.var_U = "HungChi970104"
        self.var_Score = 46
        self.var_Money = 0
        self.var_Costume = 0
        self.var_Blahg = 0
        self.var_HighNorm = 1043
        self.var_HighHard = 622

        self.list_CostShuriken = StaticList(
            []
        )

        self.sprite.layer = 0

    @on_broadcast('start')
    async def broadcast_Start(self, util):
        if eq(util.sprites["Sound"].var_costume, 1):
            self.sounds.set_volume(100)
            await self.sleep(1)
            while not eq(self.var_Lives, 3):
                await self.yield_()
            for _ in range(100):
                self.sounds.change_volume(-1)

                await self.yield_()
            self.stop_other()
            self.sounds.stop_all()
            await self.sleep(0.5)
            self.sounds.set_volume(0)
            for _ in range(20):
                self.sounds.change_volume(4)

                await self.yield_()

    @on_broadcast('fade')
    async def broadcast_Fade(self, util):
        if eq(util.sprites["Sound"].var_costume, 1):
            self.sounds.set_volume(80)
            for _ in range(20):
                self.sounds.change_volume(-4)

                await self.yield_()
            self.stop_other()
            await self.sleep(0.25)
            self.sounds.stop_all()

    @on_green_flag
    async def green_flag(self, util):
        self.sounds.set_volume(80)

    @on_broadcast('fade 2')
    async def broadcast_Fade2(self, util):
        if eq(util.sprites["Sound"].var_costume, 1):
            self.sounds.set_volume(80)
            for _ in range(20):
                self.sounds.change_volume(-4)

                await self.yield_()
            self.stop_other()
            await self.sleep(0.25)
            self.sounds.stop_all()

    @on_broadcast('hardcore')
    async def broadcast_Hardcore(self, util):
        if eq(util.sprites["Sound"].var_costume, 1):
            self.sounds.set_volume(100)
            await self.sleep(1)
            while not eq(self.var_Lives, 3):
                await self.yield_()
            for _ in range(100):
                self.sounds.change_volume(-1)

                await self.yield_()
            self.stop_other()
            self.sounds.stop_all()
            await self.sleep(0.5)
            self.sounds.set_volume(0)
            for _ in range(20):
                self.sounds.change_volume(4)

                await self.yield_()

    @on_broadcast('exit')
    async def broadcast_Exit(self, util):
        if eq(util.sprites["Sound"].var_costume, 1):
            for _ in range(50):
                self.sounds.change_volume(-2)

                await self.yield_()
            self.stop_other()
            self.sounds.stop_all()
            await self.sleep(0.5)
            self.sounds.set_volume(0)
            for _ in range(20):
                self.sounds.change_volume(4)

                await self.yield_()

    @on_broadcast('fade 3')
    async def broadcast_Fade3(self, util):
        if eq(util.sprites["Sound"].var_costume, 1):
            self.sounds.set_volume(80)
            for _ in range(20):
                self.sounds.change_volume(-4)

                await self.yield_()
            self.stop_other()
            await self.sleep(0.25)
            self.sounds.stop_all()

    @on_green_flag
    async def green_flag1(self, util):
        util.send_broadcast("Menu")
        if not eq(self.var_U, config.USERNAME):
            self.var_U = config.USERNAME
            self.var_ShurLevel = 1
            self.var_KnivesLevel = 1
            self.var_Costume = 0

    @on_broadcast('start')
    async def broadcast_Start1(self, util):
        while True:
            await self.sounds.play("Exit the Premises.mp3")

            await self.yield_()

    @on_broadcast('hardcore')
    async def broadcast_Hardcore1(self, util):
        while True:
            await self.sounds.play("Exit the Premises.mp3")

            await self.yield_()

    @on_broadcast('menu')
    async def broadcast_Menu(self, util):
        while True:
            await self.sounds.play("Village Consort.mp3")

            await self.yield_()

    @on_broadcast('music')
    async def broadcast_music(self, util):
        if eq(util.sprites["Sound"].var_costume, 1):
            self.sounds.set_volume(100)
        else:
            self.sounds.set_volume(0)


@sprite('Ninja')
class SpriteNinja(Target):
    """Sprite Ninja"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = -146
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "left-right", [
            {
                'name': "1",
                'path': "3cb9f78d086f40d2e0defe1c1e52023e.png",
                'center': (20, 20),
                'scale': 2
            },
            {
                'name': "2",
                'path': "2874cceb52a65964138b34f0ec7feeed.png",
                'center': (20, 20),
                'scale': 2
            },
            {
                'name': "3",
                'path': "4a8870fcebb0a0d3a64d33881277c135.png",
                'center': (20, 20),
                'scale': 2
            },
            {
                'name': "4",
                'path': "c569908f118e540b44dc9339109759a0.png",
                'center': (20, 20),
                'scale': 2
            },
            {
                'name': "5",
                'path': "5040e710a2393e12c64d00feb959c88b.png",
                'center': (20, 20),
                'scale': 2
            },
            {
                'name': "6",
                'path': "fd1de4498353e414231f1cd5a68b0616.png",
                'center': (20, 20),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "death",
                'path': "867cd93057bbc7fdacef4c7aa53a632b.wav"
            },
            {
                'name': "gun_ar",
                'path': "64e8f8aff579f031fb6032fff3964164.wav"
            },
            {
                'name': "hurt",
                'path': "657412e5d11d351aa7c48ed6e9d40920.wav"
            }
        ])

        self.var_Yvel = 8
        self.var_Xvel = 5



        self.sprite.layer = 20

    @warp
    async def my_Up(self, util, ):
        while not not self.get_touching(util, "Ground"):
            self.ypos += 1
        self.ypos += -1

    @on_broadcast('start')
    async def broadcast_Start(self, util):
        await self.my_Ground(util, )

    @on_broadcast('start')
    async def broadcast_Start1(self, util):
        await self.my_Looks(util, )

    @on_broadcast('start')
    async def broadcast_Start2(self, util):
        await self.sleep(1)
        while not eq(util.sprites.stage.var_Lives, 3):
            await self.yield_()
        if gt(util.sprites.stage.var_Score, util.sprites.stage.var_HighNorm):
            util.sprites.stage.var_HighNorm = util.sprites.stage.var_Score
        self.sounds.play("death")
        self.stop_other()
        self.ypos = -147
        self.costume.switch((3 + util.sprites.stage.var_Costume))

    @on_broadcast('start')
    async def broadcast_Start3(self, util):
        await self.my_UpandLR(util, )

    @on_broadcast('menu')
    async def broadcast_Menu(self, util):
        self.stop_other()
        self.costume.switch((1 + util.sprites.stage.var_Costume))
        self.gotoxy(0, -146)

    @on_broadcast('hardcore')
    async def broadcast_Hardcore(self, util):
        await self.my_UpandLR(util, )

    async def my_UpandLR(self, util, ):
        self.gotoxy(0, -146)
        self.var_Xvel = 0
        self.var_Yvel = 0
        while True:
            self.front_layer(util)
            self.change_layer(util, -1)
            if (util.inputs["up arrow"] and self.get_touching(util, "Ground")):
                self.var_Yvel = 12
                self.ypos += self.var_Yvel
            if util.inputs["right arrow"]:
                self.var_Xvel += 1
            if util.inputs["left arrow"]:
                self.var_Xvel += -1
            self.var_Xvel = (self.var_Xvel * 0.85)
            self.xpos += self.var_Xvel
            if gt(self.var_Xvel, 0):
                self.direction = -90
            else:
                self.direction = 90

            await self.yield_()

    async def my_Ground(self, util, ):
        util.sprites.stage.var_Score = 0
        while True:
            if not self.get_touching(util, "Ground"):
                while not self.get_touching(util, "Ground"):
                    self.var_Yvel += -0.98
                    self.ypos += self.var_Yvel

                    await self.yield_()
                self.var_Yvel = 0
                await self.my_Up(util, )

            await self.yield_()

    @on_broadcast('hardcore')
    async def broadcast_Hardcore1(self, util):
        await self.my_Ground(util, )

    @on_broadcast('hard')
    async def broadcast_hard(self, util):
        await self.my_Looks(util, )

    async def my_Looks(self, util, ):
        util.sprites.stage.var_Hurt = 0
        util.sprites.stage.var_Lives = 0
        self.costume.switch((1 + util.sprites.stage.var_Costume))
        while True:
            while not eq(util.sprites.stage.var_Hurt, 1):
                await self.yield_()
            self.sounds.play("hurt")
            self.var_Yvel = 8
            self.ypos += self.var_Yvel
            self.var_Xvel = toint(div(self.direction, 20))
            util.sprites.stage.var_Lives += 1
            for _ in range(3):
                self.costume.switch((2 + util.sprites.stage.var_Costume))
                await self.sleep(0.3)
                self.costume.switch((1 + util.sprites.stage.var_Costume))
                await self.sleep(0.3)

                await self.yield_()
            util.sprites.stage.var_Hurt = 0

            await self.yield_()

    @on_broadcast('change')
    async def broadcast_change(self, util):
        self.costume.switch((1 + util.sprites.stage.var_Costume))

    @on_broadcast('hardcore')
    async def broadcast_Hardcore2(self, util):
        await self.sleep(1)
        while not eq(util.sprites.stage.var_Lives, 3):
            await self.yield_()
        if gt(util.sprites.stage.var_Score, util.sprites.stage.var_HighHard):
            util.sprites.stage.var_HighHard = util.sprites.stage.var_Score
        self.sounds.play("death")
        self.stop_other()
        self.ypos = -147
        self.costume.switch((3 + util.sprites.stage.var_Costume))

    @on_broadcast('freeplay')
    async def broadcast_freeplay(self, util):
        util.sprites.stage.var_Hurt = 0
        util.sprites.stage.var_Lives = -10000
        self.costume.switch((1 + util.sprites.stage.var_Costume))
        while True:
            while not eq(util.sprites.stage.var_Hurt, 1):
                await self.yield_()
            self.sounds.play("hurt")
            self.var_Yvel = 8
            self.ypos += self.var_Yvel
            self.var_Xvel = toint(div(self.direction, 20))
            util.sprites.stage.var_Lives += 1
            for _ in range(3):
                self.costume.switch((2 + util.sprites.stage.var_Costume))
                await self.sleep(0.3)
                self.costume.switch((1 + util.sprites.stage.var_Costume))
                await self.sleep(0.3)

                await self.yield_()
            util.sprites.stage.var_Hurt = 0

            await self.yield_()


@sprite('Glob')
class SpriteGlob(Target):
    """Sprite Glob"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 240
        self._ypos = -135
        self._direction = -90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           2, 100, "left-right", [
            {
                'name': "costume1",
                'path': "fc54a9c28aad08152d711ae98a201fcc.png",
                'center': (20, 12),
                'scale': 2
            },
            {
                'name': "costume2",
                'path': "9e186ec3873a54630a42e84fe2f9cc04.png",
                'center': (20, 14),
                'scale': 2
            },
            {
                'name': "costume3",
                'path': "f1d5d56389b049ac713b6107884ad102.png",
                'center': (20, 12),
                'scale': 2
            },
            {
                'name': "costume4",
                'path': "6b5170d5cc7a1496aaa39ccb642b1c0b.png",
                'center': (20, 14),
                'scale': 2
            },
            {
                'name': "costume5",
                'path': "548af20fc18d4b2e1ef055bb633e11b3.png",
                'center': (20, 12),
                'scale': 2
            },
            {
                'name': "costume6",
                'path': "54c844636a0259f4aa1789e65221390c.png",
                'center': (20, 14),
                'scale': 2
            },
            {
                'name': "costume7",
                'path': "cb5996900dc02fda36404d4ad3c9c1b5.png",
                'center': (20, 12),
                'scale': 2
            },
            {
                'name': "costume8",
                'path': "18b32ed0a58f9ab6dc10b1da2e3a092d.png",
                'center': (20, 14),
                'scale': 2
            },
            {
                'name': "costume10",
                'path': "08cc2fc8fa374fb0a6baf0789ee7e442.png",
                'center': (20, 12),
                'scale': 2
            },
            {
                'name': "costume9",
                'path': "34cb1f02e06318a94e5d3fefd89ef753.png",
                'center': (20, 14),
                'scale': 2
            },
            {
                'name': "Bleah",
                'path': "4b952b87bf59ec992660f40f59b2f219.png",
                'center': (4, 4),
                'scale': 2
            },
            {
                'name': "Bleah2",
                'path': "7e508c467820b2f137e3119d405a6244.png",
                'center': (4, 4),
                'scale': 2
            },
            {
                'name': "Shuriken",
                'path': "47a42a0c2e0970f9e122c23775e09560.png",
                'center': (16, 16),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "hurt",
                'path': "657412e5d11d351aa7c48ed6e9d40920.wav"
            }
        ])

        self.var_Xvel = 5e-324
        self.var_Yvel = 0
        self.var_Type = 0
        self.var_X = -0.3
        self.var_Level = 0
        self.var_Steps = 9



        self.sprite.layer = 3

    @warp
    async def my_Up(self, util, ):
        while not not self.get_touching(util, "Ground"):
            self.ypos += 1
        self.ypos += -1

    @on_clone_start
    async def clone_start(self, util):
        if eq(self.var_Type, 0):
            if eq(self.var_Level, 3):
                self.costume.switch("costume7")
            else:
                if eq(self.var_Level, 2):
                    self.costume.switch("costume5")
                else:
                    if eq(self.var_Level, 1):
                        self.costume.switch("costume3")
                    else:
                        self.costume.switch("costume1")
            while True:
                await self.sleep(0.5)
                self.costume.next()
                await self.sleep(0.5)
                self.costume.switch((self.costume.number - 1))

                await self.yield_()

    @on_clone_start
    async def clone_start1(self, util):
        if eq(self.var_Type, 0):
            while True:
                if not self.get_touching(util, "Ground"):
                    while not self.get_touching(util, "Ground"):
                        self.var_Yvel += -1
                        self.ypos += self.var_Yvel

                        await self.yield_()
                    self.var_Yvel = 0
                    await self.my_Up(util, )

                await self.yield_()
        else:
            pass

    async def my_Un(self, util, ):
        self.ypos += self.var_Yvel
        while not (not self.get_touching(util, "Shuriken") and (not self.get_touching(util, "Throwing Knife") and not self.get_touching(util, "Sword"))):
            if eq(util.sprites.stage.var_Lives, 3):
                self.var_Xvel += self.var_X
            else:
                if gt(util.sprites["Ninja"].xpos, (self.xpos + 10)):
                    self.var_Xvel += 0.35
                    self.var_X = 0.35
                if lt(util.sprites["Ninja"].xpos, (self.xpos - 10)):
                    self.var_Xvel += -0.35
                    self.var_X = -0.35
            self.var_Xvel = (self.var_Xvel * 0.7)
            self.xpos += self.var_Xvel
            if gt(self.var_Xvel, 0):
                self.direction = -90
            else:
                self.direction = 90

            await self.yield_()

    async def my_Clone(self, util, ):
        self.var_Type = 1
        self.create_clone_of(util, "_myself_")
        self.create_clone_of(util, "_myself_")
        self.create_clone_of(util, "_myself_")
        self.create_clone_of(util, "_myself_")
        self.create_clone_of(util, "_myself_")
        self.create_clone_of(util, "_myself_")
        self.create_clone_of(util, "_myself_")
        self.create_clone_of(util, "_myself_")
        self.create_clone_of(util, "_myself_")
        self.create_clone_of(util, "_myself_")
        self.create_clone_of(util, "_myself_")
        self.create_clone_of(util, "_myself_")
        self.create_clone_of(util, "_myself_")
        self.create_clone_of(util, "_myself_")
        self.create_clone_of(util, "_myself_")
        self.create_clone_of(util, "_myself_")
        self.create_clone_of(util, "_myself_")
        self.create_clone_of(util, "_myself_")
        self.create_clone_of(util, "_myself_")
        self.create_clone_of(util, "_myself_")

    @on_broadcast('start')
    async def broadcast_Start(self, util):
        self.shown = False
        util.timer.reset()
        while not gt(util.timer(), 15):
            self.var_Level = 0
            self.var_Type = 0
            if eq(pick_rand(1, 2), 1):
                self.xpos = 240
            else:
                self.xpos = -240
            self.var_X = (0 - div(self.xpos, 800))
            self.ypos = -135
            self.var_Yvel = 0
            self.create_clone_of(util, "_myself_")
            await self.sleep(pick_rand(1.5, 2.5))

            await self.yield_()
        while not gt(util.timer(), 45):
            self.var_Type = 0
            if eq(pick_rand(1, 2), 1):
                self.xpos = 240
            else:
                self.xpos = -240
            self.var_X = (0 - div(self.xpos, 800))
            self.ypos = -135
            self.var_Yvel = 0
            if eq(pick_rand(1, 5), 1):
                self.var_Level = 1
            else:
                self.var_Level = 0
            self.create_clone_of(util, "_myself_")
            await self.sleep(pick_rand(1.3, 2.3))

            await self.yield_()
        while not gt(util.timer(), 75):
            self.var_Type = 0
            if eq(pick_rand(1, 2), 1):
                self.xpos = 240
            else:
                self.xpos = -240
            self.var_X = (0 - div(self.xpos, 800))
            self.ypos = -135
            self.var_Yvel = 0
            if eq(pick_rand(1, 15), 1):
                self.var_Level = 2
            else:
                if eq(pick_rand(1, 4), 1):
                    self.var_Level = 1
                else:
                    self.var_Level = 0
            self.create_clone_of(util, "_myself_")
            await self.sleep(pick_rand(1.1, 2))

            await self.yield_()
        while not gt(util.timer(), 9999):
            self.var_Type = 0
            if eq(pick_rand(1, 2), 1):
                self.xpos = 240
            else:
                self.xpos = -240
            self.var_X = (0 - div(self.xpos, 800))
            self.ypos = -135
            self.var_Yvel = 0
            if eq(pick_rand(1, 25), 1):
                self.var_Level = 3
            else:
                if eq(pick_rand(1, 10), 1):
                    self.var_Level = 2
                else:
                    if eq(pick_rand(1, 3), 1):
                        self.var_Level = 1
                    else:
                        self.var_Level = 0
            self.create_clone_of(util, "_myself_")
            await self.sleep(pick_rand(1.1, 2))

            await self.yield_()

    @on_broadcast('menu')
    async def broadcast_Menu(self, util):
        self.stop_other()
        self.delete_clone(util)

    @on_broadcast('hard')
    async def broadcast_hard(self, util):
        self.shown = False
        util.timer.reset()
        while not gt(util.timer(), 9999):
            self.var_Type = 0
            if eq(pick_rand(1, 2), 1):
                self.xpos = 240
            else:
                self.xpos = -240
            self.var_X = (0 - div(self.xpos, 800))
            self.ypos = -135
            self.var_Yvel = 0
            if eq(pick_rand(1, 25), 1):
                self.var_Level = 3
            else:
                if eq(pick_rand(1, 10), 1):
                    self.var_Level = 2
                else:
                    if eq(pick_rand(1, 3), 1):
                        self.var_Level = 1
                    else:
                        self.var_Level = 0
            self.create_clone_of(util, "_myself_")
            await self.sleep(pick_rand(1.1, 2))

            await self.yield_()

    async def my_Move(self, util, ):
        while not (self.get_touching(util, "Shuriken") or (self.get_touching(util, "Throwing Knife") or self.get_touching(util, "Sword"))):
            if eq(util.sprites.stage.var_Lives, 3):
                self.var_Xvel += self.var_X
            else:
                if gt(util.sprites["Ninja"].xpos, (self.xpos + 10)):
                    if eq(self.var_Level, 2):
                        self.var_Xvel += 0.7
                        self.var_X = 0.7
                    else:
                        self.var_Xvel += 0.35
                        self.var_X = 0.35
                if lt(util.sprites["Ninja"].xpos, (self.xpos - 10)):
                    if eq(self.var_Level, 2):
                        self.var_Xvel += -0.7
                        self.var_X = -0.7
                    else:
                        self.var_Xvel += -0.35
                        self.var_X = -0.35
            self.var_Xvel = (self.var_Xvel * 0.7)
            self.xpos += self.var_Xvel
            if gt(self.var_Xvel, 0):
                self.direction = -90
            else:
                self.direction = 90

            await self.yield_()

    @on_clone_start
    async def clone_start2(self, util):
        if (eq(self.var_Type, 0) or eq(self.var_Type, 2)):
            while True:
                while not self.get_touching(util, "Ninja"):
                    await self.yield_()
                if eq(util.sprites.stage.var_Hurt, 0):
                    util.sprites.stage.var_Hurt = 1

                await self.yield_()

    @on_clone_start
    async def clone_start3(self, util):
        if (eq(self.var_Type, 0) and eq(self.var_Level, 3)):
            await self.sleep(pick_rand(0.2, 0.5))
            while True:
                self.var_Type = 2
                self.create_clone_of(util, "_myself_")
                self.var_Type = 0
                await self.sleep(pick_rand(1.8, 4.1))

                await self.yield_()

    @on_clone_start
    async def clone_start4(self, util):
        if eq(self.var_Type, 0):
            self.shown = True
            if eq(self.var_Level, 3):
                await self.my_Un(util, )
                await self.my_Move(util, )
                self.sounds.play("hurt")
                util.sprites.stage.var_Score += 3
                self.var_Xvel = (0 - (self.var_X * pick_rand(8, 10.1)))
                self.var_Yvel = 6
                self.ypos += self.var_Yvel
                await self.my_Hurt(util, )
                await self.my_Un(util, )
                await self.my_Move(util, )
                self.sounds.play("hurt")
                util.sprites.stage.var_Score += 3
                self.var_Xvel = (0 - (self.var_X * pick_rand(8, 10.1)))
                self.var_Yvel = 6
                self.ypos += self.var_Yvel
                await self.my_Clone(util, )
                self.delete_clone(util)
            else:
                if eq(self.var_Level, 2):
                    await self.my_Un(util, )
                    await self.my_Move(util, )
                    self.var_Level += -1
                    self.var_Xvel = (0 - (self.var_X * pick_rand(8, 10.1)))
                    self.var_Yvel = 6
                    self.create_clone_of(util, "_myself_")
                    self.var_Xvel = (0 - (self.var_X * pick_rand(25.1, 60.1)))
                    self.create_clone_of(util, "_myself_")
                    util.sprites.stage.var_Score += 3
                    self.delete_clone(util)
                else:
                    if eq(self.var_Level, 1):
                        await self.my_Un(util, )
                        await self.my_Move(util, )
                        self.var_Level += -1
                        self.var_Xvel = (0 - (self.var_X * pick_rand(8, 10.1)))
                        self.var_Yvel = 6
                        self.create_clone_of(util, "_myself_")
                        self.var_Xvel = (0 - (self.var_X * pick_rand(25.1, 60.1)))
                        self.create_clone_of(util, "_myself_")
                        util.sprites.stage.var_Score += 1
                        self.delete_clone(util)
                    else:
                        await self.my_Un(util, )
                        await self.my_Move(util, )
                        self.sounds.play("hurt")
                        await self.my_Clone(util, )
                        util.sprites.stage.var_Score += 1
                        self.delete_clone(util)
        else:
            if eq(self.var_Type, 2):
                self.costume.switch("Shuriken")
                self.shown = True
                self.var_Steps = (0 - div(self.direction, 10))
                self.costume.rotation_style = 'all around'
                while not self.get_touching(util, "_edge_"):
                    self.xpos += self.var_Steps
                    self.direction += (self.var_Steps * 3)

                    await self.yield_()
                self.delete_clone(util)
            else:
                self.costume.switch("Bleah")
                if eq(pick_rand(1, 2), 1):
                    self.costume.next()
                self.ypos += pick_rand(-8, 8)
                self.xpos += pick_rand(-8, 8)
                self.var_Xvel = pick_rand(-2, 2.1)
                self.var_Yvel = pick_rand(0, 6.1)
                while not self.get_touching(util, "Ground"):
                    self.var_Yvel += -0.7
                    self.ypos += self.var_Yvel
                    self.xpos += self.var_Xvel

                    await self.yield_()
                while not self.get_touching(util, "Ground"):
                    await self.yield_()
                self.delete_clone(util)

    @on_broadcast('freeplay')
    async def broadcast_freeplay(self, util):
        self.shown = False
        util.timer.reset()
        while True:
            while not (util.inputs["1"] or (util.inputs["2"] or (util.inputs["3"] or util.inputs["4"]))):
                await self.yield_()
            self.var_Type = 0
            if eq(pick_rand(1, 2), 1):
                self.xpos = 240
            else:
                self.xpos = -240
            self.var_X = (0 - div(self.xpos, 800))
            self.ypos = -135
            self.var_Yvel = 0
            if util.inputs["4"]:
                self.var_Level = 3
            else:
                if util.inputs["3"]:
                    self.var_Level = 2
                else:
                    if util.inputs["2"]:
                        self.var_Level = 1
                    else:
                        self.var_Level = 0
            self.create_clone_of(util, "_myself_")
            while not (not util.inputs["1"] and (not util.inputs["2"] and (not util.inputs["3"] and not util.inputs["4"]))):
                await self.yield_()

            await self.yield_()

    async def my_Hurt(self, util, ):
        for _ in range(60):
            if eq(util.sprites.stage.var_Lives, 3):
                self.var_Xvel += self.var_X
            else:
                if gt(util.sprites["Ninja"].xpos, (self.xpos + 10)):
                    if eq(self.var_Level, 2):
                        self.var_Xvel += 0.7
                        self.var_X = 0.7
                    else:
                        self.var_Xvel += 0.35
                        self.var_X = 0.35
                if lt(util.sprites["Ninja"].xpos, (self.xpos - 10)):
                    if eq(self.var_Level, 2):
                        self.var_Xvel += -0.7
                        self.var_X = -0.7
                    else:
                        self.var_Xvel += -0.35
                        self.var_X = -0.35
            self.var_Xvel = (self.var_Xvel * 0.7)
            self.xpos += self.var_Xvel
            if gt(self.var_Xvel, 0):
                self.direction = -90
            else:
                self.direction = 90

            await self.yield_()

    @on_clone_start
    async def clone_start5(self, util):
        if (eq(self.var_Type, 0) and eq(self.var_Level, 3)):
            await self.sleep(0.05)
            while True:
                while not eq(self.var_Yvel, 0):
                    await self.yield_()
                while not not eq(self.var_Yvel, 0):
                    await self.yield_()
                for _ in range(2):
                    self.costume.next()
                    self.costume.next()
                    await self.sleep(0.5)
                    self.costume.switch((self.costume.number - 2))
                    await self.sleep(0.5)

                    await self.yield_()

                await self.yield_()


@sprite('Sword')
class SpriteSword(Target):
    """Sprite Sword"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -29.29039517400644
        self._ypos = -148.32000000000008
        self._direction = -80
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           1, 100, "all around", [
            {
                'name': "costume1",
                'path': "f6c88d176ae80a2493985b2de17a8636.png",
                'center': (74, 8),
                'scale': 2
            },
            {
                'name': "costume2",
                'path': "b381a1995fe1ca6d77731459761ae4e6.png",
                'center': (74, 8),
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

        self.var_X = 0



        self.sprite.layer = 11

    async def my_Play(self, util, ):
        if util.inputs["space"]:
            self.shown = True
            if eq(util.sprites["Ninja"].direction, 90):
                self.costume.switch("costume1")
                self.direction = -55
                for _ in range(9):
                    self.direction -= 25
                    self.goto(util, "Ninja")

                    await self.yield_()
            else:
                self.costume.switch("costume2")
                self.direction = 55
                for _ in range(9):
                    self.direction += 25
                    self.goto(util, "Ninja")

                    await self.yield_()
            self.shown = False
            await self.sleep(0.6)
            while not not util.inputs["space"]:
                await self.yield_()
        if util.inputs["a"]:
            self.shown = True
            self.direction = 90
            self.costume.switch("costume1")
            self.var_X = 0
            for _ in range(5):
                self.var_X += -1
                self.goto(util, "Ninja")
                self.xpos += self.var_X

                await self.yield_()
            for _ in range(5):
                self.var_X += 1
                self.goto(util, "Ninja")
                self.xpos += self.var_X

                await self.yield_()
            self.shown = False
            await self.sleep(0.4)
        if util.inputs["d"]:
            self.shown = True
            self.direction = -90
            self.costume.switch("costume2")
            self.var_X = 0
            for _ in range(5):
                self.var_X += 1
                self.goto(util, "Ninja")
                self.xpos += self.var_X

                await self.yield_()
            for _ in range(5):
                self.var_X += -1
                self.goto(util, "Ninja")
                self.xpos += self.var_X

                await self.yield_()
            self.shown = False
            await self.sleep(0.4)

    @on_broadcast('start')
    async def broadcast_Start(self, util):
        self.shown = False
        await self.sleep(0.04)
        while True:
            await self.my_Play(util, )

            await self.yield_()

    @on_broadcast('hardcore')
    async def broadcast_Hardcore(self, util):
        self.shown = False
        await self.sleep(0.04)
        while True:
            await self.my_Play(util, )

            await self.yield_()

    @on_broadcast('hardcore')
    async def broadcast_Hardcore1(self, util):
        while not eq(util.sprites.stage.var_Lives, 3):
            await self.yield_()
        self.stop_other()
        self.shown = False

    @on_broadcast('start')
    async def broadcast_Start1(self, util):
        while not eq(util.sprites.stage.var_Lives, 3):
            await self.yield_()
        self.stop_other()
        self.shown = False

    @on_broadcast('exit')
    async def broadcast_Exit(self, util):
        self.stop_other()
        self.shown = False


@sprite('Throwing Knife')
class SpriteThrowingKnife(Target):
    """Sprite Throwing Knife"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = -146
        self._direction = -165
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           1, 100, "all around", [
            {
                'name': "costume1",
                'path': "68e5cb3383aa98fefdb2da04dc341a0f.png",
                'center': (-4, 4),
                'scale': 2
            },
            {
                'name': "costume2",
                'path': "47c54fb12d5622cb7a0ad00378c066be.png",
                'center': (-4, 4),
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





        self.sprite.layer = 6

    @on_broadcast('start')
    async def broadcast_Start(self, util):
        self.shown = False
        await self.sleep(0.04)
        if eq(util.sprites.stage.var_KnivesLevel, 1):
            util.sprites.stage.var_Knives = 1
        else:
            if eq(util.sprites.stage.var_KnivesLevel, 2):
                util.sprites.stage.var_Knives = 5
            else:
                if eq(util.sprites.stage.var_KnivesLevel, 3):
                    util.sprites.stage.var_Knives = 10
                else:
                    if eq(util.sprites.stage.var_KnivesLevel, 4):
                        util.sprites.stage.var_Knives = 20
                    else:
                        util.sprites.stage.var_Knives = 50
        await self.my_Throwing(util, )

    @on_broadcast('freeplay')
    async def broadcast_freeplay(self, util):
        await self.sleep(0.02)
        util.sprites.stage.var_Knives = 100000
        await self.my_Throwing(util, )

    async def my_Throwing(self, util, ):
        while not eq(util.sprites.stage.var_Lives, 3):
            if (util.inputs["s"] and (gt(util.sprites["Ninja"].ypos, -140) and gt(util.sprites.stage.var_Knives, 0))):
                self.costume.switch("costume1")
                self.direction = 165
                self.create_clone_of(util, "_myself_")
                self.direction = 180
                self.create_clone_of(util, "_myself_")
                self.costume.switch("costume2")
                self.direction = -165
                self.create_clone_of(util, "_myself_")
                util.sprites.stage.var_Knives += -1
                while not not util.inputs["s"]:
                    await self.yield_()

            await self.yield_()

    @on_broadcast('start')
    async def broadcast_Start1(self, util):
        while True:
            self.goto(util, "Ninja")

            await self.yield_()

    @on_broadcast('freeplay')
    async def broadcast_freeplay1(self, util):
        while True:
            self.goto(util, "Ninja")

            await self.yield_()

    @on_broadcast('hardcore')
    async def broadcast_Hardcore(self, util):
        util.sprites.stage.var_Knives = 0

    @on_clone_start
    async def clone_start(self, util):
        self.shown = True
        while not self.get_touching(util, "Ground"):
            self.move(10)

            await self.yield_()
        for _ in range(10):
            self.costume.change_effect('ghost', 10)

            await self.yield_()
        self.delete_clone(util)


@sprite('Shuriken')
class SpriteShuriken(Target):
    """Sprite Shuriken"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 107.74629895150096
        self._ypos = -147
        self._direction = 36
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "costume2",
                'path': "fdb063439238550a48224f21d674bc1b.png",
                'center': (16, 16),
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

        self.var_Steps = 9



        self.sprite.layer = 4

    @on_broadcast('start')
    async def broadcast_Start(self, util):
        self.shown = False
        if eq(util.sprites.stage.var_ShurLevel, 1):
            util.sprites.stage.var_Shuriken = 1
        else:
            if eq(util.sprites.stage.var_ShurLevel, 2):
                util.sprites.stage.var_Shuriken = 3
            else:
                if eq(util.sprites.stage.var_ShurLevel, 3):
                    util.sprites.stage.var_Shuriken = 5
                else:
                    if eq(util.sprites.stage.var_ShurLevel, 4):
                        util.sprites.stage.var_Shuriken = 10
                    else:
                        util.sprites.stage.var_Shuriken = 20
        await self.sleep(0.04)
        while True:
            while not util.inputs["w"]:
                await self.yield_()
            if (gt(util.sprites.stage.var_Shuriken, 0) and not eq(util.sprites.stage.var_Lives, 3)):
                self.create_clone_of(util, "_myself_")
                util.sprites.stage.var_Shuriken += -1
                await self.sleep(0.5)

            await self.yield_()

    @on_broadcast('menu')
    async def broadcast_Menu(self, util):
        self.stop_other()
        self.shown = False
        self.delete_clone(util)

    @on_clone_start
    async def clone_start(self, util):
        self.shown = True
        self.goto(util, "Ninja")
        self.direction = util.sprites["Ninja"].direction
        self.var_Steps = (0 - div(util.sprites["Ninja"].direction, 10))
        while not self.get_touching(util, "_edge_"):
            self.xpos += self.var_Steps
            self.direction += (self.var_Steps * 3)

            await self.yield_()
        if self.get_touching(util, "Glob"):
            await self.sleep(0.05)
        self.delete_clone(util)

    @on_broadcast('freeplay')
    async def broadcast_freeplay(self, util):
        util.sprites.stage.var_Shuriken = 100000
        await self.sleep(0.04)
        while True:
            while not util.inputs["w"]:
                await self.yield_()
            if (gt(util.sprites.stage.var_Shuriken, 0) and not eq(util.sprites.stage.var_Lives, 3)):
                self.create_clone_of(util, "_myself_")
                util.sprites.stage.var_Shuriken += -1
                await self.sleep(0.5)

            await self.yield_()


@sprite('Box')
class SpriteBox(Target):
    """Sprite Box"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -166
        self._ypos = 180
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           1, 100, "left-right", [
            {
                'name': "costume2",
                'path': "d5ccac35c1bc92529f81cb330e236ad5.png",
                'center': (20, 20),
                'scale': 2
            },
            {
                'name': "costume4",
                'path': "79e5c0b8b3efa1c1ff7838705da9d283.png",
                'center': (20, 20),
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

        self.var_Yvel = -12
        self.var_Xvel = "0.059702077939105425"



        self.sprite.layer = 5

    @warp
    async def my_Up(self, util, ):
        while not not self.get_touching(util, "Ground"):
            self.ypos += 1
        self.ypos += -1

    @on_clone_start
    async def clone_start(self, util):
        self.var_Yvel = 0
        self.gotoxy(pick_rand(-220, 220), 180)
        self.shown = True
        while not (self.get_touching(util, "Ground") or self.get_touching(util, "Ninja")):
            self.var_Yvel += -1
            self.ypos += self.var_Yvel

            await self.yield_()
        await self.my_Up(util, )
        while not self.get_touching(util, "Ninja"):
            await self.yield_()
        if eq(self.costume.number, 2):
            util.sprites.stage.var_Knives += 2
        else:
            util.sprites.stage.var_Shuriken += 1
        self.delete_clone(util)

    @on_broadcast('menu')
    async def broadcast_Menu(self, util):
        self.stop_other()
        self.delete_clone(util)

    @on_broadcast('start')
    async def broadcast_Start(self, util):
        self.shown = False
        while True:
            await self.sleep(pick_rand(15, 10.1))
            self.costume.switch(pick_rand(1, 2))
            self.create_clone_of(util, "_myself_")

            await self.yield_()


@sprite('Heart')
class SpriteHeart(Target):
    """Sprite Heart"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 163
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "costume1",
                'path': "4b4d415289d5404d86a10db46db38eac.png",
                'center': (16, 12),
                'scale': 2
            },
            {
                'name': "costume2",
                'path': "db5c4e8bec3e77eb586e43eb27cb46ee.png",
                'center': (2, 2),
                'scale': 2
            },
            {
                'name': "costume3",
                'path': "fa2ddb5f99b8042f23a0ecf44f1a0875.png",
                'center': (2, 2),
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

        self.var_X = 3
        self.var_Type = 0



        self.sprite.layer = 7

    @on_broadcast('start')
    async def broadcast_Start(self, util):
        await self.my_Begin(util, )

    @warp
    async def my_Make(self, util, ):
        self.var_Type = 1
        for _ in range(15):
            self.create_clone_of(util, "_myself_")

    @on_clone_start
    async def clone_start(self, util):
        if eq(self.var_Type, 0):
            self.costume.switch("costume1")
            self.shown = True
            await self.sleep(0.1)
            while not eq(self.var_X, util.sprites.stage.var_Lives):
                await self.yield_()
            await self.my_Make(util, )
            self.delete_clone(util)
        else:
            self.costume.switch("costume2")
            if eq(pick_rand(1, 2), 1):
                self.costume.next()
            self.ypos += pick_rand(-8, 8)
            self.xpos += pick_rand(-8, 8)
            self.var_Xvel = pick_rand(-2, 2.1)
            self.var_Yvel = pick_rand(0, 6.1)
            while not self.get_touching(util, "Ground"):
                self.var_Yvel = tonum(self.var_Yvel) + -0.7
                self.ypos += tonum(self.var_Yvel)
                self.xpos += tonum(self.var_Xvel)

                await self.yield_()
            while not self.get_touching(util, "Ground"):
                await self.yield_()
            self.delete_clone(util)

    @on_broadcast('hard')
    async def broadcast_hard(self, util):
        await self.my_Begin(util, )

    async def my_Begin(self, util, ):
        self.shown = False
        self.var_Type = 0
        self.var_X = 1
        self.costume.size = 100
        self.gotoxy(-25, 163)
        self.create_clone_of(util, "_myself_")
        self.gotoxy(25, 163)
        self.var_X += 1
        self.create_clone_of(util, "_myself_")
        self.gotoxy(0, 163)
        self.var_X += 1
        self.create_clone_of(util, "_myself_")


@sprite('Shuriken2')
class SpriteShuriken2(Target):
    """Sprite Shuriken2"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 199
        self._ypos = 144
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "0",
                'path': "394c3bd1c1a2d8be16588f72534d5e4c.png",
                'center': (16, 16),
                'scale': 2
            },
            {
                'name': "1",
                'path': "4dd834681864b50cee3e2ca7ea2b987d.png",
                'center': (16, 16),
                'scale': 2
            },
            {
                'name': "2",
                'path': "cdd23b675e9ba51f3051c33fa38872ca.png",
                'center': (16, 16),
                'scale': 2
            },
            {
                'name': "3",
                'path': "86feba6638b339d13e0bb3920c62fc7f.png",
                'center': (16, 16),
                'scale': 2
            },
            {
                'name': "4",
                'path': "90883ba18c339784eaeb80ed672da6c4.png",
                'center': (16, 16),
                'scale': 2
            },
            {
                'name': "5",
                'path': "aaaed604cd6c843865608c54b57129e4.png",
                'center': (16, 16),
                'scale': 2
            },
            {
                'name': "6",
                'path': "27f68cf925325c9b1adcb6af6f902de7.png",
                'center': (16, 16),
                'scale': 2
            },
            {
                'name': "7",
                'path': "ae4bf300b808010db48a655a2c82fd26.png",
                'center': (16, 16),
                'scale': 2
            },
            {
                'name': "8",
                'path': "4a005cb066163959dc5eec38cda4d7f2.png",
                'center': (16, 16),
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

        self.var_Steps = 9



        self.sprite.layer = 9

    @on_broadcast('start')
    async def broadcast_Start(self, util):
        self.gotoxy(199, 144)
        self.shown = True
        while True:
            if gt(util.sprites.stage.var_Shuriken, 20):
                self.costume.switch(8)
            else:
                if gt(util.sprites.stage.var_Shuriken, 10):
                    self.costume.switch(7)
                else:
                    if gt(util.sprites.stage.var_Shuriken, 5):
                        self.costume.switch(6)
                    else:
                        self.costume.switch((util.sprites.stage.var_Shuriken + 1))

            await self.yield_()

    @on_broadcast('menu')
    async def broadcast_Menu(self, util):
        self.stop_other()
        self.shown = False


@sprite('Throwing Knife2')
class SpriteThrowingKnife2(Target):
    """Sprite Throwing Knife2"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 199
        self._ypos = 166
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           3, 100, "all around", [
            {
                'name': "0",
                'path': "0ac05bda7ab6a5016e34d3f33d7a05b4.png",
                'center': (20, 18),
                'scale': 2
            },
            {
                'name': "1",
                'path': "e037753b293b08ab1ee1b9b8690c57b8.png",
                'center': (20, 18),
                'scale': 2
            },
            {
                'name': "2",
                'path': "b2d8b96379c8606f1500cc0f9135cffa.png",
                'center': (20, 18),
                'scale': 2
            },
            {
                'name': "3",
                'path': "434c266a03dd805913eeb18b306da816.png",
                'center': (20, 18),
                'scale': 2
            },
            {
                'name': "4",
                'path': "73d686c467ab7e3c848d826c71f49f8e.png",
                'center': (20, 18),
                'scale': 2
            },
            {
                'name': "5",
                'path': "d047f36682af42cfbfe29cdef079c57a.png",
                'center': (20, 18),
                'scale': 2
            },
            {
                'name': "5+",
                'path': "052e538e1772f958bbe2097c6c636cfb.png",
                'center': (20, 18),
                'scale': 2
            },
            {
                'name': "10",
                'path': "b1dd13a80e4c0d0f40648aa7398a4f46.png",
                'center': (20, 18),
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





        self.sprite.layer = 8

    @on_broadcast('start')
    async def broadcast_Start(self, util):
        self.gotoxy(199, 166)
        self.shown = True
        while True:
            if gt(util.sprites.stage.var_Knives, 10):
                self.costume.switch(10)
            else:
                if gt(util.sprites.stage.var_Knives, 5):
                    self.costume.switch("5+")
                else:
                    self.costume.switch((util.sprites.stage.var_Knives + 1))

            await self.yield_()

    @on_broadcast('menu')
    async def broadcast_Menu(self, util):
        self.stop_other()
        self.shown = False


@sprite('Cloud')
class SpriteCloud(Target):
    """Sprite Cloud"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -16
        self._ypos = 43
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "costume1",
                'path': "6ea59e12b979fd7be3faa4e7c80966fa.png",
                'center': (32, 24),
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

        self.var_Speed = 0
        self.var_Dist = 0



        self.sprite.layer = 1

    @on_green_flag
    async def green_flag(self, util):
        self.shown = False
        while True:
            self.create_clone_of(util, "_myself_")
            await self.sleep(pick_rand(1, 2.2))

            await self.yield_()

    @on_clone_start
    async def clone_start(self, util):
        self.gotoxy(-300, pick_rand(0, 180))
        self.costume.set_effect('ghost', pick_rand(50, 90))
        self.costume.size = pick_rand(100, 200)
        self.shown = True
        self.var_Speed = (3 - div(round(self.costume.size), 100))
        while not gt(self.var_Dist, 500):
            self.xpos += self.var_Speed
            self.var_Dist += self.var_Speed

            await self.yield_()
        self.delete_clone(util)


@sprite('Ground')
class SpriteGround(Target):
    """Sprite Ground"""

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
           1, 100, "all around", [
            {
                'name': "backdrop1",
                'path': "ed4dd589011814ebd42ed03a95b9a757.png",
                'center': (480, -312),
                'scale': 2
            },
            {
                'name': "backdrop2",
                'path': "7cf136dd4228f286293c7d142cd4a0d5.png",
                'center': (480, -315),
                'scale': 2
            },
            {
                'name': "backdrop3",
                'path': "bff4b0a21e64a8020af5c25208f8832c.png",
                'center': (-28, -315),
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





        self.sprite.layer = 2

    @on_green_flag
    async def green_flag(self, util):
        self.gotoxy(0, 0)
        self.costume.switch("backdrop2")


@sprite('Fade')
class SpriteFade(Target):
    """Sprite Fade"""

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
                'name': "costume1",
                'path': "f5e250886e3bafbbd9bc2398a5e321c5.png",
                'center': (480, 360),
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





        self.sprite.layer = 21

    @on_green_flag
    async def green_flag(self, util):
        util.sprites.stage.var_Lives = 0
        self.shown = True
        self.costume.set_effect('ghost', 100)

    @on_broadcast('fade')
    async def broadcast_Fade(self, util):
        for _ in range(20):
            self.costume.change_effect('ghost', -5)
            self.front_layer(util)

            await self.yield_()
        await self.sleep(0.5)
        util.send_broadcast("Start")
        for _ in range(10):
            self.costume.change_effect('ghost', 10)
            self.front_layer(util)

            await self.yield_()

    @on_broadcast('start')
    async def broadcast_Start(self, util):
        self.gotoxy(0, 0)
        self.shown = True
        self.costume.set_effect('ghost', 100)
        await self.sleep(1)
        while not eq(util.sprites.stage.var_Lives, 3):
            await self.yield_()
        for _ in range(100):
            self.costume.change_effect('ghost', -1)
            self.front_layer(util)

            await self.yield_()
        await self.sleep(0.5)
        util.send_broadcast("Menu")
        for _ in range(10):
            self.costume.change_effect('ghost', 10)
            self.front_layer(util)

            await self.yield_()

    @on_broadcast('fade 2')
    async def broadcast_Fade2(self, util):
        for _ in range(20):
            self.costume.change_effect('ghost', -5)
            self.front_layer(util)

            await self.yield_()
        await self.sleep(0.5)
        util.send_broadcast("Hard")
        util.send_broadcast("Hardcore")
        for _ in range(10):
            self.costume.change_effect('ghost', 10)
            self.front_layer(util)

            await self.yield_()

    @on_broadcast('hardcore')
    async def broadcast_Hardcore(self, util):
        self.gotoxy(0, 0)
        self.shown = True
        self.costume.set_effect('ghost', 100)
        await self.sleep(1)
        while not eq(util.sprites.stage.var_Lives, 3):
            await self.yield_()
        for _ in range(100):
            self.costume.change_effect('ghost', -1)
            self.front_layer(util)

            await self.yield_()
        await self.sleep(0.5)
        util.send_broadcast("Menu")
        for _ in range(10):
            self.costume.change_effect('ghost', 10)
            self.front_layer(util)

            await self.yield_()

    @on_broadcast('fade 3')
    async def broadcast_Fade3(self, util):
        for _ in range(20):
            self.costume.change_effect('ghost', -5)
            self.front_layer(util)

            await self.yield_()
        await self.sleep(0.5)
        util.send_broadcast("Freeplay")
        util.send_broadcast("Hardcore")
        for _ in range(10):
            self.costume.change_effect('ghost', 10)
            self.front_layer(util)

            await self.yield_()

    @on_broadcast('exit')
    async def broadcast_Exit(self, util):
        self.gotoxy(0, 0)
        self.shown = True
        for _ in range(50):
            self.costume.change_effect('ghost', -2)
            self.front_layer(util)

            await self.yield_()
        await self.sleep(0.5)
        util.send_broadcast("Menu")
        for _ in range(10):
            self.costume.change_effect('ghost', 10)
            self.front_layer(util)

            await self.yield_()


@sprite('Button 1')
class SpriteButton1(Target):
    """Sprite Button 1"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 50
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 200, "all around", [
            {
                'name': "costume1",
                'path': "9cc0dbde43854ada8440c73c75e173e2.png",
                'center': (52, 20),
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





        self.sprite.layer = 12

    @on_broadcast('menu')
    async def broadcast_Menu(self, util):
        self.shown = True
        self.costume.size = 200
        while True:
            if self.get_touching(util, "_mouse_"):
                self.gotoxy(0, 49)
                if util.inputs.mouse_down:
                    util.send_broadcast("Fade")
            else:
                self.gotoxy(0, 50)

            await self.yield_()

    @on_green_flag
    async def green_flag(self, util):
        self.shown = False

    @on_broadcast('start')
    async def broadcast_Start(self, util):
        self.shown = False
        self.stop_other()

    @on_broadcast('store')
    async def broadcast_Store(self, util):
        self.shown = False
        self.stop_other()

    @on_broadcast('hardcore')
    async def broadcast_Hardcore(self, util):
        self.shown = False
        self.stop_other()


@sprite('Button 4')
class SpriteButton4(Target):
    """Sprite Button 4"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = -50
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 200, "all around", [
            {
                'name': "costume1",
                'path': "7ba1e517c330b92de51eea3786f01f42.png",
                'center': (68, 20),
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





        self.sprite.layer = 15

    @on_broadcast('menu')
    async def broadcast_Menu(self, util):
        self.shown = True
        self.costume.size = 200
        while True:
            if self.get_touching(util, "_mouse_"):
                self.gotoxy(0, -51)
                if util.inputs.mouse_down:
                    util.send_broadcast("Fade 3")
            else:
                self.gotoxy(0, -50)

            await self.yield_()

    @on_green_flag
    async def green_flag(self, util):
        self.shown = False

    @on_broadcast('start')
    async def broadcast_Start(self, util):
        self.shown = False
        self.stop_other()

    @on_broadcast('store')
    async def broadcast_Store(self, util):
        self.shown = False
        self.stop_other()

    @on_broadcast('hardcore')
    async def broadcast_Hardcore(self, util):
        self.shown = False
        self.stop_other()


@sprite('Button 3')
class SpriteButton3(Target):
    """Sprite Button 3"""

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
           0, 200, "all around", [
            {
                'name': "costume1",
                'path': "e36de5bf7b96447f37bf859ee509407a.png",
                'center': (64, 20),
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





        self.sprite.layer = 14

    @on_broadcast('menu')
    async def broadcast_Menu(self, util):
        self.shown = True
        self.costume.size = 200
        while True:
            if self.get_touching(util, "_mouse_"):
                self.gotoxy(0, -1)
                if util.inputs.mouse_down:
                    util.send_broadcast("Fade 2")
            else:
                self.gotoxy(0, 0)

            await self.yield_()

    @on_green_flag
    async def green_flag(self, util):
        self.shown = False

    @on_broadcast('start')
    async def broadcast_Start(self, util):
        self.shown = False
        self.stop_other()

    @on_broadcast('store')
    async def broadcast_Store(self, util):
        self.shown = False
        self.stop_other()

    @on_broadcast('hardcore')
    async def broadcast_Hardcore(self, util):
        self.shown = False
        self.stop_other()


@sprite('Upgrade Shuriken')
class SpriteUpgradeShuriken(Target):
    """Sprite Upgrade Shuriken"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -27
        self._ypos = -69
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 200, "all around", [
            {
                'name': "costume1",
                'path': "b2d176a675e37092515c14f1cd9457a5.png",
                'center': (36, 16),
                'scale': 2
            },
            {
                'name': "costume2",
                'path': "46eef78c21e9ee5d643a47d5c5058aa7.png",
                'center': (36, 16),
                'scale': 2
            },
            {
                'name': "costume3",
                'path': "41d7a1b3d948bb668f82c7072075e8c8.png",
                'center': (36, 16),
                'scale': 2
            },
            {
                'name': "costume4",
                'path': "e492ea98523145ebe1d8bbc447fb04e4.png",
                'center': (44, 16),
                'scale': 2
            },
            {
                'name': "costume5",
                'path': "1b0d8ceac9cfb994dd1457ff09bd77b8.png",
                'center': (12, 16),
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





        self.sprite.layer = 10

    @on_broadcast('store')
    async def broadcast_Store(self, util):
        self.gotoxy(-33, 120)
        self.costume.switch(util.sprites.stage.var_ShurLevel)
        self.costume.size = 200
        self.shown = True
        while True:
            if self.get_touching(util, "_mouse_"):
                self.gotoxy(-27, -70)
                if util.inputs.mouse_down:
                    util.send_broadcast("Up Shur")
                    while not not util.inputs.mouse_down:
                        await self.yield_()
            else:
                self.gotoxy(-27, -69)

            await self.yield_()

    @on_broadcast('menu')
    async def broadcast_Menu(self, util):
        self.shown = False

    @on_broadcast('up shur')
    async def broadcast_upshur(self, util):
        if (eq(util.sprites.stage.var_ShurLevel, 1) and gt(util.sprites.stage.var_Money, 24)):
            util.sprites.stage.var_ShurLevel += 1
            util.sprites.stage.var_Money += -25
        else:
            pass

    @on_broadcast('start')
    async def broadcast_Start(self, util):
        self.shown = False
        self.stop_other()


@sprite('No.')
class SpriteNo(Target):
    """Sprite No."""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -52
        self._ypos = 0
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           10, 200, "all around", [
            {
                'name': "0",
                'path': "504c4fa3fa4b5cab3e71fdb8755b8a7e.png",
                'center': (9, 12),
                'scale': 2
            },
            {
                'name': "1",
                'path': "e45524230a5a28bd41613cc817b22830.png",
                'center': (6, 12),
                'scale': 2
            },
            {
                'name': "2",
                'path': "0255ee8007da9ba2c3b503c982babf8d.png",
                'center': (8, 12),
                'scale': 2
            },
            {
                'name': "3",
                'path': "05185ea49f711c1792a5a269dc5d131f.png",
                'center': (8, 12),
                'scale': 2
            },
            {
                'name': "4",
                'path': "78f4bb1a0da08cc59530dfd0432d6130.png",
                'center': (12, 12),
                'scale': 2
            },
            {
                'name': "5",
                'path': "df80003fc0ff59fb4786c1437e432e6f.png",
                'center': (8, 12),
                'scale': 2
            },
            {
                'name': "6",
                'path': "f15bd19b215a31e900fa113047e11970.png",
                'center': (8, 12),
                'scale': 2
            },
            {
                'name': "7",
                'path': "ad897a284b7744fceb2784456a58e8eb.png",
                'center': (8, 12),
                'scale': 2
            },
            {
                'name': "8",
                'path': "3e964f084373b0fda945d8df682348b6.png",
                'center': (8, 12),
                'scale': 2
            },
            {
                'name': "9",
                'path': "b3f8d11f21608246bd3c6f1120cebfbb.png",
                'center': (8, 12),
                'scale': 2
            },
            {
                'name': "Cloud",
                'path': "edc82ce23e48c91c5e41374a0d045961.png",
                'center': (152, 20),
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

        self.var_Steps = 9
        self.var_No = 2



        self.sprite.layer = 13

    @on_green_flag
    async def green_flag(self, util):
        self.shown = False

    @on_broadcast('menu')
    async def broadcast_Menu(self, util):
        self.delete_clone(util)

    @warp
    async def my_PutscoreatXYSize(self, util, arg_X, arg_Y, arg_Size):
        self.shown = False
        self.costume.size = arg_Size
        self.gotoxy(arg_X, arg_Y)
        self.xpos += (13 * div(arg_Size, 50))
        self.var_No = -2
        for _ in range(4):
            self.var_No += 1
            self.create_clone_of(util, "_myself_")
            self.xpos += (0 - (13 * div(arg_Size, 100)))

    @on_broadcast('hard')
    async def broadcast_hard(self, util):
        util.sprites.stage.var_Blahg = 1
        await self.my_PutscoreatXYSize(util, 0, 0, 200)

    @on_clone_start
    async def clone_start(self, util):
        self.shown = True
        if eq(self.var_No, -1):
            self.costume.switch("Cloud")
            await self.sleep(2)
            self.delete_clone(util)
        else:
            if eq(util.sprites.stage.var_Blahg, 0):
                for _ in range(60):
                    if eq(letter_of(str(util.sprites.stage.var_HighNorm), toint((len(str(util.sprites.stage.var_HighNorm)) - self.var_No))), ""):
                        self.costume.switch(0)
                    else:
                        self.costume.switch(letter_of(str(util.sprites.stage.var_HighNorm), toint((len(str(util.sprites.stage.var_HighNorm)) - self.var_No))))

                    await self.yield_()
            else:
                for _ in range(60):
                    if eq(letter_of(str(util.sprites.stage.var_HighHard), toint((len(str(util.sprites.stage.var_HighHard)) - self.var_No))), ""):
                        self.costume.switch(0)
                    else:
                        self.costume.switch(letter_of(str(util.sprites.stage.var_HighHard), toint((len(str(util.sprites.stage.var_HighHard)) - self.var_No))))

                    await self.yield_()
            while True:
                if eq(letter_of(str(util.sprites.stage.var_Score), toint((len(str(util.sprites.stage.var_Score)) - self.var_No))), ""):
                    self.costume.switch(0)
                else:
                    self.costume.switch(letter_of(str(util.sprites.stage.var_Score), toint((len(str(util.sprites.stage.var_Score)) - self.var_No))))

                await self.yield_()

    @on_broadcast('start')
    async def broadcast_Start(self, util):
        util.sprites.stage.var_Blahg = 0
        await self.my_PutscoreatXYSize(util, 0, 0, 200)


@sprite('Ground2')
class SpriteGround2(Target):
    """Sprite Ground2"""

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
           4, 100, "all around", [
            {
                'name': "backdrop1",
                'path': "ce5b43408f44205a5da8d54f5c7dc0b6.svg",
                'center': (333, 222),
                'scale': 1
            },
            {
                'name': "backdrop2",
                'path': "9fb6fe7b5993231f56a6143c66eb1558.svg",
                'center': (333, 222),
                'scale': 1
            },
            {
                'name': "backdrop3",
                'path': "d519c3bf87f1926afb797aceacbabb71.svg",
                'center': (384, 269),
                'scale': 1
            },
            {
                'name': "Cover",
                'path': "732dce8f77a5a30e86abb76c82e5ce85.svg",
                'center': (333, 222),
                'scale': 1
            },
            {
                'name': "End screen",
                'path': "7bfc821f0b4255c6a27ff8a5e390754c.svg",
                'center': (332, 221),
                'scale': 1
            },
            {
                'name': "backdrop5",
                'path': "451d6e55ad3fc9ad93febf6f2702ccb7.svg",
                'center': (332, 221),
                'scale': 1
            },
            {
                'name': "palette",
                'path': "b9cec8bd538f003b49594b56bc884acc.svg",
                'center': (429, 299),
                'scale': 1
            },
            {
                'name': "stagey",
                'path': "160af8c060289771fd2a89958a9393d2.svg",
                'center': (304, 214),
                'scale': 1
            },
            {
                'name': "costume1",
                'path': "654d5275d25543a0575c2ed12dea3b32.svg",
                'center': (314, 202),
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





        self.sprite.layer = 22

    @on_green_flag
    async def green_flag(self, util):
        self.gotoxy(0, 0)
        self.costume.set_effect('ghost', 100)
        self.costume.switch("End screen")
        while True:
            self.front_layer(util)

            await self.yield_()


@sprite('Button 5')
class SpriteButton5(Target):
    """Sprite Button 5"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 150
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 200, "all around", [
            {
                'name': "costume2",
                'path': "bf92ebe5a40af2bf5b2c4b1750d051e3.png",
                'center': (36, 16),
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





        self.sprite.layer = 16

    @on_broadcast('freeplay')
    async def broadcast_freeplay(self, util):
        self.shown = True
        self.costume.size = 200
        while True:
            if self.get_touching(util, "_mouse_"):
                self.gotoxy(0, 149)
                if util.inputs.mouse_down:
                    util.send_broadcast("Exit")
            else:
                self.gotoxy(0, 150)

            await self.yield_()

    @on_green_flag
    async def green_flag(self, util):
        self.shown = False

    @on_broadcast('menu')
    async def broadcast_Menu(self, util):
        self.shown = False
        self.stop_other()


@sprite('Stop')
class SpriteStop(Target):
    """Sprite Stop"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 90
        self._ypos = 11
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           1, 100, "all around", [
            {
                'name': "costume1",
                'path': "1583105568e88e26d362db5f7d7baa14.svg",
                'center': (246, 42),
                'scale': 1
            },
            {
                'name': "costume2",
                'path': "828bf2a83c0d27a9482c1249580171d2.png",
                'center': (16, 16),
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



        self.list_Names = List(
            ["DarkLava", "HungChi970104"]
        )

        self.sprite.layer = 19

    @on_green_flag
    async def green_flag(self, util):
        if not config.USERNAME in self.list_Names:
            self.list_Names.append(config.USERNAME)
        self.shown = False
        self.costume.switch("costume2")
        if gt(len(self.list_Names), 2):
            self.costume.switch("costume1")
            self.shown = True
            self.gotoxy(0, 0)
            await self.sleep(4)
            for _ in range(10):
                self.costume.change_effect('ghost', 10)

                await self.yield_()
            self.costume.switch("costume2")


@sprite('Sound')
class SpriteSound(Target):
    """Sprite Sound"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -228
        self._ypos = -170
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "costume1",
                'path': "6d15efb7bb8f65eb4b4b470a8431f00d.png",
                'center': (16, 16),
                'scale': 2
            },
            {
                'name': "costume2",
                'path': "a89c002671315641bbbbfa4c752f8f76.png",
                'center': (16, 16),
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





        self.sprite.layer = 17

    @on_clicked
    async def sprite_clicked(self, util):
        self.costume.next()
        util.send_broadcast("Music")

    @on_green_flag
    async def green_flag(self, util):
        self.gotoxy(-228, -170)
        if not eq(util.sprites.stage.var_U, config.USERNAME):
            self.costume.switch("costume1")


@sprite('Choice')
class SpriteChoice(Target):
    """Sprite Choice"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 20
        self._ypos = -145
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "Right",
                'path': "ac5d44b595959e2a8a375ab1688ca972.png",
                'center': (8, 12),
                'scale': 2
            },
            {
                'name': "Left",
                'path': "16d46a0b6ee006c6b2803a85e0169fce.png",
                'center': (18, 12),
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





        self.sprite.layer = 18

    @on_broadcast('store')
    async def broadcast_Store(self, util):
        self.shown = False
        self.stop_other()
        self.delete_clone(util)

    @on_broadcast('start')
    async def broadcast_Start(self, util):
        self.shown = False
        self.stop_other()
        self.delete_clone(util)

    @on_clicked
    async def sprite_clicked(self, util):
        if eq(util.sprites.stage.var_Costume, 3):
            util.sprites.stage.var_Costume = 0
        else:
            util.sprites.stage.var_Costume = 3
        util.send_broadcast("Change")

    @on_clone_start
    async def clone_start(self, util):
        self.shown = True

    @on_broadcast('menu')
    async def broadcast_Menu(self, util):
        self.costume.switch("Left")
        self.gotoxy(-20, -145)
        self.create_clone_of(util, "_myself_")
        self.costume.switch("Right")
        self.gotoxy(20, -145)
        self.create_clone_of(util, "_myself_")

    @on_broadcast('hardcore')
    async def broadcast_Hardcore(self, util):
        self.shown = False
        self.stop_other()
        self.delete_clone(util)




if __name__ == '__main__':
    engine.start_program()
