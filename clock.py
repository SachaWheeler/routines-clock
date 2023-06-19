from os import environ, path
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' # remove pygame announcement
import pygame
from datetime import datetime, date
import math
from calendar import SCHEDULE, EVENTS, COLORS, TAGS, RANGES



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PINK = (128, 0, 0)

FONT = 'Calibri'

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
INNER_RECT = pygame.Rect(
        (ARC_WIDTH, ARC_WIDTH),
        (CLOCK_W - ARC_WIDTH * 2, CLOCK_H - ARC_WIDTH * 2)
        )
LABEL_R = CLOCK_R * 5.7 / 10 # distance of hour markings from center
EVENT_SIZE = 6
EVENT_TEXT_OFFSET = 7

STAGE_TEXT_OFFSET = 110
STAGE_PROGRESS_OFFSET = 60

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

def get_outline_coords(outline_color, text_color):
    return [(-1, -1, outline_color), (-1, 1, outline_color),
            (1, 1, outline_color), (1, -1, outline_color),
            (0, 0, text_color)]


pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(str(date.today()))

hour_font = pygame.font.SysFont(FONT, 25, True, False)
digital_font = pygame.font.SysFont(FONT, 32, False, False)
label_font = pygame.font.SysFont(FONT, 18, True, False)
event_font = pygame.font.SysFont(FONT, 14, True, False)
stage_font = pygame.font.SysFont(FONT, 48, True, False)
stage_progress_font = pygame.font.SysFont(FONT, 32, True, False)

clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(GREY)

    c_x, c_y = CLOCK_W / 2, CLOCK_H / 2
    center = (c_x, c_y)

    now = datetime.now()
    DAY_OF_WEEK = int(now.date().strftime('%w'))

    DAY_SCHEDULE = []
    DAY_CALENDAR = []

    for key, schedule in SCHEDULE.items():
        if DAY_OF_WEEK in key:
            for item in schedule:
                DAY_SCHEDULE.append(item + (TAGS[item[1]],))
            # print(item[1])

    # sort the DAY_SCHEDULE
    DAY_SCHEDULE.sort()
    DAY_SCHEDULE.insert(0, DAY_SCHEDULE.pop()) #put bedtime up front


    for x in range(len(DAY_SCHEDULE)):
        try:
            END_TIME = DAY_SCHEDULE[x+1][0]
        except:
            END_TIME = DAY_SCHEDULE[0][0]

        DAY_CALENDAR.append([
                DAY_SCHEDULE[x][0],
                END_TIME,
                DAY_SCHEDULE[x][1],
                DAY_SCHEDULE[x][2]])

    midnight = get_angle(0, HOURS_IN_CLOCK)
    current = get_angle(now.hour + 1.0 * now.minute / MINUTES_IN_HOUR, HOURS_IN_CLOCK)
    pygame.draw.arc(screen,
        PINK,
        INNER_RECT, 2 * math.pi - current, 2 * math.pi - midnight,
        ARC_WIDTH)

    # draw the schedule
    for arc in DAY_CALENDAR:
        [start, end, label, label_color] = arc
        (start_h, start_m) = start.split(":")
        (end_h, end_m) = end.split(":")

        start_mins = int(start_h) * 60 + int(start_m)
        end_mins = int(end_h) * 60 + int(end_m)
        now_mins = now.hour * 60 + now.minute

        # print current stage
        if start_mins <= now_mins and now_mins < end_mins:
            stage = str(label)
            stage_progress = f'{int((now_mins - start_mins) * 100 / (end_mins - start_mins))}%'

        start_angle = get_angle(float(start_h) + float(start_m) / MINUTES_IN_HOUR, HOURS_IN_CLOCK)
        end_angle = get_angle(float(end_h) + float(end_m) / MINUTES_IN_HOUR, HOURS_IN_CLOCK)

        # draw schedule sectors
        pygame.draw.arc(screen,
                COLORS[label_color],
                RECT, 2 * math.pi - end_angle, 2 * math.pi - start_angle,
                ARC_WIDTH)

        for (x, y, color) in get_outline_coords(BLACK, COLORS[label_color]):
            # draw schedule labels
            label_text = label_font.render(str(label), True, color)
            (label_w, label_h) = label_font.size(str(label))

            if end_angle > start_angle:
                theta = (start_angle + end_angle) / 2
            else:
                subtract = 2 * math.pi - start_angle
                theta = (end_angle  - subtract) / 2
            label_x, label_y = (circle_point(center, LABEL_R, theta))
            screen.blit(label_text, (label_x - label_w / 2 + x, label_y - label_h / 2 + x))

    inc = 10
    for range_span in RANGES:
        start, end, tag = range_span
        (start_h, start_m) = start.split(":")
        (end_h, end_m) = end.split(":")

        start_angle = get_angle(float(start_h) + float(start_m) / MINUTES_IN_HOUR, HOURS_IN_CLOCK)
        end_angle = get_angle(float(end_h) + float(end_m) / MINUTES_IN_HOUR, HOURS_IN_CLOCK)

        RANGE_RECT = pygame.Rect(
            (ARC_WIDTH + inc, ARC_WIDTH + inc),
            (
                CLOCK_W - ARC_WIDTH * 2 - inc,
                CLOCK_H - ARC_WIDTH * 2 - inc
                )
            )
        pygame.draw.arc(screen,
            BLUE,
            RANGE_RECT, 2 * math.pi - end_angle,
            2 * math.pi - start_angle,
            10)
        # inc -= inc

    for cal_event in EVENTS:
        #['12:00', 'have a drink']
        (event_time, event_label) = cal_event
        (event_h, event_m) = event_time.split(":")

        theta = get_angle(float(event_h) + float(event_m) / MINUTES_IN_HOUR, HOURS_IN_CLOCK)
        event_x, event_y = (circle_point(center, CLOCK_W / 2 - ARC_WIDTH + 20, theta))
        pygame.draw.circle(
            screen,
            BLUE,
            (event_x, event_y), EVENT_SIZE, EVENT_SIZE
        )
        event_text = event_font.render(event_label, True, BLUE)
        screen.blit(event_text, (event_x + EVENT_TEXT_OFFSET, event_y - EVENT_TEXT_OFFSET))

    # draw clock
    pygame.draw.circle(
        screen,
        BLACK,
        center, CLOCK_W / 2 - MARGIN_W / 2,
        CLOCK_STROKE
    )

    # draw hands
    hour_theta = get_angle(now.hour + now.minute / MINUTES_IN_HOUR, HOURS_IN_CLOCK)
    minute_theta = get_angle(now.minute, MINUTES_IN_HOUR)
    second_theta = get_angle(now.second, SECONDS_IN_MINUTE)

    for (radius, theta, color, stroke) in (
        (HOUR_R, hour_theta, BLACK, HOUR_STROKE),
        (MINUTE_R, minute_theta, BLACK, MINUTE_STROKE),
        (SECOND_R, second_theta, RED, SECOND_STROKE),
    ):
        line_at_angle(screen, center, radius, theta, color, stroke)

    # print current stage (over the hands) with progress
    for (x, y, color) in get_outline_coords(WHITE, BLACK):
        stage_text = stage_font.render(stage, True, color)
        (stage_w, stage_h) = stage_font.size(stage)
        screen.blit(stage_text, (c_x - stage_w/2 + x, c_y - STAGE_TEXT_OFFSET + y))
    for (x, y, color) in get_outline_coords(WHITE, BLACK):
        stage_percent = stage_progress_font.render(stage_progress, True, color)
        (stage_prog_w, stage_prog_h) = stage_progress_font.size(stage_progress)
        screen.blit(stage_percent, (c_x - stage_prog_w/2 + x, c_y - STAGE_PROGRESS_OFFSET + y))

    # draw hour markings (text)
    for hour in range(1, HOURS_IN_CLOCK + 1):
        theta = get_angle(hour, HOURS_IN_CLOCK)
        text = hour_font.render(str(hour), True, BLACK)
        (text_w, text_h) = hour_font.size(str(hour))
        text_x, text_y = (circle_point(center, TEXT_R, theta))
        screen.blit(text, (text_x - text_w / 2, text_y - text_h / 2))

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
