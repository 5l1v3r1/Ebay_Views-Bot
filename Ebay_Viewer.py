import requests
import randomheaders
import time
import random
import threading
import pyinputplus as pyip


def viewer(url, views: int):
    if views > 200:
        return
    else:
        proxy = {"http": "INSERT YOUR ROTATING PROXY HERE",}

        for i in range(views):
            time.sleep(random.randint(4, 10)) # Just chooses random seconds program should wait between views 
            requests.get(url, proxies=proxy, headers=randomheaders.LoadHeader())
            print("{} view has been completed".format(i))


def threads_viewer(url, views: int):
    urls = []
    counter = pyip.inputInt("How many url's do you want to add: ")   # Library that enures correct input format. Could just use normal input function with an if clause to make sure input is an int.

    for i in range(counter):
        urls.append(input("Enter your {} url: ".format(i + 1)))

    threads = [threading.Thread(target=viewer, args=(url, views,)) for url in urls]
    for t in threads:
        t.start()
