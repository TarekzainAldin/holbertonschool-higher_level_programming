#!/usr/bin/python3
"""contains the Serializing and Deserializing with XML"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into an XML file.

    :param dictionary: The dictionary to serialize.
    :param filename: The name of the file to save the XML data.
    """
    root = ET.Element("data")

    def build_tree(d, parent):
        for key, value in d.items():
            if isinstance(value, dict):
                child = ET.SubElement(parent, key)
                build_tree(value, child)
            else:
                child = ET.SubElement(parent, key)
                child.text = str(value)

    build_tree(dictionary, root)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a Python dictionary.

    :param filename: The name of the XML file to read.
    :return: The deserialized dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    def parse_tree(element):
        d = {}
        for child in element:
            if len(child):
                d[child.tag] = parse_tree(child)
            else:
                d[child.tag] = child.text
        return d

    return parse_tree(root)
