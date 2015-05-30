# coding=utf-8
import plugintypes


class EmoticonsPlugin(plugintypes.TelegramPlugin):
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
