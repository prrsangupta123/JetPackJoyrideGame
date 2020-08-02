import create
s1=create.rows
s2=create.columns
import random
from colorama import init, Fore, Back, Style


class Scene(object):

    s1=create.rows
    s2=create.columns
    scene_height = int(s1)
    scene_length = int(s2*5)
    ground_level = int(s1/1.3)

    def __init__(self):
        l1=Scene.scene_length
        l2=Scene.scene_height
        self.scene_start_index = 0
        self.scene_matrix = [
            [" " for x in range(l1)] for y in range(l2)]
        self.create_sky()
        self.i=create.bullet
        self.create_coins()
        self.create_beamh()
        self.c=create.coin
        self.create_beamv()
        self.create_beamd()
        self.create_magnet()
        self.create_ground()
        self.create_boost()

    def render(self):
        len=Scene.scene_height
        for y in range(3, len):
            pr = []
            for x in range(self.scene_start_index, self.scene_start_index+s2):
                pr.append(self.scene_matrix[y][x]+Style.RESET_ALL)
            print(''.join(pr))

    def shift_front(self,x):
        self.scene_start_index += x

    def create_ground(self):
        g1=Scene.ground_level
        g2=Scene.scene_height
        g3=Scene.scene_length
        for y in range(g1,g2):
            for x in range(500):
                self.scene_matrix[y][x] = "\033[37m" + "\033[40m" + "|"
        for y in range(g1, g2):
            for x in range(500, g3):
                self.scene_matrix[y][x] = "\033[37m" + "\033[40m" + "|"
        for y in range(g1, g2):
            for x in range(g3-int(s2/2), g3):
                self.scene_matrix[y][x] = "\033[37m" + "\033[40m" + "|"

    def create_beamd(self):
        x = 1
        sl=Scene.scene_length
        sh=Scene.scene_height
        while x < (sl - s2):
            offset = random.randint(70, 80)
            x += offset
            y = random.randint(int(sh/3-8), self.ground_level-10)
            for i in range(len(create.beamd)):
                for j in range(len(create.beamd[0])):
                    if(create.beamd[i][j]=='='):
                        self.scene_matrix[y+i][x+j] = "\033[31m" + \
                        "\033[47m" + "\033[1m" + create.beamd[i][j]
                    else:
                        self.scene_matrix[y+i][x+j] = "\033[37m" + "\033[46m" + " "
                        
    def create_sky(self):
        sg=Scene.ground_level
        sll=Scene.scene_length
        for y in range(1, sg):
            for x in range(sll):
                self.scene_matrix[y][x] = "\033[37m" + "\033[46m"  + " "
        for y in range(1, sg):
            for x in range(sll-int(s2/2), sll):
                self.scene_matrix[y][x] = "\033[37m" + "\033[40m" + " "

    def create_beamv(self):
        c1=Scene.scene_length
        c2=Scene.scene_height
        x = 1
        while x < (c1-s2):
            offset = random.randint(40, 50)
            x += offset
            y = random.randint(int(c2/3-7), self.ground_level-8)
            y1=create.beamv
            for i in range(len(y1)):
                for j in range(len(y1[0])):
                    self.scene_matrix[y+i][x+j] = "\033[31m" + \
                        "\033[47m" + "\033[1m" + y1[i][j]

    def create_coins(self):
        x = 1
        S1=Scene.scene_length
        S2=Scene.scene_height
        while x < (S1-s2):
            offset = random.randint(5, int(s2/2.5))
            x += offset
            y = random.randint(int(S2/3)-3, self.ground_level-14)
            y2=create.coin
            for i in range(len(y2)):
                for j in range(len(y2[0])):
                    self.scene_matrix[y+i][x+j] = "\033[33m" + \
                        "\033[46m" + "\033[1m" + create.coin[i][j]

    def create_beamh(self):
        x = 1
        d1=Scene.scene_length
        d2=Scene.scene_height
        while x < (d1-(s2)):
            offset = random.randint(50, 60)
            x += offset
            y = random.randint(int(d2/3)-3, self.ground_level-13)
            e1=create.beamh
            for i in range(len(e1)):
                for j in range(len(e1[0])):
                    self.scene_matrix[y+i][x+j] = "\033[31m" + \
                        "\033[47m" + "\033[1m" + e1[i][j]

    def draw_dragon(self,hy):
        dragony = hy
        h1=Scene.scene_length
        dragonx = h1 - int(s2/2)
        for y in range(self.scene_height):
            for x in range(len(create.dragon[0])):
                self.scene_matrix[y][x+dragonx] = "\033[33m" + \
                    "\033[40m" + "\033[1m" + " "
        dragony = hy
        dragonx = h1-int(s2/2)
        e2=create.dragon
        for y in range(len(e2)):
            for x in range(len(e2[0])):
                self.scene_matrix[y+dragony][x+dragonx] = "\033[33m" + \
                    "\033[40m" + "\033[1m" + e2[y][x]

    def create_magnet(self):
        x=random.randint(40,100)
        v1=Scene.scene_height
        y=random.randint(int(v1/3)-3,self.ground_level-5)
        self.magnet_ypos=x
        e3=create.magnet
        for i in range(len(e3)):
                for j in range(len(e3[0])):
                    self.scene_matrix[y+i][x+j] = "\033[33m" + \
                        "\033[45m" + e3[i][j]
    
    def create_boost(self):
        x = 1
        b1=Scene.scene_length
        b2=Scene.scene_height
        while x < (b1-s2):
            offset = random.randint(0,int(create.columns/2)-2)
            x += offset
            y = random.randint(int(b2/3)-7, self.ground_level-6)
            e4=create.boostup
            for i in range(len(e4)):
                for j in range(len(e4[0])):
                    self.scene_matrix[y+i][x+j] = "\033[33m" + \
                        "\033[1;31m" + e4[i][j]
