#coding:utf-8
from bs4 import BeautifulSoup
import os
for i in range(1,50):
    file_path = 'txt/'+str(i)+'.txt'
    if os.path.exists(file_path):
        print(str(i)+'.txt')
        soup = BeautifulSoup(open(file_path),'html.parser')


        for j in soup.find_all('p'):
            if j.find('script'):
                continue
            else:
                print(j.get_text())
                content_path = 'content/'+str(i)+'.txt'
                with open(content_path, 'a') as f:
                    f.write(j.get_text()+'\n')
    else:
        pass
