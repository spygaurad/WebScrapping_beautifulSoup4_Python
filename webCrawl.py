'''Author: Suraj Prasai
    Description: Web Scrapping using Python and BeautifulSoup4 module'''





# import requests       use for requests.get(url)
from bs4 import BeautifulSoup
from urllib import request
import os

def web_crawler(max_pages):
    page = 1
    while(page<= max_pages):
        batch = 'Batch'+str(2014+page)
        try:
            os.makedirs(batch)
        except FileExistsError:
            print("I already Exist")





        url = 'http://doko.dwit.edu.np/class/show/' + str(page)
        #all_text = requests.get(url)
        #useful_text = all_text.text        #no need for .text incase of urlopen

        useful_text = request.urlopen(url)
        soup = BeautifulSoup(useful_text,'html.parser')


        for link in soup.findAll('a', {'data-toggle': 'modal'}):

            link.find_all('p',{'class': 'studentNameTop text-center text-capitalize'})
            name = link.text


            for img in link.findAll('img', src=True):
                image = img['src']
                get_image_of_individuals(batch,name,image)
            #x.findAll('img',{'class':'media-object dp'})

            #

            #
            # image = link.get('src')
            # print(space_removed_name)
            # print(image)
            #get_image_of_individuals(space_removed_name)
            #to get links, .findAll('a',{}):
            #href = link.get('href')

        page += 1


def get_image_of_individuals(batch,name,image):

    #for img in link.findAll('img',{'class':'media-object dp'}):
    src = 'http://doko.dwit.edu.np'+image

    splitted_name = name.split();
    space_removed_name = ''.join(splitted_name)
    full_name = batch+'/'+space_removed_name + '.jpg'

    request.urlretrieve(src,full_name)

web_crawler(7)
