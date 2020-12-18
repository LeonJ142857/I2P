import sys
from pygame import event, QUIT, display, KEYDOWN, KEYUP, K_RIGHT, K_LEFT, K_SPACE
from bullet import Bullet
def check_keydown_events(event, ai_settings, screen, ship, bullets):
	if event.key == K_RIGHT:
		ship.moving_right = True
	elif event.key == K_LEFT:
		ship.moving_left = True
	elif event.key == K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
	if len(bullets) < ai_settings.bullets_allowed :
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def check_keyup_events(ship, event):
	if event.key == K_RIGHT:
		ship.moving_right = False
	elif event.key == K_LEFT:
		ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
	for events in event.get():
		if events.type == QUIT:
			sys.exit()
		elif events.type == KEYDOWN:
			check_keydown_events(events, ai_settings, screen, ship, bullets)
		elif events.type == KEYUP:
			check_keyup_events(ship, events)

def update_screen(ai_settings, screen, ship, bullets):
	screen.fill(ai_settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	display.flip()

def update_bullets(bullets):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

