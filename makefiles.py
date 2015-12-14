import datetime
import time
import sys


for x in range(0, 10):
    filename1 = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    sys.stdout = open(filename1 + '.jpg', 'w')
    time.sleep(1)