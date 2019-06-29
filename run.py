from lib.utils import readJsonFile
from spider.oakland import SpiderOakland



def loadConfig():
    config_path = "config/config.json"
    config_data = readJsonFile(config_path)
    oakland_url_list = config_data["oakland_url_lists"]
    for url in oakland_url_list:
        spider = SpiderOakland(url)
        spider.run()


def main():
    loadConfig()

if __name__ == "__main__":
    main()