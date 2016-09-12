# coding:utf-8
from ftplib import FTP

__author__ = 'uv2sun'

ftp = FTP('192.168.1.204')
s = ftp.login(user="app", passwd='app19850128')
print s
print ftp.getwelcome()
print ftp.nlst()
print ftp.dir()
ftp.cwd('install-files')
print ftp.dir()
# ftp.mkd("abc")
ftp.cwd('/app')
print ftp.pwd()
ftp.cwd('..')
print ftp.pwd()
r = ftp.retrlines("list")
print r
ftp.quit()
