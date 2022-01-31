from email.mime import image
from multiprocessing.dummy import current_process
import os
import pygame

pygame.init()

screen_width = 640 
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Arcade Game") #게임 이름

# FPS
clock = pygame.time.Clock()
##############################################

# 1. 사용자 게임 초기화
current_path = os.path.dirname(__file__) # 현재 파일 위치 반환
image_path = os.path.join(current_path, "img") # img 폴더 위치 반환

# 배경
backgroud = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# 이벤트 루프
running = True
while running :
    dt = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    
    screen.blit(backgroud, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))

    pygame.display.update()

pygame.quit()