import pprint
import time

from browsermobproxy import Server
from selenium import webdriver


class ProxyManager:

    __BMP = r"C:\Users\Adejoro Damilare\Downloads\browsermob-proxy-2.1.4-bin\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat"
    # input raw link to browsermobproxy here

    def __init__(self):
        self.__server = Server(ProxyManager.__BMP)
        self.__client = None

    def start_server(self):
        self.__server.start()
        return self.__server

    def start_client(self):
        self.__client = self.__server.create_proxy(params={"trustAllServers": "true"})
        return self.__client

    @property
    def client(self):
        return self.__client

    @property
    def server(self):
        return self.__server


if "__main__" == __name__:

    proxy = ProxyManager()
    server = proxy.start_server()
    client = proxy.start_client()
    client.new_har("google.com") # input url link here
    print(client.proxy)

    options = webdriver.ChromeOptions()
    options.add_argument(f"--proxy-server={client.proxy}")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://www.google.com/") # input url link here
    time.sleep(3)

    pprint.pprint(client.har)

    server.stop()
