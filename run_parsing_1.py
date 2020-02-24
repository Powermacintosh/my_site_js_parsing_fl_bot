import os
from datetime import datetime


# start = datetime.now()


# print ('Run multi_parsing_FL')
# os.system('python3 ./manage.py multi_parsing_FL')

# print ('Run multi_parsing_freelance')
# os.system('python3 ./manage.py multi_parsing_freelance')

# print ('Run multi_parsing_freelansim')
# os.system('python3 ./manage.py multi_parsing_freelansim')

# print ('Run multi_parsing_WebLancer')
# os.system('python3 ./manage.py multi_parsing_WebLancer')
while True:
	print ('Run multi_parsing_YouDo')
	os.system('python3 ./manage.py multi_parsing_YouDo_full')


# end = datetime.now()
# f = end - start
# print("**************************************************")
# print("  All Parsing:", f)
# print("**************************************************")