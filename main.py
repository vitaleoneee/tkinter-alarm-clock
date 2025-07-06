import tkinter as tk
from tkinter import ttk
from datetime import datetime
from alarm_clock.constants import HOUR_VALUES, SECOND_VALUES, MINUTE_VALUES
from alarm_clock.utils import set_alarm


def main():
    window = tk.Tk()
    window.title("Alarm clock by vitaleoneee")
    window.resizable(width=False, height=False)
    window.geometry("320x180+0+0")

    # Часы
    hour_combobox = create_combobox(window, "Hour", HOUR_VALUES, datetime.now().hour)
    minute_combobox = create_combobox(window, "Minute", MINUTE_VALUES, datetime.now().minute)
    second_combobox = create_combobox(window, "Second", SECOND_VALUES, datetime.now().second)

    btn = ttk.Button(
        window,
        text='Set an alarm',
        command=lambda: set_alarm(window, hour_combobox, minute_combobox, second_combobox, btn)
    )
    btn.pack(pady=10)

    window.mainloop()


def create_combobox(window, label_text, values, default_value):
    tk.Label(window, text=label_text).pack()
    combobox = ttk.Combobox(window, values=values, width=5)
    combobox.pack()
    combobox.set(default_value)
    return combobox


if __name__ == "__main__":
    main()
