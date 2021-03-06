import random
import pygame
import spidev
import os
import time
import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BCM)

pin_num = [16, 12, 13, 19, 26, 20, 21]
pin_dp = 6
GPIO.setwarnings(False)
for num in pin_num:
    GPIO.setup(num, GPIO.OUT)
    GPIO.output(num, GPIO.LOW)
GPIO.setup(pin_dp, GPIO.LOW)

seg = [
    [16, 12, 13, 19, 26, 20], [12, 13], [16, 12, 21, 26, 19], [16, 12, 13, 19, 21], [20, 21, 12, 13], [16, 20, 21,
                                                                                                       13, 19], [16, 20, 26, 19, 13, 21], [20, 16, 12, 13], [16, 12, 13, 19, 26, 20, 21], [16, 12, 13, 19, 20, 21], [26, 12, 21, 13, 20]
]

swt_channel = 2  # SWITCH NU REU NEUN GEO JOYSTICK = 0
vrx_channel = 1  # VRX IS CONNECTED TO 1
vry_channel = 0  # VRY IS CONNECTED TO 2

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000  # million hz!


def readChannel(channel):
    val = spi.xfer2([1, (8+channel) << 4, 0])
    data = ((val[1] & 3) << 8) + val[2]
    return data


pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Edureka')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
pin_buzzer = 14
GPIO.setup(pin_buzzer, GPIO.OUT)

pwm = GPIO.PWM(pin_buzzer, 1)

dead_sound_played = False
old_score = 0
def Your_score(score):
    global old_score
    if score > old_score:
        GPIO.output(seg[8], 0)
        if score >= 10:
            GPIO.output(seg[10], 1)
        else:
            GPIO.output(seg[score], 1)
        pwm.start(90)
        pwm.ChangeFrequency(262)
        time.sleep(.1)
        pwm.ChangeFrequency(349)
        time.sleep(.1)
        pwm.stop()
        old_score = score
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
        global dead_sound_played
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
            if not dead_sound_played:
                pwm.start(90)
                pwm.ChangeFrequency(493)
                time.sleep(.1)
                pwm.ChangeFrequency(440)
                time.sleep(.1)
                pwm.ChangeFrequency(391)
                time.sleep(.1)
                pwm.ChangeFrequency(349)
                time.sleep(.1)
                pwm.stop()
                dead_sound_played = True
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        dead_sound_played = False
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        if readChannel(vrx_channel) < 300:
            x1_change = -snake_block
            y1_change = 0
        elif readChannel(vrx_channel) > 700:
            x1_change = snake_block
            y1_change = 0
        elif readChannel(vry_channel) > 700:
            y1_change = -snake_block
            x1_change = 0
        elif readChannel(vry_channel) < 300:
            y1_change = snake_block
            x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(
                0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(
                0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
