import urllib.request, requests
from bs4 import BeautifulSoup

'''
opener = urllib.request.build_opener()
responce = opener.open("https://httpbin.org/get")

print(responce.read())

#----------------------------

responce = requests.get("https://httpbin.org/get")
print(responce.content)

responce = requests.post("https://httpbin.org/post",
                         data="Test data",
                         headers={"h1": "Test title"})
print(responce.text)
'''


#response_parse = response.text.split("<span>")
#print(response_parse)

# for elem in response_parse:
#     if elem.startswith("$"):
#         for elem2 in elem.split("</span>"):
#             if elem2.startswith("$") and elem2[1].isdigit():
#                 print(elem2)

response = requests.get("https://coinmarketcap.com/")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("span", {"class": "base-text"})
    #res = soup_list[0].find("span")
    print(soup_list)
