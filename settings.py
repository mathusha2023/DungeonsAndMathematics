class Settings:

    @staticmethod
    def config():
        with open("data/db/settings.txt") as file:
            return list(map(float, file.readlines()))

    @staticmethod
    def write():
        with open("data/db/settings.txt", "w") as file:
            file.write("\n".join(map(str, [Settings.vol_music, Settings.vol_sound, Settings.language])))

    eng = 0
    rus = 1
    langs = {0: "english", 1: "русский"}
    start_settings = config()

    vol_music = start_settings[0]
    vol_sound = start_settings[1]
    language = start_settings[2]
