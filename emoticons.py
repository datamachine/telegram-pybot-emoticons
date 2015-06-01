# coding=utf-8
from telegrambot.plugin import TelegramPlugin


class EmoticonsPlugin(TelegramPlugin):
    patterns = {
        "^!lod": "lod",
        "^!lolidk": "lolidk"
    }

    usage = [
        "!lod, !lolidk",
    ]

    def lod(self, msg, matches):
        return "ಠ_ಠ"

    def lolidk(self, msg, matches):
        return "¯\_(ツ)_/¯"
