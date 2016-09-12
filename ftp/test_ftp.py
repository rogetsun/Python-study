# coding:utf-8
from ftplib import FTP

__author__ = 'uv2sun'

ftp = FTP('192.168.1.204')
s = ftp.login(user="app", passwd='app19850128')
print s
print ftp.getwelcome()
# r = ftp.retrlines("list")
ftp.quit()
