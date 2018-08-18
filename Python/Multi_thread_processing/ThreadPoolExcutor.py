# ThreadPoolExecutor best to use when io bound operation

from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen


def load_url(url, timeout):
    print('processing :', url)
    with urlopen(url, timeout=timeout) as conn:
        print('processing :', url)
        return conn.read()


with ThreadPoolExecutor(max_workers=2) as executor:
    url1 = 'http://codecops.in'
    url2 = 'http://beginer2cs.blogspot.com'
    f1 = executor.submit(load_url, url1, 60)
    f2 = executor.submit(load_url, url2, 60)
    # Submit return object immediately and does't block the main process
    # we don't need  to call executor.shutdown() method as with block automatically call it


try:
    data1 = f1.result() # result function will block main thread and with untill f1 thread completed
    print("{} page is {} bytes".format(url1,len(data1)))
    data2 = f2.result()
    print("{} page is {} bytes".format(url2,len(data2)))
except Exception as e:
    print(e)