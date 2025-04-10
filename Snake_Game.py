import tkinter
import turtle
import random
import time
import tkinter as tk
from tkinter import *
from typing import Tuple
from playsound import playsound
import pygame


pygame.mixer.init()

def start_game():
    # sound = pygame.mixer.Sound(r'bg_music_1.mp3')
    # pygame.mixer.Sound.play(sound)
    pygame.mixer.music.load(r'bg_music_1.mp3')
    pygame.mixer.music.play()
    delay=0.1
    score=0
    highest_score=0

    bodies=[]
    count=-1


    s=turtle.Screen()   
    s.title('Snake Game')
    s.bgcolor('gray')
    s.setup(width=600,height=600)

    head=turtle.Turtle()
    head.speed(0)
    head.shape('square')
    head.color('white')
    head.fillcolor('blue')
    head.penup()
    head.goto(0,0)
    head.direction='stop'

    food=turtle.Turtle()
    food.speed(0)
    food.shape('square')
    food.color('yellow')
    food.fillcolor('green')
    food.penup()
    food.ht()
    food.goto(0,200)
    food.st()

    sb=turtle.Turtle()
    sb.shape('square')
    sb.fillcolor('black')
    sb.penup()
    sb.ht()
    sb.goto(-250,-250)
    sb.write('Score : 0 | Highest Score : 0')

    gm=turtle.Turtle()
    gm.shape('square')
    gm.fillcolor('white')
    gm.color('black')
    gm.penup()
    gm.ht()
    gm.goto(0,0)
    gm.write('')


    def moveup():
        if head.direction!='down':
            head.direction='up'
    def movedown():
        if head.direction!='up':
            head.direction='down'
    def moveleft():
        if head.direction!='right':
            head.direction='left'
    def moveright():
        if head.direction!='left':
            head.direction='right'
    def movestop():
        head.direction='stop'
    def move():
        if head.direction=='up':
            y=head.ycor()
            head.sety(y+20)
        if head.direction=='down':
            y=head.ycor()
            head.sety(y-20)
        if head.direction=='left':
            x=head.xcor()
            head.setx(x-20)
        if head.direction=='right':
            x=head.xcor()
            head.setx(x+20)

    s.listen()
    s.onkey(moveup,'Up')
    s.onkey(movedown,'Down')
    s.onkey(moveleft,'Left')
    s.onkey(moveright,'Right')
    s.onkey(movestop,'space')


    while True:
        # music = pygame.mixer.music(r'bg_music_1.mp3')
        # pygame.mixer.music.play()
        s.update()

        if head.xcor()>290:
            head.setx(-290)
        elif head.xcor()<-290:
            head.setx(290)
        elif head.ycor()>290:
            head.sety(-290)
        elif head.ycor()<-290:
            head.sety(290)
        if head.distance(food)<20:
            x=random.randint(-290,290)
            y=random.randint(-290,290)
            food.goto(x,y)
            body=turtle.Turtle()
            count+=1
            body.speed(0)
            body.penup()
            body.shape('square')
            body.color('red')
            body.fillcolor('black')
            bodies.append(body)
            # playsound(f'ding.mp3')

            sound = pygame.mixer.Sound(r'ding.mp3')
            pygame.mixer.Sound.play(sound)

            # print(len(bodies))



    


            score+=10

            delay-=0.001


            if score>highest_score:
                highest_score=score
            sb.clear()
            
            sb.write(f'Score : {score} | Highest Score : {highest_score}')


        # x=random.randint(-290,290)
        # y=random.randint(-290,290)
        # food.goto(x,y)
        # body=turtle.Turtle()
        # count+=1
        # body.speed(0)
        # body.penup()
        # body.shape('square')
        # body.color('red')
        # body.fillcolor('black')
        # bodies.append(body)
        # score+=10
        # if     score>highest_score:
        #     highest_score=score
        #     sb.clear()
    #             sb.write(f'Score : {score} | Highest Score : {highest_score}')



        
        # for index in range(len(bodies)-10000,0,-1):
        #     x=bodies[index-1],turtle.xcor()
        #     y=bodies[index-1],turtle.ycor()
        #     bodies[index].goto(x,y)

        if len(bodies)>0:
            x=head.xcor()
            y=head.ycor()
            bodies[0].goto(x,y)
            # if head.direction=='up':
            #     y=head.ycor()
            #     x=head.xcor()
            #         bodies[0].goto(x,y)
            # if head.direction=='down':
            #     y=head.ycor()
            #     x=head.xcor()
            #     bodies[0].goto(x,y)
            # if head.direction=='left':
            #     x=head.xcor()
            #     y=head.ycor()
        #   
                #   bodies[0].goto(x,y)
            # if head.direction=='right':
            #     x=head.xcor()
            #     y=head.ycor()
            #     bodies[0].goto(x,y)
        # co    unt=0
            # q=0
            # for count in range(len(bodies)):
            #     # x=bodies[count].xcor()
            #     # y=bodies[count].ycor()
        #         # bodies[count].goto(x,y)
                #     q+=1
            #     if q!=1:
            #         if head.direction=='up':
        #                 y=bodies[count-1].ycor()
        #             x=bodies[count-1].xcor()
        #             bodies[count].goto(x,y-20)
        #         if head.direction=='down':
        #             y=bodies[count-1].ycor()
        #             x=bodies[count-1].xcor()
        #             bodies[count].goto(x,y+20)
        #         if head.direction=='left':
        #             x=bodies[count-1].xcor()
        #             y=bodies[count-1].ycor()
        #             bodies[count].goto(x+20,y)
        #         if head.direction=='right':
        #             x=bodies[count-1].xcor()
        #             y=bodies[count-1].ycor()
        #             bodies[count].goto(x-20,y)
        #     # else:
        #     #     if head.direction=='up':
        #     #         y=bodies[0].ycor()
        #     #         x=bodies[0].xcor()
        #     #         bodies[1].goto(x,y)
        #     #     if head.direction=='down':
        #     #         y=bodies[0].ycor()
        #     #         x=bodies[0].xcor()
        #     #         bodies[1].goto(x,y)
        #     #     if head.direction=='left':
        #     #         x=bodies[0].xcor()
        #     #         y=bodies[0].ycor()
        #     #         bodies[1].goto(x,y)
        #     #     if head.direction=='right':
        #     #         x=bodies[0].xcor()
        #     #         y=bodies[0].ycor()
        #     #         bodies[1].goto(x,y)
        #     # count+=1
        # # count+=1

        a=1
    # if len(bodies)==2:
    #     print("Done")
    #     x=round(bodies[0].xcor(),0)
    #     y=round(bodies[0].ycor(),0)
    #     bodies[1].goto(x,y)


        if len(bodies)==1:
            bodies.append(body)
            bodies.append(body)



        for index in range(len(bodies)-1,0,-1):
            # if len(bodies) < 2:
            print(index)
            x=round(bodies[index-1].xcor(),0)
            y=round(bodies[index-1].ycor(),0)
            a=1
            bodies[index].goto(x,y)
                # if index==len(bodies):
                    # break
        # else:
            # x=round(bodies[0].xcor(),0)
            # y=round(bodies[0].ycor(),0)
            # bodies[1].goto(x,y)
            # bodies.append(body)
            # a=2
        move()

        for body in bodies:
            if body.distance(head)<20:
                sound = pygame.mixer.Sound(r'crash.mp3')
                pygame.mixer.Sound.play(sound)
                gm.clear()
                gm.write('GAME OVER')
                time.sleep(1)
                head.goto(0,0)
                # label=tk.Label(pygame.Surface,text='Game Over',bg='black',fg='white')

                head.direction='stop'

                for body in bodies:
                    body.ht()
                bodies.clear()

                score=0
                delay=0.1


                sb.clear()
                sb.write(f'Score : 0 | Highest Score : {highest_score}')
        time.sleep(delay)
    


start_game()


    

