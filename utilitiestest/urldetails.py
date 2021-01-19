from APIAutomation.utilitiestest.configuration import *
from APIAutomation.utilitiestest.Resources import *

def NeededUrl():
    url = Configurationtest()['API']['end_point']
    return url
