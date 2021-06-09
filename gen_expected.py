import requests

def check_url(addr, method):
    if method != "GET" or method != "POST":
        print("Method must be GET or POST")
        return False
    return True

def create_expected(addr, method):
    if method == 'GET':
        resp = requests.get(addr)
        if resp.status_code == 200:
            fname = addr.replace("/", "") + ".txt"
            with open("expected_responses/" + fname, "wb") as f:
                f.write(resp.content)
                f.close()
        else:
            print("GET request failed for " + addr)
            return False
    return True

if __name__ == '__main__':
    urlfile = open("urls_to_test.txt")
    urls = urlfile.readlines()

    for url in urls:
        spliturl = url.split(",")
        addr = spliturl[0].strip()
        method = spliturl[1].strip()
        create_expected(addr, method)

