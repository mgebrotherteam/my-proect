
win_width = 700
class GameSprite(sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
win_height = 500

window =display.set_mode((win_width,win_height))
display.set_caption('Maze')
background = transform.scale(image.load('background.jpg'),(win_width,win_heigth):
super().__init__()
    self.image =transform.scale(image.load(player_image),(65,65))
    self.speed =player_speed
    self.rect  =self.image.get_rect()
    self.rect.x=player_x
    self.rect.x=player_y
def reset(self):
    window.blit(self.image,(self.rect.x,self.rect.y))

mixer.init()
mixer.music.load('jingles.ogg')
mixer.music.play()

player =GameSprite('hero.jpg',5,10,5)
monster=GameSprite('cyborg.jpg',650,230,2)
final =GameSprite('hero.jpg',650,230,2)
game =True
while game:

    for e in event.get():
        if e.type() ==QUIT:
            game =False

window.blit(background,(0,0))

deisplay.update()
clock.tick(FPS)

class Wall(sprite.sprite):
    def__init__(self,color_2,color_3,wall_x,wall_y,wall_width,wall_height):
    (self, color 1, color 2, color 3, wall x, wally, wall width, wall_height): () init()
self.color 1 color 1 self.color 2 color 2
self.color 3 color 3
self.width wall width
self.height wall height
self.image Surface ((self.width, self.height))
self.image.fill((color 1, color 2, color_3))
self.rect self.image.get_ract()
self.rect.x wall x
self.rect.y wally def draw(self):
window.blit(self.image, (self.rect.x, self.rect.y

if sprite.collide_rect (player, monster) or sprite.collide_rect (player, w1) or sprite.collide_rect(player w3)
finish True
window.blit(loss, (200, 200))
kick.play()
#Ситуация "Выигрыш"
if sprite.collide_rect (player, final):

    finish True

    window.blit (win, (200, 200))

    money.play()

    display.update()

clock.tick (FPS)
