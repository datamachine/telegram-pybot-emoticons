# coding=utf-8
from telex.plugin import TelexPlugin


class EmoticonsPlugin(TelexPlugin):
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
