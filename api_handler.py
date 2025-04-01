import requests as req

class API_Handler():
    def __init__(self):
        self.__platform = None
        self.__base_url = "https://www.gamerpower.com/api/giveaways"
        self.__platformDictionary = {
            "PC": "pc",
            "Steam": "steam",
            "Epic Games Store": "epic-games-store",
            "Ubisoft Connect": "ubisoft",
            "GOG": "gog",
            "itch.io": "itchio",
            "PlayStation 4": "ps4",
            "PlayStation 5": "ps5",
            "Xbox One": "xbox-one",
            "Xbox Series X|S": "xbox-series-xs",
            "Nintendo Switch": "switch",
            "Android": "android",
            "iOS": "ios",
            "Virtual Reality": "vr",
            "Battle.net": "battlenet",
            "EA Origin": "origin",
            "DRM-Free": "drm-free",
            "Xbox 360": "xbox-360"
        }

    def set_platform(self, platform):
        if platform in self.__platformDictionary:
            self.__platform = self.__platformDictionary[platform]
        else:
            raise ValueError

    def get_platforms(self):
        return self.__platformDictionary

    def build(self):
        if self.__platform != None:
            platform =  f"?platform={self.__platform}"
        else:
            platform = ""
        return f"{self.__base_url}{platform}"
    
    def call(self):
        return req.get(self.build()).json()