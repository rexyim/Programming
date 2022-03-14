import sys
sys.path.append('/home/aparashar/Workspace/meraki')
sys.path.append('/home/aparashar/Workspace')
# the above code added initialization module and myfunction module ( which has binary search function) to python3 path to look for modules
import initialization, meraki, myfunctions, re
dashboard = meraki.DashboardAPI(initialization.API_KEY)
clients=[]
arr=[]
hpmac='04:0e:3c'
with open('z3-netwroks.secret','r') as list:
    lines = list.readlines()
    for line in lines:
        arr.append(line.strip())
    arr.sort()
# the above with code block is reading all the z3 meraki serial number and storing them in a sorted array
with open('sn-no-network.secret','r') as input:
    lines = input.readlines()
    for line in lines:
        index=myfunctions.binary_search(arr,0,len(arr)-1,line.strip())
        if index != -1:
              del arr[index]
# the above with code block is searching the z3 meraki serial no. sorted array with serial no. of merakis with no network. This will avoid passing meraki serial no.
# with no network associated with it to the .getdevice api call 
try:
    for sn in arr:
           serial=sn   # storing serial for O/P in case of error
           response=dashboard.devices.getDevice(sn)
           clients.append({'serial': response['serial'], 'mac': response['mac']})
except:
       print("Oops!", sys.exc_info()[0], "occurred.")
       print(serial)
with open('output.secret','w') as output:
    for i in clients:
  #      if re.match(hpmac,i['mac'], re.IGNORECASE):
                output.write(i+'\n')
# the above with code writes the serial no. and mac of meraki that matches the search criteria to the output file.