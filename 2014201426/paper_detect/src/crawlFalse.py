import requests
from bs4 import BeautifulSoup

savePath = '/home/victoria/Desktop/AI/paper_detect/PDF/False/'
url = 'http://pdos.csail.mit.edu/cgi-bin/sciredirect.cgi?author=&author=&author=&author=&author='
 
def download_file(url,local_filename):
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
    return local_filename
 
for i in xrange(200):
    try:
        r=requests.get(url)
        if r.status_code==200:
            soup=BeautifulSoup(r.text)   
            link = soup.find_all('a')[1]
            new_link='http://scigen.csail.mit.edu'+link.get('href')
            filename = r.url.split('/')[-1][:-4]+'pdf'
            file_path=download_file(new_link,savePath + filename)
            print str(i+1) + '  downloading: '+filename
        else:
            print 'errors: ' +str(i)
    except Exception,e:
        print e

