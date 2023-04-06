# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/3 16:17
# @Author  : Yanjun Hao
# @Site    : 
# @File    : bridge_qrcode.py
# @Software: PyCharm 
# @Comment :
# NOTE:
#   Linking: https://blog.csdn.net/cnds123/article/details/123158166
#            https://zhuanlan.zhihu.com/p/124225423
#            https://www.jianshu.com/p/c0073c6aa544

# 带有logo图案的二维码
from PIL import Image
import qrcode


def get_qrcode(msg: str, logo_path: str, save_path: str) -> None:
    # QRCode()这里我们创建了一个对象：
    qr = qrcode.QRCode(version=5, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=8, border=4)
    # version：值为1~40的整数，控制二维码的大小（最小值是1，是个21×21的矩阵）
    # error_correction：控制二维码的错误纠正功能。可取值下列4个常量：
    '''
    qrcode.constants.ERROR_CORRECT_X：
        1. X=L时，大约7%或更少的错误能被纠正。 
        2. X=M（默认）时，大约15%或更少的错误能被纠正。
        3. X=Q时，25%以下的错误会被纠正。
        4. X=H时，大约30%或更少的错误能被纠正。
    '''
    # box_size：控制二维码中每个小格子包含的像素数。
    # border：控制边框（二维码与图片边界的距离）包含的格子数（默认为4)

    # 向二维码中添加信息
    qr.add_data(msg)

    qr.make(fit=True)

    img = qr.make_image(fill_color="green", back_color="white")
    # 二维码设置为彩色
    img = img.convert('RGBA')
    # 打开logo图片
    logo = Image.open(logo_path)
    # 二维码尺寸
    img_w, img_h = img.size
    # 默认LOGO最大设为图片的1/4
    factor = 6
    # 最大logo尺寸
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)
    # logo的尺寸
    logo_w, logo_h = logo.size

    if logo_w > size_w or logo_h > size_h:
        logo_w = size_w
        logo_h = size_h
    logo = logo.resize((logo_w, logo_h), Image.ANTIALIAS).convert('RGBA')
    l_w = int((img_w - logo_w) / 2)
    l_h = int((img_h - logo_h) / 2)
    # 替换指定位置
    img.paste(logo, (l_w, l_h), logo)
    img.show()
    img.save(save_path)


if __name__ == '__main__':
    get_qrcode(msg="https://www.sxhis.cn/#/",
               logo_path="../data/src.jpg",
               save_path="../data/figure.png")
