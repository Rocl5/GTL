import requests 
import threading
import argparse
import time, os
from Script.UseGetSubdomain import Getdomain
from Script.CheckDomain import CheckDomain


"""
@auther: ro4lsc 
@version: v0.2
@descript: 配合Getsubdomain模块，达到收集域名的效果，并且将访问有效的链接放到result.txt里面
@time: 2020-08-09
"""


parser = argparse.ArgumentParser(description="GTL (Get Targets Link)")
parser.add_argument('-u', '--url', help='Taget URL', default='www.baidu.com')
parser.add_argument('-f', '--file', help='Place files for all domain names', default='targets.txt')
# parser.add_argument('-s', '--subdomain', help='放置所有域名的file', default='Y')
args = parser.parse_args()  # 实例化
targets_file = args.file
# YorN_GetSubdomain = args.subdomain


if os.path.exists('subdomain.txt'):
    if os.path.getsize('subdomain.txt') > 0:
        print('\033[031m[WARN]\033[0m Check \033[032msubdomain.txt\033[0m exists and it not \033[031mnull\033[0m!')
        YorN_GetSubdomain = input('\033[33m[INFO]\033[0m Have You need to subdomain detect? [\033[032mY\033[0m/\033[031mN\033[0m] ')

YorN_GetSubdomain = 'Y'


if YorN_GetSubdomain == 'Y':
    starttime = time.time()
    Getdomain = Getdomain(targets_file)
    Getdomain.Get_domain()
    CheckDomain = CheckDomain()
    CheckDomain.start()
    endtime = time.time()
else: 
    starttime = time.time()
    CheckDomain = CheckDomain()
    CheckDomain.start()
    endtime = time.time()
print('\033[32m[INFO]\033[0m All target links have been collected!')

print('\033[32m[INFO]\033[0m The program is running time: %.2fs' % (endtime-starttime))