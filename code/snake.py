import random
import time
import turtle

delay=0.1
score=0
highestscore=0
#bodies
bodies=[]
#getting a screen
s=turtle.Screen()
s.bgcolor("grey11")
s.setup(width=750, height=600)
s.title("Snake Game")
s.tracer(0)
#create snake head

head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("red")
head.goto(0,0)
head.penup()
head.direction="stop"
#create snake food

food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("white")
food.fillcolor("yellow")
food.penup()
food.ht()
food.goto(0,150)
food.st()
#create scoreboard
sb=turtle.Turtle()
sb.speed(0)
sb.shape("square")
sb.fillcolor("white")
sb.color('gold1')
sb.penup()
sb.hideturtle()
sb.goto(0, 250)
sb.write("Score : 0  High Score : 0", align="center",
          font=("cambria", 24, "bold"))
#defining function
def moveup():
    if head.direction!="down":
        head.direction="up"
def movedown():
    if head.direction!="up":
        head.direction="down"
def moveleft():
    if head.direction!="right":
        head.direction="left"
def moveright():
    if head.direction!="left":
        head.direction="right"
def movestop():
    head.direction="stop"
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y + 20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y - 20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x - 20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x + 20)
#eventhandling
s.listen()
s.onkey(moveup,"Up")
s.onkey(movedown,"Down")
s.onkey(moveleft,"Left")
s.onkey(moveright,"Right")
s.onkey(movestop,"space")
#main loop
while True:
    s.update()

    if head.xcor()>290:
        head.setx(-290)
    if head.ycor()>290:
        head.sety(-290)
    if head.ycor()<-290:
        head.sety(290)
    if head.xcor()<-290:
        head.setx(290)

    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("gold1")
        body.fillcolor("green")
        body.penup()
        bodies.append(body) 

        score+=10

        delay+=0.001 
        #update highest score

        if score>highestscore:
            highestscore=score
        sb.write("Score : {} High Score : {} ".format(
            score, highestscore), align="center", font=("cambria", 24, "bold"))
#move the snake body
    for index in range(len(bodies)-1,0,-1):
        x=bodies[index-1].xcor()
        y=bodies[index-1].ycor()
        bodies[index].goto(x,y)

    if len(bodies)>0:
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
    move()
#check collison wth snake body
    for body in bodies:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop" 
            #hide bodies

            for body in bodies:
                body.goto(1000,1000)
        
            bodies.clear()
            score = 0
            delay = 0.1
            #pdate score
        sb.clear()
        sb.write("Score : {} High Score : {} ".format(
            score, highestscore), align="center", font=("cambria", 24, "bold"))
        save_score(highestscore)    

          #  score=0
           # delay=0.1  
            #update score card

           # sb.clear()
           # sb.write("Score:{}   Highest Score: {}".format(score,highestscore))
    
    def save_score(scr):
        with open("G55\score text\snake_score.txt","w") as f:
            f.write(f"{scr}\n")

    
    time.sleep(delay)
s.mainloop() 
#end of program