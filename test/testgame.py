import pygame

pygame.init #초기화

#화면 크기 설정
screen_width = 480 #가로
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Arcade Game") #게임 이름

#FPS
clock = pygame.time.Clock()

#배경 이미지 불러오기
backgroud = pygame.image.load("img\\background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("img\\character.png")
character_size = character.get_rect().size #이미지 크기 구하기
character_width = character_size[0] #캐릭터 가로 크기
character_height = character_size[1] #캐릭터 세로 크기
character_x_pos = (screen_width/2) - (character_width/2) #화면 가로 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height #화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 적 캐릭터
enemy = pygame.image.load("img\\character.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width/2) - (enemy_width/2) 
enemy_y_pos = (screen_height/2) - (enemy_height/2)
enemy_speed = 10


#이동할 좌표
to_x = 0
to_y = 0

#이동 속도
character_speed = 0.6


#폰트 정의
game_font = pygame.font.Font(None, 40) #폰트 객체 (폰트, 크기)

#총 시간
total_time = 10

#시작 시간
start_ticks = pygame.time.get_ticks()


#이벤트 루프
running = True #게임 진행 체크

while running :
    dt = clock.tick(10) #초당 프레임 수

    for event in pygame.event.get(): #어떤 이벤트가 발생하였는지 체크
        if event.type == pygame.QUIT: #창이 닫히는 이벤트 발생 체크
            running = False #게임 중지

        if event.type == pygame.KEYDOWN: #키보드 키
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    
    #충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos


    #충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌")
        running = False


    screen.blit(backgroud, (0, 0)) #배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))


    #타이머
    #경과 시간 계산
    elasped_time = (pygame.time.get_ticks() - start_ticks) / 1000
    #경과 시간(ms)을 1000으로 나누어서 초(s)단위로 표시

    #출력할 글자, True, 글자 색상
    timer = game_font.render(str(int(total_time - elasped_time)), True, (255, 255, 255))
    
    screen.blit(timer,(10, 10))

    if total_time - elasped_time <= 0:
        print("타임아웃")
        running = False

    
    pygame.display.update() #게임 화면 다시 그리기


#잠시 대기
pygame.time.delay(2000) #2초 대기

#pygame 종료
pygame.quit()