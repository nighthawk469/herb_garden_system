"""Uploads a file to sheridan server every 10 seconds.
"""

import os
import time
import sys



def uploadFile(file):
    """Use bash rsync to upload given file to remote server.
    """
    os.system("rsync -zvh {} crawfoni@dev.fast.sheridanc.on.ca:/home/crawfoni/public_html"
        .format(file))
    #print("Upload successful\n")


def main():
    """Upload file every ten seconds until keyboard interrupt
    """
    try:
        while True:
            time.sleep(10)
            uploadFile('data/soilMoisture.csv')
    except(KeyboardInterrupt):
        sys.exit()


if __name__ == "__main__":
    main()