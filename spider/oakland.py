import requests
import bs4
from config.header import default_firefox_headers
from lib.utils import writeToCSV



# requests.get(burp0_url, headers=burp0_headers)
class SpiderOakland(object):
    def __init__(self, url):
        self.url = url
        self.header = default_firefox_headers

    def getPath(self, url):
        _url = url.split("/")
        _url[0] = _url[0] + "//"
        url = "".join(_url[:-1])
        return url

    def download(self, url, name):
        # file_url = "http://codex.cs.yale.edu/avi/db-book/db4/slide-dir/ch1-2.pdf"
        print(url)
        res = requests.get(url, stream=True)
        with open("data/" + name, "wb") as pdf:
            for chunk in res.iter_content(chunk_size=1024):
                if chunk:
                    pdf.write(chunk)

    def downloadFromPage(self, url):
        name = url
        url = self.getPath(self.url) + "/" + url
        print(url)
        self.download(url, name)

    def downloadFromCom(self, url):
        pass


    def parse(self, content):
        bs_content = bs4.BeautifulSoup(content)
        elements = bs_content.select("a")
        for ele in elements:
            # print(ele["href"])
            url = ele["href"]
            if(url.find("www.computer.org") != -1):
                self.downloadFromCom(url)
            elif((url.find("pdf") != -1) and (url.find("http") !=  0)):
                self.downloadFromPage(url)
            else:
                pass


    def run(self):
        response = requests.get(self.url, headers=self.header)
        if response.status_code == 200:
            self.parse(response.content)
        else:
            print(response.status_code)
