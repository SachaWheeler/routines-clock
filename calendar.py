GREY = (224, 224, 224)
GREEN = (0, 204, 0)
LIGHT_GREEN = (102, 255, 102)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
BLUE = (0, 255, 255)

SLEEP = 1,
ENERGY = 2,
PRIVATE = 3,
WORK = 4,
EXERCISE = 5,
ENTERTAINMENT = 6

COLORS = {
    SLEEP: GREY,
    ENERGY: ORANGE,
    PRIVATE: LIGHT_GREEN,
    WORK: GREEN,
    EXERCISE: BLUE,
    ENTERTAINMENT: PURPLE
}

SCHEDULE = [
    # [start_hour_min, end_hour_min, color, label]
    ['22:30', '06:00', 'sleep', SLEEP],
    ['06:00', '06:30', 'coffee', ENERGY],
    ['06:30', '08:30', 'read', PRIVATE],
    ['08:30', '09:00', 'breakfast', ENERGY],
    ['09:00', '13:00', 'work', WORK],
    ['13:00', '14:30', 'lunch', ENERGY],
    ['14:30', '15:00', 'exercise', EXERCISE],
    ['15:00', '16:30', 'work', WORK],
    ['16:30', '20:30', 'personal', PRIVATE],
    ['20:30', '22:30', 'tv', ENTERTAINMENT],
        ]

EVENTS = [
    # [hour_min, color, label]
    ['12:00', 'have a drink'],
    ['17:00', 'turn off phone'],
    ['20:00', 'smoke'],
        ]
