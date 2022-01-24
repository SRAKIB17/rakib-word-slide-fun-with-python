import pygame
import time

screen_size = [950, 950]
#enter time:
screen = pygame.display.set_mode(screen_size)
fps = 60
#while True:
an = [0,1,2,3,4]
x = 5
y = 60
clock = pygame.time.Clock()
while True:
    
    time.sleep(0.0001)
    bg = pygame.image.load('bg.png')
    screen.blit(bg,[46,60])
    for i in an:
     time.sleep(0.001)
     clock.tick(fps)
     if x <= 950:
            
            #pygame.display.update() 
            b = pygame.image.load(f'{i}.png')
            time.sleep(0.1)
            x += 60
            screen.blit(b,[x,y])
            pygame.display.update()
            
        
     elif y <= 950 and x >= 950:
        x = 5
        y += 60
        
     else:
            x = 5
            y = 60
            
			
	
		
