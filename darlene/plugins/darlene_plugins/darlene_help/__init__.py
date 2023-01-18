"""
Nonebot 2 Help Plugin
Author: XZhouQD
Since: 16 May 2021
"""
import nonebot
from .handler import helper


default_start = list(nonebot.get_driver().config.command_start)[0]

# New way of self registering (use PluginMetadata)
__plugin_meta__ = nonebot.plugin.PluginMetadata(
    name='Darlene 帮助菜单',
    description='轻量级帮助插件',
    usage=f'''欢迎使用Darlene 帮助菜单
本插件提供公共帮助菜单能力
Darlene 配置的命令前缀：{" ".join(list(nonebot.get_driver().config.command_start))}
{default_start}help  # 获取本插件帮助
{default_start}help list  # 展示已加载插件列表
{default_start}help <插件名>  # 调取目标插件帮助信息
''',
    extra={
        "version": "0.1.0",
        "author": "bob",
        }
)