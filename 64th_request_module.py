# import requests
#
# r = requests.get("https://financialmodelingprep.com/api/v3/historical-chart/1min/AAPL")
# print(r)
#
# #!/usr/bin/env python
#
# # try:
# #     # For Python 3.0 and later
# #     from urllib.request import urlopen
# # except ImportError:
# #     # Fall back to Python 2's urllib2
# #     from urllib2 import urlopen
# #
# # import json
# #
# # def get_jsonparsed_data(url):
# #     """
# #     Receive the content of ``url``, parse it as JSON and return the object.
# #
# #     Parameters
# #     ----------
# #     url : str
# #
# #     Returns
# #     -------
# #     dict
# #     """
# #     response = urlopen(url)
# #     data = response.read().decode("utf-8")
# #     return json.loads(data)
#
# url = ("https://financialmodelingprep.com/api/v3/company/profile/AAPL")
# print(get_jsonparsed_data(url))
import requests
import json

url = ('http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=fe216fa7a6834d7d923181b929ba2920')
response = requests.get(url).text
parse = json.loads(response)

print(parse["status"])
