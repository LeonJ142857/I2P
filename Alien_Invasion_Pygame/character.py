from pygame import *
class Artorias():
	def __init__(self, screen):
		self.screen = screen
		self.image = image.load('images/artorias.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.rect.center = self.screen_rect.center
		self.image.set_colorkey((255, 255, 255))
	def blitme(self):
		self.screen.blit(self.image, self.rect)
