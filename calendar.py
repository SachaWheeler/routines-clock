GREY = (224, 224, 224)
GREEN = (0, 204, 0)
LIGHT_GREEN = (102, 255, 102)
ORANGE = (255, 153, 51)
BLUE = (0, 255, 255)

schedule = [
    # [start_hour_min, end_hour_min, color, label]
    ['22:30', '06:30', GREY, 'sleep'],
    ['06:30', '08:30', GREEN, 'read'],
    ['08:30', '09:00', ORANGE, 'coffee'],
    ['09:15', '12:00', LIGHT_GREEN, 'work'],
    ['12:00', '14:00', ORANGE, 'lunch'],
    ['14:00', '15:00', BLUE, 'exercise'],
    ['15:00', '16:00', LIGHT_GREEN, 'work'],
        ]

events = [
    # [hour_min, color, label]
    ['12:00', BLUE, 'have a drink'],
        ]
