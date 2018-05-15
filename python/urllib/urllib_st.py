#!/usr/bin/env python3


from urllib.parse import urlparse, unquote

print(urlparse("file:///home/wangj/Documents/python-3.6.5-docs-html/library/urllib.parse.html"))
print(urlparse("https://bitbucket.srv.westpac.com.au/projects/ADTB/repos/databank-ng/pull-requests"))


url3 = "https://www.expedia.com.au/Flights-Search?flight-type=on&starDate=25%2F05%2F2018&endDate=28%2F06%2F2018&_xpid=11905%7C1&mode=search&trip=roundtrip&leg1=from%3Asydney%2Cto%3AShenzhen%2C+China+%28SZX-Shenzhen+Intl.%29%2Cdeparture%3A25%2F05%2F2018TANYT&leg2=from%3AShenzhen%2C+China+%28SZX-Shenzhen+Intl.%29%2Cto%3Asydney%2Cdeparture%3A28%2F06%2F2018TANYT&passengers=children%3A2%5B8%3B15%5D%2Cadults%3A1%2Cseniors%3A0%2Cinfantinlap%3AY"

o3 = urlparse(url3)

print(o3)

print("query = {!r}".format(unquote(o3.query)))


print(urlparse("https://mail.google.com/mail/u/0/#inbox/1635f8fe4df5257c"))
