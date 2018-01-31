# -*- coding: utf-8 -*-
from eve import Eve
from computer import Computer
import platform
import psutil
import json
from flask import Response
 
app = Eve()

@app.route('/processor', methods = ['GET'])
def processor():
    
    computerDetails = Computer(platform.processor(),
                               psutil.virtual_memory(), 
                               psutil.disk_usage('/'), 
                               platform.version(),  
                               platform.system(),  
                               platform.node(), 
                               platform.machine(), 
                               psutil.cpu_percent())
    
    sdata = json.dumps(computerDetails.__dict__)
    
    res = Response(response=sdata, status=200, mimetype="application/json")
    res.headers["Content-Type"] = "application/json; charset=utf-8"
    
    return res

@app.route('/hello')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
    
