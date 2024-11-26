import pygame
import random
import sys
from pac1 import *
#from pac2 import *


class Game :
  def __init__(self):
    pygame.init()
    pygame.mixer.init()
    self.AMARILLO = (220,190,0)
    self.BLANCO = (240,240,240)
    self.GRIS_FONDO = (73,73,73)
    self.ROJO = (230,0,0)
    self.VERDE_FONDO = (20,110,40)
    self.AZUL_C = (144,205,205)
    self.gameover = True
    self.nivel_superado = True
    self.pausa_superado_tomartiempo = pygame.time.get_ticks()
    BLOQUE_SIZE_X = 50
    BLOQUE_SIZE_Y = 50
    self.BSX =  BLOQUE_SIZE_X
    self.BSY =  BLOQUE_SIZE_Y
    self.crear_laberinto = [
			9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,
			9,5,1,1,1,1,1,1,1,9,1,1,1,1,1,1,1,5,9,
			9,1,9,9,1,9,9,9,1,9,1,9,9,9,1,9,9,1,9,

			9,1,9,9,1,9,9,9,1,9,1,9,9,9,1,9,9,1,9,
			9,1,1,1,2,1,1,1,1,0,1,1,1,1,2,1,1,1,9,
			9,1,9,9,1,9,1,9,9,9,9,9,1,9,1,9,9,1,9,

			9,1,1,1,1,9,1,1,1,9,1,1,1,1,1,1,1,1,9,
			9,9,9,9,1,9,9,9,1,9,1,9,9,9,1,9,9,9,9,
			9,1,1,1,2,1,1,1,1,1,1,1,1,1,2,1,1,1,9,

			9,1,9,9,1,9,1,9,9,9,9,9,1,9,1,9,9,1,9,
			9,1,9,9,1,9,1,9,9,9,9,9,1,9,1,9,9,1,9,
			0,1,1,1,1,9,1,1,1,0,1,1,1,9,1,1,1,1,0,

			9,1,9,9,1,9,1,9,9,9,9,9,1,9,1,9,9,1,9,
			9,5,1,1,2,1,1,1,1,0,1,1,1,1,2,1,1,5,9,
			9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,
			]
    self.puntos = 0
    self.nivel  = 1
    self.vidas  = 3
    self.PAUSA_VIDAS = 2000
    self.RESOLUCION = (1200,700)
    self.FPS = 60
    self.pantalla = pygame.display.set_mode(self.RESOLUCION)
    pygame.display.set_caption("PacJon by Diego Hernan")
    self.reloj = pygame.time.Clock()
    self.lista_sprites_adibujar = pygame.sprite.Group()
    self.lista_pacman = pygame.sprite.Group()
    self.lista_laberinto = pygame.sprite.Group()
    
    self.crear_pantalla()
    
    
    
    
  def crear_pantalla(self):
    contador = -1
    for y in range(21):
      for x in range(19):
        contador += 1
        valor = self.crear_laberinto[contador]
        if valor == 9 :
          self.laberinto = Laberinto(self,x * self.BSX,y*self.BSY,valor)
          self.lista_sprites_adibujar_add(self.laberinto)
    
        
  
  def new_game(self):
    self.puntos = 0
    self,nivel = 1
    self.vidas = 3
    
    self.pacman = PacMan(self,75,75)
    self.lista_sprites_adibujar.add(self.pacman)
    self.lista_pacman.add(self.pacman)
  def check_nivelsuperado(self):
    pass
  
  def pausa_nivelsuperado(self):
    pass
  
  def update(self):
    self.lista_sprites_adibujar.update
    
    
    pygame.display.flip()
    self.reloj.tick(self.FPS)
    
  def draw(self):
    self.pantalla.fill(self.GRIS_FONDO)
    #self.pantalla.blit(self.fondo,[0,0])
    self.lista_sprites_adibujar.draw(self.pantalla)
    
  def check_si_instancia_otro_pacman(self):
    pass
  
  def check_event(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT :
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN and self.gameover :
        if pygame.K_KP_ENTER:
          self.gameover = False
          self.new_game()
          self.run()
        
      elif not self.gameover :
        self.pacman.leer_teclado()
        
        
        
  def run(self) :
    while not self.gameover :
      self.check_event()
      self.update()
      self.draw()
      
      
    while self.gameover:
      self.update()
      self.draw()
      self.check_event()
      
      
if __name__ == '__main__' :
  game = Game()
  game.run()
      
    
  
  
    
    
