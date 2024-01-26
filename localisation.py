import random
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
    __clear = {settings.eng: "Clear", settings.rus: "Сбросить"}
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
    __audiophrase_path = {settings.eng: "data/audio/bossphrases/eng/phrase{}_eng.wav",
                          settings.rus: "data/audio/bossphrases/rus/phrase{}_rus.wav"}
    __tobecontinued = {settings.eng: "To be continued...", settings.rus: "Продолжение следует..."}
    __youdead = {settings.eng: "YOU ARE DEAD!", settings.rus: "Ты был убит!"}
    __youdevoured = {settings.eng: "YOU WERE DEVOURED!", settings.rus: "Пауки сожрали тебя!"}
    __spiderdungeon_path = {settings.eng: "data/audio/spider_dungeon_en.ogg",
                            settings.rus: "data/audio/spider_dungeon_ru.ogg"}
    __title1 = {settings.eng: "2 + 2 = 5", settings.rus: "2 + 2 = 5"}
    __title2 = {settings.eng: "physics is better", settings.rus: "физика лучше!"}
    __title3 = {settings.eng: "the story of useless science", settings.rus: "история о бесполезной науке"}
    __title4 = {settings.eng: "kill them all!", settings.rus: "убей их всех!"}
    __title5 = {settings.eng: "try Soul Knight!", settings.rus: "попробуй Soul Knight!"}
    __title6 = {settings.eng: "just don't touch the right corner of the settings!",
                settings.rus: "только не трогай правый угол настроек!"}

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
    def clear():
        return Localisation.__clear[settings.language]

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

    @staticmethod
    def audiophrase_path():
        return Localisation.__audiophrase_path[settings.language]

    @staticmethod
    def to_be_continued():
        return Localisation.__tobecontinued[settings.language]

    @staticmethod
    def you_dead():
        return Localisation.__youdead[settings.language]

    @staticmethod
    def you_devoured():
        return Localisation.__youdevoured[settings.language]

    @staticmethod
    def spider_dungeon_music_path():
        return Localisation.__spiderdungeon_path[settings.language]

    @staticmethod
    def title():
        return random.choice((Localisation.__title1, Localisation.__title2, Localisation.__title3,
                              Localisation.__title4, Localisation.__title5, Localisation.__title6))[settings.language]
