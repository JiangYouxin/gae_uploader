#!/usr/bin/env python
# coding:utf-8

import sys
import os

BANNER = '''\
===============================================================
 Google App Engine 服务端部署程序, 开始上传 python 服务端
===============================================================

请输入您的appid, 多个appid请用|号隔开
'''

FOOTER = '''\
上传成功。
'''

def main():
    import appcfg
    dirname = os.path.dirname(os.path.abspath(__file__))
    if dirname.endswith('.zip'):
    	dirname = os.path.dirname(dirname)
    os.chdir(dirname)
    appcfg.main()

if __name__ == '__main__':
   try:
        print BANNER.decode('utf-8').encode(sys.getfilesystemencoding(), 'replace')
        main()
        print
        print FOOTER.decode('utf-8').encode(sys.getfilesystemencoding(), 'replace')
        raw_input()
   except KeyboardInterrupt:
        pass
