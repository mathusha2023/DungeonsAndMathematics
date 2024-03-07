from settings import settings
import specfunctions


class Skins:
    __character = {0: [specfunctions.load_image("ura/default/ura_left_st.png"),
                       specfunctions.load_image("ura/default/ura_left_go1.png"),
                       specfunctions.load_image("ura/default/ura_left_go2.png"),
                       specfunctions.load_image("ura/default/ura_right_st.png"),
                       specfunctions.load_image("ura/default/ura_right_go1.png"),
                       specfunctions.load_image("ura/default/ura_right_go2.png")],
                   1: [specfunctions.load_image("ura/evil/ura_left_st.png"),
                       specfunctions.load_image("ura/evil/ura_left_go1.png"),
                       specfunctions.load_image("ura/evil/ura_left_go2.png"),
                       specfunctions.load_image("ura/evil/ura_right_st.png"),
                       specfunctions.load_image("ura/evil/ura_right_go1.png"),
                       specfunctions.load_image("ura/evil/ura_right_go2.png")]}

    @staticmethod
    def character():
        return Skins.__character[settings.character_skin]
