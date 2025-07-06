import pygame
from datetime import datetime, timedelta


def date_creation(hour_value, minute_value, second_value):
    """Returns the alarm datetime, adding a day if the time has already passed."""
    hours = int(hour_value.get())
    minutes = int(minute_value.get())
    seconds = int(second_value.get())

    now = datetime.now()
    alarm_time = now.replace(hour=hours, minute=minutes, second=seconds, microsecond=0)

    if alarm_time < now:
        alarm_time += timedelta(days=1)

    return alarm_time


def check_alarm(window, alarm_datetime, btn):
    """Checks if the alarm time has arrived"""
    now = datetime.now()
    if now >= alarm_datetime:
        try:
            pygame.mixer.init()
            pygame.mixer.music.load('media/alarm_sound.mp3')
            pygame.mixer.music.play()
            btn['text'] = 'The alarm went off!'
            window.deiconify()
        except Exception:
            print('Audio playback error')
    else:
        window.after(1000, check_alarm, window, alarm_datetime, btn)


def set_alarm(window, hour_combobox, minute_combobox, second_combobox, btn):
    """Sets the alarm and hides the window"""
    alarm_time = date_creation(hour_combobox, minute_combobox, second_combobox)
    window.withdraw()
    btn['text'] = 'Alarm clock set!'
    check_alarm(window, alarm_time, btn)
