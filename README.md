# GTL (Get Target Link)

## What can it do? 
>它可以获取指定文本中域名(例如: targets.txt)的子域名，并将可以访问的link放到result.txt，子域名放到subdomain.txt

## How is it achieved?
>首先需要一个文件，使用参数-f指定

**command:**
```
python3 GTL.py -f targets.txt 
```


目前想法是与crawlergo+xray进行联动,后续有时间的话将会更新