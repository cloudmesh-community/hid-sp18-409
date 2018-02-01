def deleteDbSpecificData(dictObj):
    for key, value in list(dictObj.items()):
        if key.startswith('_'):
            del dictObj[key]
    return dictObj;


class Message(object):
    
    def __init__(self, status=None, message=None, data=None, error=None):
        self.status=status
        self.message=message
        self.data=data
        self.error=error