import urlutils as ut

def veryify_and_wait():
    print("Verifying ...")
    utils.verify()
    rkey = input("Press r to regenerate expected_responses or any other key to quit ")
    return rkey

if __name__ == '__main__':
    utils = ut.UrlUtils()
    rkey = veryify_and_wait()
    if rkey == 'r' or rkey == 'R':
        print("Regenerating ...")
        utils.generate()
        veryify_and_wait()
