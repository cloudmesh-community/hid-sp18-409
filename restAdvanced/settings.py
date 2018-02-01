
MONGO_HOST = 'localhost'
MONGO_PORT = 27017

# Skip these if your db has no auth. But it really should.
#MONGO_USERNAME = ''
#MONGO_PASSWORD = ''
#Account for DB_apitest_
MONGO_USERNAME = 'testuser'
MONGO_PASSWORD = 'testuser@123'

MONGO_DBNAME = 'computer_information'

# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

com_infor_schema = {

    'name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 10,
        'required': True,
        'unique': True,
    },    
    'processorName': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 50,
        'required': True,
    },
    'ram': {
        'type': 'list',
        'required': True,
        
    },
    'disk': {
        'type': 'list',
        'required': True,
    },
    'version': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 50,
        'required': True,
    },
    'system': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 50,
        'required': True,
    },
    'node': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 50,
        'required': True,
    },
    'machine': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 50,
        'required': True,
    },
    'cpu_percent': {
        'type': 'float',
        'minlength': 1,
        'maxlength': 50,
        'required': True,
    },
}
    
computer = {

    'item_title': 'computer',
    
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'name'
    },

    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    'resource_methods': ['GET', 'POST'],
    
    'schema': com_infor_schema
}  
    
DOMAIN = {
    'computer': computer,
}