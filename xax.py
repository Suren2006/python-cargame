from tkinter import *
import time, random
import tkinter.font as font
from PIL import Image, ImageTk

xax = Tk()
xax.title('My First Game')
xax.state('zoomed')
xax['bg']= '#4caf50'
xax.iconphoto(False, PhotoImage(file='icon.png'))
canvas1 = Canvas(xax, bg='black')
canvas1.place(relx=0.5,rely=0.75,anchor=CENTER, relwidth=1, relheight=0.4)
canvas111 = Canvas(xax, bg='black')
canvas111.place(relx=0.5,rely=0.35,anchor=CENTER, relwidth=1, relheight=0.4)
canvas2 = Canvas(canvas1, bg='white', width=30, height=2)
canvas3 = Canvas(canvas1, bg='white', width=30, height=2)
canvas4 = Canvas(canvas1, bg='white', width=30, height=2)
canvas5 = Canvas(canvas1, bg='white', width=30, height=2)
canvas6 = Canvas(canvas1, bg='white', width=30, height=2)
canvas7 = Canvas(canvas1, bg='white', width=30, height=2)
canvas8 = Canvas(canvas1, bg='white', width=30, height=2)
canvas9 = Canvas(canvas1, bg='white', width=30, height=2)
canvas10 = Canvas(canvas1, bg='white', width=30, height=2)
canvas11 = Canvas(canvas1, bg='white', width=30, height=2)
canvas12 = Canvas(canvas1, bg='white', width=30, height=2)
canvas13 = Canvas(canvas1, bg='white', width=30, height=2)
canvas14 = Canvas(canvas1, bg='white', width=30, height=2)
canvas15 = Canvas(canvas1, bg='white', width=30, height=2)
canvas16 = Canvas(canvas1, bg='white', width=30, height=2)
canvas17 = Canvas(canvas1, bg='white', width=30, height=2)
canvas18 = Canvas(canvas1, bg='white', width=30, height=2)
canvas19 = Canvas(canvas1, bg='white', width=30, height=2)
canvas20 = Canvas(canvas1, bg='white', width=30, height=2)
canvas112 = Canvas(canvas111, bg='white', width=30, height=2)
canvas113 = Canvas(canvas111, bg='white', width=30, height=2)
canvas114 = Canvas(canvas111, bg='white', width=30, height=2)
canvas115 = Canvas(canvas111, bg='white', width=30, height=2)
canvas116 = Canvas(canvas111, bg='white', width=30, height=2)
canvas117 = Canvas(canvas111, bg='white', width=30, height=2)
canvas118 = Canvas(canvas111, bg='white', width=30, height=2)
canvas119 = Canvas(canvas111, bg='white', width=30, height=2)
canvas1110 = Canvas(canvas111, bg='white', width=30, height=2)
canvas1111 = Canvas(canvas111, bg='white', width=30, height=2)
canvas1112 = Canvas(canvas111, bg='white', width=30, height=2)
canvas1113 = Canvas(canvas111, bg='white', width=30, height=2)
canvas1114 = Canvas(canvas111, bg='white', width=30, height=2)
canvas1115 = Canvas(canvas111, bg='white', width=30, height=2)
canvas1116 = Canvas(canvas111, bg='white', width=30, height=2)
canvas1117 = Canvas(canvas111, bg='white', width=30, height=2)
canvas1118 = Canvas(canvas111, bg='white', width=30, height=2)
canvas1119 = Canvas(canvas111, bg='white', width=30, height=2)
canvas1120 = Canvas(canvas111, bg='white', width=30, height=2)
canvas20.place(relx=1.9, rely=0.5,anchor=CENTER)
canvas18.place(relx=1.7, rely=0.5,anchor=CENTER)
canvas16.place(relx=1.5, rely=0.5,anchor=CENTER)
canvas14.place(relx=1.3, rely=0.5,anchor=CENTER)
canvas12.place(relx=1.1, rely=0.5,anchor=CENTER)
canvas10.place(relx=0.9, rely=0.5,anchor=CENTER)
canvas8.place(relx=0.7, rely=0.5,anchor=CENTER)
canvas6.place(relx=0.5, rely=0.5,anchor=CENTER)
canvas4.place(relx=0.3, rely=0.5,anchor=CENTER)
canvas2.place(relx=0.1, rely=0.5,anchor=CENTER)

canvas1120.place(relx=1.9, rely=0.5,anchor=CENTER)
canvas1118.place(relx=1.7, rely=0.5,anchor=CENTER)
canvas1116.place(relx=1.5, rely=0.5,anchor=CENTER)
canvas1114.place(relx=1.3, rely=0.5,anchor=CENTER)
canvas1112.place(relx=1.1, rely=0.5,anchor=CENTER)
canvas1110.place(relx=0.9, rely=0.5,anchor=CENTER)
canvas118.place(relx=0.7, rely=0.5,anchor=CENTER)
canvas116.place(relx=0.5, rely=0.5,anchor=CENTER)
canvas114.place(relx=0.3, rely=0.5,anchor=CENTER)
canvas112.place(relx=0.1, rely=0.5,anchor=CENTER)



screen_width = xax.winfo_screenwidth()
screen_height = xax.winfo_screenheight()
width_scale = 1366 / 417
height_scale = 768 / 121
width = int((screen_width / width_scale) / 2 )
height = int((screen_height / height_scale) / 2)
car_picture = Image.open('car1.png')
car_resized = car_picture.resize((int(width*1.2), int(height*1.2)), Image.Resampling.LANCZOS)
car_new = ImageTk.PhotoImage(car_resized)
car2_picture = Image.open('car-enemy-1.png')
car2_resized = car2_picture.resize((int(width*1.2), int(height*1.2)), Image.Resampling.LANCZOS)
car2_new = ImageTk.PhotoImage(car2_resized)
car3_picture = Image.open('car-enemy-2.png')
car3_resized = car3_picture.resize((int(width*1.2), int(height*1.7)), Image.Resampling.LANCZOS)
car3_new = ImageTk.PhotoImage(car3_resized)
car4_picture = Image.open('car-enemy-3.png')
car4_resized = car4_picture.resize((int(width*1.2), int(height*1.4)), Image.Resampling.LANCZOS)
car4_new = ImageTk.PhotoImage(car4_resized)
trees_picture = Image.open('tree1.png')
trees_resized = trees_picture.resize((width, int(height*1.8)), Image.Resampling.LANCZOS)
trees_new = ImageTk.PhotoImage(trees_resized)

def up(event):
    if car['text'] == 0.85:
        car.place(rely=0.65)
        car['text'] = 0.65
    elif car['text'] == 0.65:
        car.place(rely=0.45)
        car['text'] = 0.45
    else:
        car.place(rely=0.25)
        car['text'] = 0.25



    
def down(event):
    if car['text'] == 0.25:
        car.place(rely=0.45)
        car['text'] = 0.45
    elif car['text'] == 0.45:
        car.place(rely=0.65)
        car['text'] = 0.65
    else:
        car.place(rely=0.85)
        car['text'] = 0.85

def rely_coordinate(event):
    rely = ['0.25', '0.45', '0.65', '0.85']
    rely2 = random.choice(rely)
    return rely2

def rely_coordinate2(event):
    rely = ['0.25', '0.45', '0.65',  '0.85']
    rely3 = random.choice(rely)
    return rely3

def rely_coordinate3(event):
    rely = ['0.25', '0.45', '0.65',  '0.85']
    rely4 = random.choice(rely)
    return rely4


def quitgame(a):
    xax.destroy()

def sleepgame(a):
    time.sleep(2)
    



xax.bind('<Up>', up)
xax.bind('<Down>', down)
xax.bind('w', up)
xax.bind('s', down)
xax.bind('q', quitgame)
xax.bind('<Control-s>', sleepgame)

tree1 = Label(xax, image=trees_new, border=0)
tree2 = Label(xax, image=trees_new, border=0)
tree3 = Label(xax, image=trees_new, border=0)
tree4 = Label(xax, image=trees_new, border=0)
tree5 = Label(xax, image=trees_new, border=0)
tree6 = Label(xax, image=trees_new, border=0)
tree7 = Label(xax, image=trees_new, border=0)
tree1.place(relx=0.25, rely=0, anchor=N)
tree2.place(relx=0.5, rely=0, anchor=N)
tree3.place(relx=0.75, rely=0, anchor=N)
tree4.place(relx=1, rely=0, anchor=N)
tree5.place(relx=1.25, rely=0, anchor=N)
tree6.place(relx=1.5, rely=0, anchor=N)
tree7.place(relx=1.75, rely=0, anchor=N)

            
controls = Label(xax, fg='white', bg='#4caf50')
controls['text'] = 'ArrowUp or W - Up    ArrowDown or S - Down'
controls['font'] = font.Font(size=18)
controls.place(relx=0, rely=1, anchor=SW)
car2 = Label(xax, image=car2_new, border=0)
car3 = Label(xax, image=car3_new, border=0)
car4 = Label(xax, image=car4_new, border=0)
start = Label(xax, fg='white', bg='#4caf50')
start['text'] = '  Press (R) for start \n Press (Q) for Quit'
start['font'] = font.Font(size=18)
start.place(relx=0, rely=0, anchor=NW)
gameover = Canvas(xax, bg='red', width=400, height=230, border=5)
gameoverlabel = Label(gameover, bg='red')

car = Label(xax, image=car_new, border=0)
car['text'] = 0.45
car['font'] = font.Font(size=1)
car.place(relx=0.01, rely=0.45, anchor=W)

def go(a):
    r = open('high score/high-score.txt')
    high_score = int(r.read())
    r.close()
    speed = 40
    score = 0
    mode = 'Easy'
    gameover.place(relx=0.5, rely=2,anchor=CENTER)
    gameoverlabel.place(relx=0.5, rely=2,anchor=CENTER)
    for i in range(100000):
        xax.update()
        count = 1
        h = rely_coordinate('event')
        g = rely_coordinate2('event')
        j = rely_coordinate3('event')
        if h == g:
            h = rely_coordinate('event')
        if h == g:
            h = rely_coordinate('event')
        if h == j:
            g = rely_coordinate2('event')
        if h == j:
            g = rely_coordinate2('event')
        if j == g:
            j = rely_coordinate3('event')
        if j == g:
            j = rely_coordinate3('event')
        if score >= 479 and score < 1007:
            speed = 33
            mode = 'Medium'
        if score >= 1007 and score< 1482:
            speed = 25
            mode = 'Hard'
        if score >= 1482 and score< 1982:
            speed = 20
            mode = 'Very Hard'
        if score >= 1982:
            speed = 16
            mode = 'Pro Gamer'
        for i in range(speed):
            xax.update()
            time.sleep(0.0001)
            if float(car['text']) == float(h) and i >= speed - (speed / (17/3)):
                break
            if float(car['text']) == float(g) and i >= speed - (speed / (17/3)):
                break
            if float(car['text']) == float(j) and i >= speed - (speed / (17/3)):
                break
            tree1.place(relx=count-0.75, rely=0, anchor=N)
            tree2.place(relx=count-0.5, rely=0, anchor=N)
            tree3.place(relx=count-0.25, rely=0, anchor=N)
            tree4.place(relx=count, rely=0, anchor=N)
            tree5.place(relx=count+0.25, rely=0, anchor=N)
            tree6.place(relx=count+0.5, rely=0, anchor=N)
            tree7.place(relx=count+0.75, rely=0, anchor=N)
            xax.update()
            car2.place(relx=count, rely=g, anchor=W)
            car3.place(relx=count, rely=h, anchor=W)
            car4.place(relx=count, rely=j, anchor=W)
            xax.update()
            canvas20.place(relx=count + 0.9)
            canvas18.place(relx=count + 0.7)
            canvas16.place(relx=count + 0.5)
            canvas14.place(relx=count + 0.3)
            canvas12.place(relx=count + 0.1)
            canvas10.place(relx=count - 0.1)
            canvas8.place(relx=count - 0.3)
            canvas6.place(relx=count - 0.5)
            canvas4.place(relx=count - 0.7)
            canvas2.place(relx=count - 0.9)

            canvas1120.place(relx=count + 0.9)
            canvas1118.place(relx=count + 0.7)
            canvas1116.place(relx=count + 0.5)
            canvas1114.place(relx=count + 0.3)
            canvas1112.place(relx=count + 0.1)
            canvas1110.place(relx=count - 0.1)
            canvas118.place(relx=count - 0.3)
            canvas116.place(relx=count - 0.5)
            canvas114.place(relx=count - 0.7)
            canvas112.place(relx=count - 0.9)
                
            
            if score <479:
                count -= 0.025
            if score>= 479 and score < 1007:
                count -= 0.03
            if score>= 1007 and score < 1482:
                count -= 0.04
            if score >= 1482 and score<1982:
                count -= 0.05
            if score >= 1982:
                count -= 0.0625
            
            if score == high_score:
                high_score += 1
            score +=1
            xax.update()
            scorelabel = Label(xax, fg='white', bg='#4caf50')
            scorelabel['text'] ='High Score: '+str(high_score)+'\n'+'Score'+str(score)
            scorelabel['font'] = font.Font(size=18)
            scorelabel.place(relx=1, rely=0, relwidth=0.2, anchor=NE)
            start['text'] = 'Mode: ' + mode
            
            r = open('high score/high-score.txt', 'w')
            r.write(str(high_score))
            r.close()
            
            xax.update()

        if i<speed - 1:
            gameover.place(relx=0.5, rely=0.5, anchor=CENTER)
            gameoverlabel['text'] = 'Game Over \n Mode: ' + mode + '\nYour score is ' + str(score) + '\n Press (R) for start \n Press (Q) for quit'                                
            gameoverlabel['font'] = font.Font(size=30)
            gameoverlabel.place(relx=0.5, rely=0.5, anchor=CENTER)
            break
        
        
            

xax.bind('r', go)
xax.mainloop()
