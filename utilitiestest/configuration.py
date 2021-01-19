import configparser


def Configurationtest():
    config = configparser.ConfigParser()
    config.read("C:/Users/Shivani Desai/PycharmProjects/APITesting/APIAutomation/utilitiestest/properties.ini")
    return config