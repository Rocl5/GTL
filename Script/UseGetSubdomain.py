from Core.GetSubdomain import ce_baidu, hackertarget, crtsh, qianxun, aizhan, IP138

class Getdomain:


    def __init__(self, targets_filename):
        self.targets_filename = targets_filename  # 放置域名的txt
        self.subdomain_filename = 'subdomain.txt'  ## 子域名result 
        # self.filename = input('请输入文件名: ')


    def Get_domain(self):
        # --定义header头
        print('\033[033m[INFO]\033[0m GetDomain Module Running!')
        open_subdomainfile = open(self.subdomain_filename, 'w')
        arr_subdomain = []
        with open(file=self.targets_filename, mode='r') as domain:
            for url in domain.readlines():
                print('\033[33m[INFO]\033[0m Retrieving: %s' % url, end="")
                for i in ce_baidu(url.strip('\n')):
                    arr_subdomain.append(i + '\n')
                for i in hackertarget(url.strip('\n')):
                    arr_subdomain.append(i + '\n')
                for i in IP138(url.strip('\n')):
                    arr_subdomain.append(i + '\n')
                for i in crtsh(url.strip('\n')):
                    arr_subdomain.append(i + '\n')
                for i in qianxun(url.strip('\n')):
                    arr_subdomain.append(i + '\n')
                for i in aizhan(url.strip('\n')):
                    arr_subdomain.append(i + '\n')
                    # --- 域名去重
            for i in range(len(arr_subdomain), 0, -1):
                for j in range(1, len(arr_subdomain)):  # 这个为0就把自己给删了，所以需要注意
                    try:
                        if arr_subdomain[i] == arr_subdomain[i-j]:
                            del arr_subdomain[i]
                    except:
                        pass
            for i in arr_subdomain:
                open_subdomainfile.write(i)
        open_subdomainfile.close()
        print('\033[032m[INFO]\033[0m GetDomain Module Has Finished Running!')

		