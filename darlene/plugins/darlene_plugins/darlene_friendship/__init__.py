from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name = "Darlene 好感度",
    description = "和 Darlene 社交噢~",
    usage = """
    /查询好感度 ——查询你和 Darlene 的好感度
    """,

    extra = {
        "author": "Bob",
        "version": "0.0.1"
    }
)

from .poke import *

from .pohai import *

from greetings import *