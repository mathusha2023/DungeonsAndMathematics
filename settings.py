class Settings:
    eng = 0
    rus = 1
    langs = {0: "english", 1: "русский"}
    spiders = False

    def __init__(self):
        with open("data/db/settings.txt") as file:
            a, b, c, d = list(map(float, file.readlines()))
        self.vol_music = a
        self.vol_sound = b
        self.language = int(c)
        self.character_skin = int(d)

    def write(self):
        with open("data/db/settings.txt", "w") as file:
            file.write("\n".join(map(str, [self.vol_music, self.vol_sound, self.language, self.character_skin])))

    def change_spiders(self):
        self.spiders = not self.spiders


settings = Settings()
