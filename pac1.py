import pygame

class PacMan(pygame.sprite.Sprite):
  def __init__(self, game, centerx, centery):
    super().__init__()
    self.game = game
    
    self.enemigos_anima = []
    for i in range(9):
      file = 'pacGraf/pacman{}.png'.format(i)
      img = pygame.image.load(file).convert()
      img.set_colorkey((255,255,255))
      self.enemigos_anima.append(img)
    
    self.image= self.enemigos_anima[1]  
    self.rect = self.image.get_rect()
    self.rect.centerx = centerx
    self.rect.centery = centery
    self.pulsada = "right"
    self.orientacion = 1
    self.orientacion_max = self.orientacion + 6
    self.vel_x = 2
    self.vel_y = 0
    self.ultimo_update = pygame.time.get_ticks()
    self.fotograma_vel = 50
    
  def update(self):
    calculo = pygame.time.get_ticks()
    if calculo - self.ultimo_update > self.fototgrama_vel :
      self.ultimo_update = calculo
      self.orientacion+= 1
      if self.orientacion >= self.orientacion_max :
        self.orientacion = self.orientacion_max - 6 
        
        centerx = self.rect.centerx
        centery = self.rect.centery
        self.image = self.enemigos_anima[self.orientacion]
        self.rect.centerx = centerx
        self.rect.centery = centery
        
        
    if self.rect.centerx % 25 == 0 and  self.rect.centery % 25 == 0:
      if self.pulsada == 'left':
        self.rect.centerx -= self.game.BSX
        laberinto = self.check_colision_laberinto()
        if not laberinto:
          self.orientacion = 1
          self.orientacio_max = self.orientacion + 6
          self.vel_x = -2
          self.vel_y = 0
        self.rect.centerx += self.game.BSX
      
      if self.pulsada == 'right':
        self.rect.centerx += self.game.BSX
        laberinto = self.check_colision_laberinto()
        if not laberinto:
          self.orientacion = 3
          self.orientacio_max = self.orientacion + 6
          self.vel_x = 2
          self.vel_y = 0
        self.rect.centerx -= self.game.BSX
        
      if self.pulsada == 'up':
        self.rect.centerx -= self.game.BSY
        laberinto = self.check_colision_laberinto()
        if not laberinto:
          self.orientacion = 6
          self.orientacio_max = self.orientacion + 6
          self.vel_x = 0
          self.vel_y = -2
        self.rect.centerx += self.game.BSY
      
      if self.pulsada == 'down':
        self.rect.centerx += self.game.BSY
        laberinto = self.check_colision_laberinto()
        if not laberinto:
          self.orientacion = 8
          self.orientacio_max = self.orientacion + 6
          self.vel_x = 0
          self.vel_y = 2
        self.rect.centerx -= self.game.BSY
      
    laberinto = self.check_colision_laberinto()
    if not laberinto :
      self.rect.centerx += self.vel_x
      self.rect.centery += self.vel_y
    else :
      self.rect.centerx += -self.vel_x
      self.rect.centery += -self.vel_y
      
        
        
        
        
        
  def leer_teclado(self):
    tecla = pygame.key.get_pressed()
    
    if tecla[pygame.K_LEFT]:
      self.pulsada ='left'
    elif tecla[pygame.K_RIGHT]:
      self.pulsada ='right'
    elif tecla[pygame.K_UP]:
      self.pulsada ='up'
    elif tecla[pygame.K_DOWN]:
      self.pulsada ='down'
    
    
  def check_colision_laberiento(self):
    impactos = pygame.sprite.groupcollide(self.game.lista_laberinto, self.game.lista_pacman,False,True)
    for impacto in impactos :
      return True
    
    return False
    
class Laberinto(pygame.sprite.Sprite):
  def __init__(self,game,x,y,valor):
    super().__init__()
    self.image = pygame.image.load('pacGraf/bloquepac.png').convert()
    self.image.set_colorkey((255,255,255))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.valor = valor
  def update(self):
    pass



    
        