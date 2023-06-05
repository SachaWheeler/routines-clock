from os import environ, path
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' # remove pygame announcement
import pygame
from datetime import datetime
import math
from calendar import SCHEDULE, EVENTS, COLORS


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

DIGITAL_H = 100 # height of digital clock
W = 700 # screen width
H = W + DIGITAL_H # screen height
CLOCK_W = W # analog clock width
CLOCK_H = 700 # analog clock height
MARGIN_H = MARGIN_W = 5 # margin of analog clock from window border
CLOCK_R = (W - MARGIN_W) / 2 # clock radius
HOUR_R = CLOCK_R / 2 # hour hand length
MINUTE_R = CLOCK_R * 7 / 10 # minute hand length
SECOND_R = CLOCK_R * 8 / 10 # second hand length
TEXT_R = CLOCK_R * 9 / 10 # distance of hour markings from center
TICK_R = 2 # stroke width of minute markings
TICK_LENGTH = 5 # stroke length of minute markings
HOUR_STROKE = 5 # hour hand stroke width
MINUTE_STROKE = 2 # minute hand stroke width
SECOND_STROKE = 2 # second hand stroke width
CLOCK_STROKE = 2 # clock circle stroke width
CENTER_W = 10 # clock center mount width
CENTER_H = 10 # clock center mount height
HOURS_IN_CLOCK = 24
MINUTES_IN_HOUR = 60
SECONDS_IN_MINUTE = 60
SIZE = (W, H)

ARC_WIDTH = 100
RECT = pygame.Rect((0, 0), (CLOCK_W, CLOCK_H))
PI_2 = 3.14159 * 2
LABEL_R = CLOCK_R * 5.7 / 10 # distance of hour markings from center

def circle_point(center, radius, theta):
    """Calculates the location of a point of a circle given the circle's
       center and radius as well as the point's angle from the xx' axis"""

    return (center[0] + radius * math.cos(theta),
            center[1] + radius * math.sin(theta))

def line_at_angle(screen, center, radius, theta, color, width):
    """Draws a line from a center towards an angle. The angle is given in
       radians."""
    point = circle_point(center, radius, theta)
    pygame.draw.line(screen, color, center, point, width)

def get_angle(unit, total):
    """Calculates the angle, in radians, corresponding to a portion of the clock
       counting using the given units up to a given total and starting from 12
       o'clock and moving clock-wise."""
    return 2 * math.pi * unit / total - math.pi / 2

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Clock')
hour_font = pygame.font.SysFont('Calibri', 25, True, False)
digital_font = pygame.font.SysFont('Calibri', 32, False, False)

label_font = pygame.font.SysFont('Calibri', 18, True, False)

clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    c_x, c_y = CLOCK_W / 2, CLOCK_H / 2
    center = (c_x, c_y)

    # draw the schedule
    for arc in SCHEDULE:
        # ['22:30', '06:30', (224, 224, 224), 'sleep']
        [start, end, label] = arc
        (start_h, start_m) = start.split(":")
        (end_h, end_m) = end.split(":")

        start_angle = get_angle(float(start_h) + 1 * float(start_m) / MINUTES_IN_HOUR, HOURS_IN_CLOCK)
        end_angle = get_angle(float(end_h) + 1 * float(end_m) / MINUTES_IN_HOUR, HOURS_IN_CLOCK)

        # draw schedule sectors
        pygame.draw.arc(screen, COLORS[label], RECT, PI_2 - end_angle, PI_2 - start_angle, ARC_WIDTH)

        # draw schedule labels
        label_text = label_font.render(str(label), True, COLORS[label])
        (label_w, label_h) = label_font.size(str(label))
        #print(label_w, label_h)
        if end_angle > start_angle:
            theta = (start_angle + end_angle) / 2
        else:
            subtract = PI_2 - start_angle
            theta = (end_angle  - subtract) / 2
        label_x, label_y = (circle_point(center, LABEL_R, theta))
        screen.blit(label_text, (label_x - label_w / 2, label_y))


    now = datetime.now()

    # draw clock
    pygame.draw.circle(
        screen,
        BLACK,
        center, CLOCK_W / 2 - MARGIN_W / 2,
        CLOCK_STROKE
    )

    # draw hands
    hour_theta = get_angle(now.hour + 1.0 * now.minute / MINUTES_IN_HOUR, HOURS_IN_CLOCK)
    minute_theta = get_angle(now.minute, MINUTES_IN_HOUR)
    second_theta = get_angle(now.second, SECONDS_IN_MINUTE)

    for (radius, theta, color, stroke) in (
        (HOUR_R, hour_theta, BLACK, HOUR_STROKE),
        (MINUTE_R, minute_theta, BLACK, MINUTE_STROKE),
        (SECOND_R, second_theta, RED, SECOND_STROKE),
    ):
        line_at_angle(screen, center, radius, theta, color, stroke)

    # draw hour markings (text)
    for hour in range(1, HOURS_IN_CLOCK + 1):
        theta = get_angle(hour, HOURS_IN_CLOCK)
        text = hour_font.render(str(hour), True, BLACK)
        screen.blit(text, circle_point(center, TEXT_R, theta))

    # draw minute markings (lines)
    for minute in range(0, MINUTES_IN_HOUR):
        theta = get_angle(minute, MINUTES_IN_HOUR)
        p1 = circle_point(center, CLOCK_R - TICK_LENGTH, theta)
        p2 = circle_point(center, CLOCK_R, theta)
        pygame.draw.line(screen, BLACK, p1, p2, TICK_R)

    # draw digital clock
    digital_text = now.strftime('%H:%M:%S')
    text = digital_font.render(digital_text, True, BLACK)
    screen.blit(
        text,
        [
            W / 2 - digital_font.size(digital_text)[0] / 2,
            H - DIGITAL_H / 2 - digital_font.size(digital_text)[1] / 2
        ]
    )
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
