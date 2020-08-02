import create
import global_var
import global_funct
import random
import os
import time
from colorama import init, Fore, Back, Style


class Person(object):

    ''' Characters of the game '''

    def __init__(self, character, x, y):
        self._width = len(character[0])
        self.style=create.mando
        self._height = len(character)
        self._posx = x
        self._posy = y
        
    
    def get_height(self):
        return self._height

    def get_posx(self):
        return self._posx

    def get_width(self):
        return self._width

    def render(self):
        for i in range(self._width):
            for j in range(self._height):
                self.k3=global_var.lives1
                global_var.scenery.scene_matrix[j+self._posy][i +
                                                             self._posx] = '\033[31m' + '\033[46m' + '\033[1m' + self.style[j][i]
    def get_posy(self):
        return self._posy

    def clear(self):
        for i in range(self._width):
            for j in range(self._height):
                self.k4=global_var.lives1
                global_var.scenery.scene_matrix[j+self._posy][i +
                                                             self._posx] = '\033[31m' + '\033[46m' + ' '

    def die(self):
        global_var.lives -= 1
        self.clear()
        self._posy = global_var.scenery.ground_level-len(create.mando)

    def move_left(self):
        self.clear()
        #print(self._posx)
        if(self._posx-4>global_var.scenery.scene_start_index):
            self._posx -= 1
        self.render()

    def check_left(self):
        self.check_collision_rl(-1)
        self.move_left()

    def move_right(self):
        self.clear()
        if(self._posx<global_var.scenery.scene_start_index+ 164-47 and self._posx<537):
            self._posx += 1
        self.render()

    def check_right(self):
        self.check_collision_rl(self._width+1)
        self.move_right()

    def move_up(self):
        self.clear()
        if(self._posy > 3):
            self._posy -= 1
        self.render()

    def move_down(self):
        self.clear()
        self._posy += 1
        #print(self._posy)
        if(self._posy >= 22):
            self._posy = 22
        self.render()

    def check_collision_rl(self, j):
        for i in range(self._height):
            if ' ' in global_var.scenery.scene_matrix[self._posy+i][self._posx+j]:
                continue
            elif '=' in global_var.scenery.scene_matrix[self._posy+i][self._posx+j]:
                if global_var.shield <= 0:
                    self.die()
                    return
                else:
                    global_var.shield=0
                    self.style=create.mando
                    global_var.lives+=1
                    global_var.shield_cooldown=60
                    self.die()
                    return
            elif '*' in  global_var.scenery.scene_matrix[self._posy+i][self._posx+j]:
                if global_var.shield <= 0:
                    self.die()
                    return
                else:
                    global_var.shield=0
                    self.style=create.mando
                    global_var.shield_cooldown=60
                    global_var.lives+=1
                    self.die()
                    return
            elif '+' in global_var.scenery.scene_matrix[self._posy+i][self._posx+j]:
                global_var.boost += 1
                global_var.scenery.scene_matrix[self._posy+i][self._posx+j] = "\033[37m" + "\033[46m" + ' '
                return
            elif '$' in global_var.scenery.scene_matrix[self._posy+i][self._posx+j]:
                global_var.score += 5
                global_var.scenery.scene_matrix[self._posy+i][self._posx+j] = "\033[37m" + "\033[46m" + ' '
                return

    def check_collision_up(self, i):

        for j in range(self._width):
            if ' ' in global_var.scenery.scene_matrix[self._posy+i][self._posx+j]:
                continue
            elif '=' in global_var.scenery.scene_matrix[self._posy+i][self._posx+j]:
                if global_var.shield <= 0:
                    self.die()
                    return
                else:
                    global_var.shield=0
                    self.style=create.mando
                    global_var.lives+=1
                    global_var.shield_cooldown=60
                    self.die()
                    return
            elif '*' in  global_var.scenery.scene_matrix[self._posy+i][self._posx+j]:
                if global_var.shield <= 0:
                    self.die()
                    return
                else:
                    global_var.shield=0
                    self.style=create.mando
                    global_var.lives+=1
                    global_var.shield_cooldown=60
                    self.die()
                    return
            elif '+' in global_var.scenery.scene_matrix[self._posy+i][self._posx+j]:
                global_var.boost += 1
                global_var.scenery.scene_matrix[self._posy+i][self._posx+j] = "\033[37m" + "\033[46m" + ' '
                return
            elif '$' in global_var.scenery.scene_matrix[self._posy+i][self._posx+j]:
                global_var.score += 5
                global_var.scenery.scene_matrix[self._posy+i][self._posx+j] = "\033[37m" + "\033[46m" + ' '
                return

    def check_up(self):
        self.check_collision_up(-1)
        self.move_up()

    def check_down(self):

        self.check_collision_up(self._height+1)
        self.move_down()


