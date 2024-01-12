from settings import Settings


class Localisation:
    __play = {Settings.eng: "Play!", Settings.rus: "Играть!"}
    __records = {Settings.eng: "Records", Settings.rus: "Рекорды"}
    __settings = {Settings.eng: "Settings", Settings.rus: "Настройки"}
    __exit = {Settings.eng: "Exit", Settings.rus: "Выход"}
    __support = {Settings.eng: "Buy us a coffee", Settings.rus: "Поддержать автора"}
    __music = {Settings.eng: "Music:", Settings.rus: "Музыка:"}
    __sound = {Settings.eng: "Sound:", Settings.rus: "Звуки:"}
    __language = {Settings.eng: "Language:", Settings.rus: "Язык:"}
    __back = {Settings.eng: "Back", Settings.rus: "Назад"}
    __weapon = {Settings.eng: "Weapon", Settings.rus: "Оружие"}
    __time = {Settings.eng: "Time spent", Settings.rus: "Затрачено времени"}
    __date = {Settings.eng: "Date", Settings.rus: "Дата прохождения"}
    __sine = {Settings.eng: "Sine, Envoy of the Mathematics", Settings.rus: "Синус, Посланник Математики"}
    __reply_time = {Settings.eng: "Reply time:", Settings.rus: "Время на ответ:"}
    __sphrase1 = {Settings.eng: "Who are you?",
                 Settings.rus: "Кто ты такой?"}
    __sphrase2 = {Settings.eng: "Some kid got here? Impossible!",
                 Settings.rus: "Какой-то мальчишка добрался сюда? Невозможно!"}
    __sphrase3 = {Settings.eng: "Are you looking for knowledge in mathematics? Well, well, well...",
                 Settings.rus: "Ты ищешь знаний в математике? Ну хорошо"}
    __sphrase4 = {Settings.eng: "If so, you'll have to defeat me!",
                 Settings.rus: "Только для начала тебе придется победить меня!"}
    __sphrase5 = {Settings.eng: "Oh well, you have defeated me",
                 Settings.rus: "Что ж, ты победил меня"}
    __sphrase6 = {Settings.eng: "I will endow you with all my knowledge of mathematics",
                 Settings.rus: "Я дарую тебе все свои знания в математике"}
    __sphrase7 = {Settings.eng: "But will it be enough to fulfill your goal?",
                 Settings.rus: "Но будет ли этого достаточно для выполнения твоей цели?"}

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

    @staticmethod
    def sphrase1():
        return Localisation.__sphrase1[Settings.language]

    @staticmethod
    def sphrase2():
        return Localisation.__sphrase2[Settings.language]

    @staticmethod
    def sphrase3():
        return Localisation.__sphrase3[Settings.language]

    @staticmethod
    def sphrase4():
        return Localisation.__sphrase4[Settings.language]

    @staticmethod
    def sphrase5():
        return Localisation.__sphrase5[Settings.language]

    @staticmethod
    def sphrase6():
        return Localisation.__sphrase6[Settings.language]

    @staticmethod
    def sphrase7():
        return Localisation.__sphrase7[Settings.language]
