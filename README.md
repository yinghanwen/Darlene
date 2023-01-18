# Darlene

Darlene 是一款基于 NoneBot2 和 OneBot V11 的多功能机器人。

![Python Version](https://img.shields.io/badge/python-3.10.9-blue.svg?style=flat-square)
![NoneBot Version](https://img.shields.io/badge/nonebot-2.0.0rc2+-red.svg?style=flat-square)
[![OneBot V12](https://img.shields.io/badge/OneBot-11-black?style=flat-square)](https://12.onebot.dev/)

## 关于

由于机器人还没写好人设，这段咕咕咕。

## 声明

本项目仅供学习交流使用，不支持任何盈利或非法行为。

## 功能
要访问 Darlene 的功能和命令，请使用命令：/help

## 特色

好像没有（划掉）

## 部署

```bash
git clone git@github.com:yinghanwen/Darlene.git
cd Darlene
pip3 install -r requirements.txt
nb run
```

或者，您可以使用 python 启动机器人，但不推荐：
```bash
python bot.py
```

## 协议

本项目采用 ```MIT``` 协议

```
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```



## 开发环境
Gentoo Linux + vscode remote ssh + conda + python 3.10.9

## 感谢

[botuniverse / onebot](https://github.com/botuniverse/onebot) : 统一的聊天机器人应用接口标准 

[Mrs4s / go-cqhttp](https://github.com/Mrs4s/go-cqhttp) ：cqhttp 的 golang 实现，轻量、原生跨平台

[nonebot / nonebot2](https://github.com/nonebot/nonebot2) ：跨平台 Python 异步机器人框架

[mnixry / nonebot-plugin-gocqhttp](https://github.com/mnixry/nonebot-plugin-gocqhttp) : 一款在NoneBot2中直接运行go-cqhttp的插件, 无需额外下载安装