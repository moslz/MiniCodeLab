import xml.etree.ElementTree as ET

class Node:
    def __init__(self, name, node_type, parent=None, children=None):
        self.name = name
        self.node_type = node_type
        self.parent = parent
        self.children = children if children else []

    def add_child(self, child):
        self.children.append(child)

def read_behavior_tree_from_file(file_path):
    tree = ET.parse(file_path)
    return tree.getroot()

def build_node_tree(element, parent=None):
    node_type = element.tag
    node_name = element.get("name", None)
    node = Node(node_name, node_type, parent)
    for child in element:
        child_node = build_node_tree(child, node)
        node.children.append(child_node)
    return node