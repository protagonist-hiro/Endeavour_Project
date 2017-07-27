from parsingrss import *

import RAKE
import operator
Rake=RAKE.Rake('SmartStoplist.txt')

hello=news(distinct_item)

print("1. To get keywords from titles\n")
print("2. To get keywords from descriptions\n")
sel=input()

if sel=='1':
    for item in distinct_item:
        print(hello.get_title(item))
        print(Rake.run(str(hello.get_title(item))))

elif sel=='2':
    for item in distinct_item:
        print(hello.get_description(item))
        print(Rake.run(str(hello.get_description(item))))
