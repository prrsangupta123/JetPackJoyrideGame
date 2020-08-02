import os
import create
import background
import characters
q1 = create.rows
import global_var
import global_funct
import random
import time
import fire
from colorama import init, Fore, Back, Style
k = create.columns


if __name__ == "__main__":

    os.system('tput reset')
    s = time.time()
    print("Enter your cool name :D ")
    global_var.username = input()
    os.system('tput reset')
    create.create_banner()
    lst = s
    mando = characters.Person(
        create.mando, 0, global_var.scenery.ground_level-len(create.mando))
    mando.render()
    uptime=0
    global_var.scenery.render()
    global_funct.create_footer()
    
    shifting_time = 0.5
    while True:
        #lt=int(s-time.time()+80)
        print(Fore.WHITE + Style.BRIGHT + Back.RED + str(s-time.time()+300))
        global_var.scenery.draw_dragon(mando.get_posy())
        if(lst-time.time()+shifting_time <= 0):
            if not ((global_var.scenery.scene_length)<=global_var.scenery.scene_start_index+150 and (global_var.scenery.scene_length-int(create.columns/2))>=global_var.scenery.scene_start_index):
                global_var.scenery.shift_front(1)
                global_funct.reset_scenery()
                mando.check_right()
            
            #mando.check_down()
            lst = time.time()
            if (global_var.boost == 1):
                shifting_time = 0.05
                global_var.boost1 += 1
                if(global_var.boost1 >= 30):
                    global_var.boost1 = global_var.boost = 0
                    shifting_time = 0.5
            #magnet part

            if(global_var.scenery.magnet_ypos>=global_var.scenery.scene_start_index):
                if(global_var.scenery.magnet_ypos<=global_var.scenery.scene_start_index+120):
                    #print("MAGGI ON SCENE at ",global_var.scenery.magnet_ypos," start at ",global_var.scenery.scene_start_index)
                    if(mando.get_posx()>global_var.scenery.magnet_ypos):
                        mando.check_left()
                        mando.check_left()

                    elif(mando.get_posx()<global_var.scenery.magnet_ypos):
                        mando.check_right()
                        mando.check_right()
            # SHIELDED
            if(global_var.shield==1):
                cur_time=time.time()
                if(cur_time-global_var.shield_time>=10):
                    global_var.shield=0
                    mando.style=create.mando
                    #cur_time=-1
                    global_var.shield_cooldown=60
            global_var.shield_cooldown-=shifting_time
            if(global_var.shield_cooldown<=0):
                global_var.shield_cooldown=0
        #timing of game
        if s-time.time()+300 <= 0:
            global_funct.display_ending("TIME OUT :(")
            break

        if global_var.lives <= 0:
            global_funct.display_ending("YOU LOST!")
            break

        if global_var.quit_flag:
            global_funct.display_ending("YOU LOST!")
            break
        
        event = create.get_key(create.get_input())

        cnt=0

        cnt2=0
        if event == create.QUIT:
            global_funct.display_ending("GAME OVER!")
            break
        #To check if shield is there or not and 60s are done
        elif event == create.SHIELD:
            if global_var.shield==0 and global_var.shield_cooldown<=0:
                global_var.shield_time=time.time()
                global_var.shield=1
                mando.style=create.mando1

        elif event == create.LEFT:
            mando.check_left()
        
        elif cnt>0:
            cnt2=1
            mando.check_left()
        
        elif event == create.RIGHT: 
            mando.check_right()
        #bullet part
        elif event == create.FIRE:
            if not global_var.bullet_present and not global_var.bullets1_present:
                global_var.bullets_present = True
                bullet = fire.Bullet(mando.get_posx()+mando.get_width(), int(mando.get_posy()+mando.get_height()/2))
                global_var.lives1+=1
                global_var.bullet_present = True
                
                
        elif event == create.UP:
            mando.check_up()
            uptime=time.time()
            stage=0

        #gravity with acceleration

        elif event == create.DOWN:
            mando.check_down()
        somearry=[1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1]
        if(uptime!=0 and (time.time()-uptime)-somearry[stage]>=0):
          #  print(time.time()-uptime)
            uptime=time.time()
            stage+=1
            if(stage>9):
                stage=9
            mando.check_down()
       # cnt=0
        if global_var.bullet_present:
            k1=bullet.move_right()
            k2=bullet.move_right()
            k3 = bullet.move_right()
            cnt+=1
            if(cnt>5) or k1==1 or k2==1 or k3==1:
                del bullet
                global_var.bullet_present = False
       # cnt2=0 
        # fire at hero
        if not global_var.bullet_dr:
                bulletd = fire.Bulletdr(
                 537
                 , int(mando.get_posy()+mando.get_height()/2))
                global_var.bullet_dr = True
        if global_var.bullet_dr:
           k1=bulletd.move_left()
           k2=bulletd.move_left()
           k3=bulletd.move_left()
           cnt2+=1
           if(cnt2>5) or k1==1 or k2==1 or k3==1:
                del bulletd
                global_var.bullet_dr = False
        if( global_var.dragon_lives<=0):
            global_var.dragon_lives=0
            global_funct.display_ending("YOU WON! :) ")
            break

        global_funct.reset_scenery()
