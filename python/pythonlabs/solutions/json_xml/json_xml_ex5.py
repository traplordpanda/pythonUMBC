#!/usr/bin/env python3
'''
json_xml_ex5/py

Create a program that reads plants.xml.
Diplay the plant common name, botanical name, and light
  for all plants that cost less than $4.
'''

import xml.etree.ElementTree as ET


def main():
    root = ET.parse("plants.xml").getroot()

    print("Common Name, Botanical Name, Light")
    for plant in root.iter("plant"):
        common = plant.find("common").text
        botanical = plant.find("botanical").text
        light = plant.find("light").text
        price = float(plant.find("price").text)

        if price < 4:
            print(f"{common}, {botanical}, {light}")


if __name__ == "__main__":
    main()
