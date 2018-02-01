# -*- coding: utf-8 -*-
from eve import Eve
from flask import request, Response
import json
from computer import Computer
from restUtils import deleteDbSpecificData, Message
import platform
import psutil

app = Eve()
#mongoDb object
mongo = app.data.driver


#This end point directly returns the server/backend computer details without touching DB
@app.route('/getcomputerInfor', methods = ['GET'])
def getcomputerInfor():
    
    computerDetails = Computer("Kadupitiya",
                               platform.processor(),
                               psutil.virtual_memory(), 
                               psutil.disk_usage('/'), 
                               platform.version(),  
                               platform.system(),  
                               platform.node(), 
                               platform.machine(), 
                               psutil.cpu_percent())
    
    josnData = json.dumps(computerDetails.__dict__)
    
    response = Response()
    response.headers["status"] = 200
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    response.data= josnData
    
    return response


# 1 : This end point collect server/backend computer details + username sent by user and push that data to the Mongo DB through eve app inbuilt method
# 2 : Then it find that same data/document from mongoDB and send that result back to user
@app.route('/complexComputer', methods = ['POST'])
def getcomputerInforAndAdd():
    
    #Response object
    response = Response()
    response.headers["status"] = 200
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    
    try:
    
        #get user data from user end using request object
        userData = request.get_json(silent=True)
            
        computerDetails = Computer(userData['name'],
                                       platform.processor(),
                                       psutil.virtual_memory(), 
                                       psutil.disk_usage('/'), 
                                       platform.version(),  
                                       platform.system(),  
                                       platform.node(), 
                                       platform.machine(), 
                                       psutil.cpu_percent())
        
    
        #create a unique key to make sure that no duplicates to DB : My primary/ unique key is 'name'
        mongo.db.computer.create_index([('name', 1)], unique=True)   
        #pass the data to the Mongo DB , if the same datafound just replace, if not insert
        mongo.db.computer.insert_one(computerDetails.__dict__)
        
        #Pymomgo DB request with the name given by user input     
        dictObj = mongo.db.computer.find_one_or_404({'name': userData['name'] })
        
        #Deleting DB parameters which should not be visible for user : Ex :-Object ID
        dictObj= deleteDbSpecificData(dictObj)
        
        #create a custom message for user-end
        message = Message(True, "Success", dictObj);
        
        #convert data to the json format
        josnData = json.dumps(message.__dict__)
        response.data= josnData

    except Exception as e:
        #create a custom message for user-end
        message = Message(False, "Error occured");
        message.error =  str(e)
        #convert data to the json format
        josnData = json.dumps(message.__dict__)
        response.data= josnData
        
    return response 

if __name__ == '__main__':
    app.run()
    
