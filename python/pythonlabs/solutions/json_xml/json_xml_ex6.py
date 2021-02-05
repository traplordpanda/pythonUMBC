#!/usr/bin/env python3
'''
json_xml_ex6.py

The following API endpoint will return valid XML of a random user:
  https://randomuser.me/api/?format=xml
Create a program that gets a random user from the API and
  saves it to an XML file.
Reading the XML file, print the first name, last name, and
  email address of the user.
  The tag names are first, last, and email.
'''

import requests
from xml.dom import minidom

url = "https://randomuser.me/api/?format=xml"
response = requests.get(url)
if response.status_code == 200:
    with open("random_user.xml", "w") as output:
        print(response.content.decode(), file=output)
    doc = minidom.parse("random_user.xml")
    print(doc.getElementsByTagName("first")[0].childNodes[0].data, end=" ")
    print(doc.getElementsByTagName("last")[0].childNodes[0].data, end=" ")
    print(doc.getElementsByTagName("email")[0].childNodes[0].data, end=" ")
    print()
else:
    print("response status:", response.status_code)
