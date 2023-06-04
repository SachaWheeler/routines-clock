GREY = (224, 224, 224)
GREEN = (0, 204, 0)
LIGHT_GREEN = (102, 255, 102)
ORANGE = (255, 153, 51)
BLUE = (0, 255, 255)

COLORS = {
    "sleep": GREY,
    "read": LIGHT_GREEN,
    "coffee": ORANGE,
    "breakfast": ORANGE,
    "work": GREEN,
    "lunch": ORANGE,
    "exercise": BLUE,
    "personal": LIGHT_GREEN,
    "tv": ORANGE,
        }

SCHEDULE = [
    # [start_hour_min, end_hour_min, color, label]
    ['22:30', '06:30', 'sleep'],
    ['06:30', '07:00', 'coffee'],
    ['07:00', '08:45', 'read'],
    ['08:45', '09:00', 'breakfast'],
    ['09:15', '12:00', 'work'],
    ['12:00', '14:00', 'lunch'],
    ['14:00', '15:00', 'exercise'],
    ['15:00', '16:00', 'work'],
    ['16:00', '20:30', 'personal'],
    ['20:30', '22:30', 'tv'],
        ]

EVENTS = [
    # [hour_min, color, label]
    ['12:00', 'have a drink'],
        ]
