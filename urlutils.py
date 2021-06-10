import requests
import difflib

class UrlUtils:
    def __init__(self):
        self.urldict = {}
        urlfile = open("urls_to_test.txt")
        urls = urlfile.readlines()
        for url in urls:
            spliturl = url.split(",")
            addr = spliturl[0].strip()
            method = spliturl[1].strip()
            self.urldict[addr] = method

    def generate(self):
        for url in self.urldict:
            if self.urldict[url] == 'GET':
                self.create_expected_get(url)
            else:
                print("Only GET requests are currently supported")

    def create_expected_get(self, addr):
        resp = requests.get(addr)
        if resp.status_code == 200:
            fname = self.sanitize_fname(addr)
            with open("expected_responses/" + fname, "wb") as f:
                f.write(resp.content)
                f.close()
        else:
            print("GET request failed for " + addr)

    def verify_get(self, addr):
        resp = requests.get(addr)
        if resp.status_code == 200:
            fname = self.sanitize_fname(addr)
            expected = open("expected_responses/" + fname, "rb").read()
            if resp.content == expected:
                print(str(addr) + " - GET - OK")
            else:
                print(str(addr) + " POTENTIAL GET FAILURE ... DIFF")
                self.expected_actual_diff(expected, resp.content)
        else:
            print(str(addr) + " FAILURE HTTP GET ... HTTP ERROR CODE " + str(resp.status_code))

    def expected_actual_diff(self, expected, actual):
        try:
            expected = str(expected)
            actual = str(actual)
            d = difflib.unified_diff(expected, actual)
            printdiff = "".join(d)
            print("Diff of expected vs actual")
            print(printdiff)
        except:
            print("Diff failed") 

    def sanitize_fname(self, addr):
        fname = addr.replace("/", "")
        fname = fname.replace(":", "") + ".txt"
        return fname

    def verify(self):
        for url in self.urldict:
            if self.urldict[url] == 'GET':
                self.verify_get(url)
            else:
                print("Only GET requests are currently supported")
