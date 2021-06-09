import requests

url = 'http://davesprojects.net'
resp = requests.get(url)

if __name__ == '__main__':
    allurls = open("urls_to_test.txt")
    lines = allurls.readlines()
    for url in lines:
        spliturl = url.split(",")
        # this needs to be in a class - DRY
