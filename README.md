# verifypy
This project will verify all urls in a given text file. It is designed to be used with Windows Task Scheduler or cron to check the status of web instances on a regular basis

# Track URLs
Input the url or IP address in the text file, urls_to_test.txt, followed by a comma and then an HTTP method. Currently only GET is supported. See example below. Note that direct IP addresses may need to be prefixed by http://
```
http://davesprojects.net/index.html, GET
http://davesprojects.net/about.html, GET
http://davesprojects.net/acft.html, GET
http://davesprojects.net/contact.html, GET
http://11.111.11.11/ipexample, GET
```

# Generate Expected Response
Ensure you have the requests package installed for Python
```
$ python -m pip install requests
```
Now run the gen_expected.py script which will write the expected responses to the folder expected_responses
```
$ python gen_expected.py
```

# Verify
Run the verifypy.py script and observe the results. If the request was succesful but different from what was expected, a diff will be printed out
```
$ python verifypy.py
```