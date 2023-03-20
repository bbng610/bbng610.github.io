import django
#import requests
#import os
#import sys
import datetime

def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


print(django.__version__)

name ='Billy';

print("Hello ", name);

print (get_current_time())
