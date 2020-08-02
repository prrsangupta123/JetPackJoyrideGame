import characters
import create
import global_funct
import global_var


class Bullet(characters.Person):

    def __init__(self, x, y):
        characters.Person.__init__(self, create.bullet, x, y)

    def clr1(self):
        s=global_var.lives
        s-=1
        self.die()

    def __del__(self):
        self.clear()
    
    def move(self):
        self.move_left()

    def render(self):
        k=create.bullet
        for i in range(self._width):
            for j in range(self._height):
                global_var.scenery.scene_matrix[j+self._posy][i +
                                                             self._posx] = "\033[32m" + "\033[40m" + "\033[1m" + k[j][i]
    def ren(self):
        self.die()
        self.render()

    s=global_var.scenery.scene_length

    

    def clear(self):
        cr=create.columns
        for i in range(self._width):
            for j in range(self._height):
                row1=create.rows
                if self._posx <= self.s-int(cr/2) - 1:
                    global_var.scenery.scene_matrix[j+self._posy][i +
                                                                 self._posx] = "\033[31m" + "\033[46m" + " "
                    row1+=create.rows
                else:
                    global_var.scenery.scene_matrix[j+self._posy][i +
                                                                 self._posx] = "\033[31m" + "\033[40m" + " "
                    row1-=create.rows

    def move_right(self):
        self.clear()
        if('=' in global_var.scenery.scene_matrix[self._posy][self._posx+3]):
            # beam
            xpos=self._posx+3
            ypos=self._posy
            # vertical

            # check up
            if('=' in global_var.scenery.scene_matrix[ypos-1][xpos] or '=' in global_var.scenery.scene_matrix[ypos+1][xpos]):
                while('=' in global_var.scenery.scene_matrix[ypos][xpos]): 
                    global_var.scenery.scene_matrix[ypos][xpos]= "\033[31m" + "\033[46m" + ' ' 
                    ypos-=1
                ypos=self._posy+1
                # check down
                while('=' in global_var.scenery.scene_matrix[ypos][xpos]): 
                    global_var.scenery.scene_matrix[ypos][xpos]= "\033[31m" + "\033[46m" + ' ' 
                    ypos+=1
                ypos=self._posy
            # check left
            """ 
            while('=' in global_var.scenery.scene_matrix[ypos][xpos]): 
                global_var.scenery.scene_matrix[ypos][xpos]=' ' 
                xpos+=1
            xpos=self._posx+3-1
            while('=' in global_var.scenery.scene_matrix[ypos][xpos]): 
                global_var.scenery.scene_matrix[ypos][xpos]=' ' 
                xpos-=1
            """
            # check up diag
            xpos=self._posx+3
            ypos=self._posy
            while('=' in global_var.scenery.scene_matrix[ypos][xpos]): 
                global_var.scenery.scene_matrix[ypos][xpos]= "\033[31m" + "\033[46m" + ' ' 
                xpos+=1
                ypos+=1
            xpos=self._posx+3-1
            ypos=self._posy-1
            while('=' in global_var.scenery.scene_matrix[ypos][xpos]): 
                global_var.scenery.scene_matrix[ypos][xpos]= "\033[31m" + "\033[46m" + ' ' 
                xpos-=1
                ypos-=1
            # check around
            global_var.score += 20
        elif '$' in global_var.scenery.scene_matrix[self._posy][self._posx+3]:
            global_var.score+=5
        elif '*' in global_var.scenery.scene_matrix[self._posy][self._posx+3]:
            global_var.scenery.scene_matrix[self._posy][self._posx+3] = "\033[33m" + "\033[45m" + '*'
            global_var.lives-=1
        else:
            bossy = ['(', '~', '{', '}', ')', "'", "-", "."]
            for i in bossy:
                if(i in global_var.scenery.scene_matrix[self._posy][self._posx+3]):
                    global_var.score += 100
                    global_var.dragon_lives -= 1
                    self.clear()
                    return 1

        if(self._posx >= global_var.scenery.scene_start_index+500-382):
            self.clear()
            return 1
        else:
            self._posx += 1
        self.render()
        return 0

class Bulletdr(characters.Person):

    """ BUllets that Dragon fires """
    def move(self):
        self.move_left()

    def __init__(self, x, y):
        characters.Person.__init__(self, create.bullet1, x, y)

    def clr1(self):
        s=global_var.lives
        s-=1
        self.die()
    
    def __del__(self):
        self.clear()

    def render(self):
        d1=create.bullet1
        for i in range(self._width):
            for j in range(self._height):
                global_var.scenery.scene_matrix[j+self._posy][i +
                                                             self._posx] = "\033[32m" + "\033[40m" + "\033[1m" + d1[j][i]
    def ren(self):
        self.die()
        self.render()

    s=global_var.scenery.scene_length

    def clear(self):
        s1=self.s
        cr1=create.columns
        for i in range(self._width):
            for j in range(self._height):
                if self._posx <= self.s-int(cr1/2) - 1:
                    global_var.scenery.scene_matrix[j+self._posy][i +
                                                                 self._posx] = "\033[31m" + "\033[46m" + " "
                    s1-=1
                else:
                    global_var.scenery.scene_matrix[j+self._posy][i +
                                                                 self._posx] = "\033[31m" + "\033[40m" + " "

    def move_left(self):
        self.clear()
        din = ['@', '\\', '|']
        for i in din:
            if(i in global_var.scenery.scene_matrix[self._posy][self._posx-2]):
                if global_var.shield <= 0:
                    global_var.lives -= 1
                else:
                    global_var.shield=0
                    global_var.shield_cooldown=60
                self.clear()
                return 1
        if(self._posx<=440):
            self.clear()
            return 1
        self._posx -= 1
        self.render()
        return 0
