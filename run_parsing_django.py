import os
from datetime import datetime
from time import sleep


# time_out = 1000

# while True:
# 	sleep(time_out)
start = datetime.now()

print("--------------------------------------------------")
print ('Run multi_parsing_FL')
os.system('python3 ./manage.py multi_parsing_FL_django')

print ('Run multi_parsing_freelance')
os.system('python3 ./manage.py multi_parsing_freelance_django')

print ('Run multi_parsing_freelansim')
os.system('python3 ./manage.py multi_parsing_freelansim_django')

print ('Run multi_parsing_WebLancer')
os.system('python3 ./manage.py multi_parsing_WebLancer_django')



end = datetime.now()
f = end - start
print("**************************************************")
print("  All Parsing:", f)
print("**************************************************")