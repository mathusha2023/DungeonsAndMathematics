from settings import settings


class Localisation:
    __play = {settings.eng: "Play!", settings.rus: "Играть!"}
    __records = {settings.eng: "Records", settings.rus: "Рекорды"}
    __settings = {settings.eng: "Settings", settings.rus: "Настройки"}
    __exit = {settings.eng: "Exit", settings.rus: "Выход"}
    __support = {settings.eng: "Buy us a coffee", settings.rus: "Поддержать автора"}
    __music = {settings.eng: "Music:", settings.rus: "Музыка:"}
    __sound = {settings.eng: "Sound:", settings.rus: "Звуки:"}
    __language = {settings.eng: "Language:", settings.rus: "Язык:"}
    __back = {settings.eng: "Back", settings.rus: "Назад"}
    __weapon = {settings.eng: "Weapon", settings.rus: "Оружие"}
    __time = {settings.eng: "Time spent", settings.rus: "Затрачено времени"}
    __date = {settings.eng: "Date", settings.rus: "Дата прохождения"}
    __sine = {settings.eng: "Sine, Envoy of the Mathematics", settings.rus: "Синус, Посланник Математики"}
    __reply_time = {settings.eng: "Reply time:", settings.rus: "Время на ответ:"}
    __sphrase1 = {settings.eng: "Who are you?",
                  settings.rus: "Кто ты такой?"}
    __sphrase2 = {settings.eng: "Some kid got here? Impossible!",
                  settings.rus: "Какой-то мальчишка добрался сюда? Невозможно!"}
    __sphrase3 = {settings.eng: "Are you looking for knowledge in mathematics? Well, well, well...",
                  settings.rus: "Ты ищешь знаний в математике? Ну хорошо"}
    __sphrase4 = {settings.eng: "If so, you'll have to defeat me!",
                  settings.rus: "Только для начала тебе придется победить меня!"}
    __sphrase5 = {settings.eng: "Oh well, you have defeated me",
                  settings.rus: "Что ж, ты победил меня"}
    __sphrase6 = {settings.eng: "I will endow you with all my knowledge of mathematics",
                  settings.rus: "Я дарую тебе все свои знания в математике"}
    __sphrase7 = {settings.eng: "But will it be enough to fulfill your goal?",
                  settings.rus: "Но будет ли этого достаточно для выполнения твоей цели?"}

    @staticmethod
    def play():
        return Localisation.__play[settings.language]

    @staticmethod
    def records():
        return Localisation.__records[settings.language]

    @staticmethod
    def settings():
        return Localisation.__settings[settings.language]

    @staticmethod
    def exit():
        return Localisation.__exit[settings.language]

    @staticmethod
    def support():
        return Localisation.__support[settings.language]

    @staticmethod
    def music():
        return Localisation.__music[settings.language]

    @staticmethod
    def sound():
        return Localisation.__sound[settings.language]

    @staticmethod
    def language():
        return Localisation.__language[settings.language]

    @staticmethod
    def back():
        return Localisation.__back[settings.language]

    @staticmethod
    def weapon():
        return Localisation.__weapon[settings.language]

    @staticmethod
    def date():
        return Localisation.__date[settings.language]

    @staticmethod
    def time():
        return Localisation.__time[settings.language]

    @staticmethod
    def sine():
        return Localisation.__sine[settings.language]

    @staticmethod
    def reply_time():
        return Localisation.__reply_time[settings.language]

    @staticmethod
    def sphrase1():
        return Localisation.__sphrase1[settings.language]

    @staticmethod
    def sphrase2():
        return Localisation.__sphrase2[settings.language]

    @staticmethod
    def sphrase3():
        return Localisation.__sphrase3[settings.language]

    @staticmethod
    def sphrase4():
        return Localisation.__sphrase4[settings.language]

    @staticmethod
    def sphrase5():
        return Localisation.__sphrase5[settings.language]

    @staticmethod
    def sphrase6():
        return Localisation.__sphrase6[settings.language]

    @staticmethod
    def sphrase7():
        return Localisation.__sphrase7[settings.language]
