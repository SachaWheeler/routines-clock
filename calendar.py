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

SCHEDULE = {
    WORKDAY:(
        ('05:00', 'wake/coffee', ENERGY),
        ('06:30', 'read', PRIVATE),
        ('09:00', 'work', WORK),
        ('15:00', 'work', WORK),
        ('16:30', 'personal', PRIVATE),
        ('20:30', 'tv', ENTERTAINMENT),
        ),
    NON_WORK:(
        ('06:30', 'wake/coffee', ENERGY),
        ('07:00', 'read', PRIVATE),
        ('09:00', 'personal', PRIVATE),
        ('15:00', 'personal', PRIVATE),
        ),
    EVERYDAY:(
        ('22:30', 'sleep', SLEEP),
        ('08:30', 'breakfast', ENERGY),
        ('13:00', 'lunch', ENERGY),
        ('14:30', 'exercise', EXERCISE),
        ('20:30', 'tv', ENTERTAINMENT),
        )
    }

EVENTS = [
    # [hour_min, color, label]
    ['12:00', 'have a drink'],
    ['17:00', 'turn off phone'],
    ['20:00', 'smoke'],
        ]
