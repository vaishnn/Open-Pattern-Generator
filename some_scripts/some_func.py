import bpy  # noqa: F401


def get_nodes(obj, type_node):
    """
    Recursively finds all Geometry Nodes modifiers on an object that contain Bake nodes.
    """
    md_ls = []
    nodes_ls = []

    def check_node_group(node_group):
        if node_group:
            for node in node_group.nodes:
                if node.type == type_node:
                    nodes_ls.append(node)
                    return True
                elif node.type == "GROUP" and node.node_tree:
                    if check_node_group(node.node_tree):
                        return True
        return False

    if obj and obj.modifiers:
        for md in obj.modifiers:
            if md.type == "NODES" and md.node_group:
                if check_node_group(md.node_group):
                    md_ls.append(md)

    print(nodes_ls)
    return md_ls, nodes_ls[0]


def node_group_name_exists(name, node_type):
    node_groups = bpy.data.node_groups
    geometry_nodes = []
    for node_group in node_groups:
        if node_group.type == node_type:
            geometry_nodes.append(node_group.name)

    # print(geometry_nodes)
    return name in geometry_nodes


class names_nodes:
    def __init__(self):
        self.main_geo_name = ""

    def set_main_geo_name(self, name):
        self.main_geo_name = name
