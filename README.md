# GTL (Get Target Link)

## What can it do? 
>它可以获取指定文本中域名(例如: targets.txt)的子域名，并将可以访问的link放到result.txt，子域名放到subdomain.txt

## How to use?
>编辑一个targets.txt，写入需要探测的域名，使用参数-f指定文件

**Usage:**
```
python3 GTL.py -f targets.txt 
```


目前想法是与crawlergo+xray进行联动,后续有时间的话将会更新