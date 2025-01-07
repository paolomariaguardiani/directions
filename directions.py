x = 800
y = 300
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{x}, {y}'

import pgzrun
from random import randint

TITLE = "DIRECTIONS"
WIDTH = 512
HEIGHT = 512

bee = Actor('bee')
bee.pos = WIDTH / 2, HEIGHT / 2
bee.angle = 0
flower = Actor('flower2')

bee_angle = 0  # i need this variable for def on_mouse_down(pos)

sinistra = Actor('sinistra', (60, 480))
destra = Actor('destra', ((60+130*1), 480))
avanti = Actor('avanti', ((60+130*2), 480))
indietro = Actor('indietro', ((60+130*3), 480))

score = 0

sounds.intro_haydn_symph_94.play()


def update():
    global score, bee_angle
    if keyboard.left:
        bee.x -= 2
        bee_angle = 90
    elif keyboard.right:
        bee.x += 2
        bee_angle = 270
    elif keyboard.up:
        bee.y -= 2
        bee_angle = 0
    elif keyboard.down:
        bee.y += 2
        bee_angle = 180
    if bee.colliderect(flower):
        # sounds.retro_coin.play()
        place_flower()
        clock.schedule(play_coin, 0.2)
        clock.schedule(change_score, 1)
        # score += 1
    bee.angle = bee_angle



def draw():
    screen.clear()
    screen.blit('grass03', (0,0))
    screen.draw.text(f"SCORE: {score}", center=(WIDTH/2, 40), fontsize= 60)
    flower.draw()
    bee.draw()

    sinistra.draw()
    destra.draw()
    avanti.draw()
    indietro.draw()


def place_flower():  # thanks to a course on Udemy
    flower.x = randint(50, WIDTH-50)
    flower.y = randint(250, HEIGHT-150)


def on_mouse_down(pos):
    global score, bee_angle
    
    if bee.colliderect(flower):
        # clock.schedule(play_coin, 0.7)
        sounds.retro_coin.play()
        clock.schedule(change_score, 1)

    if sinistra.collidepoint(pos):
        bee.x -= 20
        bee_angle = 90
    elif destra.collidepoint(pos):
        bee.x += 20
        bee_angle = 270
    elif avanti.collidepoint(pos):
        bee.y -= 20
        bee_angle = 0
    elif indietro.collidepoint(pos):
        bee.y += 20
        bee_angle = 180    
    sounds.click_1.play()


def play_coin():
    sounds.retro_coin.play()


def change_score():
    global score
    score += 1

place_flower()
pgzrun.go()
