# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/3 16:46
# @Author  : Yanjun Hao
# @Site    : 
# @File    : brigde_qrcode_MyQR.py
# @Software: PyCharm 
# @Comment :
# NOTE:
#   Linking: https://zhuanlan.zhihu.com/p/124225423

from MyQR import myqr


def get_qrcode(msg: str, src_path: str, save_path: str) -> None:
    myqr.run(
        words=msg,  # 包含信息
        picture=src_path,  # 背景图片
        colorized=True,  # 是否有颜色，如果为False则为黑白
        save_name=save_path  # 输出文件名
    )


if __name__ == '__main__':
    get_qrcode(msg='https://www.sxhis.cn/#/',
               src_path='../data/src.jpg',
               save_path='../data/output.png')
