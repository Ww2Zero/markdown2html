# -*- coding: utf-8 -*-

HTML_HEAD = """
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<style type="text/css">
{}
</style>
"""

import os
import markdown
import click


def getCss():
    """
    从文件中获取css样式
    :return : css文本
    """
    with open("github.css") as gcss:
        hcss = gcss.read()
        head = HTML_HEAD.format(hcss)
    return head


def mk2html(mkpath):
    """
    :mkpath :markdown文件路径
    :return :markdown转换的html标签
    """
    with open(mkpath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        html = markdown.markdown(text)
    return html


def save2html(cssstyle, htmlstyle, htmlpath):
    """
    合并css和html并保存为html 
    :cssstyle :css的样式
    :htmlstyle : html的文本
    :htmlpath : 保存html的路径
    """
    with open(htmlpath, "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
        output_file.write(cssstyle + htmlstyle)


@click.command()
@click.option('--mkpath', prompt='输入markdown名称', help='')
@click.option('--htmlpath', prompt='输入保存html名称', help='')
def main(mkpath, htmlpath):
    cssstyle = getCss()
    htmlstyle = mk2html(mkpath)
    save2html(cssstyle, htmlstyle, htmlpath)


if __name__ == "__main__":
    main()
