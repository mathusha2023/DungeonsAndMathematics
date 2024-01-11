from settings import Settings


class Localisation:
    __play = {Settings.eng: "Play!", Settings.rus: "Играть!"}
    __records = {Settings.eng: "Records", Settings.rus: "Рекорды"}
    __settings = {Settings.eng: "Settings", Settings.rus: "Настройки"}
    __exit = {Settings.eng: "Exit", Settings.rus: "Выход"}
    __support = {Settings.eng: "Support author", Settings.rus: "Поддержать автора"}
    __music = {Settings.eng: "Music:", Settings.rus: "Музыка:"}
    __sound = {Settings.eng: "Sound:", Settings.rus: "Звуки:"}
    __language = {Settings.eng: "Language:", Settings.rus: "Язык:"}
    __back = {Settings.eng: "Back", Settings.rus: "Назад"}
    __weapon = {Settings.eng: "Weapon", Settings.rus: "Оружие"}
    __time = {Settings.eng: "Time needed", Settings.rus: "Затрачено времени"}
    __date = {Settings.eng: "Date", Settings.rus: "Дата прохождения"}
    __sine = {Settings.eng: "Sine, Envoy of the Mathematics", Settings.rus: "Синус, Посланник Математики"}
    __reply_time = {Settings.eng: "Reply time:", Settings.rus: "Время на ответ:"}

    @staticmethod
    def play():
        return Localisation.__play[Settings.language]

    @staticmethod
    def records():
        return Localisation.__records[Settings.language]

    @staticmethod
    def settings():
        return Localisation.__settings[Settings.language]

    @staticmethod
    def exit():
        return Localisation.__exit[Settings.language]

    @staticmethod
    def support():
        return Localisation.__support[Settings.language]

    @staticmethod
    def music():
        return Localisation.__music[Settings.language]

    @staticmethod
    def sound():
        return Localisation.__sound[Settings.language]

    @staticmethod
    def language():
        return Localisation.__language[Settings.language]

    @staticmethod
    def back():
        return Localisation.__back[Settings.language]

    @staticmethod
    def weapon():
        return Localisation.__weapon[Settings.language]

    @staticmethod
    def date():
        return Localisation.__date[Settings.language]

    @staticmethod
    def time():
        return Localisation.__time[Settings.language]

    @staticmethod
    def sine():
        return Localisation.__sine[Settings.language]

    @staticmethod
    def reply_time():
        return Localisation.__reply_time[Settings.language]
