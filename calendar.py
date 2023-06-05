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
    ['22:30', '06:00', 'sleep'],
    ['06:00', '06:30', 'coffee'],
    ['06:30', '08:30', 'read'],
    ['08:30', '09:00', 'breakfast'],
    ['09:00', '12:00', 'work'],
    ['12:00', '13:30', 'lunch'],
    ['13:30', '15:00', 'exercise'],
    ['15:00', '16:30', 'work'],
    ['16:30', '20:30', 'personal'],
    ['20:30', '22:30', 'tv'],
        ]

EVENTS = [
    # [hour_min, color, label]
    ['12:00', 'have a drink'],
    ['17:00', 'turn off phone'],
        ]
