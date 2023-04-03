from flask import Flask, request
from flask_restful import Api, Resource
import requests
import json
from bs4 import BeautifulSoup
import urllib.request
import cv2
import os.path
from os import path
from cartoonize import caart
import random
import base64



app = Flask(__name__)


def random_id(length):
    number = '0123456789'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    id = ''
    for i in range(0,length,2):
        id += random.choice(number)
        id += random.choice(alpha)
    return id


link = 'images/'
cartoon = 'image_cartoon/'
@app.route('/', methods = ["GET"])
@app.route('/cartoon', methods = ["GET"])
def add_img():
    name_image = random_id(7)
    link_full = request.headers.get('Link-Full')
    str = link_full[-5:]
    if str == '.jpeg':
        name = name_image + str
        all_link = link + name
        link_cartoon = cartoon + name
    
        urllib.request.urlretrieve(link_full,all_link)            
        output=caart(cv2.imread(all_link))
        cv2.imwrite(link_cartoon, output)  
        
        with open(link_cartoon, "rb") as img_file:
            my_string = base64.b64encode(img_file.read())
        my_string.decode('utf-8')
            
        
    else:
        string_ = link_full[-4:]
        if string_ == '.jpg' or string_ == '.png':
            name = name_image + string_
            all_link = link + name 
            link_cartoon = cartoon + name   
            urllib.request.urlretrieve(link_full,all_link)
                
            output=caart(cv2.imread(all_link))
            cv2.imwrite(link_cartoon, output)
            
            
            with open(link_cartoon, "rb") as img_file:
                my_string = base64.b64encode(img_file.read())
            my_string.decode('utf-8')  
        else:
            temp = 'No success'
        
        
    return my_string


 
if __name__ == '__main__':
    app.run()