import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.response import Response
from swagger_server.models.data import Data
from swagger_server import util

import swagger_server.controllers.base_auth as auth
import swagger_server.controllers.util as utility

  
@auth.requires_auth
def data_fetch_get():  # noqa: E501
    """Fetch data to the server

    This data fetch endpoint upload the csv datafile to the server using predeifned url # noqa: E501


    :rtype: object
    """
    if utility.downloadData():
        return Response(True,"Data fetch successfull")
    else:
        return Response(False,"Data fetch failed")
    

@auth.requires_auth
def data_get():  # noqa: E501
    """returns the folder name and file name of the dataset

    The data endpoint returns a data object conataining information about dataset files. # noqa: E501


    :rtype: object
    """
    return Data(utility.getBasePath(),
                utility.getDataFilePath(),
                utility.getDataFilePath(),
                utility.getdownloadLink())
