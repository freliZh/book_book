#encoding:utf8
#功能处理原始豆瓣图书数据
import os
def get_filelist():
    for files in os.listdir("."):
        print files

def process():
    get_filelist()



if __name__ == "__main__":
    process()


