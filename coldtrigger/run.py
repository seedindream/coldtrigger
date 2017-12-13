import os
import json
import time
import urllib
import subprocess

postreqdata = json.loads(open(os.environ['req']).read())
url = postreqdata['url']
time_rq = time.time()
content=urllib.urlopen(url).read()  
time_feed = time.time()
print(content)
print("request time "+str(time_rq))
cmdCommand = 'powershell D:\\home\\site\\wwwroot\\coldtrigger\\record.exe' #specify your cmd command
process = subprocess.Popen(cmdCommand.split(), shell=True,stdout=subprocess.PIPE)
output5, error = process.communicate()



response = open(os.environ['res'], 'w')
response.write("request time "+str(time_rq)+"feedback time "+str(time_feed)+"@@"+content+"%%"+output5)
response.close()