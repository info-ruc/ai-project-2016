import re, os
refer = re.compile(r'\[\d*\]')
other = re.compile(r'[(),<>-_"]')
num = re.compile(r'\d+(.\d+)?')
txtpath = r'./TXT/True/'
outpath = r'./data/True/'
 
files = os.walk(txtpath).next()[-1]
for file in files:
    print file
    with open(txtpath+file,'r') as f:
        content = f.read().lower()
 
        temp_index = content.find('abstract') 
        if temp_index != -1: content = content[temp_index+8:]
     
        temp_index = content.rfind('references')    
        if temp_index != -1: content = content[:temp_index]
        f.close()
        with open(outpath+file, 'w') as wf:   
            wf.write(num.sub('1',other.sub(' ',refer.sub('',content))))