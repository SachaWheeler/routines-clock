GREY = (224, 224, 224)
GREEN = (0, 204, 0)
LIGHT_GREEN = (102, 255, 102)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
BLUE = (0, 255, 255)

(SLEEP, ENERGY, PRIVATE, WORK, EXERCISE, ENTERTAINMENT) = (
        1, 2, 3, 4, 5, 6)

(SUN, MON, TUE, WED, THU, FRI, SAT) = (0,1,2,3,4,5,6)
WEEKDAY = (MON, TUE, WED, THU, FRI)
WEEKEND = (SUN, SAT)
WORKDAY = (MON, TUE, WED)

EVERYDAY = WEEKEND + WEEKDAY
NON_WORK = tuple(set(EVERYDAY) ^ set(WORKDAY))

COLORS = {
    SLEEP: GREY,
    ENERGY: ORANGE,
    PRIVATE: LIGHT_GREEN,
    WORK: GREEN,
    EXERCISE: BLUE,
    ENTERTAINMENT: PURPLE
}

TAGS = {
       'wake/coffee': ENERGY,
       'read': PRIVATE,
       'work': WORK,
       'personal': PRIVATE,
       'tv': ENTERTAINMENT,
       'sleep': SLEEP,
       'breakfast': ENERGY,
       'lunch': ENERGY,
       'exercise': EXERCISE,
}

SCHEDULE = {
    WORKDAY:(
        ('05:00', 'wake/coffee'),
        ('06:30', 'read'),
        ('09:00', 'work'),
        ('15:00', 'work'),
        ('16:30', 'personal'),
        ),
    NON_WORK:(
        ('06:30', 'wake/coffee'),
        ('07:00', 'read'),
        ('09:00', 'personal'),
        ('15:00', 'personal'),
        ),
    EVERYDAY:(
        ('22:30', 'sleep'),
        ('08:30', 'breakfast'),
        ('13:00', 'lunch'),
        ('14:30', 'exercise'),
        ('20:30', 'tv'),
        )
    }

RANGES = [
    ['06:00', '10:00', 'coffee'],
    ['12:00', '17:00', 'beer'],
    ['19:00', '23:00', 'smoke'],
        ]

EVENTS = [
    # [hour_min, color, label]
    ['12:00', 'have a drink'],
    ['17:00', 'turn off phone'],
        ]
