from pathlib import Path
from typing import Optional, Union


def check_dir(path: Union[str, Path]) -> bool:
    '''
    检查目录是否存在，并递归创建目标目录，若目录已存在则不进行更改。
    :param path: 目标目录路径
    :rtype: 返回该目录是否本就存在
    '''
    path = Path(path)
    if path.is_dir():
        return True
    else:
        check_dir(path.parent)
        path.mkdir()
        return False



def check_file(path: Union[str, Path]):
    '''
    检查文件是否存在，并递归创建父目录和该文件，若文件已存在则不进行更改。
    :param path: 目标文件路径
    :rtype: 返回该文件是否本就存在
    '''
    path = Path(path)
    if path.is_file():
        return True
    else:
        check_dir(path.parent)
        with open(path, "w"):
            pass
        return False



def rm_path(path: Union[str, Path]):
    '''
    递归删除目录或删除文件。
    :param path: 目标路径
    '''
    path = Path(path)
    if path.is_file():
        path.unlink()
    elif path.is_dir():
        for i in path.iterdir():
            rm_path(i)
