#!/usr/bin/env python3

import yaml
import urllib.request as serverRC

conf="config/config.yml"

try:
    configF = yaml.load(open(conf)) 
    if configF['switch']=='small':
        DataFilePath=str(configF['data']['basepath']+"/"+configF['data']['basefile'])
        URL=configF['data']['downlink'] 
    else:
        DataFilePath=str(configF['data']['basepath']+"/"+configF['data']['basefileFull'])
        URL=configF['data']['downlinkFull']
except FileNotFoundError:
    import sys
    import logging
    logging.error('Please create config.yml with uplink and basefile')
    sys.exit(1)    


# download the data
def downloadData():
    try:
        serverRC.urlretrieve(getdownloadLink(), getDataFilePath())    
        return True
    except Exception as e:
        return False


#getter for dataFile path
def getDataFilePath():
    return DataFilePath

#getter for downloadLink
def getdownloadLink():
    return URL

#getter for basepath
def getBasePath():
    return configF['data']['basepath']

 
    


