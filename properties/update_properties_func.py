import bpy
from ..class_properties import classproperties

properties = classproperties()
value_socket_dict = properties.get_variable_and_sockets()
modifier_name = properties.get_geometrynode_name()

def update_count_sizeandshape(self, context):
    value = self.count_sizeandshape
    context.object.modifiers[modifier_name][value_socket_dict["count_sizeandshape"]] = value
    bpy.context.view_layer.update() #Redraw viewport if necessary

def update_size_sizeandshape(self, context):
    value = self.size_sizeandshape
    context.object.modifiers[modifier_name][value_socket_dict["size_sizeandshape"]] = value
    bpy.context.view_layer.update() #Redraw viewport if necessary

def update_offset_sizeandshape(self, context):
    value = self.offset_sizeandshape
    context.object.modifiers[modifier_name][value_socket_dict["offset_sizeandshape"]] = value
    bpy.context.view_layer.update() #Redraw viewport if necessary

def update_seed_sizeandshape(self, context):
    value = self.seed_sizeandshape
    context.object.modifiers[modifier_name][value_socket_dict["seed_sizeandshape"]] = value
    bpy.context.view_layer.update() #Redraw viewport if necessary

def update_grain_sizeandshape(self, context):
    value = self.grain_sizeandshape
    context.object.modifiers[modifier_name][value_socket_dict["grain_sizeandshape"]] = value
    bpy.context.view_layer.update() #Redraw viewport if necessary

def update_resolution_of_tubes_curves(self, context):
    value = self.resolution_of_tubes_curves
    context.object.modifiers[modifier_name][value_socket_dict["resolution_of_tubes_curves"]] = value
    bpy.context.view_layer.update() #Redraw viewport if necessary


def update_resolution_of_curves_curves(self, context):
    value = self.resolution_of_curves_curves
    context.object.modifiers[modifier_name][value_socket_dict["resolution_of_curves_curves"]] = value
    bpy.context.view_layer.update() #Redraw viewport if necessary

def update_1st_curve_segments_curves(self, context):
    value = self.first_curve_segments_curves
    context.object.modifiers[modifier_name][value_socket_dict["first_curve_segments_curves"]] = value
    bpy.context.view_layer.update() #Redraw viewport if necessary

def update_2nd_curve_segments_curves(self, context):
    value = self.second_curve_segments_curves
    context.object.modifiers[modifier_name][value_socket_dict["second_curve_segments_curves"]] = value
    bpy.context.view_layer.update() #Redraw viewport if necessary

def update_radius_of_tubes_curves(self, context):
    value = self.radius_of_tubes_curves
    context.object.modifiers[modifier_name][value_socket_dict["radius_of_tubes_curves"]] = value
    bpy.context.view_layer.update() #Redraw viewport if necessary