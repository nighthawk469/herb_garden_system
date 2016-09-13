import os
import time
import sys

'''
uploads a file to sheridan server every 10 seconds
'''

def uploadFile(file):    
    os.system("rsync -zvh {} crawfoni@dev.fast.sheridanc.on.ca:/home/crawfoni/public_html"
        .format(file))
    #print("Upload successful\n")


def main():
    try:
        while True:
            time.sleep(10)
            uploadFile('data/soilMoisture.csv')
    except(KeyboardInterrupt):
        sys.exit()


if __name__ == "__main__":
    main()