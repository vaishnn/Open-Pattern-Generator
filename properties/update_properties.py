import bpy
from .update_properties_func import *

def property_update():
    bpy.types.Object.count_sizeandshape = bpy.props.IntProperty(
        name="Count",
        update=update_count_sizeandshape,  # Assign the update function
        default=15, 
        min = 0, 
        max = 1000, 
    )
    bpy.types.Object.size_sizeandshape = bpy.props.IntProperty(
        name="Size",
        update=update_size_sizeandshape,  # Assign the update function
        default=5, 
        min = 1, 
        max = 1000, 
    )
    bpy.types.Object.offset_sizeandshape = bpy.props.FloatProperty(
        name="Offset",
        update=update_offset_sizeandshape,  # Assign the update function
        default=0.83, 
        min = 0.5, 
        max = 1, 
    )
    bpy.types.Object.seed_sizeandshape = bpy.props.IntProperty(
        name="Seed",
        update=update_seed_sizeandshape,  # Assign the update function
        default=0, 
        min = -1000, 
        max = 1000, 
    )
    bpy.types.Object.grain_sizeandshape = bpy.props.FloatProperty(
        name="Grain",
        update=update_grain_sizeandshape,  # Assign the update function
        default=0.98,
        min = 0,
        max = 1,
    )
    bpy.types.Object.resolution_of_tubes_curves = bpy.props.IntProperty(
        name="Resolution of Tubes",
        update=update_resolution_of_tubes_curves,  # Assign the update function
        default=16,
        min = 2,
        max = 512)
    bpy.types.Object.resolution_of_curves_curves = bpy.props.IntProperty(
        name="Resolution of Curves",
        update=update_resolution_of_curves_curves,  # Assign the update function
        default=16,
        min = 2,
        max = 512)
    bpy.types.Object.first_curve_segments_curves = bpy.props.IntProperty(
        name="1st Curve Segments",
        update=update_1st_curve_segments_curves,  # Assign the update function
        default=10,
        min = 2,
        max = 512)
    bpy.types.Object.second_curve_segments_curves = bpy.props.IntProperty(
        name="2nd Curve Segements",
        update=update_2nd_curve_segments_curves,  # Assign the update function
        default=10,
        min = 2,
        max = 512)
    bpy.types.Object.radius_of_tubes_curves = bpy.props.FloatProperty(
        name="Radius of Tubes",
        update=update_radius_of_tubes_curves,  # Assign the update function
        min=0.0001,
        max=100,
        default=0.01)