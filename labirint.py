# Разработай свою игру в этом файле!
from pygame import *
win_width=700
win_height=500
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(65,65))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
        
class GameSprite1(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(100,100))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))



class Player(GameSprite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_LEFT] and self.rect.x >5:
            self.rect.x-=self.speed
        
        if keys[K_DOWN] and self.rect.y < win_height-80:
            self.rect.y+=self.speed
        if keys[K_RIGHT] and self.rect.x < 620:
            self.rect.x+=self.speed
        if keys[K_UP] and self.rect.y > 10:
            self.rect.y-=self.speed
class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <=470:
            self.direction='right'
        if self.rect.x >win_width-85:
            self.direction='left'
        if self.direction=='left':
            self.rect.x -= self.speed
        else:
            self.rect.x +=self.speed
class Enemy1(GameSprite):
    direction = "up"
    def update1(self):
        if self.rect.y <=1:
            self.direction='down'
        if self.rect.y >win_height-80:
            self.direction='up'
        if self.direction=='up':
            self.rect.y -= self.speed
        else:
            self.rect.y +=self.speed
class Wall(sprite.Sprite):
    def __init__(self,color_1,color_2,color_3,wall_x,wall_y,wall_width,wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width=wall_width
        self.height=wall_height
        self.image=Surface((self.width,self.height))
        self.image.fill((color_1,color_2,color_3))
        self.rect=self.image.get_rect()
        self.rect.x=wall_x
        self.rect.y=wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

player=Player('hero.png',30,350 - 80,4)
monster=Enemy('cyborg.png',win_width - 80,280,2)
monster2=Enemy1('cyborg1.png',win_height - 40,160,2)
final=GameSprite1('treasure.png',win_width-200,win_height - 100,0)


w1 = Wall(61, 168, 120, 100, 20 , 450, 10)
w2 = Wall(61, 168, 120, 100, 480, 350, 10)
w3 = Wall(61, 168, 120, 200, 20 , 10, 350)
w4 = Wall(61, 168, 120, 300, 100 , 10, 380)  
w5 = Wall(61, 168, 120, 300, 200, 150, 10)
w6 = Wall(61, 168, 120, 100, 20 , 10, 350)
w7 = Wall(61, 168, 120, 400, 20 , 10, 80)
w8 = Wall(61, 168, 120, 450, 200 , 10, 290)

window=display.set_mode((700,500))
background=transform.scale(image.load('background.jpg'),(700,500))
display.set_caption('Maze')
game=True
finish=False
clock=time.Clock()
FPS=600

font.init()
font=font.SysFont('Arial',70)
win=font.render('You WIN!!!', True,(255,215,0))
lose = font.render('You lose!',True,(180,0,0))

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
money=mixer.Sound('money.ogg')
kick=mixer.Sound('kick.ogg')
while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
    if finish !=True:
        window.blit(background,(0,0))
        player.update()
        monster.update()
        monster2.update1()
    
        player.reset()
        monster.reset()
        monster2.reset()
        final.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()


        if sprite.collide_rect(player,monster) or sprite.collide_rect(player,monster2) or sprite.collide_rect(player, w1) or sprite.collide_rect (player, w2) or sprite.collide_rect (player, w3) or sprite.collide_rect (player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect (player, w6) or sprite.collide_rect (player, w7) or sprite.collide_rect (player, w8):
            finish = True
            window.blit(lose,(200,200))
            kick.play()
            a=0
        if sprite.collide_rect(player,final):
            finish=True 
            window.blit(win,(200,200))
            money.play()
        display.update()
        clock.tick(FPS)
    else:
        finish=False
        time.delay(1000)
        player=Player('hero.png',5,win_height-80,4)
        player.reset()
    time.delay(10)
    display.update()    