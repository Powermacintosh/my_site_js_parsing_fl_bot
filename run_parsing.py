import os
from datetime import datetime
from time import sleep


# time_out = 1000

# while True:
# 	sleep(time_out)

start = datetime.now()

print("--------------------------------------------------")
# print ('Run multi_parsing_FL')
# os.system('python3 ./manage.py multi_parsing_FL')

# print ('Run multi_parsing_freelance')
# os.system('python3 ./manage.py multi_parsing_freelance')

# print ('Run multi_parsing_freelansim')
# os.system('python3 ./manage.py multi_parsing_freelansim')

# print ('Run multi_parsing_WebLancer')
# os.system('python3 ./manage.py multi_parsing_WebLancer')



end = datetime.now()
f = end - start
print("**************************************************")
print("  All Parsing:", f)
print("**************************************************")