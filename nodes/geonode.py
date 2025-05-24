import bpy
from ..some_scripts.some_func import node_group_name_exists
import random


# initialize creating_curves node group
def creating_curves_node_group():
    name = "Pattern Generator"
    while True:
        if node_group_name_exists(name, "GEOMETRY"):
            name = "Pattern Generator" + str(random.randint(0, 1000))
        else:
            creating_curves = bpy.data.node_groups.new(
                type="GeometryNodeTree", name=name
            )
            break
    creating_curves.color_tag = "NONE"
    creating_curves.description = ""

    creating_curves.is_modifier = True

    # creating_curves interface
    # Socket Geometry
    geometry_socket_3 = creating_curves.interface.new_socket(
        name="Geometry", in_out="OUTPUT", socket_type="NodeSocketGeometry"
    )
    geometry_socket_3.attribute_domain = "POINT"

    # Panel Size and Shape
    size_and_shape_panel_1 = creating_curves.interface.new_panel(
        "Size and Shape", default_closed=True
    )
    # Socket Count
    count_socket_1 = creating_curves.interface.new_socket(
        name="Count",
        in_out="INPUT",
        socket_type="NodeSocketInt",
        parent=size_and_shape_panel_1,
    )
    count_socket_1.default_value = 15
    count_socket_1.min_value = 1
    count_socket_1.max_value = 2147483647
    count_socket_1.subtype = "NONE"
    count_socket_1.default_attribute_name = "count_size"
    count_socket_1.attribute_domain = "POINT"

    # Socket Size X
    size_x_socket_1 = creating_curves.interface.new_socket(
        name="Size X",
        in_out="INPUT",
        socket_type="NodeSocketInt",
        parent=size_and_shape_panel_1,
    )
    size_x_socket_1.default_value = 5
    size_x_socket_1.min_value = 1
    size_x_socket_1.max_value = 2147483647
    size_x_socket_1.subtype = "NONE"
    size_x_socket_1.attribute_domain = "POINT"

    # Socket Size Y
    size_y_socket_1 = creating_curves.interface.new_socket(
        name="Size Y",
        in_out="INPUT",
        socket_type="NodeSocketInt",
        parent=size_and_shape_panel_1,
    )
    size_y_socket_1.default_value = 5
    size_y_socket_1.min_value = 1
    size_y_socket_1.max_value = 2147483647
    size_y_socket_1.subtype = "NONE"
    size_y_socket_1.attribute_domain = "POINT"

    # Socket Offset
    offset_socket_1 = creating_curves.interface.new_socket(
        name="Offset",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=size_and_shape_panel_1,
    )
    offset_socket_1.default_value = 0.8299999833106995
    offset_socket_1.min_value = 0.5
    offset_socket_1.max_value = 1.0
    offset_socket_1.subtype = "NONE"
    offset_socket_1.attribute_domain = "POINT"

    # Socket Seed
    seed_socket_3 = creating_curves.interface.new_socket(
        name="Seed",
        in_out="INPUT",
        socket_type="NodeSocketInt",
        parent=size_and_shape_panel_1,
    )
    seed_socket_3.default_value = 7
    seed_socket_3.min_value = -10000
    seed_socket_3.max_value = 10000
    seed_socket_3.subtype = "NONE"
    seed_socket_3.attribute_domain = "POINT"

    # Socket Grain
    grain_socket_1 = creating_curves.interface.new_socket(
        name="Grain",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=size_and_shape_panel_1,
    )
    grain_socket_1.default_value = 0.9800000190734863
    grain_socket_1.min_value = 0.0
    grain_socket_1.max_value = 1.0
    grain_socket_1.subtype = "NONE"
    grain_socket_1.attribute_domain = "POINT"

    # Socket Rotation Random
    rotation_random_socket_1 = creating_curves.interface.new_socket(
        name="Rotation Random",
        in_out="INPUT",
        socket_type="NodeSocketBool",
        parent=size_and_shape_panel_1,
    )
    rotation_random_socket_1.default_value = True
    rotation_random_socket_1.attribute_domain = "POINT"

    # Socket Rotation
    rotation_socket_1 = creating_curves.interface.new_socket(
        name="Rotation",
        in_out="INPUT",
        socket_type="NodeSocketInt",
        parent=size_and_shape_panel_1,
    )
    rotation_socket_1.default_value = 0
    rotation_socket_1.min_value = 0
    rotation_socket_1.max_value = 3
    rotation_socket_1.subtype = "NONE"
    rotation_socket_1.attribute_domain = "POINT"

    # Panel Curves
    curves_panel_1 = creating_curves.interface.new_panel("Curves", default_closed=True)
    # Socket Resolution of Tubes
    resolution_of_tubes_socket_1 = creating_curves.interface.new_socket(
        name="Resolution of Tubes",
        in_out="INPUT",
        socket_type="NodeSocketInt",
        parent=curves_panel_1,
    )
    resolution_of_tubes_socket_1.default_value = 32
    resolution_of_tubes_socket_1.min_value = 2
    resolution_of_tubes_socket_1.max_value = 512
    resolution_of_tubes_socket_1.subtype = "NONE"
    resolution_of_tubes_socket_1.attribute_domain = "POINT"

    # Socket 1st Curve Segments
    _1st_curve_segments_socket_1 = creating_curves.interface.new_socket(
        name="1st Curve Segments",
        in_out="INPUT",
        socket_type="NodeSocketInt",
        parent=curves_panel_1,
    )
    _1st_curve_segments_socket_1.default_value = 10
    _1st_curve_segments_socket_1.min_value = 2
    _1st_curve_segments_socket_1.max_value = 100000
    _1st_curve_segments_socket_1.subtype = "NONE"
    _1st_curve_segments_socket_1.attribute_domain = "POINT"

    # Socket 2nd Curve Segements
    _2nd_curve_segements_socket_1 = creating_curves.interface.new_socket(
        name="2nd Curve Segements",
        in_out="INPUT",
        socket_type="NodeSocketInt",
        parent=curves_panel_1,
    )
    _2nd_curve_segements_socket_1.default_value = 10
    _2nd_curve_segements_socket_1.min_value = 2
    _2nd_curve_segements_socket_1.max_value = 100000
    _2nd_curve_segements_socket_1.subtype = "NONE"
    _2nd_curve_segements_socket_1.attribute_domain = "POINT"

    # Socket Radius of Tubes
    radius_of_tubes_socket_1 = creating_curves.interface.new_socket(
        name="Radius of Tubes",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=curves_panel_1,
    )
    radius_of_tubes_socket_1.default_value = 0.009999999776482582
    radius_of_tubes_socket_1.min_value = 0.0
    radius_of_tubes_socket_1.max_value = 3.4028234663852886e38
    radius_of_tubes_socket_1.subtype = "DISTANCE"
    radius_of_tubes_socket_1.attribute_domain = "POINT"

    # Panel Curve Trimming
    curve_trimming_panel_1 = creating_curves.interface.new_panel(
        "Curve Trimming", default_closed=True
    )
    # Socket Random Portion
    random_portion_socket_1 = creating_curves.interface.new_socket(
        name="Random Portion",
        in_out="INPUT",
        socket_type="NodeSocketBool",
        parent=curve_trimming_panel_1,
    )
    random_portion_socket_1.default_value = True
    random_portion_socket_1.attribute_domain = "POINT"

    # Socket True Random Portion
    true_random_portion_socket_1 = creating_curves.interface.new_socket(
        name="True Random Portion",
        in_out="INPUT",
        socket_type="NodeSocketBool",
        parent=curve_trimming_panel_1,
    )
    true_random_portion_socket_1.default_value = False
    true_random_portion_socket_1.attribute_domain = "POINT"

    # Socket Every Section
    every_section_socket_1 = creating_curves.interface.new_socket(
        name="Every Section",
        in_out="INPUT",
        socket_type="NodeSocketBool",
        parent=curve_trimming_panel_1,
    )
    every_section_socket_1.default_value = False
    every_section_socket_1.attribute_domain = "POINT"

    # Socket Seed - Triming
    seed___triming_socket_1 = creating_curves.interface.new_socket(
        name="Seed - Triming",
        in_out="INPUT",
        socket_type="NodeSocketInt",
        parent=curve_trimming_panel_1,
    )
    seed___triming_socket_1.default_value = 0
    seed___triming_socket_1.min_value = -10000
    seed___triming_socket_1.max_value = 10000
    seed___triming_socket_1.subtype = "NONE"
    seed___triming_socket_1.attribute_domain = "POINT"

    # Socket Trim - Portion
    trim___portion_socket_1 = creating_curves.interface.new_socket(
        name="Trim - Portion",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=curve_trimming_panel_1,
    )
    trim___portion_socket_1.default_value = 0.5
    trim___portion_socket_1.min_value = 0.0
    trim___portion_socket_1.max_value = 1.0
    trim___portion_socket_1.subtype = "FACTOR"
    trim___portion_socket_1.attribute_domain = "POINT"

    # Socket From Start
    from_start_socket_1 = creating_curves.interface.new_socket(
        name="From Start",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=curve_trimming_panel_1,
    )
    from_start_socket_1.default_value = 0.0
    from_start_socket_1.min_value = 0.0
    from_start_socket_1.max_value = 1.0
    from_start_socket_1.subtype = "FACTOR"
    from_start_socket_1.attribute_domain = "POINT"

    # Socket From End
    from_end_socket_1 = creating_curves.interface.new_socket(
        name="From End",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=curve_trimming_panel_1,
    )
    from_end_socket_1.default_value = 1.0
    from_end_socket_1.min_value = 0.0
    from_end_socket_1.max_value = 1.0
    from_end_socket_1.subtype = "FACTOR"
    from_end_socket_1.attribute_domain = "POINT"

    # Panel Merge
    merge_panel_1 = creating_curves.interface.new_panel("Merge")
    # Socket Merge Probability
    merge_probability_socket_1 = creating_curves.interface.new_socket(
        name="Merge Probability",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=merge_panel_1,
    )
    merge_probability_socket_1.default_value = 0.0
    merge_probability_socket_1.min_value = 0.0
    merge_probability_socket_1.max_value = 1.0
    merge_probability_socket_1.subtype = "FACTOR"
    merge_probability_socket_1.attribute_domain = "POINT"

    # Socket Merge Seed
    merge_seed_socket_1 = creating_curves.interface.new_socket(
        name="Merge Seed",
        in_out="INPUT",
        socket_type="NodeSocketInt",
        parent=merge_panel_1,
    )
    merge_seed_socket_1.default_value = 0
    merge_seed_socket_1.min_value = -2147483648
    merge_seed_socket_1.max_value = 2147483647
    merge_seed_socket_1.subtype = "NONE"
    merge_seed_socket_1.attribute_domain = "POINT"

    # Socket Merge Distance
    merge_distance_socket_1 = creating_curves.interface.new_socket(
        name="Merge Distance",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=merge_panel_1,
    )
    merge_distance_socket_1.default_value = 0.0010000000474974513
    merge_distance_socket_1.min_value = 0.0
    merge_distance_socket_1.max_value = 3.4028234663852886e38
    merge_distance_socket_1.subtype = "NONE"
    merge_distance_socket_1.attribute_domain = "POINT"

    # Panel Custom Mode
    custom_mode_panel_1 = creating_curves.interface.new_panel("Custom Mode")
    # Socket Mode
    mode_socket_1 = creating_curves.interface.new_socket(
        name="Mode",
        in_out="INPUT",
        socket_type="NodeSocketString",
        parent=custom_mode_panel_1,
    )
    mode_socket_1.default_value = "None"
    mode_socket_1.attribute_domain = "POINT"
    mode_socket_1.force_non_field = True

    # Socket Method
    method_socket_1 = creating_curves.interface.new_socket(
        name="Method",
        in_out="INPUT",
        socket_type="NodeSocketString",
        parent=custom_mode_panel_1,
    )
    method_socket_1.default_value = ""
    method_socket_1.attribute_domain = "POINT"

    # Socket String
    string_socket_1 = creating_curves.interface.new_socket(
        name="String",
        in_out="INPUT",
        socket_type="NodeSocketString",
        parent=custom_mode_panel_1,
    )
    string_socket_1.default_value = ""
    string_socket_1.attribute_domain = "POINT"

    # Socket String Size
    string_size_socket_1 = creating_curves.interface.new_socket(
        name="String Size",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=custom_mode_panel_1,
    )
    string_size_socket_1.default_value = 2.0
    string_size_socket_1.min_value = 0.0
    string_size_socket_1.max_value = 3.4028234663852886e38
    string_size_socket_1.subtype = "NONE"
    string_size_socket_1.attribute_domain = "POINT"

    # Socket Gap Between Characters
    gap_between_characters_socket_1 = creating_curves.interface.new_socket(
        name="Gap Between Characters",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=custom_mode_panel_1,
    )
    gap_between_characters_socket_1.default_value = 0.0
    gap_between_characters_socket_1.min_value = 0.0
    gap_between_characters_socket_1.max_value = 3.4028234663852886e38
    gap_between_characters_socket_1.subtype = "NONE"
    gap_between_characters_socket_1.attribute_domain = "POINT"

    # Socket Scale
    scale_socket_1 = creating_curves.interface.new_socket(
        name="Scale",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=custom_mode_panel_1,
    )
    scale_socket_1.default_value = 1.0
    scale_socket_1.min_value = 0.0
    scale_socket_1.max_value = 3.4028234663852886e38
    scale_socket_1.subtype = "NONE"
    scale_socket_1.attribute_domain = "POINT"

    # Socket Image
    image_socket_3 = creating_curves.interface.new_socket(
        name="Image",
        in_out="INPUT",
        socket_type="NodeSocketImage",
        parent=custom_mode_panel_1,
    )
    image_socket_3.attribute_domain = "POINT"

    # Socket Image Smoothness (Subdivision)
    image_smoothness__subdivision__socket_1 = creating_curves.interface.new_socket(
        name="Image Smoothness (Subdivision)",
        in_out="INPUT",
        socket_type="NodeSocketInt",
        parent=custom_mode_panel_1,
    )
    image_smoothness__subdivision__socket_1.default_value = 4
    image_smoothness__subdivision__socket_1.min_value = 0
    image_smoothness__subdivision__socket_1.max_value = 100
    image_smoothness__subdivision__socket_1.subtype = "NONE"
    image_smoothness__subdivision__socket_1.attribute_domain = "POINT"

    # Panel Colors
    colors_panel_1 = creating_curves.interface.new_panel("Colors", default_closed=True)
    # Socket Material (Curves)
    material__curves__socket_1 = creating_curves.interface.new_socket(
        name="Material (Curves)",
        in_out="INPUT",
        socket_type="NodeSocketMaterial",
        parent=colors_panel_1,
    )
    material__curves__socket_1.attribute_domain = "POINT"

    # Socket Emission Stenght
    emission_stenght_socket_1 = creating_curves.interface.new_socket(
        name="Emission Stenght",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=colors_panel_1,
    )
    emission_stenght_socket_1.default_value = 1.0
    emission_stenght_socket_1.min_value = 0.0
    emission_stenght_socket_1.max_value = 3.4028234663852886e38
    emission_stenght_socket_1.subtype = "NONE"
    emission_stenght_socket_1.attribute_domain = "POINT"

    # Socket Color Attribute
    color_attribute_socket_1 = creating_curves.interface.new_socket(
        name="Color Attribute",
        in_out="INPUT",
        socket_type="NodeSocketString",
        parent=colors_panel_1,
    )
    color_attribute_socket_1.default_value = "S"
    color_attribute_socket_1.attribute_domain = "POINT"

    # Socket Animate
    animate_socket_2 = creating_curves.interface.new_socket(
        name="Animate",
        in_out="INPUT",
        socket_type="NodeSocketBool",
        parent=colors_panel_1,
    )
    animate_socket_2.default_value = True
    animate_socket_2.attribute_domain = "POINT"

    # Socket Animation Type
    animation_type_socket_2 = creating_curves.interface.new_socket(
        name="Animation Type",
        in_out="INPUT",
        socket_type="NodeSocketString",
        parent=colors_panel_1,
    )
    animation_type_socket_2.default_value = ""
    animation_type_socket_2.attribute_domain = "POINT"

    # Socket Color
    color_socket_2 = creating_curves.interface.new_socket(
        name="Color",
        in_out="INPUT",
        socket_type="NodeSocketString",
        parent=colors_panel_1,
    )
    color_socket_2.default_value = ""
    color_socket_2.attribute_domain = "POINT"

    # Socket Wave Motion
    wave_motion_socket_2 = creating_curves.interface.new_socket(
        name="Wave Motion",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=colors_panel_1,
    )
    wave_motion_socket_2.default_value = 1000.0
    wave_motion_socket_2.min_value = 0.0
    wave_motion_socket_2.max_value = 1000.0
    wave_motion_socket_2.subtype = "FACTOR"
    wave_motion_socket_2.attribute_domain = "POINT"

    # Socket Seed - Colors
    seed___colors_socket_1 = creating_curves.interface.new_socket(
        name="Seed - Colors",
        in_out="INPUT",
        socket_type="NodeSocketInt",
        parent=colors_panel_1,
    )
    seed___colors_socket_1.default_value = 0
    seed___colors_socket_1.min_value = -2147483648
    seed___colors_socket_1.max_value = 2147483647
    seed___colors_socket_1.subtype = "NONE"
    seed___colors_socket_1.attribute_domain = "POINT"

    # Socket Speed
    speed_socket_2 = creating_curves.interface.new_socket(
        name="Speed",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=colors_panel_1,
    )
    speed_socket_2.default_value = 2.0
    speed_socket_2.min_value = 0.0
    speed_socket_2.max_value = 3.4028234663852886e38
    speed_socket_2.subtype = "NONE"
    speed_socket_2.attribute_domain = "POINT"

    # Socket Type
    type_socket = creating_curves.interface.new_socket(
        name="Type", in_out="INPUT", socket_type="NodeSocketMenu", parent=colors_panel_1
    )
    type_socket.attribute_domain = "POINT"

    # Socket Gradient
    gradient_socket = creating_curves.interface.new_socket(
        name="Gradient",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=colors_panel_1,
    )
    gradient_socket.default_value = 1.0
    gradient_socket.min_value = 0.0
    gradient_socket.max_value = 1.0
    gradient_socket.subtype = "FACTOR"
    gradient_socket.attribute_domain = "POINT"

    # Socket Image
    image_socket_4 = creating_curves.interface.new_socket(
        name="Image",
        in_out="INPUT",
        socket_type="NodeSocketImage",
        parent=colors_panel_1,
    )
    image_socket_4.attribute_domain = "POINT"

    # Socket Color 1
    color_1_socket_2 = creating_curves.interface.new_socket(
        name="Color 1",
        in_out="INPUT",
        socket_type="NodeSocketColor",
        parent=colors_panel_1,
    )
    color_1_socket_2.default_value = (0.0, 0.0, 0.0, 1.0)
    color_1_socket_2.attribute_domain = "POINT"

    # Socket Color 2
    color_2_socket_2 = creating_curves.interface.new_socket(
        name="Color 2",
        in_out="INPUT",
        socket_type="NodeSocketColor",
        parent=colors_panel_1,
    )
    color_2_socket_2.default_value = (0.0, 0.0, 0.0, 1.0)
    color_2_socket_2.attribute_domain = "POINT"

    # Socket Color 3
    color_3_socket_2 = creating_curves.interface.new_socket(
        name="Color 3",
        in_out="INPUT",
        socket_type="NodeSocketColor",
        parent=colors_panel_1,
    )
    color_3_socket_2.default_value = (0.0, 0.0, 0.0, 1.0)
    color_3_socket_2.attribute_domain = "POINT"

    # Socket Color 4
    color_4_socket_2 = creating_curves.interface.new_socket(
        name="Color 4",
        in_out="INPUT",
        socket_type="NodeSocketColor",
        parent=colors_panel_1,
    )
    color_4_socket_2.default_value = (0.0, 0.0, 0.0, 1.0)
    color_4_socket_2.attribute_domain = "POINT"

    # Panel As Prop
    as_prop_panel = creating_curves.interface.new_panel("As Prop")
    # Socket Prop
    prop_socket_1 = creating_curves.interface.new_socket(
        name="Prop", in_out="INPUT", socket_type="NodeSocketBool", parent=as_prop_panel
    )
    prop_socket_1.default_value = False
    prop_socket_1.attribute_domain = "POINT"

    # Socket Seed
    seed_socket_4 = creating_curves.interface.new_socket(
        name="Seed", in_out="INPUT", socket_type="NodeSocketInt", parent=as_prop_panel
    )
    seed_socket_4.default_value = 2
    seed_socket_4.min_value = -10000
    seed_socket_4.max_value = 10000
    seed_socket_4.subtype = "NONE"
    seed_socket_4.attribute_domain = "POINT"

    # Socket Material (Hangers)
    material__hangers__socket_1 = creating_curves.interface.new_socket(
        name="Material (Hangers)",
        in_out="INPUT",
        socket_type="NodeSocketMaterial",
        parent=as_prop_panel,
    )
    material__hangers__socket_1.attribute_domain = "POINT"

    # Socket Distance
    distance_socket_1 = creating_curves.interface.new_socket(
        name="Distance",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=as_prop_panel,
    )
    distance_socket_1.default_value = 0.0
    distance_socket_1.min_value = 0.0
    distance_socket_1.max_value = 3.4028234663852886e38
    distance_socket_1.subtype = "NONE"
    distance_socket_1.attribute_domain = "POINT"

    # Socket Radius (Comparing)
    radius__comparing__socket_1 = creating_curves.interface.new_socket(
        name="Radius (Comparing)",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=as_prop_panel,
    )
    radius__comparing__socket_1.default_value = 50.0
    radius__comparing__socket_1.min_value = 0.0
    radius__comparing__socket_1.max_value = 100.0
    radius__comparing__socket_1.subtype = "PERCENTAGE"
    radius__comparing__socket_1.attribute_domain = "POINT"

    # Socket Have Back Plate
    have_back_plate_socket_1 = creating_curves.interface.new_socket(
        name="Have Back Plate",
        in_out="INPUT",
        socket_type="NodeSocketBool",
        parent=as_prop_panel,
    )
    have_back_plate_socket_1.default_value = False
    have_back_plate_socket_1.attribute_domain = "POINT"

    # Socket Material (Back Plate)
    material__back_plate__socket_1 = creating_curves.interface.new_socket(
        name="Material (Back Plate)",
        in_out="INPUT",
        socket_type="NodeSocketMaterial",
        parent=as_prop_panel,
    )
    material__back_plate__socket_1.attribute_domain = "POINT"

    # Panel Custom Mode More
    custom_mode_more_panel_1 = creating_curves.interface.new_panel("Custom Mode More")
    # Socket Subset
    subset_socket_2 = creating_curves.interface.new_socket(
        name="Subset",
        in_out="INPUT",
        socket_type="NodeSocketBool",
        parent=custom_mode_more_panel_1,
    )
    subset_socket_2.default_value = False
    subset_socket_2.attribute_domain = "POINT"

    # Socket Outside
    outside_socket_1 = creating_curves.interface.new_socket(
        name="Outside",
        in_out="INPUT",
        socket_type="NodeSocketBool",
        parent=custom_mode_more_panel_1,
    )
    outside_socket_1.default_value = False
    outside_socket_1.attribute_domain = "POINT"

    # Socket Both Outside and Inside
    both_outside_and_inside_socket_1 = creating_curves.interface.new_socket(
        name="Both Outside and Inside",
        in_out="INPUT",
        socket_type="NodeSocketBool",
        parent=custom_mode_more_panel_1,
    )
    both_outside_and_inside_socket_1.default_value = False
    both_outside_and_inside_socket_1.attribute_domain = "POINT"

    # initialize creating_curves nodes
    # node Group Input.003
    group_input_003_2 = creating_curves.nodes.new("NodeGroupInput")
    group_input_003_2.name = "Group Input.003"

    # node Group
    group = creating_curves.nodes.new("GeometryNodeGroup")
    group.name = "Group"
    group.node_tree = pattern_generator_node_group()
    # Socket_13
    group.inputs[41].default_value = False
    # Socket_26
    group.inputs[43].default_value = False

    # node Group Output
    group_output_3 = creating_curves.nodes.new("NodeGroupOutput")
    group_output_3.name = "Group Output"
    group_output_3.is_active_output = True

    # Set locations
    group_input_003_2.location = (1360.0, 1380.0)
    group.location = (1700.0, 1100.0)
    group_output_3.location = (1953.2476806640625, 571.3312377929688)

    # Set dimensions
    group_input_003_2.width, group_input_003_2.height = 140.0, 100.0
    group.width, group.height = 168.7896728515625, 100.0
    group_output_3.width, group_output_3.height = 140.0, 100.0

    # initialize creating_curves links
    # group_input_003_2.Count -> group.Count
    creating_curves.links.new(group_input_003_2.outputs[0], group.inputs[0])
    # group_input_003_2.Size X -> group.Size X
    creating_curves.links.new(group_input_003_2.outputs[1], group.inputs[1])
    # group_input_003_2.Size Y -> group.Size Y
    creating_curves.links.new(group_input_003_2.outputs[2], group.inputs[2])
    # group_input_003_2.Offset -> group.Offset
    creating_curves.links.new(group_input_003_2.outputs[3], group.inputs[3])
    # group_input_003_2.Seed -> group.Seed
    creating_curves.links.new(group_input_003_2.outputs[4], group.inputs[4])
    # group_input_003_2.Grain -> group.Grain
    creating_curves.links.new(group_input_003_2.outputs[5], group.inputs[5])
    # group_input_003_2.1st Curve Segments -> group.1st Curve Segments
    creating_curves.links.new(group_input_003_2.outputs[9], group.inputs[9])
    # group_input_003_2.Radius of Tubes -> group.Radius of Tubes
    creating_curves.links.new(group_input_003_2.outputs[11], group.inputs[11])
    # group_input_003_2.2nd Curve Segements -> group.2nd Curve Segements
    creating_curves.links.new(group_input_003_2.outputs[10], group.inputs[10])
    # group_input_003_2.Resolution of Tubes -> group.Resolution of Tubes
    creating_curves.links.new(group_input_003_2.outputs[8], group.inputs[8])
    # group_input_003_2.Random Portion -> group.Random Portion
    creating_curves.links.new(group_input_003_2.outputs[12], group.inputs[12])
    # group_input_003_2.Seed - Triming -> group.Seed - Triming
    creating_curves.links.new(group_input_003_2.outputs[15], group.inputs[15])
    # group_input_003_2.Trim - Portion -> group.Trim - Portion
    creating_curves.links.new(group_input_003_2.outputs[16], group.inputs[16])
    # group_input_003_2.From Start -> group.From Start
    creating_curves.links.new(group_input_003_2.outputs[17], group.inputs[17])
    # group_input_003_2.From End -> group.From End
    creating_curves.links.new(group_input_003_2.outputs[18], group.inputs[18])
    # group_input_003_2.Material (Curves) -> group.Material (Curves)
    creating_curves.links.new(group_input_003_2.outputs[30], group.inputs[30])
    # group_input_003_2.Animate -> group.Animate
    creating_curves.links.new(group_input_003_2.outputs[33], group.inputs[33])
    # group_input_003_2.Animation Type -> group.Animation Type
    creating_curves.links.new(group_input_003_2.outputs[34], group.inputs[34])
    # group_input_003_2.Wave Motion -> group.Wave Motion
    creating_curves.links.new(group_input_003_2.outputs[36], group.inputs[36])
    # group_input_003_2.Speed -> group.Speed
    creating_curves.links.new(group_input_003_2.outputs[38], group.inputs[38])
    # group_input_003_2.Seed - Colors -> group.Seed - Colors
    creating_curves.links.new(group_input_003_2.outputs[37], group.inputs[37])
    # group_input_003_2.Type -> group.Color Distribution
    creating_curves.links.new(group_input_003_2.outputs[39], group.inputs[39])
    # group_input_003_2.Gradient -> group.Blackness
    creating_curves.links.new(group_input_003_2.outputs[40], group.inputs[40])
    # group_input_003_2.Image -> group.Image
    creating_curves.links.new(group_input_003_2.outputs[41], group.inputs[42])
    # group_input_003_2.Color 1 -> group.Color 1
    creating_curves.links.new(group_input_003_2.outputs[42], group.inputs[44])
    # group_input_003_2.Color 2 -> group.Color 2
    creating_curves.links.new(group_input_003_2.outputs[43], group.inputs[45])
    # group_input_003_2.Color 3 -> group.Color 3
    creating_curves.links.new(group_input_003_2.outputs[44], group.inputs[46])
    # group_input_003_2.Color 4 -> group.Color 4
    creating_curves.links.new(group_input_003_2.outputs[45], group.inputs[47])
    # group_input_003_2.Prop -> group.Prop
    creating_curves.links.new(group_input_003_2.outputs[46], group.inputs[48])
    # group_input_003_2.Material (Hangers) -> group.Material (Hangers)
    creating_curves.links.new(group_input_003_2.outputs[48], group.inputs[50])
    # group_input_003_2.Distance -> group.Distance
    creating_curves.links.new(group_input_003_2.outputs[49], group.inputs[51])
    # group_input_003_2.Radius (Comparing) -> group.Radius (Comparing)
    creating_curves.links.new(group_input_003_2.outputs[50], group.inputs[52])
    # group_input_003_2.Have Back Plate -> group.Have Back Plate
    creating_curves.links.new(group_input_003_2.outputs[51], group.inputs[53])
    # group_input_003_2.Material (Back Plate) -> group.Material (Back Plate)
    creating_curves.links.new(group_input_003_2.outputs[52], group.inputs[54])
    # group_input_003_2.Seed -> group.Seed
    creating_curves.links.new(group_input_003_2.outputs[47], group.inputs[49])
    # group_input_003_2.Rotation -> group.Rotation
    creating_curves.links.new(group_input_003_2.outputs[7], group.inputs[7])
    # group_input_003_2.Rotation Random -> group.Rotation Random
    creating_curves.links.new(group_input_003_2.outputs[6], group.inputs[6])
    # group_input_003_2.Every Section -> group.Every Section
    creating_curves.links.new(group_input_003_2.outputs[14], group.inputs[14])
    # group_input_003_2.Color Attribute -> group.Color Attribute
    creating_curves.links.new(group_input_003_2.outputs[32], group.inputs[32])
    # group.Geometry -> group_output_3.Geometry
    creating_curves.links.new(group.outputs[0], group_output_3.inputs[0])
    # group_input_003_2.Mode -> group.Mode
    creating_curves.links.new(group_input_003_2.outputs[22], group.inputs[22])
    # group_input_003_2.String -> group.String
    creating_curves.links.new(group_input_003_2.outputs[24], group.inputs[24])
    # group_input_003_2.Gap Between Characters -> group.Gap Between Characters
    creating_curves.links.new(group_input_003_2.outputs[26], group.inputs[26])
    # group_input_003_2.String Size -> group.String Size
    creating_curves.links.new(group_input_003_2.outputs[25], group.inputs[25])
    # group_input_003_2.Scale -> group.Scale
    creating_curves.links.new(group_input_003_2.outputs[27], group.inputs[27])
    # group_input_003_2.Emission Stenght -> group.Emission Stenght
    creating_curves.links.new(group_input_003_2.outputs[31], group.inputs[31])
    # group_input_003_2.Method -> group.Method
    creating_curves.links.new(group_input_003_2.outputs[23], group.inputs[23])
    # group_input_003_2.True Random Portion -> group.True Random Portion
    creating_curves.links.new(group_input_003_2.outputs[13], group.inputs[13])
    # group_input_003_2.Merge Probability -> group.Merge Probability
    creating_curves.links.new(group_input_003_2.outputs[19], group.inputs[19])
    # group_input_003_2.Merge Seed -> group.Merge Seed
    creating_curves.links.new(group_input_003_2.outputs[20], group.inputs[20])
    # group_input_003_2.Merge Distance -> group.Merge Distance
    creating_curves.links.new(group_input_003_2.outputs[21], group.inputs[21])
    # group_input_003_2.Image Smoothness (Subdivision) -> group.Image Smoothness (Subdivision)
    creating_curves.links.new(group_input_003_2.outputs[29], group.inputs[29])
    # group_input_003_2.Image -> group.Image
    creating_curves.links.new(group_input_003_2.outputs[28], group.inputs[28])
    # group_input_003_2.Color -> group.Color
    creating_curves.links.new(group_input_003_2.outputs[35], group.inputs[35])
    # group_input_003_2.Subset -> group.Subset
    creating_curves.links.new(group_input_003_2.outputs[53], group.inputs[55])
    # group_input_003_2.Outside -> group.Outside
    creating_curves.links.new(group_input_003_2.outputs[54], group.inputs[56])
    # group_input_003_2.Both Outside and Inside -> group.Both Outside and Inside
    creating_curves.links.new(group_input_003_2.outputs[55], group.inputs[57])
    type_socket.default_value = "Constant"
    return creating_curves, name


# initialize method_calculation node group
def method_calculation_node_group():
    name = "Method Calculation"
    while True:
        if node_group_name_exists(name, "GEOMETRY"):
            name = "Method Calculation" + str(random.randint(0, 1000))
        else:
            method_calculation = bpy.data.node_groups.new(
                type="GeometryNodeTree", name=name
            )
            break
    method_calculation.color_tag = "NONE"
    method_calculation.description = ""

    # method_calculation interface
    # Socket Method 1
    method_1_socket = method_calculation.interface.new_socket(
        name="Method 1", in_out="OUTPUT", socket_type="NodeSocketGeometry"
    )
    method_1_socket.attribute_domain = "POINT"

    # Socket Method 2
    method_2_socket = method_calculation.interface.new_socket(
        name="Method 2", in_out="OUTPUT", socket_type="NodeSocketGeometry"
    )
    method_2_socket.attribute_domain = "POINT"

    # Socket OG Geometry
    og_geometry_socket = method_calculation.interface.new_socket(
        name="OG Geometry", in_out="INPUT", socket_type="NodeSocketGeometry"
    )
    og_geometry_socket.attribute_domain = "POINT"

    # Socket Cutout Instance
    cutout_instance_socket = method_calculation.interface.new_socket(
        name="Cutout Instance", in_out="INPUT", socket_type="NodeSocketGeometry"
    )
    cutout_instance_socket.attribute_domain = "POINT"

    # Socket Subset
    subset_socket = method_calculation.interface.new_socket(
        name="Subset", in_out="INPUT", socket_type="NodeSocketBool"
    )
    subset_socket.default_value = False
    subset_socket.attribute_domain = "POINT"

    # initialize method_calculation nodes
    # node Group Input
    group_input = method_calculation.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # node Extrude Mesh.002
    extrude_mesh_002 = method_calculation.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh_002.name = "Extrude Mesh.002"
    extrude_mesh_002.mode = "FACES"
    # Selection
    extrude_mesh_002.inputs[1].default_value = True
    # Offset
    extrude_mesh_002.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Offset Scale
    extrude_mesh_002.inputs[3].default_value = 0.019999999552965164
    # Individual
    extrude_mesh_002.inputs[4].default_value = True

    # node Attribute Statistic.004
    attribute_statistic_004 = method_calculation.nodes.new(
        "GeometryNodeAttributeStatistic"
    )
    attribute_statistic_004.name = "Attribute Statistic.004"
    attribute_statistic_004.data_type = "FLOAT"
    attribute_statistic_004.domain = "POINT"
    attribute_statistic_004.inputs[1].hide = True
    attribute_statistic_004.outputs[1].hide = True
    attribute_statistic_004.outputs[2].hide = True
    attribute_statistic_004.outputs[3].hide = True
    attribute_statistic_004.outputs[4].hide = True
    attribute_statistic_004.outputs[5].hide = True
    attribute_statistic_004.outputs[6].hide = True
    attribute_statistic_004.outputs[7].hide = True
    # Selection
    attribute_statistic_004.inputs[1].default_value = True

    # node Position.004
    position_004 = method_calculation.nodes.new("GeometryNodeInputPosition")
    position_004.name = "Position.004"

    # node Transform Geometry.003
    transform_geometry_003 = method_calculation.nodes.new("GeometryNodeTransform")
    transform_geometry_003.name = "Transform Geometry.003"
    transform_geometry_003.mode = "COMPONENTS"
    transform_geometry_003.inputs[2].hide = True
    transform_geometry_003.inputs[3].hide = True
    transform_geometry_003.inputs[4].hide = True
    # Rotation
    transform_geometry_003.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_003.inputs[3].default_value = (1.0, 1.0, 1.0)

    # node Realize Instances.010
    realize_instances_010 = method_calculation.nodes.new("GeometryNodeRealizeInstances")
    realize_instances_010.name = "Realize Instances.010"
    realize_instances_010.inputs[1].hide = True
    realize_instances_010.inputs[2].hide = True
    realize_instances_010.inputs[3].hide = True
    # Selection
    realize_instances_010.inputs[1].default_value = True
    # Realize All
    realize_instances_010.inputs[2].default_value = True
    # Depth
    realize_instances_010.inputs[3].default_value = 0

    # node Extrude Mesh.003
    extrude_mesh_003 = method_calculation.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh_003.name = "Extrude Mesh.003"
    extrude_mesh_003.mode = "EDGES"
    # Selection
    extrude_mesh_003.inputs[1].default_value = True
    # Offset Scale
    extrude_mesh_003.inputs[3].default_value = 9.999999747378752e-05

    # node Mesh Boolean.001
    mesh_boolean_001 = method_calculation.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean_001.name = "Mesh Boolean.001"
    mesh_boolean_001.operation = "INTERSECT"
    mesh_boolean_001.solver = "EXACT"
    # Self Intersection
    mesh_boolean_001.inputs[2].default_value = False
    # Hole Tolerant
    mesh_boolean_001.inputs[3].default_value = False

    # node Combine XYZ.005
    combine_xyz_005 = method_calculation.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_005.name = "Combine XYZ.005"
    combine_xyz_005.inputs[0].hide = True
    combine_xyz_005.inputs[1].hide = True
    # X
    combine_xyz_005.inputs[0].default_value = 0.0
    # Y
    combine_xyz_005.inputs[1].default_value = 0.0

    # node Separate XYZ.003
    separate_xyz_003 = method_calculation.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_003.name = "Separate XYZ.003"
    separate_xyz_003.outputs[0].hide = True
    separate_xyz_003.outputs[1].hide = True

    # node Store Named Attribute.007
    store_named_attribute_007 = method_calculation.nodes.new(
        "GeometryNodeStoreNamedAttribute"
    )
    store_named_attribute_007.name = "Store Named Attribute.007"
    store_named_attribute_007.data_type = "FLOAT"
    store_named_attribute_007.domain = "POINT"
    # Selection
    store_named_attribute_007.inputs[1].default_value = True
    # Name
    store_named_attribute_007.inputs[2].default_value = "value_not_deleted"
    # Value
    store_named_attribute_007.inputs[3].default_value = 1.0

    # node Join Geometry.004
    join_geometry_004 = method_calculation.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_004.name = "Join Geometry.004"

    # node Mesh Boolean.002
    mesh_boolean_002 = method_calculation.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean_002.name = "Mesh Boolean.002"
    mesh_boolean_002.operation = "DIFFERENCE"
    mesh_boolean_002.solver = "EXACT"
    # Self Intersection
    mesh_boolean_002.inputs[2].default_value = False
    # Hole Tolerant
    mesh_boolean_002.inputs[3].default_value = False

    # node Store Named Attribute.008
    store_named_attribute_008 = method_calculation.nodes.new(
        "GeometryNodeStoreNamedAttribute"
    )
    store_named_attribute_008.name = "Store Named Attribute.008"
    store_named_attribute_008.data_type = "FLOAT"
    store_named_attribute_008.domain = "POINT"
    store_named_attribute_008.inputs[1].hide = True
    store_named_attribute_008.inputs[2].hide = True
    store_named_attribute_008.inputs[3].hide = True
    # Selection
    store_named_attribute_008.inputs[1].default_value = True
    # Name
    store_named_attribute_008.inputs[2].default_value = "value_not_deleted"
    # Value
    store_named_attribute_008.inputs[3].default_value = 0.0

    # node Store Named Attribute.002
    store_named_attribute_002 = method_calculation.nodes.new(
        "GeometryNodeStoreNamedAttribute"
    )
    store_named_attribute_002.name = "Store Named Attribute.002"
    store_named_attribute_002.data_type = "FLOAT"
    store_named_attribute_002.domain = "POINT"
    store_named_attribute_002.inputs[1].hide = True
    store_named_attribute_002.inputs[2].hide = True
    # Selection
    store_named_attribute_002.inputs[1].default_value = True
    # Name
    store_named_attribute_002.inputs[2].default_value = "value_not_deleted"

    # node Named Attribute
    named_attribute = method_calculation.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute.name = "Named Attribute"
    named_attribute.data_type = "FLOAT"
    named_attribute.inputs[0].hide = True
    named_attribute.outputs[1].hide = True
    # Name
    named_attribute.inputs[0].default_value = "value_not_deleted"

    # node Delete Geometry.003
    delete_geometry_003 = method_calculation.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_003.name = "Delete Geometry.003"
    delete_geometry_003.domain = "POINT"
    delete_geometry_003.mode = "ALL"

    # node Combine XYZ.006
    combine_xyz_006 = method_calculation.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_006.name = "Combine XYZ.006"
    # X
    combine_xyz_006.inputs[0].default_value = 0.0
    # Y
    combine_xyz_006.inputs[1].default_value = 0.0
    # Z
    combine_xyz_006.inputs[2].default_value = 1.0

    # node Compare.005
    compare_005 = method_calculation.nodes.new("FunctionNodeCompare")
    compare_005.name = "Compare.005"
    compare_005.data_type = "FLOAT"
    compare_005.mode = "ELEMENT"
    compare_005.operation = "GREATER_THAN"
    # B
    compare_005.inputs[1].default_value = 0.0

    # node Delete Geometry.004
    delete_geometry_004 = method_calculation.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_004.name = "Delete Geometry.004"
    delete_geometry_004.domain = "POINT"
    delete_geometry_004.mode = "ALL"

    # node Store Named Attribute.010
    store_named_attribute_010 = method_calculation.nodes.new(
        "GeometryNodeStoreNamedAttribute"
    )
    store_named_attribute_010.name = "Store Named Attribute.010"
    store_named_attribute_010.data_type = "FLOAT"
    store_named_attribute_010.domain = "POINT"
    # Selection
    store_named_attribute_010.inputs[1].default_value = True
    # Name
    store_named_attribute_010.inputs[2].default_value = "value_not_deleted"
    # Value
    store_named_attribute_010.inputs[3].default_value = 0.0

    # node Group Output
    group_output = method_calculation.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # node Reroute
    reroute = method_calculation.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    # node Reroute.001
    reroute_001 = method_calculation.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    # node Reroute.002
    reroute_002 = method_calculation.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    # node Reroute.003
    reroute_003 = method_calculation.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    # node Reroute.004
    reroute_004 = method_calculation.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    # node Reroute.005
    reroute_005 = method_calculation.nodes.new("NodeReroute")
    reroute_005.name = "Reroute.005"
    # node Reroute.006
    reroute_006 = method_calculation.nodes.new("NodeReroute")
    reroute_006.name = "Reroute.006"

    # Set locations
    group_input.location = (-1024.06494140625, 310.4301452636719)
    extrude_mesh_002.location = (-631.56494140625, 179.93014526367188)
    attribute_statistic_004.location = (-384.5679931640625, 667.93017578125)
    position_004.location = (-821.56494140625, 667.93017578125)
    transform_geometry_003.location = (32.9320068359375, 539.93017578125)
    realize_instances_010.location = (-821.56494140625, 179.93014526367188)
    extrude_mesh_003.location = (-182.0679931640625, 440.9301452636719)
    mesh_boolean_001.location = (247.9320068359375, 539.93017578125)
    combine_xyz_005.location = (-182.0679931640625, 667.93017578125)
    separate_xyz_003.location = (-609.3164672851562, 667.93017578125)
    store_named_attribute_007.location = (437.9320068359375, 539.93017578125)
    join_geometry_004.location = (652.9320068359375, 179.93014526367188)
    mesh_boolean_002.location = (247.9320068359375, 179.93014526367188)
    store_named_attribute_008.location = (437.9320068359375, 179.93014526367188)
    store_named_attribute_002.location = (1057.9320068359375, -49.069854736328125)
    named_attribute.location = (652.9320068359375, -209.06985473632812)
    delete_geometry_003.location = (855.4320068359375, 48.930145263671875)
    combine_xyz_006.location = (-384.5679931640625, 411.9301452636719)
    compare_005.location = (855.4320068359375, -209.06985473632812)
    delete_geometry_004.location = (652.9320068359375, 539.93017578125)
    store_named_attribute_010.location = (855.4320068359375, 539.93017578125)
    group_output.location = (1272.9320068359375, 180.43014526367188)
    reroute.location = (-821.56494140625, 469.9301452636719)
    reroute_001.location = (-244.5679931640625, 469.9301452636719)
    reroute_002.location = (172.9320068359375, 144.99600219726562)
    reroute_003.location = (32.9320068359375, -82.06985473632812)
    reroute_004.location = (577.9320068359375, -82.06985473632812)
    reroute_005.location = (652.9320068359375, -82.06985473632812)
    reroute_006.location = (1197.9320068359375, 504.9960021972656)

    # Set dimensions
    group_input.width, group_input.height = 140.0, 100.0
    extrude_mesh_002.width, extrude_mesh_002.height = 184.4969482421875, 100.0
    attribute_statistic_004.width, attribute_statistic_004.height = 140.0, 100.0
    position_004.width, position_004.height = 140.0, 100.0
    transform_geometry_003.width, transform_geometry_003.height = 140.0, 100.0
    realize_instances_010.width, realize_instances_010.height = 140.0, 100.0
    extrude_mesh_003.width, extrude_mesh_003.height = 140.0, 100.0
    mesh_boolean_001.width, mesh_boolean_001.height = 140.0, 100.0
    combine_xyz_005.width, combine_xyz_005.height = 140.0, 100.0
    separate_xyz_003.width, separate_xyz_003.height = 140.0, 100.0
    store_named_attribute_007.width, store_named_attribute_007.height = 140.0, 100.0
    join_geometry_004.width, join_geometry_004.height = 140.0, 100.0
    mesh_boolean_002.width, mesh_boolean_002.height = 140.0, 100.0
    store_named_attribute_008.width, store_named_attribute_008.height = 140.0, 100.0
    store_named_attribute_002.width, store_named_attribute_002.height = 140.0, 100.0
    named_attribute.width, named_attribute.height = 140.0, 100.0
    delete_geometry_003.width, delete_geometry_003.height = 140.0, 100.0
    combine_xyz_006.width, combine_xyz_006.height = 140.0, 100.0
    compare_005.width, compare_005.height = 140.0, 100.0
    delete_geometry_004.width, delete_geometry_004.height = 140.0, 100.0
    store_named_attribute_010.width, store_named_attribute_010.height = 140.0, 100.0
    group_output.width, group_output.height = 140.0, 100.0
    reroute.width, reroute.height = 16.0, 100.0
    reroute_001.width, reroute_001.height = 16.0, 100.0
    reroute_002.width, reroute_002.height = 16.0, 100.0
    reroute_003.width, reroute_003.height = 16.0, 100.0
    reroute_004.width, reroute_004.height = 16.0, 100.0
    reroute_005.width, reroute_005.height = 16.0, 100.0
    reroute_006.width, reroute_006.height = 16.0, 100.0

    # initialize method_calculation links
    # delete_geometry_003.Geometry -> store_named_attribute_002.Geometry
    method_calculation.links.new(
        delete_geometry_003.outputs[0], store_named_attribute_002.inputs[0]
    )
    # mesh_boolean_001.Mesh -> store_named_attribute_007.Geometry
    method_calculation.links.new(
        mesh_boolean_001.outputs[0], store_named_attribute_007.inputs[0]
    )
    # combine_xyz_006.Vector -> extrude_mesh_003.Offset
    method_calculation.links.new(combine_xyz_006.outputs[0], extrude_mesh_003.inputs[2])
    # delete_geometry_004.Geometry -> store_named_attribute_010.Geometry
    method_calculation.links.new(
        delete_geometry_004.outputs[0], store_named_attribute_010.inputs[0]
    )
    # store_named_attribute_008.Geometry -> join_geometry_004.Geometry
    method_calculation.links.new(
        store_named_attribute_008.outputs[0], join_geometry_004.inputs[0]
    )
    # extrude_mesh_003.Mesh -> transform_geometry_003.Geometry
    method_calculation.links.new(
        extrude_mesh_003.outputs[0], transform_geometry_003.inputs[0]
    )
    # separate_xyz_003.Z -> attribute_statistic_004.Attribute
    method_calculation.links.new(
        separate_xyz_003.outputs[2], attribute_statistic_004.inputs[2]
    )
    # store_named_attribute_007.Geometry -> delete_geometry_004.Geometry
    method_calculation.links.new(
        store_named_attribute_007.outputs[0], delete_geometry_004.inputs[0]
    )
    # realize_instances_010.Geometry -> extrude_mesh_002.Mesh
    method_calculation.links.new(
        realize_instances_010.outputs[0], extrude_mesh_002.inputs[0]
    )
    # attribute_statistic_004.Mean -> combine_xyz_005.Z
    method_calculation.links.new(
        attribute_statistic_004.outputs[0], combine_xyz_005.inputs[2]
    )
    # mesh_boolean_002.Mesh -> store_named_attribute_008.Geometry
    method_calculation.links.new(
        mesh_boolean_002.outputs[0], store_named_attribute_008.inputs[0]
    )
    # named_attribute.Attribute -> compare_005.A
    method_calculation.links.new(named_attribute.outputs[0], compare_005.inputs[0])
    # combine_xyz_005.Vector -> transform_geometry_003.Translation
    method_calculation.links.new(
        combine_xyz_005.outputs[0], transform_geometry_003.inputs[1]
    )
    # compare_005.Result -> store_named_attribute_002.Value
    method_calculation.links.new(
        compare_005.outputs[0], store_named_attribute_002.inputs[3]
    )
    # position_004.Position -> separate_xyz_003.Vector
    method_calculation.links.new(position_004.outputs[0], separate_xyz_003.inputs[0])
    # join_geometry_004.Geometry -> delete_geometry_003.Geometry
    method_calculation.links.new(
        join_geometry_004.outputs[0], delete_geometry_003.inputs[0]
    )
    # group_input.Cutout Instance -> realize_instances_010.Geometry
    method_calculation.links.new(
        group_input.outputs[1], realize_instances_010.inputs[0]
    )
    # extrude_mesh_002.Mesh -> attribute_statistic_004.Geometry
    method_calculation.links.new(
        extrude_mesh_002.outputs[0], attribute_statistic_004.inputs[0]
    )
    # transform_geometry_003.Geometry -> mesh_boolean_002.Mesh 1
    method_calculation.links.new(
        transform_geometry_003.outputs[0], mesh_boolean_002.inputs[0]
    )
    # store_named_attribute_002.Geometry -> group_output.Method 2
    method_calculation.links.new(
        store_named_attribute_002.outputs[0], group_output.inputs[1]
    )
    # group_input.OG Geometry -> reroute.Input
    method_calculation.links.new(group_input.outputs[0], reroute.inputs[0])
    # reroute.Output -> reroute_001.Input
    method_calculation.links.new(reroute.outputs[0], reroute_001.inputs[0])
    # reroute_001.Output -> extrude_mesh_003.Mesh
    method_calculation.links.new(reroute_001.outputs[0], extrude_mesh_003.inputs[0])
    # extrude_mesh_002.Mesh -> reroute_002.Input
    method_calculation.links.new(extrude_mesh_002.outputs[0], reroute_002.inputs[0])
    # reroute_002.Output -> mesh_boolean_002.Mesh 2
    method_calculation.links.new(reroute_002.outputs[0], mesh_boolean_002.inputs[1])
    # reroute_002.Output -> mesh_boolean_001.Mesh 2
    method_calculation.links.new(reroute_002.outputs[0], mesh_boolean_001.inputs[1])
    # extrude_mesh_003.Top -> reroute_003.Input
    method_calculation.links.new(extrude_mesh_003.outputs[1], reroute_003.inputs[0])
    # reroute_003.Output -> reroute_004.Input
    method_calculation.links.new(reroute_003.outputs[0], reroute_004.inputs[0])
    # reroute_004.Output -> delete_geometry_004.Selection
    method_calculation.links.new(reroute_004.outputs[0], delete_geometry_004.inputs[1])
    # reroute_004.Output -> reroute_005.Input
    method_calculation.links.new(reroute_004.outputs[0], reroute_005.inputs[0])
    # reroute_005.Output -> delete_geometry_003.Selection
    method_calculation.links.new(reroute_005.outputs[0], delete_geometry_003.inputs[1])
    # store_named_attribute_010.Geometry -> reroute_006.Input
    method_calculation.links.new(
        store_named_attribute_010.outputs[0], reroute_006.inputs[0]
    )
    # reroute_006.Output -> group_output.Method 1
    method_calculation.links.new(reroute_006.outputs[0], group_output.inputs[0])
    # store_named_attribute_007.Geometry -> join_geometry_004.Geometry
    method_calculation.links.new(
        store_named_attribute_007.outputs[0], join_geometry_004.inputs[0]
    )
    # transform_geometry_003.Geometry -> mesh_boolean_001.Mesh 2
    method_calculation.links.new(
        transform_geometry_003.outputs[0], mesh_boolean_001.inputs[1]
    )
    return method_calculation


# initialize subset_curve node group
def subset_curve_node_group():
    name = "Subset Curve"
    while True:
        if node_group_name_exists(name, "GEOMETRY"):
            name = "Subset Curve" + str(random.randint(0, 1000))
        else:
            subset_curve = bpy.data.node_groups.new(type="GeometryNodeTree", name=name)
            break
    subset_curve.color_tag = "NONE"
    subset_curve.description = ""

    # subset_curve interface
    # Socket Output
    output_socket = subset_curve.interface.new_socket(
        name="Output", in_out="OUTPUT", socket_type="NodeSocketGeometry"
    )
    output_socket.attribute_domain = "POINT"

    # Socket Geometry
    geometry_socket = subset_curve.interface.new_socket(
        name="Geometry", in_out="INPUT", socket_type="NodeSocketGeometry"
    )
    geometry_socket.attribute_domain = "POINT"

    # Socket not_to_be_deleted
    not_to_be_deleted_socket = subset_curve.interface.new_socket(
        name="not_to_be_deleted", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    not_to_be_deleted_socket.default_value = 0.0
    not_to_be_deleted_socket.min_value = -3.4028234663852886e38
    not_to_be_deleted_socket.max_value = 3.4028234663852886e38
    not_to_be_deleted_socket.subtype = "NONE"
    not_to_be_deleted_socket.attribute_domain = "POINT"

    # initialize subset_curve nodes
    # node Group Output
    group_output_1 = subset_curve.nodes.new("NodeGroupOutput")
    group_output_1.name = "Group Output"
    group_output_1.is_active_output = True

    # node Group Input
    group_input_1 = subset_curve.nodes.new("NodeGroupInput")
    group_input_1.name = "Group Input"

    # node Sample Index
    sample_index = subset_curve.nodes.new("GeometryNodeSampleIndex")
    sample_index.name = "Sample Index"
    sample_index.clamp = False
    sample_index.data_type = "INT"
    sample_index.domain = "POINT"
    # Index
    sample_index.inputs[2].default_value = 0

    # node Repeat Input
    repeat_input = subset_curve.nodes.new("GeometryNodeRepeatInput")
    repeat_input.name = "Repeat Input"
    # node Repeat Output
    repeat_output = subset_curve.nodes.new("GeometryNodeRepeatOutput")
    repeat_output.name = "Repeat Output"
    repeat_output.active_index = 2
    repeat_output.inspection_index = 0
    repeat_output.repeat_items.clear()
    # Create item "Geometry"
    repeat_output.repeat_items.new("GEOMETRY", "Geometry")
    # Create item "Iterations"
    repeat_output.repeat_items.new("INT", "Iterations")
    # Create item "Geometry.001"
    repeat_output.repeat_items.new("GEOMETRY", "Geometry.001")

    # node Math
    math = subset_curve.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = "ADD"
    math.use_clamp = False
    # Value_001
    math.inputs[1].default_value = 1.0

    # node Separate Geometry
    separate_geometry = subset_curve.nodes.new("GeometryNodeSeparateGeometry")
    separate_geometry.name = "Separate Geometry"
    separate_geometry.domain = "POINT"

    # node Compare.001
    compare_001 = subset_curve.nodes.new("FunctionNodeCompare")
    compare_001.name = "Compare.001"
    compare_001.data_type = "INT"
    compare_001.mode = "ELEMENT"
    compare_001.operation = "EQUAL"

    # node Switch
    switch = subset_curve.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.input_type = "GEOMETRY"

    # node Attribute Statistic
    attribute_statistic = subset_curve.nodes.new("GeometryNodeAttributeStatistic")
    attribute_statistic.name = "Attribute Statistic"
    attribute_statistic.data_type = "FLOAT"
    attribute_statistic.domain = "POINT"
    # Selection
    attribute_statistic.inputs[1].default_value = True

    # node Compare.002
    compare_002 = subset_curve.nodes.new("FunctionNodeCompare")
    compare_002.name = "Compare.002"
    compare_002.data_type = "FLOAT"
    compare_002.mode = "ELEMENT"
    compare_002.operation = "GREATER_THAN"
    # B
    compare_002.inputs[1].default_value = 0.0

    # node Join Geometry
    join_geometry = subset_curve.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"

    # node Mesh Island
    mesh_island = subset_curve.nodes.new("GeometryNodeInputMeshIsland")
    mesh_island.name = "Mesh Island"

    # node Mesh Island.001
    mesh_island_001 = subset_curve.nodes.new("GeometryNodeInputMeshIsland")
    mesh_island_001.name = "Mesh Island.001"

    # node Reroute
    reroute_1 = subset_curve.nodes.new("NodeReroute")
    reroute_1.name = "Reroute"
    # node Reroute.001
    reroute_001_1 = subset_curve.nodes.new("NodeReroute")
    reroute_001_1.name = "Reroute.001"
    # node Reroute.002
    reroute_002_1 = subset_curve.nodes.new("NodeReroute")
    reroute_002_1.name = "Reroute.002"
    # node Reroute.003
    reroute_003_1 = subset_curve.nodes.new("NodeReroute")
    reroute_003_1.name = "Reroute.003"
    # node Reroute.004
    reroute_004_1 = subset_curve.nodes.new("NodeReroute")
    reroute_004_1.name = "Reroute.004"
    # node Reroute.005
    reroute_005_1 = subset_curve.nodes.new("NodeReroute")
    reroute_005_1.name = "Reroute.005"
    # node Reroute.006
    reroute_006_1 = subset_curve.nodes.new("NodeReroute")
    reroute_006_1.name = "Reroute.006"
    # node Reroute.007
    reroute_007 = subset_curve.nodes.new("NodeReroute")
    reroute_007.name = "Reroute.007"
    # node Reroute.008
    reroute_008 = subset_curve.nodes.new("NodeReroute")
    reroute_008.name = "Reroute.008"
    # node Reroute.009
    reroute_009 = subset_curve.nodes.new("NodeReroute")
    reroute_009.name = "Reroute.009"
    # node Reroute.010
    reroute_010 = subset_curve.nodes.new("NodeReroute")
    reroute_010.name = "Reroute.010"

    # Process zone input Repeat Input
    repeat_input.pair_with_output(repeat_output)
    # Item_1
    repeat_input.inputs[2].default_value = 0

    # Set locations
    group_output_1.location = (889.79345703125, 329.216552734375)
    group_input_1.location = (-1185.20654296875, -36.283447265625)
    sample_index.location = (-982.70654296875, 206.716552734375)
    repeat_input.location = (-792.70654296875, 85.216552734375)
    repeat_output.location = (699.79345703125, 329.216552734375)
    math.location = (497.29345703125, 329.216552734375)
    separate_geometry.location = (-325.20654296875, 172.216552734375)
    compare_001.location = (-540.20654296875, -286.783447265625)
    switch.location = (282.29345703125, 172.216552734375)
    attribute_statistic.location = (-110.20654296875, 143.216552734375)
    compare_002.location = (79.79345703125, 143.216552734375)
    join_geometry.location = (497.29345703125, -13.783447265625)
    mesh_island.location = (-792.70654296875, -542.783447265625)
    mesh_island_001.location = (-1185.20654296875, 206.716552734375)
    reroute_1.location = (-842.70654296875, -71.283447265625)
    reroute_001_1.location = (-982.70654296875, -484.783447265625)
    reroute_002_1.location = (-185.20654296875, -484.783447265625)
    reroute_003_1.location = (-540.20654296875, 387.216552734375)
    reroute_004_1.location = (-400.20654296875, 387.216552734375)
    reroute_005_1.location = (-540.20654296875, 220.716552734375)
    reroute_006_1.location = (-540.20654296875, -228.783447265625)
    reroute_007.location = (422.29345703125, -228.783447265625)
    reroute_008.location = (637.29345703125, 387.216552734375)
    reroute_009.location = (-110.20654296875, 201.216552734375)
    reroute_010.location = (219.79345703125, 201.216552734375)

    # Set dimensions
    group_output_1.width, group_output_1.height = 140.0, 100.0
    group_input_1.width, group_input_1.height = 140.0, 100.0
    sample_index.width, sample_index.height = 140.0, 100.0
    repeat_input.width, repeat_input.height = 140.0, 100.0
    repeat_output.width, repeat_output.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0
    separate_geometry.width, separate_geometry.height = 140.0, 100.0
    compare_001.width, compare_001.height = 140.0, 100.0
    switch.width, switch.height = 140.0, 100.0
    attribute_statistic.width, attribute_statistic.height = 140.0, 100.0
    compare_002.width, compare_002.height = 140.0, 100.0
    join_geometry.width, join_geometry.height = 140.0, 100.0
    mesh_island.width, mesh_island.height = 140.0, 100.0
    mesh_island_001.width, mesh_island_001.height = 140.0, 100.0
    reroute_1.width, reroute_1.height = 16.0, 100.0
    reroute_001_1.width, reroute_001_1.height = 16.0, 100.0
    reroute_002_1.width, reroute_002_1.height = 16.0, 100.0
    reroute_003_1.width, reroute_003_1.height = 16.0, 100.0
    reroute_004_1.width, reroute_004_1.height = 16.0, 100.0
    reroute_005_1.width, reroute_005_1.height = 16.0, 100.0
    reroute_006_1.width, reroute_006_1.height = 16.0, 100.0
    reroute_007.width, reroute_007.height = 16.0, 100.0
    reroute_008.width, reroute_008.height = 16.0, 100.0
    reroute_009.width, reroute_009.height = 16.0, 100.0
    reroute_010.width, reroute_010.height = 16.0, 100.0

    # initialize subset_curve links
    # join_geometry.Geometry -> repeat_output.Geometry.001
    subset_curve.links.new(join_geometry.outputs[0], repeat_output.inputs[2])
    # sample_index.Value -> repeat_input.Iterations
    subset_curve.links.new(sample_index.outputs[0], repeat_input.inputs[0])
    # attribute_statistic.Mean -> compare_002.A
    subset_curve.links.new(attribute_statistic.outputs[0], compare_002.inputs[0])
    # math.Value -> repeat_output.Iterations
    subset_curve.links.new(math.outputs[0], repeat_output.inputs[1])
    # switch.Output -> join_geometry.Geometry
    subset_curve.links.new(switch.outputs[0], join_geometry.inputs[0])
    # compare_001.Result -> separate_geometry.Selection
    subset_curve.links.new(compare_001.outputs[0], separate_geometry.inputs[1])
    # compare_002.Result -> switch.Switch
    subset_curve.links.new(compare_002.outputs[0], switch.inputs[0])
    # repeat_input.Iterations -> compare_001.A
    subset_curve.links.new(repeat_input.outputs[1], compare_001.inputs[2])
    # separate_geometry.Selection -> attribute_statistic.Geometry
    subset_curve.links.new(separate_geometry.outputs[0], attribute_statistic.inputs[0])
    # group_input_1.Geometry -> sample_index.Geometry
    subset_curve.links.new(group_input_1.outputs[0], sample_index.inputs[0])
    # mesh_island.Island Index -> compare_001.B
    subset_curve.links.new(mesh_island.outputs[0], compare_001.inputs[3])
    # mesh_island_001.Island Count -> sample_index.Value
    subset_curve.links.new(mesh_island_001.outputs[1], sample_index.inputs[1])
    # repeat_output.Geometry.001 -> group_output_1.Output
    subset_curve.links.new(repeat_output.outputs[2], group_output_1.inputs[0])
    # group_input_1.Geometry -> reroute_1.Input
    subset_curve.links.new(group_input_1.outputs[0], reroute_1.inputs[0])
    # reroute_1.Output -> repeat_input.Geometry
    subset_curve.links.new(reroute_1.outputs[0], repeat_input.inputs[1])
    # group_input_1.not_to_be_deleted -> reroute_001_1.Input
    subset_curve.links.new(group_input_1.outputs[1], reroute_001_1.inputs[0])
    # reroute_001_1.Output -> reroute_002_1.Input
    subset_curve.links.new(reroute_001_1.outputs[0], reroute_002_1.inputs[0])
    # reroute_002_1.Output -> attribute_statistic.Attribute
    subset_curve.links.new(reroute_002_1.outputs[0], attribute_statistic.inputs[2])
    # repeat_input.Geometry -> reroute_003_1.Input
    subset_curve.links.new(repeat_input.outputs[0], reroute_003_1.inputs[0])
    # reroute_003_1.Output -> reroute_004_1.Input
    subset_curve.links.new(reroute_003_1.outputs[0], reroute_004_1.inputs[0])
    # reroute_004_1.Output -> separate_geometry.Geometry
    subset_curve.links.new(reroute_004_1.outputs[0], separate_geometry.inputs[0])
    # repeat_input.Iterations -> reroute_005_1.Input
    subset_curve.links.new(repeat_input.outputs[1], reroute_005_1.inputs[0])
    # reroute_005_1.Output -> math.Value
    subset_curve.links.new(reroute_005_1.outputs[0], math.inputs[0])
    # repeat_input.Geometry.001 -> reroute_006_1.Input
    subset_curve.links.new(repeat_input.outputs[2], reroute_006_1.inputs[0])
    # reroute_006_1.Output -> reroute_007.Input
    subset_curve.links.new(reroute_006_1.outputs[0], reroute_007.inputs[0])
    # reroute_004_1.Output -> reroute_008.Input
    subset_curve.links.new(reroute_004_1.outputs[0], reroute_008.inputs[0])
    # reroute_008.Output -> repeat_output.Geometry
    subset_curve.links.new(reroute_008.outputs[0], repeat_output.inputs[0])
    # separate_geometry.Selection -> reroute_009.Input
    subset_curve.links.new(separate_geometry.outputs[0], reroute_009.inputs[0])
    # reroute_009.Output -> reroute_010.Input
    subset_curve.links.new(reroute_009.outputs[0], reroute_010.inputs[0])
    # reroute_010.Output -> switch.True
    subset_curve.links.new(reroute_010.outputs[0], switch.inputs[2])
    # reroute_007.Output -> join_geometry.Geometry
    subset_curve.links.new(reroute_007.outputs[0], join_geometry.inputs[0])
    return subset_curve


# initialize pattern_generator node group
def pattern_generator_node_group():
    name = "Pattern Generator inside"
    while True:
        if node_group_name_exists(name, "GEOMETRY"):
            name = "Pattern Generator insde" + str(random.randint(0, 1000))
        else:
            pattern_generator = bpy.data.node_groups.new(
                type="GeometryNodeTree", name=name
            )
            break
    pattern_generator.color_tag = "NONE"
    pattern_generator.description = ""

    # pattern_generator interface
    # Socket Geometry
    geometry_socket_2 = pattern_generator.interface.new_socket(
        name="Geometry", in_out="OUTPUT", socket_type="NodeSocketGeometry"
    )
    geometry_socket_2.attribute_domain = "POINT"

    # Panel Size and Shape
    size_and_shape_panel = pattern_generator.interface.new_panel(
        "Size and Shape", default_closed=True
    )
    # Socket Count
    count_socket = pattern_generator.interface.new_socket(
        name="Count",
        in_out="INPUT",
        socket_type="NodeSocketInt",
        parent=size_and_shape_panel,
    )
    count_socket.default_value = 12
    count_socket.min_value = 1
    count_socket.max_value = 2147483647
    count_socket.subtype = "NONE"
    count_socket.attribute_domain = "POINT"

    # Socket Size X
    size_x_socket = pattern_generator.interface.new_socket(
        name="Size X",
        in_out="INPUT",
        socket_type="NodeSocketInt",
        parent=size_and_shape_panel,
    )
    size_x_socket.default_value = 12
    size_x_socket.min_value = -2147483648
    size_x_socket.max_value = 2147483647
    size_x_socket.subtype = "NONE"
    size_x_socket.attribute_domain = "POINT"

    # Socket Size Y
    size_y_socket = pattern_generator.interface.new_socket(
        name="Size Y",
        in_out="INPUT",
        socket_type="NodeSocketInt",
        parent=size_and_shape_panel,
    )
    size_y_socket.default_value = 12
    size_y_socket.min_value = -2147483648
    size_y_socket.max_value = 2147483647
    size_y_socket.subtype = "NONE"
    size_y_socket.attribute_domain = "POINT"

    # Socket Offset
    offset_socket = pattern_generator.interface.new_socket(
        name="Offset",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=size_and_shape_panel,
    )
    offset_socket.default_value = 0.8299999833106995
    offset_socket.min_value = -10000.0
    offset_socket.max_value = 10000.0
    offset_socket.subtype = "NONE"
    offset_socket.attribute_domain = "POINT"

    # Socket Seed
    seed_socket_1 = pattern_generator.interface.new_socket(
        name="Seed",
        in_out="INPUT",
        socket_type="NodeSocketInt",
        parent=size_and_shape_panel,
    )
    seed_socket_1.default_value = 2
    seed_socket_1.min_value = -10000
    seed_socket_1.max_value = 10000
    seed_socket_1.subtype = "NONE"
    seed_socket_1.attribute_domain = "POINT"

    # Socket Grain
    grain_socket = pattern_generator.interface.new_socket(
        name="Grain",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=size_and_shape_panel,
    )
    grain_socket.default_value = 0.5899990200996399
    grain_socket.min_value = 0.0
    grain_socket.max_value = 1.0
    grain_socket.subtype = "NONE"
    grain_socket.attribute_domain = "POINT"

    # Socket Rotation Random
    rotation_random_socket = pattern_generator.interface.new_socket(
        name="Rotation Random",
        in_out="INPUT",
        socket_type="NodeSocketBool",
        parent=size_and_shape_panel,
    )
    rotation_random_socket.default_value = False
    rotation_random_socket.attribute_domain = "POINT"

    # Socket Rotation
    rotation_socket = pattern_generator.interface.new_socket(
        name="Rotation",
        in_out="INPUT",
        socket_type="NodeSocketInt",
        parent=size_and_shape_panel,
    )
    rotation_socket.default_value = 0
    rotation_socket.min_value = -2147483648
    rotation_socket.max_value = 2147483647
    rotation_socket.subtype = "NONE"
    rotation_socket.attribute_domain = "POINT"

    # Panel Curves
    curves_panel = pattern_generator.interface.new_panel("Curves", default_closed=True)
    # Socket Resolution of Tubes
    resolution_of_tubes_socket = pattern_generator.interface.new_socket(
        name="Resolution of Tubes",
        in_out="INPUT",
        socket_type="NodeSocketInt",
        parent=curves_panel,
    )
    resolution_of_tubes_socket.default_value = 32
    resolution_of_tubes_socket.min_value = 2
    resolution_of_tubes_socket.max_value = 512
    resolution_of_tubes_socket.subtype = "NONE"
    resolution_of_tubes_socket.attribute_domain = "POINT"

    # Socket 1st Curve Segments
    _1st_curve_segments_socket = pattern_generator.interface.new_socket(
        name="1st Curve Segments",
        in_out="INPUT",
        socket_type="NodeSocketInt",
        parent=curves_panel,
    )
    _1st_curve_segments_socket.default_value = 10
    _1st_curve_segments_socket.min_value = 1
    _1st_curve_segments_socket.max_value = 100000
    _1st_curve_segments_socket.subtype = "NONE"
    _1st_curve_segments_socket.attribute_domain = "POINT"

    # Socket 2nd Curve Segements
    _2nd_curve_segements_socket = pattern_generator.interface.new_socket(
        name="2nd Curve Segements",
        in_out="INPUT",
        socket_type="NodeSocketInt",
        parent=curves_panel,
    )
    _2nd_curve_segements_socket.default_value = 10
    _2nd_curve_segements_socket.min_value = 1
    _2nd_curve_segements_socket.max_value = 100000
    _2nd_curve_segements_socket.subtype = "NONE"
    _2nd_curve_segements_socket.attribute_domain = "POINT"

    # Socket Radius of Tubes
    radius_of_tubes_socket = pattern_generator.interface.new_socket(
        name="Radius of Tubes",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=curves_panel,
    )
    radius_of_tubes_socket.default_value = 0.009999999776482582
    radius_of_tubes_socket.min_value = 0.0
    radius_of_tubes_socket.max_value = 3.4028234663852886e38
    radius_of_tubes_socket.subtype = "DISTANCE"
    radius_of_tubes_socket.attribute_domain = "POINT"

    # Panel Curve Trimming
    curve_trimming_panel = pattern_generator.interface.new_panel(
        "Curve Trimming", default_closed=True
    )
    # Socket Random Portion
    random_portion_socket = pattern_generator.interface.new_socket(
        name="Random Portion",
        in_out="INPUT",
        socket_type="NodeSocketBool",
        parent=curve_trimming_panel,
    )
    random_portion_socket.default_value = False
    random_portion_socket.attribute_domain = "POINT"

    # Socket True Random Portion
    true_random_portion_socket = pattern_generator.interface.new_socket(
        name="True Random Portion",
        in_out="INPUT",
        socket_type="NodeSocketBool",
        parent=curve_trimming_panel,
    )
    true_random_portion_socket.default_value = False
    true_random_portion_socket.attribute_domain = "POINT"

    # Socket Every Section
    every_section_socket = pattern_generator.interface.new_socket(
        name="Every Section",
        in_out="INPUT",
        socket_type="NodeSocketBool",
        parent=curve_trimming_panel,
    )
    every_section_socket.default_value = False
    every_section_socket.attribute_domain = "POINT"

    # Socket Seed - Triming
    seed___triming_socket = pattern_generator.interface.new_socket(
        name="Seed - Triming",
        in_out="INPUT",
        socket_type="NodeSocketInt",
        parent=curve_trimming_panel,
    )
    seed___triming_socket.default_value = 0
    seed___triming_socket.min_value = -10000
    seed___triming_socket.max_value = 10000
    seed___triming_socket.subtype = "NONE"
    seed___triming_socket.attribute_domain = "POINT"

    # Socket Trim - Portion
    trim___portion_socket = pattern_generator.interface.new_socket(
        name="Trim - Portion",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=curve_trimming_panel,
    )
    trim___portion_socket.default_value = 0.5
    trim___portion_socket.min_value = 0.0
    trim___portion_socket.max_value = 1.0
    trim___portion_socket.subtype = "FACTOR"
    trim___portion_socket.attribute_domain = "POINT"

    # Socket From Start
    from_start_socket = pattern_generator.interface.new_socket(
        name="From Start",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=curve_trimming_panel,
    )
    from_start_socket.default_value = 0.0
    from_start_socket.min_value = 0.0
    from_start_socket.max_value = 1.0
    from_start_socket.subtype = "FACTOR"
    from_start_socket.attribute_domain = "POINT"

    # Socket From End
    from_end_socket = pattern_generator.interface.new_socket(
        name="From End",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=curve_trimming_panel,
    )
    from_end_socket.default_value = 1.0
    from_end_socket.min_value = 0.0
    from_end_socket.max_value = 1.0
    from_end_socket.subtype = "FACTOR"
    from_end_socket.attribute_domain = "POINT"

    # Panel Merge
    merge_panel = pattern_generator.interface.new_panel("Merge")
    # Socket Merge Probability
    merge_probability_socket = pattern_generator.interface.new_socket(
        name="Merge Probability",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=merge_panel,
    )
    merge_probability_socket.default_value = 0.0
    merge_probability_socket.min_value = 0.0
    merge_probability_socket.max_value = 1.0
    merge_probability_socket.subtype = "FACTOR"
    merge_probability_socket.attribute_domain = "POINT"

    # Socket Merge Seed
    merge_seed_socket = pattern_generator.interface.new_socket(
        name="Merge Seed",
        in_out="INPUT",
        socket_type="NodeSocketInt",
        parent=merge_panel,
    )
    merge_seed_socket.default_value = 0
    merge_seed_socket.min_value = -2147483648
    merge_seed_socket.max_value = 2147483647
    merge_seed_socket.subtype = "NONE"
    merge_seed_socket.attribute_domain = "POINT"

    # Socket Merge Distance
    merge_distance_socket = pattern_generator.interface.new_socket(
        name="Merge Distance",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=merge_panel,
    )
    merge_distance_socket.default_value = 0.0010000000474974513
    merge_distance_socket.min_value = 9.999999747378752e-05
    merge_distance_socket.max_value = 3.4028234663852886e38
    merge_distance_socket.subtype = "NONE"
    merge_distance_socket.attribute_domain = "POINT"

    # Panel Custom Mode
    custom_mode_panel = pattern_generator.interface.new_panel("Custom Mode")
    # Socket Mode
    mode_socket = pattern_generator.interface.new_socket(
        name="Mode",
        in_out="INPUT",
        socket_type="NodeSocketString",
        parent=custom_mode_panel,
    )
    mode_socket.default_value = ""
    mode_socket.attribute_domain = "POINT"

    # Socket Method
    method_socket = pattern_generator.interface.new_socket(
        name="Method",
        in_out="INPUT",
        socket_type="NodeSocketString",
        parent=custom_mode_panel,
    )
    method_socket.default_value = ""
    method_socket.attribute_domain = "POINT"

    # Socket String
    string_socket = pattern_generator.interface.new_socket(
        name="String",
        in_out="INPUT",
        socket_type="NodeSocketString",
        parent=custom_mode_panel,
    )
    string_socket.default_value = "Neon"
    string_socket.attribute_domain = "POINT"

    # Socket String Size
    string_size_socket = pattern_generator.interface.new_socket(
        name="String Size",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=custom_mode_panel,
    )
    string_size_socket.default_value = 0.0
    string_size_socket.min_value = -3.4028234663852886e38
    string_size_socket.max_value = 3.4028234663852886e38
    string_size_socket.subtype = "NONE"
    string_size_socket.attribute_domain = "POINT"

    # Socket Gap Between Characters
    gap_between_characters_socket = pattern_generator.interface.new_socket(
        name="Gap Between Characters",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=custom_mode_panel,
    )
    gap_between_characters_socket.default_value = 1.0
    gap_between_characters_socket.min_value = -3.4028234663852886e38
    gap_between_characters_socket.max_value = 3.4028234663852886e38
    gap_between_characters_socket.subtype = "NONE"
    gap_between_characters_socket.attribute_domain = "POINT"

    # Socket Scale
    scale_socket = pattern_generator.interface.new_socket(
        name="Scale",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=custom_mode_panel,
    )
    scale_socket.default_value = 1.0
    scale_socket.min_value = 0.0
    scale_socket.max_value = 3.4028234663852886e38
    scale_socket.subtype = "NONE"
    scale_socket.attribute_domain = "POINT"

    # Socket Image
    image_socket_1 = pattern_generator.interface.new_socket(
        name="Image",
        in_out="INPUT",
        socket_type="NodeSocketImage",
        parent=custom_mode_panel,
    )
    image_socket_1.attribute_domain = "POINT"

    # Socket Image Smoothness (Subdivision)
    image_smoothness__subdivision__socket = pattern_generator.interface.new_socket(
        name="Image Smoothness (Subdivision)",
        in_out="INPUT",
        socket_type="NodeSocketInt",
        parent=custom_mode_panel,
    )
    image_smoothness__subdivision__socket.default_value = 1
    image_smoothness__subdivision__socket.min_value = 0
    image_smoothness__subdivision__socket.max_value = 6
    image_smoothness__subdivision__socket.subtype = "NONE"
    image_smoothness__subdivision__socket.attribute_domain = "POINT"

    # Panel Colors
    colors_panel = pattern_generator.interface.new_panel("Colors", default_closed=True)
    # Socket Material (Curves)
    material__curves__socket = pattern_generator.interface.new_socket(
        name="Material (Curves)",
        in_out="INPUT",
        socket_type="NodeSocketMaterial",
        parent=colors_panel,
    )
    material__curves__socket.attribute_domain = "POINT"

    # Socket Emission Stenght
    emission_stenght_socket = pattern_generator.interface.new_socket(
        name="Emission Stenght",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=colors_panel,
    )
    emission_stenght_socket.default_value = 1.0
    emission_stenght_socket.min_value = 0.0
    emission_stenght_socket.max_value = 3.4028234663852886e38
    emission_stenght_socket.subtype = "NONE"
    emission_stenght_socket.attribute_domain = "POINT"

    # Socket Color Attribute
    color_attribute_socket = pattern_generator.interface.new_socket(
        name="Color Attribute",
        in_out="INPUT",
        socket_type="NodeSocketString",
        parent=colors_panel,
    )
    color_attribute_socket.default_value = "S"
    color_attribute_socket.attribute_domain = "POINT"

    # Socket Animate
    animate_socket_1 = pattern_generator.interface.new_socket(
        name="Animate",
        in_out="INPUT",
        socket_type="NodeSocketBool",
        parent=colors_panel,
    )
    animate_socket_1.default_value = False
    animate_socket_1.attribute_domain = "POINT"

    # Socket Animation Type
    animation_type_socket_1 = pattern_generator.interface.new_socket(
        name="Animation Type",
        in_out="INPUT",
        socket_type="NodeSocketString",
        parent=colors_panel,
    )
    animation_type_socket_1.default_value = ""
    animation_type_socket_1.attribute_domain = "POINT"

    # Socket Color
    color_socket_1 = pattern_generator.interface.new_socket(
        name="Color",
        in_out="INPUT",
        socket_type="NodeSocketString",
        parent=colors_panel,
    )
    color_socket_1.default_value = ""
    color_socket_1.attribute_domain = "POINT"

    # Socket Wave Motion
    wave_motion_socket_1 = pattern_generator.interface.new_socket(
        name="Wave Motion",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=colors_panel,
    )
    wave_motion_socket_1.default_value = 0.0
    wave_motion_socket_1.min_value = 0.0
    wave_motion_socket_1.max_value = 1.0
    wave_motion_socket_1.subtype = "FACTOR"
    wave_motion_socket_1.attribute_domain = "POINT"

    # Socket Seed - Colors
    seed___colors_socket = pattern_generator.interface.new_socket(
        name="Seed - Colors",
        in_out="INPUT",
        socket_type="NodeSocketInt",
        parent=colors_panel,
    )
    seed___colors_socket.default_value = 0
    seed___colors_socket.min_value = -2147483648
    seed___colors_socket.max_value = 2147483647
    seed___colors_socket.subtype = "NONE"
    seed___colors_socket.attribute_domain = "POINT"

    # Socket Speed
    speed_socket_1 = pattern_generator.interface.new_socket(
        name="Speed", in_out="INPUT", socket_type="NodeSocketFloat", parent=colors_panel
    )
    speed_socket_1.default_value = 5.0
    speed_socket_1.min_value = 0.0
    speed_socket_1.max_value = 3.4028234663852886e38
    speed_socket_1.subtype = "NONE"
    speed_socket_1.attribute_domain = "POINT"

    # Socket Color Distribution
    color_distribution_socket = pattern_generator.interface.new_socket(
        name="Color Distribution",
        in_out="INPUT",
        socket_type="NodeSocketMenu",
        parent=colors_panel,
    )
    color_distribution_socket.attribute_domain = "POINT"

    # Socket Blackness
    blackness_socket_1 = pattern_generator.interface.new_socket(
        name="Blackness",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=colors_panel,
    )
    blackness_socket_1.default_value = 0.25
    blackness_socket_1.min_value = 0.0
    blackness_socket_1.max_value = 1.0
    blackness_socket_1.subtype = "FACTOR"
    blackness_socket_1.attribute_domain = "POINT"

    # Socket Use Image Texture
    use_image_texture_socket = pattern_generator.interface.new_socket(
        name="Use Image Texture",
        in_out="INPUT",
        socket_type="NodeSocketBool",
        parent=colors_panel,
    )
    use_image_texture_socket.default_value = False
    use_image_texture_socket.attribute_domain = "POINT"

    # Socket Image
    image_socket_2 = pattern_generator.interface.new_socket(
        name="Image", in_out="INPUT", socket_type="NodeSocketImage", parent=colors_panel
    )
    image_socket_2.attribute_domain = "POINT"

    # Socket Custom Colors
    custom_colors_socket = pattern_generator.interface.new_socket(
        name="Custom Colors",
        in_out="INPUT",
        socket_type="NodeSocketBool",
        parent=colors_panel,
    )
    custom_colors_socket.default_value = False
    custom_colors_socket.attribute_domain = "POINT"

    # Socket Color 1
    color_1_socket_1 = pattern_generator.interface.new_socket(
        name="Color 1",
        in_out="INPUT",
        socket_type="NodeSocketColor",
        parent=colors_panel,
    )
    color_1_socket_1.default_value = (0.0, 0.0, 0.0, 1.0)
    color_1_socket_1.attribute_domain = "POINT"

    # Socket Color 2
    color_2_socket_1 = pattern_generator.interface.new_socket(
        name="Color 2",
        in_out="INPUT",
        socket_type="NodeSocketColor",
        parent=colors_panel,
    )
    color_2_socket_1.default_value = (0.0, 0.0, 0.0, 1.0)
    color_2_socket_1.attribute_domain = "POINT"

    # Socket Color 3
    color_3_socket_1 = pattern_generator.interface.new_socket(
        name="Color 3",
        in_out="INPUT",
        socket_type="NodeSocketColor",
        parent=colors_panel,
    )
    color_3_socket_1.default_value = (0.0, 0.0, 0.0, 1.0)
    color_3_socket_1.attribute_domain = "POINT"

    # Socket Color 4
    color_4_socket_1 = pattern_generator.interface.new_socket(
        name="Color 4",
        in_out="INPUT",
        socket_type="NodeSocketColor",
        parent=colors_panel,
    )
    color_4_socket_1.default_value = (0.0, 0.0, 0.0, 1.0)
    color_4_socket_1.attribute_domain = "POINT"

    # Panel As Prop (Wall Hanging)
    as_prop__wall_hanging__panel = pattern_generator.interface.new_panel(
        "As Prop (Wall Hanging)", default_closed=True
    )
    # Socket Prop
    prop_socket = pattern_generator.interface.new_socket(
        name="Prop",
        in_out="INPUT",
        socket_type="NodeSocketBool",
        parent=as_prop__wall_hanging__panel,
    )
    prop_socket.default_value = False
    prop_socket.attribute_domain = "POINT"

    # Socket Seed
    seed_socket_2 = pattern_generator.interface.new_socket(
        name="Seed",
        in_out="INPUT",
        socket_type="NodeSocketInt",
        parent=as_prop__wall_hanging__panel,
    )
    seed_socket_2.default_value = 2
    seed_socket_2.min_value = -10000
    seed_socket_2.max_value = 10000
    seed_socket_2.subtype = "NONE"
    seed_socket_2.attribute_domain = "POINT"

    # Socket Material (Hangers)
    material__hangers__socket = pattern_generator.interface.new_socket(
        name="Material (Hangers)",
        in_out="INPUT",
        socket_type="NodeSocketMaterial",
        parent=as_prop__wall_hanging__panel,
    )
    material__hangers__socket.attribute_domain = "POINT"

    # Socket Distance
    distance_socket = pattern_generator.interface.new_socket(
        name="Distance",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=as_prop__wall_hanging__panel,
    )
    distance_socket.default_value = 0.0
    distance_socket.min_value = 0.0
    distance_socket.max_value = 3.4028234663852886e38
    distance_socket.subtype = "DISTANCE"
    distance_socket.attribute_domain = "POINT"

    # Socket Radius (Comparing)
    radius__comparing__socket = pattern_generator.interface.new_socket(
        name="Radius (Comparing)",
        in_out="INPUT",
        socket_type="NodeSocketFloat",
        parent=as_prop__wall_hanging__panel,
    )
    radius__comparing__socket.default_value = 100.0
    radius__comparing__socket.min_value = 0.0
    radius__comparing__socket.max_value = 100.0
    radius__comparing__socket.subtype = "PERCENTAGE"
    radius__comparing__socket.attribute_domain = "POINT"

    # Socket Have Back Plate
    have_back_plate_socket = pattern_generator.interface.new_socket(
        name="Have Back Plate",
        in_out="INPUT",
        socket_type="NodeSocketBool",
        parent=as_prop__wall_hanging__panel,
    )
    have_back_plate_socket.default_value = False
    have_back_plate_socket.attribute_domain = "POINT"

    # Socket Material (Back Plate)
    material__back_plate__socket = pattern_generator.interface.new_socket(
        name="Material (Back Plate)",
        in_out="INPUT",
        socket_type="NodeSocketMaterial",
        parent=as_prop__wall_hanging__panel,
    )
    material__back_plate__socket.attribute_domain = "POINT"

    # Panel Custom Mode More
    custom_mode_more_panel = pattern_generator.interface.new_panel("Custom Mode More")
    # Socket Subset
    subset_socket_1 = pattern_generator.interface.new_socket(
        name="Subset",
        in_out="INPUT",
        socket_type="NodeSocketBool",
        parent=custom_mode_more_panel,
    )
    subset_socket_1.default_value = False
    subset_socket_1.attribute_domain = "POINT"

    # Socket Outside
    outside_socket = pattern_generator.interface.new_socket(
        name="Outside",
        in_out="INPUT",
        socket_type="NodeSocketBool",
        parent=custom_mode_more_panel,
    )
    outside_socket.default_value = False
    outside_socket.attribute_domain = "POINT"

    # Socket Both Outside and Inside
    both_outside_and_inside_socket = pattern_generator.interface.new_socket(
        name="Both Outside and Inside",
        in_out="INPUT",
        socket_type="NodeSocketBool",
        parent=custom_mode_more_panel,
    )
    both_outside_and_inside_socket.default_value = False
    both_outside_and_inside_socket.attribute_domain = "POINT"

    # initialize pattern_generator nodes
    # node Group Input
    group_input_3 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_3.name = "Group Input"
    group_input_3.outputs[0].hide = True
    group_input_3.outputs[3].hide = True
    group_input_3.outputs[4].hide = True
    group_input_3.outputs[5].hide = True
    group_input_3.outputs[6].hide = True
    group_input_3.outputs[7].hide = True
    group_input_3.outputs[8].hide = True
    group_input_3.outputs[9].hide = True
    group_input_3.outputs[10].hide = True
    group_input_3.outputs[11].hide = True
    group_input_3.outputs[12].hide = True
    group_input_3.outputs[13].hide = True
    group_input_3.outputs[14].hide = True
    group_input_3.outputs[15].hide = True
    group_input_3.outputs[16].hide = True
    group_input_3.outputs[17].hide = True
    group_input_3.outputs[18].hide = True
    group_input_3.outputs[19].hide = True
    group_input_3.outputs[20].hide = True
    group_input_3.outputs[21].hide = True
    group_input_3.outputs[22].hide = True
    group_input_3.outputs[23].hide = True
    group_input_3.outputs[24].hide = True
    group_input_3.outputs[25].hide = True
    group_input_3.outputs[26].hide = True
    group_input_3.outputs[27].hide = True
    group_input_3.outputs[28].hide = True
    group_input_3.outputs[29].hide = True
    group_input_3.outputs[30].hide = True
    group_input_3.outputs[31].hide = True
    group_input_3.outputs[32].hide = True
    group_input_3.outputs[33].hide = True
    group_input_3.outputs[34].hide = True
    group_input_3.outputs[35].hide = True
    group_input_3.outputs[36].hide = True
    group_input_3.outputs[37].hide = True
    group_input_3.outputs[38].hide = True
    group_input_3.outputs[39].hide = True
    group_input_3.outputs[40].hide = True
    group_input_3.outputs[41].hide = True
    group_input_3.outputs[42].hide = True
    group_input_3.outputs[43].hide = True
    group_input_3.outputs[44].hide = True
    group_input_3.outputs[45].hide = True
    group_input_3.outputs[46].hide = True
    group_input_3.outputs[47].hide = True
    group_input_3.outputs[48].hide = True
    group_input_3.outputs[49].hide = True
    group_input_3.outputs[50].hide = True
    group_input_3.outputs[51].hide = True
    group_input_3.outputs[52].hide = True
    group_input_3.outputs[53].hide = True
    group_input_3.outputs[54].hide = True
    group_input_3.outputs[55].hide = True
    group_input_3.outputs[56].hide = True
    group_input_3.outputs[57].hide = True
    group_input_3.outputs[58].hide = True

    # node Set Material
    set_material = pattern_generator.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    set_material.inputs[1].hide = True
    # Selection
    set_material.inputs[1].default_value = True

    # node Arc
    arc = pattern_generator.nodes.new("GeometryNodeCurveArc")
    arc.name = "Arc"
    arc.mode = "RADIUS"
    arc.inputs[1].hide = True
    arc.inputs[2].hide = True
    arc.inputs[3].hide = True
    arc.inputs[4].hide = True
    arc.inputs[5].hide = True
    arc.inputs[6].hide = True
    arc.inputs[7].hide = True
    arc.inputs[8].hide = True
    arc.inputs[9].hide = True
    arc.outputs[1].hide = True
    arc.outputs[2].hide = True
    arc.outputs[3].hide = True
    # Radius
    arc.inputs[4].default_value = 1.0
    # Start Angle
    arc.inputs[5].default_value = 0.0
    # Sweep Angle
    arc.inputs[6].default_value = 1.5707963705062866
    # Connect Center
    arc.inputs[8].default_value = False
    # Invert Arc
    arc.inputs[9].default_value = False

    # node Instance on Points
    instance_on_points = pattern_generator.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points.name = "Instance on Points"
    instance_on_points.inputs[1].hide = True
    instance_on_points.inputs[3].hide = True
    instance_on_points.inputs[4].hide = True
    instance_on_points.inputs[5].hide = True
    # Selection
    instance_on_points.inputs[1].default_value = True
    # Pick Instance
    instance_on_points.inputs[3].default_value = False
    # Instance Index
    instance_on_points.inputs[4].default_value = 0
    # Rotation
    instance_on_points.inputs[5].default_value = (0.0, 0.0, 0.0)

    # node Points
    points = pattern_generator.nodes.new("GeometryNodePoints")
    points.name = "Points"
    points.inputs[1].hide = True
    points.inputs[2].hide = True
    # Position
    points.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Radius
    points.inputs[2].default_value = 0.09999999403953552

    # node Index
    index_1 = pattern_generator.nodes.new("GeometryNodeInputIndex")
    index_1.name = "Index"

    # node Map Range
    map_range_1 = pattern_generator.nodes.new("ShaderNodeMapRange")
    map_range_1.name = "Map Range"
    map_range_1.clamp = True
    map_range_1.data_type = "FLOAT"
    map_range_1.interpolation_type = "LINEAR"
    map_range_1.inputs[1].hide = True
    map_range_1.inputs[5].hide = True
    map_range_1.inputs[6].hide = True
    map_range_1.inputs[7].hide = True
    map_range_1.inputs[8].hide = True
    map_range_1.inputs[9].hide = True
    map_range_1.inputs[10].hide = True
    map_range_1.inputs[11].hide = True
    map_range_1.outputs[1].hide = True
    # From Min
    map_range_1.inputs[1].default_value = 1.0

    # node Math
    math_2 = pattern_generator.nodes.new("ShaderNodeMath")
    math_2.name = "Math"
    math_2.operation = "SUBTRACT"
    math_2.use_clamp = False
    math_2.inputs[1].hide = True
    math_2.inputs[2].hide = True
    # Value_001
    math_2.inputs[1].default_value = 1.0

    # node Transform Geometry
    transform_geometry = pattern_generator.nodes.new("GeometryNodeTransform")
    transform_geometry.name = "Transform Geometry"
    transform_geometry.mode = "COMPONENTS"
    transform_geometry.inputs[1].hide = True
    transform_geometry.inputs[2].hide = True
    transform_geometry.inputs[3].hide = True
    transform_geometry.inputs[4].hide = True
    # Translation
    transform_geometry.inputs[1].default_value = (1.0, 1.0, 0.0)
    # Rotation
    transform_geometry.inputs[2].default_value = (0.0, 0.0, 3.1415927410125732)
    # Scale
    transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)

    # node Join Geometry
    join_geometry_1 = pattern_generator.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_1.name = "Join Geometry"

    # node Grid
    grid = pattern_generator.nodes.new("GeometryNodeMeshGrid")
    grid.name = "Grid"
    grid.outputs[1].hide = True

    # node Instance on Points.001
    instance_on_points_001 = pattern_generator.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_001.name = "Instance on Points.001"
    instance_on_points_001.inputs[1].hide = True
    instance_on_points_001.inputs[3].hide = True
    instance_on_points_001.inputs[4].hide = True
    instance_on_points_001.inputs[5].hide = True
    instance_on_points_001.inputs[6].hide = True
    # Selection
    instance_on_points_001.inputs[1].default_value = True
    # Pick Instance
    instance_on_points_001.inputs[3].default_value = False
    # Instance Index
    instance_on_points_001.inputs[4].default_value = 0
    # Rotation
    instance_on_points_001.inputs[5].default_value = (0.0, 0.0, 0.0)
    # Scale
    instance_on_points_001.inputs[6].default_value = (1.0, 1.0, 1.0)

    # node Math.001
    math_001_1 = pattern_generator.nodes.new("ShaderNodeMath")
    math_001_1.name = "Math.001"
    math_001_1.operation = "ADD"
    math_001_1.use_clamp = False
    math_001_1.inputs[1].hide = True
    math_001_1.inputs[2].hide = True
    # Value_001
    math_001_1.inputs[1].default_value = 1.0

    # node Transform Geometry.001
    transform_geometry_001 = pattern_generator.nodes.new("GeometryNodeTransform")
    transform_geometry_001.name = "Transform Geometry.001"
    transform_geometry_001.mode = "COMPONENTS"
    transform_geometry_001.inputs[1].hide = True
    transform_geometry_001.inputs[2].hide = True
    transform_geometry_001.inputs[3].hide = True
    transform_geometry_001.inputs[4].hide = True
    # Translation
    transform_geometry_001.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Rotation
    transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)

    # node Math.002
    math_002_1 = pattern_generator.nodes.new("ShaderNodeMath")
    math_002_1.name = "Math.002"
    math_002_1.operation = "SUBTRACT"
    math_002_1.use_clamp = False
    math_002_1.inputs[0].hide = True
    math_002_1.inputs[2].hide = True
    # Value
    math_002_1.inputs[0].default_value = 1.0

    # node Realize Instances
    realize_instances = pattern_generator.nodes.new("GeometryNodeRealizeInstances")
    realize_instances.name = "Realize Instances"
    realize_instances.inputs[1].hide = True
    realize_instances.inputs[2].hide = True
    realize_instances.inputs[3].hide = True
    # Selection
    realize_instances.inputs[1].default_value = True
    # Realize All
    realize_instances.inputs[2].default_value = True
    # Depth
    realize_instances.inputs[3].default_value = 0

    # node Curve to Mesh
    curve_to_mesh = pattern_generator.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh.name = "Curve to Mesh"
    curve_to_mesh.inputs[1].hide = True
    curve_to_mesh.inputs[2].hide = True
    # Fill Caps
    curve_to_mesh.inputs[2].default_value = False

    # node Delete Geometry
    delete_geometry = pattern_generator.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry.name = "Delete Geometry"
    delete_geometry.domain = "POINT"
    delete_geometry.mode = "ALL"

    # node Position
    position_1 = pattern_generator.nodes.new("GeometryNodeInputPosition")
    position_1.name = "Position"

    # node Vector Math
    vector_math = pattern_generator.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = "LENGTH"
    vector_math.inputs[1].hide = True
    vector_math.inputs[2].hide = True
    vector_math.inputs[3].hide = True
    vector_math.outputs[0].hide = True

    # node Compare
    compare_1 = pattern_generator.nodes.new("FunctionNodeCompare")
    compare_1.name = "Compare"
    compare_1.data_type = "FLOAT"
    compare_1.mode = "ELEMENT"
    compare_1.operation = "LESS_THAN"
    compare_1.inputs[2].hide = True
    compare_1.inputs[3].hide = True
    compare_1.inputs[4].hide = True
    compare_1.inputs[5].hide = True
    compare_1.inputs[6].hide = True
    compare_1.inputs[7].hide = True
    compare_1.inputs[8].hide = True
    compare_1.inputs[9].hide = True
    compare_1.inputs[10].hide = True
    compare_1.inputs[11].hide = True
    compare_1.inputs[12].hide = True

    # node Math.003
    math_003_1 = pattern_generator.nodes.new("ShaderNodeMath")
    math_003_1.name = "Math.003"
    math_003_1.operation = "ADD"
    math_003_1.use_clamp = True
    math_003_1.inputs[2].hide = True

    # node Rotate Instances
    rotate_instances = pattern_generator.nodes.new("GeometryNodeRotateInstances")
    rotate_instances.name = "Rotate Instances"
    rotate_instances.inputs[1].hide = True
    rotate_instances.inputs[3].hide = True
    rotate_instances.inputs[4].hide = True
    # Selection
    rotate_instances.inputs[1].default_value = True
    # Pivot Point
    rotate_instances.inputs[3].default_value = (0.5, 0.5, 0.0)
    # Local Space
    rotate_instances.inputs[4].default_value = True

    # node Math.004
    math_004_1 = pattern_generator.nodes.new("ShaderNodeMath")
    math_004_1.name = "Math.004"
    math_004_1.operation = "MULTIPLY"
    math_004_1.use_clamp = False
    math_004_1.inputs[0].hide = True
    math_004_1.inputs[2].hide = True
    # Value
    math_004_1.inputs[0].default_value = 1.5707963705062866

    # node Random Value.001
    random_value_001_1 = pattern_generator.nodes.new("FunctionNodeRandomValue")
    random_value_001_1.name = "Random Value.001"
    random_value_001_1.data_type = "INT"
    random_value_001_1.inputs[0].hide = True
    random_value_001_1.inputs[1].hide = True
    random_value_001_1.inputs[2].hide = True
    random_value_001_1.inputs[3].hide = True
    random_value_001_1.inputs[4].hide = True
    random_value_001_1.inputs[5].hide = True
    random_value_001_1.inputs[6].hide = True
    random_value_001_1.inputs[7].hide = True
    random_value_001_1.outputs[0].hide = True
    random_value_001_1.outputs[1].hide = True
    random_value_001_1.outputs[3].hide = True
    # Min_002
    random_value_001_1.inputs[4].default_value = 0
    # Max_002
    random_value_001_1.inputs[5].default_value = 100
    # ID
    random_value_001_1.inputs[7].default_value = 0

    # node Combine XYZ
    combine_xyz = pattern_generator.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    combine_xyz.inputs[0].hide = True
    combine_xyz.inputs[1].hide = True
    # X
    combine_xyz.inputs[0].default_value = 0.0
    # Y
    combine_xyz.inputs[1].default_value = 0.0

    # node Curve Circle
    curve_circle = pattern_generator.nodes.new("GeometryNodeCurvePrimitiveCircle")
    curve_circle.name = "Curve Circle"
    curve_circle.mode = "RADIUS"
    curve_circle.inputs[1].hide = True
    curve_circle.inputs[2].hide = True
    curve_circle.inputs[3].hide = True
    curve_circle.outputs[1].hide = True

    # node Curve to Mesh.001
    curve_to_mesh_001 = pattern_generator.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh_001.name = "Curve to Mesh.001"
    curve_to_mesh_001.inputs[2].hide = True
    # Fill Caps
    curve_to_mesh_001.inputs[2].default_value = True

    # node Mesh to Curve
    mesh_to_curve = pattern_generator.nodes.new("GeometryNodeMeshToCurve")
    mesh_to_curve.name = "Mesh to Curve"
    mesh_to_curve.inputs[1].hide = True
    # Selection
    mesh_to_curve.inputs[1].default_value = True

    # node Realize Instances.001
    realize_instances_001 = pattern_generator.nodes.new("GeometryNodeRealizeInstances")
    realize_instances_001.name = "Realize Instances.001"
    realize_instances_001.inputs[1].hide = True
    realize_instances_001.inputs[2].hide = True
    realize_instances_001.inputs[3].hide = True
    # Selection
    realize_instances_001.inputs[1].default_value = True
    # Realize All
    realize_instances_001.inputs[2].default_value = True
    # Depth
    realize_instances_001.inputs[3].default_value = 0

    # node Curve to Mesh.002
    curve_to_mesh_002 = pattern_generator.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh_002.name = "Curve to Mesh.002"
    curve_to_mesh_002.inputs[1].hide = True
    curve_to_mesh_002.inputs[2].hide = True
    # Fill Caps
    curve_to_mesh_002.inputs[2].default_value = False

    # node Resample Curve
    resample_curve = pattern_generator.nodes.new("GeometryNodeResampleCurve")
    resample_curve.name = "Resample Curve"
    resample_curve.mode = "COUNT"
    resample_curve.inputs[1].hide = True
    resample_curve.inputs[3].hide = True
    # Selection
    resample_curve.inputs[1].default_value = True

    # node Resample Curve.001
    resample_curve_001 = pattern_generator.nodes.new("GeometryNodeResampleCurve")
    resample_curve_001.name = "Resample Curve.001"
    resample_curve_001.mode = "COUNT"
    resample_curve_001.inputs[1].hide = True
    resample_curve_001.inputs[3].hide = True
    # Selection
    resample_curve_001.inputs[1].default_value = True

    # node Group Input.004
    group_input_004_1 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_004_1.name = "Group Input.004"
    group_input_004_1.outputs[0].hide = True
    group_input_004_1.outputs[1].hide = True
    group_input_004_1.outputs[2].hide = True
    group_input_004_1.outputs[3].hide = True
    group_input_004_1.outputs[4].hide = True
    group_input_004_1.outputs[6].hide = True
    group_input_004_1.outputs[7].hide = True
    group_input_004_1.outputs[8].hide = True
    group_input_004_1.outputs[9].hide = True
    group_input_004_1.outputs[10].hide = True
    group_input_004_1.outputs[11].hide = True
    group_input_004_1.outputs[12].hide = True
    group_input_004_1.outputs[13].hide = True
    group_input_004_1.outputs[14].hide = True
    group_input_004_1.outputs[15].hide = True
    group_input_004_1.outputs[16].hide = True
    group_input_004_1.outputs[17].hide = True
    group_input_004_1.outputs[18].hide = True
    group_input_004_1.outputs[19].hide = True
    group_input_004_1.outputs[20].hide = True
    group_input_004_1.outputs[21].hide = True
    group_input_004_1.outputs[22].hide = True
    group_input_004_1.outputs[23].hide = True
    group_input_004_1.outputs[24].hide = True
    group_input_004_1.outputs[25].hide = True
    group_input_004_1.outputs[26].hide = True
    group_input_004_1.outputs[27].hide = True
    group_input_004_1.outputs[28].hide = True
    group_input_004_1.outputs[29].hide = True
    group_input_004_1.outputs[30].hide = True
    group_input_004_1.outputs[31].hide = True
    group_input_004_1.outputs[32].hide = True
    group_input_004_1.outputs[33].hide = True
    group_input_004_1.outputs[34].hide = True
    group_input_004_1.outputs[35].hide = True
    group_input_004_1.outputs[36].hide = True
    group_input_004_1.outputs[37].hide = True
    group_input_004_1.outputs[38].hide = True
    group_input_004_1.outputs[39].hide = True
    group_input_004_1.outputs[40].hide = True
    group_input_004_1.outputs[41].hide = True
    group_input_004_1.outputs[42].hide = True
    group_input_004_1.outputs[43].hide = True
    group_input_004_1.outputs[44].hide = True
    group_input_004_1.outputs[45].hide = True
    group_input_004_1.outputs[46].hide = True
    group_input_004_1.outputs[47].hide = True
    group_input_004_1.outputs[48].hide = True
    group_input_004_1.outputs[49].hide = True
    group_input_004_1.outputs[50].hide = True
    group_input_004_1.outputs[51].hide = True
    group_input_004_1.outputs[52].hide = True
    group_input_004_1.outputs[53].hide = True
    group_input_004_1.outputs[54].hide = True
    group_input_004_1.outputs[55].hide = True
    group_input_004_1.outputs[56].hide = True
    group_input_004_1.outputs[57].hide = True
    group_input_004_1.outputs[58].hide = True

    # node Group Input.005
    group_input_005_1 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_005_1.name = "Group Input.005"
    group_input_005_1.outputs[1].hide = True
    group_input_005_1.outputs[2].hide = True
    group_input_005_1.outputs[3].hide = True
    group_input_005_1.outputs[4].hide = True
    group_input_005_1.outputs[5].hide = True
    group_input_005_1.outputs[6].hide = True
    group_input_005_1.outputs[7].hide = True
    group_input_005_1.outputs[8].hide = True
    group_input_005_1.outputs[9].hide = True
    group_input_005_1.outputs[10].hide = True
    group_input_005_1.outputs[11].hide = True
    group_input_005_1.outputs[12].hide = True
    group_input_005_1.outputs[13].hide = True
    group_input_005_1.outputs[14].hide = True
    group_input_005_1.outputs[15].hide = True
    group_input_005_1.outputs[16].hide = True
    group_input_005_1.outputs[17].hide = True
    group_input_005_1.outputs[18].hide = True
    group_input_005_1.outputs[19].hide = True
    group_input_005_1.outputs[20].hide = True
    group_input_005_1.outputs[21].hide = True
    group_input_005_1.outputs[22].hide = True
    group_input_005_1.outputs[23].hide = True
    group_input_005_1.outputs[24].hide = True
    group_input_005_1.outputs[25].hide = True
    group_input_005_1.outputs[26].hide = True
    group_input_005_1.outputs[27].hide = True
    group_input_005_1.outputs[28].hide = True
    group_input_005_1.outputs[29].hide = True
    group_input_005_1.outputs[30].hide = True
    group_input_005_1.outputs[31].hide = True
    group_input_005_1.outputs[32].hide = True
    group_input_005_1.outputs[33].hide = True
    group_input_005_1.outputs[34].hide = True
    group_input_005_1.outputs[35].hide = True
    group_input_005_1.outputs[36].hide = True
    group_input_005_1.outputs[37].hide = True
    group_input_005_1.outputs[38].hide = True
    group_input_005_1.outputs[39].hide = True
    group_input_005_1.outputs[40].hide = True
    group_input_005_1.outputs[41].hide = True
    group_input_005_1.outputs[42].hide = True
    group_input_005_1.outputs[43].hide = True
    group_input_005_1.outputs[44].hide = True
    group_input_005_1.outputs[45].hide = True
    group_input_005_1.outputs[46].hide = True
    group_input_005_1.outputs[47].hide = True
    group_input_005_1.outputs[48].hide = True
    group_input_005_1.outputs[49].hide = True
    group_input_005_1.outputs[50].hide = True
    group_input_005_1.outputs[51].hide = True
    group_input_005_1.outputs[52].hide = True
    group_input_005_1.outputs[53].hide = True
    group_input_005_1.outputs[54].hide = True
    group_input_005_1.outputs[55].hide = True
    group_input_005_1.outputs[56].hide = True
    group_input_005_1.outputs[57].hide = True
    group_input_005_1.outputs[58].hide = True

    # node Group Input.006
    group_input_006_1 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_006_1.name = "Group Input.006"
    group_input_006_1.outputs[0].hide = True
    group_input_006_1.outputs[1].hide = True
    group_input_006_1.outputs[2].hide = True
    group_input_006_1.outputs[3].hide = True
    group_input_006_1.outputs[4].hide = True
    group_input_006_1.outputs[5].hide = True
    group_input_006_1.outputs[6].hide = True
    group_input_006_1.outputs[7].hide = True
    group_input_006_1.outputs[9].hide = True
    group_input_006_1.outputs[10].hide = True
    group_input_006_1.outputs[11].hide = True
    group_input_006_1.outputs[12].hide = True
    group_input_006_1.outputs[13].hide = True
    group_input_006_1.outputs[14].hide = True
    group_input_006_1.outputs[15].hide = True
    group_input_006_1.outputs[16].hide = True
    group_input_006_1.outputs[17].hide = True
    group_input_006_1.outputs[18].hide = True
    group_input_006_1.outputs[19].hide = True
    group_input_006_1.outputs[20].hide = True
    group_input_006_1.outputs[21].hide = True
    group_input_006_1.outputs[22].hide = True
    group_input_006_1.outputs[23].hide = True
    group_input_006_1.outputs[24].hide = True
    group_input_006_1.outputs[25].hide = True
    group_input_006_1.outputs[26].hide = True
    group_input_006_1.outputs[27].hide = True
    group_input_006_1.outputs[28].hide = True
    group_input_006_1.outputs[29].hide = True
    group_input_006_1.outputs[30].hide = True
    group_input_006_1.outputs[31].hide = True
    group_input_006_1.outputs[32].hide = True
    group_input_006_1.outputs[33].hide = True
    group_input_006_1.outputs[34].hide = True
    group_input_006_1.outputs[35].hide = True
    group_input_006_1.outputs[36].hide = True
    group_input_006_1.outputs[37].hide = True
    group_input_006_1.outputs[38].hide = True
    group_input_006_1.outputs[39].hide = True
    group_input_006_1.outputs[40].hide = True
    group_input_006_1.outputs[41].hide = True
    group_input_006_1.outputs[42].hide = True
    group_input_006_1.outputs[43].hide = True
    group_input_006_1.outputs[44].hide = True
    group_input_006_1.outputs[45].hide = True
    group_input_006_1.outputs[46].hide = True
    group_input_006_1.outputs[47].hide = True
    group_input_006_1.outputs[48].hide = True
    group_input_006_1.outputs[49].hide = True
    group_input_006_1.outputs[50].hide = True
    group_input_006_1.outputs[51].hide = True
    group_input_006_1.outputs[52].hide = True
    group_input_006_1.outputs[53].hide = True
    group_input_006_1.outputs[54].hide = True
    group_input_006_1.outputs[55].hide = True
    group_input_006_1.outputs[56].hide = True
    group_input_006_1.outputs[57].hide = True
    group_input_006_1.outputs[58].hide = True

    # node Group Input.007
    group_input_007_1 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_007_1.name = "Group Input.007"
    group_input_007_1.outputs[0].hide = True
    group_input_007_1.outputs[1].hide = True
    group_input_007_1.outputs[2].hide = True
    group_input_007_1.outputs[4].hide = True
    group_input_007_1.outputs[5].hide = True
    group_input_007_1.outputs[6].hide = True
    group_input_007_1.outputs[7].hide = True
    group_input_007_1.outputs[8].hide = True
    group_input_007_1.outputs[9].hide = True
    group_input_007_1.outputs[10].hide = True
    group_input_007_1.outputs[11].hide = True
    group_input_007_1.outputs[12].hide = True
    group_input_007_1.outputs[13].hide = True
    group_input_007_1.outputs[14].hide = True
    group_input_007_1.outputs[15].hide = True
    group_input_007_1.outputs[16].hide = True
    group_input_007_1.outputs[17].hide = True
    group_input_007_1.outputs[18].hide = True
    group_input_007_1.outputs[19].hide = True
    group_input_007_1.outputs[20].hide = True
    group_input_007_1.outputs[21].hide = True
    group_input_007_1.outputs[22].hide = True
    group_input_007_1.outputs[23].hide = True
    group_input_007_1.outputs[24].hide = True
    group_input_007_1.outputs[25].hide = True
    group_input_007_1.outputs[26].hide = True
    group_input_007_1.outputs[27].hide = True
    group_input_007_1.outputs[28].hide = True
    group_input_007_1.outputs[29].hide = True
    group_input_007_1.outputs[30].hide = True
    group_input_007_1.outputs[31].hide = True
    group_input_007_1.outputs[32].hide = True
    group_input_007_1.outputs[33].hide = True
    group_input_007_1.outputs[34].hide = True
    group_input_007_1.outputs[35].hide = True
    group_input_007_1.outputs[36].hide = True
    group_input_007_1.outputs[37].hide = True
    group_input_007_1.outputs[38].hide = True
    group_input_007_1.outputs[39].hide = True
    group_input_007_1.outputs[40].hide = True
    group_input_007_1.outputs[41].hide = True
    group_input_007_1.outputs[42].hide = True
    group_input_007_1.outputs[43].hide = True
    group_input_007_1.outputs[44].hide = True
    group_input_007_1.outputs[45].hide = True
    group_input_007_1.outputs[46].hide = True
    group_input_007_1.outputs[47].hide = True
    group_input_007_1.outputs[48].hide = True
    group_input_007_1.outputs[49].hide = True
    group_input_007_1.outputs[50].hide = True
    group_input_007_1.outputs[51].hide = True
    group_input_007_1.outputs[52].hide = True
    group_input_007_1.outputs[53].hide = True
    group_input_007_1.outputs[54].hide = True
    group_input_007_1.outputs[55].hide = True
    group_input_007_1.outputs[56].hide = True
    group_input_007_1.outputs[57].hide = True
    group_input_007_1.outputs[58].hide = True

    # node Group Input.008
    group_input_008_1 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_008_1.name = "Group Input.008"
    group_input_008_1.outputs[0].hide = True
    group_input_008_1.outputs[1].hide = True
    group_input_008_1.outputs[2].hide = True
    group_input_008_1.outputs[4].hide = True
    group_input_008_1.outputs[5].hide = True
    group_input_008_1.outputs[6].hide = True
    group_input_008_1.outputs[7].hide = True
    group_input_008_1.outputs[8].hide = True
    group_input_008_1.outputs[9].hide = True
    group_input_008_1.outputs[10].hide = True
    group_input_008_1.outputs[11].hide = True
    group_input_008_1.outputs[12].hide = True
    group_input_008_1.outputs[13].hide = True
    group_input_008_1.outputs[14].hide = True
    group_input_008_1.outputs[15].hide = True
    group_input_008_1.outputs[16].hide = True
    group_input_008_1.outputs[17].hide = True
    group_input_008_1.outputs[18].hide = True
    group_input_008_1.outputs[19].hide = True
    group_input_008_1.outputs[20].hide = True
    group_input_008_1.outputs[21].hide = True
    group_input_008_1.outputs[22].hide = True
    group_input_008_1.outputs[23].hide = True
    group_input_008_1.outputs[24].hide = True
    group_input_008_1.outputs[25].hide = True
    group_input_008_1.outputs[26].hide = True
    group_input_008_1.outputs[27].hide = True
    group_input_008_1.outputs[28].hide = True
    group_input_008_1.outputs[29].hide = True
    group_input_008_1.outputs[30].hide = True
    group_input_008_1.outputs[31].hide = True
    group_input_008_1.outputs[32].hide = True
    group_input_008_1.outputs[33].hide = True
    group_input_008_1.outputs[34].hide = True
    group_input_008_1.outputs[35].hide = True
    group_input_008_1.outputs[36].hide = True
    group_input_008_1.outputs[37].hide = True
    group_input_008_1.outputs[38].hide = True
    group_input_008_1.outputs[39].hide = True
    group_input_008_1.outputs[40].hide = True
    group_input_008_1.outputs[41].hide = True
    group_input_008_1.outputs[42].hide = True
    group_input_008_1.outputs[43].hide = True
    group_input_008_1.outputs[44].hide = True
    group_input_008_1.outputs[45].hide = True
    group_input_008_1.outputs[46].hide = True
    group_input_008_1.outputs[47].hide = True
    group_input_008_1.outputs[48].hide = True
    group_input_008_1.outputs[49].hide = True
    group_input_008_1.outputs[50].hide = True
    group_input_008_1.outputs[51].hide = True
    group_input_008_1.outputs[52].hide = True
    group_input_008_1.outputs[53].hide = True
    group_input_008_1.outputs[54].hide = True
    group_input_008_1.outputs[55].hide = True
    group_input_008_1.outputs[56].hide = True
    group_input_008_1.outputs[57].hide = True
    group_input_008_1.outputs[58].hide = True

    # node Group Input.009
    group_input_009_1 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_009_1.name = "Group Input.009"
    group_input_009_1.outputs[0].hide = True
    group_input_009_1.outputs[1].hide = True
    group_input_009_1.outputs[2].hide = True
    group_input_009_1.outputs[3].hide = True
    group_input_009_1.outputs[5].hide = True
    group_input_009_1.outputs[6].hide = True
    group_input_009_1.outputs[7].hide = True
    group_input_009_1.outputs[8].hide = True
    group_input_009_1.outputs[9].hide = True
    group_input_009_1.outputs[10].hide = True
    group_input_009_1.outputs[11].hide = True
    group_input_009_1.outputs[12].hide = True
    group_input_009_1.outputs[13].hide = True
    group_input_009_1.outputs[14].hide = True
    group_input_009_1.outputs[15].hide = True
    group_input_009_1.outputs[16].hide = True
    group_input_009_1.outputs[17].hide = True
    group_input_009_1.outputs[18].hide = True
    group_input_009_1.outputs[19].hide = True
    group_input_009_1.outputs[20].hide = True
    group_input_009_1.outputs[21].hide = True
    group_input_009_1.outputs[22].hide = True
    group_input_009_1.outputs[23].hide = True
    group_input_009_1.outputs[24].hide = True
    group_input_009_1.outputs[25].hide = True
    group_input_009_1.outputs[26].hide = True
    group_input_009_1.outputs[27].hide = True
    group_input_009_1.outputs[28].hide = True
    group_input_009_1.outputs[29].hide = True
    group_input_009_1.outputs[30].hide = True
    group_input_009_1.outputs[31].hide = True
    group_input_009_1.outputs[32].hide = True
    group_input_009_1.outputs[33].hide = True
    group_input_009_1.outputs[34].hide = True
    group_input_009_1.outputs[35].hide = True
    group_input_009_1.outputs[36].hide = True
    group_input_009_1.outputs[37].hide = True
    group_input_009_1.outputs[38].hide = True
    group_input_009_1.outputs[39].hide = True
    group_input_009_1.outputs[40].hide = True
    group_input_009_1.outputs[41].hide = True
    group_input_009_1.outputs[42].hide = True
    group_input_009_1.outputs[43].hide = True
    group_input_009_1.outputs[44].hide = True
    group_input_009_1.outputs[45].hide = True
    group_input_009_1.outputs[46].hide = True
    group_input_009_1.outputs[47].hide = True
    group_input_009_1.outputs[48].hide = True
    group_input_009_1.outputs[49].hide = True
    group_input_009_1.outputs[50].hide = True
    group_input_009_1.outputs[51].hide = True
    group_input_009_1.outputs[52].hide = True
    group_input_009_1.outputs[53].hide = True
    group_input_009_1.outputs[54].hide = True
    group_input_009_1.outputs[55].hide = True
    group_input_009_1.outputs[56].hide = True
    group_input_009_1.outputs[57].hide = True
    group_input_009_1.outputs[58].hide = True

    # node Group Input.010
    group_input_010_1 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_010_1.name = "Group Input.010"
    group_input_010_1.outputs[0].hide = True
    group_input_010_1.outputs[1].hide = True
    group_input_010_1.outputs[2].hide = True
    group_input_010_1.outputs[3].hide = True
    group_input_010_1.outputs[4].hide = True
    group_input_010_1.outputs[5].hide = True
    group_input_010_1.outputs[6].hide = True
    group_input_010_1.outputs[7].hide = True
    group_input_010_1.outputs[9].hide = True
    group_input_010_1.outputs[10].hide = True
    group_input_010_1.outputs[12].hide = True
    group_input_010_1.outputs[13].hide = True
    group_input_010_1.outputs[14].hide = True
    group_input_010_1.outputs[15].hide = True
    group_input_010_1.outputs[16].hide = True
    group_input_010_1.outputs[17].hide = True
    group_input_010_1.outputs[18].hide = True
    group_input_010_1.outputs[19].hide = True
    group_input_010_1.outputs[20].hide = True
    group_input_010_1.outputs[21].hide = True
    group_input_010_1.outputs[22].hide = True
    group_input_010_1.outputs[23].hide = True
    group_input_010_1.outputs[24].hide = True
    group_input_010_1.outputs[25].hide = True
    group_input_010_1.outputs[26].hide = True
    group_input_010_1.outputs[27].hide = True
    group_input_010_1.outputs[28].hide = True
    group_input_010_1.outputs[29].hide = True
    group_input_010_1.outputs[30].hide = True
    group_input_010_1.outputs[31].hide = True
    group_input_010_1.outputs[32].hide = True
    group_input_010_1.outputs[33].hide = True
    group_input_010_1.outputs[34].hide = True
    group_input_010_1.outputs[35].hide = True
    group_input_010_1.outputs[36].hide = True
    group_input_010_1.outputs[37].hide = True
    group_input_010_1.outputs[38].hide = True
    group_input_010_1.outputs[39].hide = True
    group_input_010_1.outputs[40].hide = True
    group_input_010_1.outputs[41].hide = True
    group_input_010_1.outputs[42].hide = True
    group_input_010_1.outputs[43].hide = True
    group_input_010_1.outputs[44].hide = True
    group_input_010_1.outputs[45].hide = True
    group_input_010_1.outputs[46].hide = True
    group_input_010_1.outputs[47].hide = True
    group_input_010_1.outputs[48].hide = True
    group_input_010_1.outputs[49].hide = True
    group_input_010_1.outputs[50].hide = True
    group_input_010_1.outputs[51].hide = True
    group_input_010_1.outputs[52].hide = True
    group_input_010_1.outputs[53].hide = True
    group_input_010_1.outputs[54].hide = True
    group_input_010_1.outputs[55].hide = True
    group_input_010_1.outputs[56].hide = True
    group_input_010_1.outputs[57].hide = True
    group_input_010_1.outputs[58].hide = True

    # node Group Input.011
    group_input_011_1 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_011_1.name = "Group Input.011"
    group_input_011_1.outputs[0].hide = True
    group_input_011_1.outputs[1].hide = True
    group_input_011_1.outputs[2].hide = True
    group_input_011_1.outputs[3].hide = True
    group_input_011_1.outputs[4].hide = True
    group_input_011_1.outputs[5].hide = True
    group_input_011_1.outputs[6].hide = True
    group_input_011_1.outputs[7].hide = True
    group_input_011_1.outputs[8].hide = True
    group_input_011_1.outputs[9].hide = True
    group_input_011_1.outputs[11].hide = True
    group_input_011_1.outputs[12].hide = True
    group_input_011_1.outputs[13].hide = True
    group_input_011_1.outputs[14].hide = True
    group_input_011_1.outputs[15].hide = True
    group_input_011_1.outputs[16].hide = True
    group_input_011_1.outputs[17].hide = True
    group_input_011_1.outputs[18].hide = True
    group_input_011_1.outputs[19].hide = True
    group_input_011_1.outputs[20].hide = True
    group_input_011_1.outputs[21].hide = True
    group_input_011_1.outputs[22].hide = True
    group_input_011_1.outputs[23].hide = True
    group_input_011_1.outputs[24].hide = True
    group_input_011_1.outputs[25].hide = True
    group_input_011_1.outputs[26].hide = True
    group_input_011_1.outputs[27].hide = True
    group_input_011_1.outputs[28].hide = True
    group_input_011_1.outputs[29].hide = True
    group_input_011_1.outputs[30].hide = True
    group_input_011_1.outputs[31].hide = True
    group_input_011_1.outputs[32].hide = True
    group_input_011_1.outputs[33].hide = True
    group_input_011_1.outputs[34].hide = True
    group_input_011_1.outputs[35].hide = True
    group_input_011_1.outputs[36].hide = True
    group_input_011_1.outputs[37].hide = True
    group_input_011_1.outputs[38].hide = True
    group_input_011_1.outputs[39].hide = True
    group_input_011_1.outputs[40].hide = True
    group_input_011_1.outputs[41].hide = True
    group_input_011_1.outputs[42].hide = True
    group_input_011_1.outputs[43].hide = True
    group_input_011_1.outputs[44].hide = True
    group_input_011_1.outputs[45].hide = True
    group_input_011_1.outputs[46].hide = True
    group_input_011_1.outputs[47].hide = True
    group_input_011_1.outputs[48].hide = True
    group_input_011_1.outputs[49].hide = True
    group_input_011_1.outputs[50].hide = True
    group_input_011_1.outputs[51].hide = True
    group_input_011_1.outputs[52].hide = True
    group_input_011_1.outputs[53].hide = True
    group_input_011_1.outputs[54].hide = True
    group_input_011_1.outputs[55].hide = True
    group_input_011_1.outputs[56].hide = True
    group_input_011_1.outputs[57].hide = True
    group_input_011_1.outputs[58].hide = True

    # node Group Input.012
    group_input_012_1 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_012_1.name = "Group Input.012"
    group_input_012_1.outputs[0].hide = True
    group_input_012_1.outputs[1].hide = True
    group_input_012_1.outputs[2].hide = True
    group_input_012_1.outputs[3].hide = True
    group_input_012_1.outputs[4].hide = True
    group_input_012_1.outputs[5].hide = True
    group_input_012_1.outputs[6].hide = True
    group_input_012_1.outputs[7].hide = True
    group_input_012_1.outputs[8].hide = True
    group_input_012_1.outputs[10].hide = True
    group_input_012_1.outputs[11].hide = True
    group_input_012_1.outputs[12].hide = True
    group_input_012_1.outputs[13].hide = True
    group_input_012_1.outputs[14].hide = True
    group_input_012_1.outputs[15].hide = True
    group_input_012_1.outputs[16].hide = True
    group_input_012_1.outputs[17].hide = True
    group_input_012_1.outputs[18].hide = True
    group_input_012_1.outputs[19].hide = True
    group_input_012_1.outputs[20].hide = True
    group_input_012_1.outputs[21].hide = True
    group_input_012_1.outputs[22].hide = True
    group_input_012_1.outputs[23].hide = True
    group_input_012_1.outputs[24].hide = True
    group_input_012_1.outputs[25].hide = True
    group_input_012_1.outputs[26].hide = True
    group_input_012_1.outputs[27].hide = True
    group_input_012_1.outputs[28].hide = True
    group_input_012_1.outputs[29].hide = True
    group_input_012_1.outputs[30].hide = True
    group_input_012_1.outputs[31].hide = True
    group_input_012_1.outputs[32].hide = True
    group_input_012_1.outputs[33].hide = True
    group_input_012_1.outputs[34].hide = True
    group_input_012_1.outputs[35].hide = True
    group_input_012_1.outputs[36].hide = True
    group_input_012_1.outputs[37].hide = True
    group_input_012_1.outputs[38].hide = True
    group_input_012_1.outputs[39].hide = True
    group_input_012_1.outputs[40].hide = True
    group_input_012_1.outputs[41].hide = True
    group_input_012_1.outputs[42].hide = True
    group_input_012_1.outputs[43].hide = True
    group_input_012_1.outputs[44].hide = True
    group_input_012_1.outputs[45].hide = True
    group_input_012_1.outputs[46].hide = True
    group_input_012_1.outputs[47].hide = True
    group_input_012_1.outputs[48].hide = True
    group_input_012_1.outputs[49].hide = True
    group_input_012_1.outputs[50].hide = True
    group_input_012_1.outputs[51].hide = True
    group_input_012_1.outputs[52].hide = True
    group_input_012_1.outputs[53].hide = True
    group_input_012_1.outputs[54].hide = True
    group_input_012_1.outputs[55].hide = True
    group_input_012_1.outputs[56].hide = True
    group_input_012_1.outputs[57].hide = True
    group_input_012_1.outputs[58].hide = True

    # node Trim Curve
    trim_curve = pattern_generator.nodes.new("GeometryNodeTrimCurve")
    trim_curve.name = "Trim Curve"
    trim_curve.mode = "FACTOR"
    trim_curve.inputs[4].hide = True
    trim_curve.inputs[5].hide = True

    # node Random Value
    random_value_1 = pattern_generator.nodes.new("FunctionNodeRandomValue")
    random_value_1.name = "Random Value"
    random_value_1.data_type = "BOOLEAN"
    random_value_1.inputs[0].hide = True
    random_value_1.inputs[1].hide = True
    random_value_1.inputs[2].hide = True
    random_value_1.inputs[3].hide = True
    random_value_1.inputs[4].hide = True
    random_value_1.inputs[5].hide = True
    random_value_1.inputs[7].hide = True
    random_value_1.outputs[0].hide = True
    random_value_1.outputs[1].hide = True
    random_value_1.outputs[2].hide = True
    # ID
    random_value_1.inputs[7].default_value = 0

    # node Group Input.016
    group_input_016_1 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_016_1.name = "Group Input.016"
    group_input_016_1.outputs[0].hide = True
    group_input_016_1.outputs[1].hide = True
    group_input_016_1.outputs[2].hide = True
    group_input_016_1.outputs[3].hide = True
    group_input_016_1.outputs[4].hide = True
    group_input_016_1.outputs[5].hide = True
    group_input_016_1.outputs[6].hide = True
    group_input_016_1.outputs[7].hide = True
    group_input_016_1.outputs[8].hide = True
    group_input_016_1.outputs[9].hide = True
    group_input_016_1.outputs[10].hide = True
    group_input_016_1.outputs[11].hide = True
    group_input_016_1.outputs[12].hide = True
    group_input_016_1.outputs[13].hide = True
    group_input_016_1.outputs[14].hide = True
    group_input_016_1.outputs[17].hide = True
    group_input_016_1.outputs[18].hide = True
    group_input_016_1.outputs[19].hide = True
    group_input_016_1.outputs[20].hide = True
    group_input_016_1.outputs[21].hide = True
    group_input_016_1.outputs[22].hide = True
    group_input_016_1.outputs[23].hide = True
    group_input_016_1.outputs[24].hide = True
    group_input_016_1.outputs[25].hide = True
    group_input_016_1.outputs[26].hide = True
    group_input_016_1.outputs[27].hide = True
    group_input_016_1.outputs[28].hide = True
    group_input_016_1.outputs[29].hide = True
    group_input_016_1.outputs[30].hide = True
    group_input_016_1.outputs[31].hide = True
    group_input_016_1.outputs[32].hide = True
    group_input_016_1.outputs[33].hide = True
    group_input_016_1.outputs[34].hide = True
    group_input_016_1.outputs[35].hide = True
    group_input_016_1.outputs[36].hide = True
    group_input_016_1.outputs[37].hide = True
    group_input_016_1.outputs[38].hide = True
    group_input_016_1.outputs[39].hide = True
    group_input_016_1.outputs[40].hide = True
    group_input_016_1.outputs[41].hide = True
    group_input_016_1.outputs[42].hide = True
    group_input_016_1.outputs[43].hide = True
    group_input_016_1.outputs[44].hide = True
    group_input_016_1.outputs[45].hide = True
    group_input_016_1.outputs[46].hide = True
    group_input_016_1.outputs[47].hide = True
    group_input_016_1.outputs[48].hide = True
    group_input_016_1.outputs[49].hide = True
    group_input_016_1.outputs[50].hide = True
    group_input_016_1.outputs[51].hide = True
    group_input_016_1.outputs[52].hide = True
    group_input_016_1.outputs[53].hide = True
    group_input_016_1.outputs[54].hide = True
    group_input_016_1.outputs[55].hide = True
    group_input_016_1.outputs[56].hide = True
    group_input_016_1.outputs[57].hide = True
    group_input_016_1.outputs[58].hide = True

    # node Group Input.017
    group_input_017_1 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_017_1.name = "Group Input.017"
    group_input_017_1.outputs[0].hide = True
    group_input_017_1.outputs[1].hide = True
    group_input_017_1.outputs[2].hide = True
    group_input_017_1.outputs[3].hide = True
    group_input_017_1.outputs[4].hide = True
    group_input_017_1.outputs[5].hide = True
    group_input_017_1.outputs[6].hide = True
    group_input_017_1.outputs[7].hide = True
    group_input_017_1.outputs[8].hide = True
    group_input_017_1.outputs[9].hide = True
    group_input_017_1.outputs[10].hide = True
    group_input_017_1.outputs[11].hide = True
    group_input_017_1.outputs[12].hide = True
    group_input_017_1.outputs[13].hide = True
    group_input_017_1.outputs[14].hide = True
    group_input_017_1.outputs[15].hide = True
    group_input_017_1.outputs[16].hide = True
    group_input_017_1.outputs[19].hide = True
    group_input_017_1.outputs[20].hide = True
    group_input_017_1.outputs[21].hide = True
    group_input_017_1.outputs[22].hide = True
    group_input_017_1.outputs[23].hide = True
    group_input_017_1.outputs[24].hide = True
    group_input_017_1.outputs[25].hide = True
    group_input_017_1.outputs[26].hide = True
    group_input_017_1.outputs[27].hide = True
    group_input_017_1.outputs[28].hide = True
    group_input_017_1.outputs[29].hide = True
    group_input_017_1.outputs[30].hide = True
    group_input_017_1.outputs[31].hide = True
    group_input_017_1.outputs[32].hide = True
    group_input_017_1.outputs[33].hide = True
    group_input_017_1.outputs[34].hide = True
    group_input_017_1.outputs[35].hide = True
    group_input_017_1.outputs[36].hide = True
    group_input_017_1.outputs[37].hide = True
    group_input_017_1.outputs[38].hide = True
    group_input_017_1.outputs[39].hide = True
    group_input_017_1.outputs[40].hide = True
    group_input_017_1.outputs[41].hide = True
    group_input_017_1.outputs[42].hide = True
    group_input_017_1.outputs[43].hide = True
    group_input_017_1.outputs[44].hide = True
    group_input_017_1.outputs[45].hide = True
    group_input_017_1.outputs[46].hide = True
    group_input_017_1.outputs[47].hide = True
    group_input_017_1.outputs[48].hide = True
    group_input_017_1.outputs[49].hide = True
    group_input_017_1.outputs[50].hide = True
    group_input_017_1.outputs[51].hide = True
    group_input_017_1.outputs[52].hide = True
    group_input_017_1.outputs[53].hide = True
    group_input_017_1.outputs[54].hide = True
    group_input_017_1.outputs[55].hide = True
    group_input_017_1.outputs[56].hide = True
    group_input_017_1.outputs[57].hide = True
    group_input_017_1.outputs[58].hide = True

    # node Random Value.002
    random_value_002_1 = pattern_generator.nodes.new("FunctionNodeRandomValue")
    random_value_002_1.name = "Random Value.002"
    random_value_002_1.data_type = "FLOAT"
    random_value_002_1.inputs[0].hide = True
    random_value_002_1.inputs[1].hide = True
    random_value_002_1.inputs[2].hide = True
    random_value_002_1.inputs[3].hide = True
    random_value_002_1.inputs[4].hide = True
    random_value_002_1.inputs[5].hide = True
    random_value_002_1.inputs[7].hide = True
    random_value_002_1.outputs[0].hide = True
    random_value_002_1.outputs[2].hide = True
    random_value_002_1.outputs[3].hide = True
    # Min_001
    random_value_002_1.inputs[2].default_value = 0.0
    # Max_001
    random_value_002_1.inputs[3].default_value = 1.0
    # ID
    random_value_002_1.inputs[7].default_value = 0

    # node Math.006
    math_006_1 = pattern_generator.nodes.new("ShaderNodeMath")
    math_006_1.name = "Math.006"
    math_006_1.operation = "MULTIPLY"
    math_006_1.use_clamp = False
    math_006_1.inputs[2].hide = True

    # node Switch
    switch_2 = pattern_generator.nodes.new("GeometryNodeSwitch")
    switch_2.name = "Switch"
    switch_2.input_type = "FLOAT"

    # node Group Input.018
    group_input_018_1 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_018_1.name = "Group Input.018"
    group_input_018_1.outputs[0].hide = True
    group_input_018_1.outputs[1].hide = True
    group_input_018_1.outputs[2].hide = True
    group_input_018_1.outputs[3].hide = True
    group_input_018_1.outputs[4].hide = True
    group_input_018_1.outputs[5].hide = True
    group_input_018_1.outputs[6].hide = True
    group_input_018_1.outputs[7].hide = True
    group_input_018_1.outputs[8].hide = True
    group_input_018_1.outputs[9].hide = True
    group_input_018_1.outputs[10].hide = True
    group_input_018_1.outputs[11].hide = True
    group_input_018_1.outputs[13].hide = True
    group_input_018_1.outputs[14].hide = True
    group_input_018_1.outputs[15].hide = True
    group_input_018_1.outputs[16].hide = True
    group_input_018_1.outputs[17].hide = True
    group_input_018_1.outputs[18].hide = True
    group_input_018_1.outputs[19].hide = True
    group_input_018_1.outputs[20].hide = True
    group_input_018_1.outputs[21].hide = True
    group_input_018_1.outputs[22].hide = True
    group_input_018_1.outputs[23].hide = True
    group_input_018_1.outputs[24].hide = True
    group_input_018_1.outputs[25].hide = True
    group_input_018_1.outputs[26].hide = True
    group_input_018_1.outputs[27].hide = True
    group_input_018_1.outputs[28].hide = True
    group_input_018_1.outputs[29].hide = True
    group_input_018_1.outputs[30].hide = True
    group_input_018_1.outputs[31].hide = True
    group_input_018_1.outputs[32].hide = True
    group_input_018_1.outputs[33].hide = True
    group_input_018_1.outputs[34].hide = True
    group_input_018_1.outputs[35].hide = True
    group_input_018_1.outputs[36].hide = True
    group_input_018_1.outputs[37].hide = True
    group_input_018_1.outputs[38].hide = True
    group_input_018_1.outputs[39].hide = True
    group_input_018_1.outputs[40].hide = True
    group_input_018_1.outputs[41].hide = True
    group_input_018_1.outputs[42].hide = True
    group_input_018_1.outputs[43].hide = True
    group_input_018_1.outputs[44].hide = True
    group_input_018_1.outputs[45].hide = True
    group_input_018_1.outputs[46].hide = True
    group_input_018_1.outputs[47].hide = True
    group_input_018_1.outputs[48].hide = True
    group_input_018_1.outputs[49].hide = True
    group_input_018_1.outputs[50].hide = True
    group_input_018_1.outputs[51].hide = True
    group_input_018_1.outputs[52].hide = True
    group_input_018_1.outputs[53].hide = True
    group_input_018_1.outputs[54].hide = True
    group_input_018_1.outputs[55].hide = True
    group_input_018_1.outputs[56].hide = True
    group_input_018_1.outputs[57].hide = True
    group_input_018_1.outputs[58].hide = True

    # node Group Input.019
    group_input_019_1 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_019_1.name = "Group Input.019"
    group_input_019_1.outputs[0].hide = True
    group_input_019_1.outputs[1].hide = True
    group_input_019_1.outputs[2].hide = True
    group_input_019_1.outputs[3].hide = True
    group_input_019_1.outputs[4].hide = True
    group_input_019_1.outputs[5].hide = True
    group_input_019_1.outputs[6].hide = True
    group_input_019_1.outputs[7].hide = True
    group_input_019_1.outputs[8].hide = True
    group_input_019_1.outputs[9].hide = True
    group_input_019_1.outputs[10].hide = True
    group_input_019_1.outputs[11].hide = True
    group_input_019_1.outputs[12].hide = True
    group_input_019_1.outputs[13].hide = True
    group_input_019_1.outputs[14].hide = True
    group_input_019_1.outputs[15].hide = True
    group_input_019_1.outputs[16].hide = True
    group_input_019_1.outputs[18].hide = True
    group_input_019_1.outputs[19].hide = True
    group_input_019_1.outputs[20].hide = True
    group_input_019_1.outputs[21].hide = True
    group_input_019_1.outputs[22].hide = True
    group_input_019_1.outputs[23].hide = True
    group_input_019_1.outputs[24].hide = True
    group_input_019_1.outputs[25].hide = True
    group_input_019_1.outputs[26].hide = True
    group_input_019_1.outputs[27].hide = True
    group_input_019_1.outputs[28].hide = True
    group_input_019_1.outputs[29].hide = True
    group_input_019_1.outputs[30].hide = True
    group_input_019_1.outputs[31].hide = True
    group_input_019_1.outputs[32].hide = True
    group_input_019_1.outputs[33].hide = True
    group_input_019_1.outputs[34].hide = True
    group_input_019_1.outputs[35].hide = True
    group_input_019_1.outputs[36].hide = True
    group_input_019_1.outputs[37].hide = True
    group_input_019_1.outputs[38].hide = True
    group_input_019_1.outputs[39].hide = True
    group_input_019_1.outputs[40].hide = True
    group_input_019_1.outputs[41].hide = True
    group_input_019_1.outputs[42].hide = True
    group_input_019_1.outputs[43].hide = True
    group_input_019_1.outputs[44].hide = True
    group_input_019_1.outputs[45].hide = True
    group_input_019_1.outputs[46].hide = True
    group_input_019_1.outputs[47].hide = True
    group_input_019_1.outputs[48].hide = True
    group_input_019_1.outputs[49].hide = True
    group_input_019_1.outputs[50].hide = True
    group_input_019_1.outputs[51].hide = True
    group_input_019_1.outputs[52].hide = True
    group_input_019_1.outputs[53].hide = True
    group_input_019_1.outputs[54].hide = True
    group_input_019_1.outputs[55].hide = True
    group_input_019_1.outputs[56].hide = True
    group_input_019_1.outputs[57].hide = True
    group_input_019_1.outputs[58].hide = True

    # node Compare.001
    compare_001_2 = pattern_generator.nodes.new("FunctionNodeCompare")
    compare_001_2.name = "Compare.001"
    compare_001_2.data_type = "FLOAT"
    compare_001_2.mode = "ELEMENT"
    compare_001_2.operation = "EQUAL"
    compare_001_2.inputs[1].hide = True
    compare_001_2.inputs[2].hide = True
    compare_001_2.inputs[3].hide = True
    compare_001_2.inputs[4].hide = True
    compare_001_2.inputs[5].hide = True
    compare_001_2.inputs[6].hide = True
    compare_001_2.inputs[7].hide = True
    compare_001_2.inputs[8].hide = True
    compare_001_2.inputs[9].hide = True
    compare_001_2.inputs[10].hide = True
    compare_001_2.inputs[11].hide = True
    compare_001_2.inputs[12].hide = True
    # B
    compare_001_2.inputs[1].default_value = 0.0
    # Epsilon
    compare_001_2.inputs[12].default_value = 0.0010000000474974513

    # node Switch.001
    switch_001_1 = pattern_generator.nodes.new("GeometryNodeSwitch")
    switch_001_1.name = "Switch.001"
    switch_001_1.input_type = "GEOMETRY"

    # node Compare.002
    compare_002_2 = pattern_generator.nodes.new("FunctionNodeCompare")
    compare_002_2.name = "Compare.002"
    compare_002_2.data_type = "FLOAT"
    compare_002_2.mode = "ELEMENT"
    compare_002_2.operation = "EQUAL"
    compare_002_2.inputs[1].hide = True
    compare_002_2.inputs[2].hide = True
    compare_002_2.inputs[3].hide = True
    compare_002_2.inputs[4].hide = True
    compare_002_2.inputs[5].hide = True
    compare_002_2.inputs[6].hide = True
    compare_002_2.inputs[7].hide = True
    compare_002_2.inputs[8].hide = True
    compare_002_2.inputs[9].hide = True
    compare_002_2.inputs[10].hide = True
    compare_002_2.inputs[11].hide = True
    compare_002_2.inputs[12].hide = True
    # B
    compare_002_2.inputs[1].default_value = 1.0
    # Epsilon
    compare_002_2.inputs[12].default_value = 0.0010000000474974513

    # node Boolean Math
    boolean_math_1 = pattern_generator.nodes.new("FunctionNodeBooleanMath")
    boolean_math_1.name = "Boolean Math"
    boolean_math_1.operation = "AND"

    # node Delete Geometry.001
    delete_geometry_001 = pattern_generator.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_001.name = "Delete Geometry.001"
    delete_geometry_001.domain = "POINT"
    delete_geometry_001.mode = "ALL"

    # node Spline Length
    spline_length = pattern_generator.nodes.new("GeometryNodeSplineLength")
    spline_length.name = "Spline Length"
    spline_length.outputs[1].hide = True

    # node Compare.003
    compare_003_1 = pattern_generator.nodes.new("FunctionNodeCompare")
    compare_003_1.name = "Compare.003"
    compare_003_1.data_type = "FLOAT"
    compare_003_1.mode = "ELEMENT"
    compare_003_1.operation = "EQUAL"
    compare_003_1.inputs[1].hide = True
    compare_003_1.inputs[2].hide = True
    compare_003_1.inputs[3].hide = True
    compare_003_1.inputs[4].hide = True
    compare_003_1.inputs[5].hide = True
    compare_003_1.inputs[6].hide = True
    compare_003_1.inputs[7].hide = True
    compare_003_1.inputs[8].hide = True
    compare_003_1.inputs[9].hide = True
    compare_003_1.inputs[10].hide = True
    compare_003_1.inputs[11].hide = True
    compare_003_1.inputs[12].hide = True
    # B
    compare_003_1.inputs[1].default_value = 0.0
    # Epsilon
    compare_003_1.inputs[12].default_value = 0.0010000000474974513

    # node Random Value.003
    random_value_003_1 = pattern_generator.nodes.new("FunctionNodeRandomValue")
    random_value_003_1.name = "Random Value.003"
    random_value_003_1.data_type = "INT"
    random_value_003_1.inputs[0].hide = True
    random_value_003_1.inputs[1].hide = True
    random_value_003_1.inputs[2].hide = True
    random_value_003_1.inputs[3].hide = True
    random_value_003_1.inputs[4].hide = True
    random_value_003_1.inputs[5].hide = True
    random_value_003_1.inputs[6].hide = True
    random_value_003_1.inputs[7].hide = True
    random_value_003_1.outputs[0].hide = True
    random_value_003_1.outputs[1].hide = True
    random_value_003_1.outputs[3].hide = True
    # Min_002
    random_value_003_1.inputs[4].default_value = 0
    # Max_002
    random_value_003_1.inputs[5].default_value = 100
    # ID
    random_value_003_1.inputs[7].default_value = 0

    # node Join Geometry.001
    join_geometry_001 = pattern_generator.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_001.name = "Join Geometry.001"

    # node Instance on Points.002
    instance_on_points_002 = pattern_generator.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_002.name = "Instance on Points.002"
    instance_on_points_002.inputs[3].hide = True
    instance_on_points_002.inputs[4].hide = True
    instance_on_points_002.inputs[5].hide = True
    instance_on_points_002.inputs[6].hide = True
    # Pick Instance
    instance_on_points_002.inputs[3].default_value = False
    # Instance Index
    instance_on_points_002.inputs[4].default_value = 0
    # Rotation
    instance_on_points_002.inputs[5].default_value = (0.0, 0.0, 0.0)
    # Scale
    instance_on_points_002.inputs[6].default_value = (1.0, 1.0, 1.0)

    # node Endpoint Selection
    endpoint_selection = pattern_generator.nodes.new(
        "GeometryNodeCurveEndpointSelection"
    )
    endpoint_selection.name = "Endpoint Selection"
    endpoint_selection.inputs[0].hide = True
    endpoint_selection.inputs[1].hide = True
    # Start Size
    endpoint_selection.inputs[0].default_value = 1
    # End Size
    endpoint_selection.inputs[1].default_value = 0

    # node Trim Curve.001
    trim_curve_001 = pattern_generator.nodes.new("GeometryNodeTrimCurve")
    trim_curve_001.name = "Trim Curve.001"
    trim_curve_001.mode = "FACTOR"
    trim_curve_001.inputs[1].hide = True
    trim_curve_001.inputs[3].hide = True
    trim_curve_001.inputs[4].hide = True
    trim_curve_001.inputs[5].hide = True
    # Selection
    trim_curve_001.inputs[1].default_value = True
    # End
    trim_curve_001.inputs[3].default_value = 1.0

    # node Random Value.004
    random_value_004_1 = pattern_generator.nodes.new("FunctionNodeRandomValue")
    random_value_004_1.name = "Random Value.004"
    random_value_004_1.data_type = "FLOAT"
    random_value_004_1.inputs[0].hide = True
    random_value_004_1.inputs[1].hide = True
    random_value_004_1.inputs[2].hide = True
    random_value_004_1.inputs[3].hide = True
    random_value_004_1.inputs[4].hide = True
    random_value_004_1.inputs[5].hide = True
    random_value_004_1.inputs[6].hide = True
    random_value_004_1.inputs[7].hide = True
    random_value_004_1.outputs[0].hide = True
    random_value_004_1.outputs[2].hide = True
    random_value_004_1.outputs[3].hide = True
    # Min_001
    random_value_004_1.inputs[2].default_value = 0.20000000298023224
    # Max_001
    random_value_004_1.inputs[3].default_value = 0.800000011920929
    # ID
    random_value_004_1.inputs[7].default_value = 0

    # node Curve Line
    curve_line = pattern_generator.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line.name = "Curve Line"
    curve_line.mode = "POINTS"
    curve_line.inputs[0].hide = True
    curve_line.inputs[2].hide = True
    curve_line.inputs[3].hide = True
    # Start
    curve_line.inputs[0].default_value = (0.0, 0.0, 0.0)

    # node Group Input.001
    group_input_001_1 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_001_1.name = "Group Input.001"
    group_input_001_1.outputs[0].hide = True
    group_input_001_1.outputs[1].hide = True
    group_input_001_1.outputs[2].hide = True
    group_input_001_1.outputs[3].hide = True
    group_input_001_1.outputs[4].hide = True
    group_input_001_1.outputs[5].hide = True
    group_input_001_1.outputs[6].hide = True
    group_input_001_1.outputs[7].hide = True
    group_input_001_1.outputs[8].hide = True
    group_input_001_1.outputs[9].hide = True
    group_input_001_1.outputs[10].hide = True
    group_input_001_1.outputs[11].hide = True
    group_input_001_1.outputs[12].hide = True
    group_input_001_1.outputs[13].hide = True
    group_input_001_1.outputs[14].hide = True
    group_input_001_1.outputs[15].hide = True
    group_input_001_1.outputs[16].hide = True
    group_input_001_1.outputs[17].hide = True
    group_input_001_1.outputs[18].hide = True
    group_input_001_1.outputs[19].hide = True
    group_input_001_1.outputs[20].hide = True
    group_input_001_1.outputs[21].hide = True
    group_input_001_1.outputs[22].hide = True
    group_input_001_1.outputs[23].hide = True
    group_input_001_1.outputs[24].hide = True
    group_input_001_1.outputs[25].hide = True
    group_input_001_1.outputs[26].hide = True
    group_input_001_1.outputs[27].hide = True
    group_input_001_1.outputs[28].hide = True
    group_input_001_1.outputs[29].hide = True
    group_input_001_1.outputs[30].hide = True
    group_input_001_1.outputs[31].hide = True
    group_input_001_1.outputs[32].hide = True
    group_input_001_1.outputs[33].hide = True
    group_input_001_1.outputs[34].hide = True
    group_input_001_1.outputs[35].hide = True
    group_input_001_1.outputs[36].hide = True
    group_input_001_1.outputs[37].hide = True
    group_input_001_1.outputs[38].hide = True
    group_input_001_1.outputs[39].hide = True
    group_input_001_1.outputs[40].hide = True
    group_input_001_1.outputs[41].hide = True
    group_input_001_1.outputs[42].hide = True
    group_input_001_1.outputs[43].hide = True
    group_input_001_1.outputs[44].hide = True
    group_input_001_1.outputs[45].hide = True
    group_input_001_1.outputs[46].hide = True
    group_input_001_1.outputs[47].hide = True
    group_input_001_1.outputs[48].hide = True
    group_input_001_1.outputs[49].hide = True
    group_input_001_1.outputs[50].hide = True
    group_input_001_1.outputs[52].hide = True
    group_input_001_1.outputs[53].hide = True
    group_input_001_1.outputs[54].hide = True
    group_input_001_1.outputs[55].hide = True
    group_input_001_1.outputs[56].hide = True
    group_input_001_1.outputs[57].hide = True
    group_input_001_1.outputs[58].hide = True

    # node Combine XYZ.001
    combine_xyz_001 = pattern_generator.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.name = "Combine XYZ.001"
    combine_xyz_001.inputs[0].hide = True
    combine_xyz_001.inputs[1].hide = True
    # X
    combine_xyz_001.inputs[0].default_value = 0.0
    # Y
    combine_xyz_001.inputs[1].default_value = 0.0

    # node Math.007
    math_007_1 = pattern_generator.nodes.new("ShaderNodeMath")
    math_007_1.name = "Math.007"
    math_007_1.operation = "MULTIPLY"
    math_007_1.use_clamp = False
    math_007_1.inputs[1].hide = True
    math_007_1.inputs[2].hide = True
    # Value_001
    math_007_1.inputs[1].default_value = -1.0

    # node Curve to Mesh.003
    curve_to_mesh_003 = pattern_generator.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh_003.name = "Curve to Mesh.003"
    curve_to_mesh_003.inputs[2].hide = True
    # Fill Caps
    curve_to_mesh_003.inputs[2].default_value = True

    # node Curve Circle.001
    curve_circle_001 = pattern_generator.nodes.new("GeometryNodeCurvePrimitiveCircle")
    curve_circle_001.name = "Curve Circle.001"
    curve_circle_001.mode = "RADIUS"
    curve_circle_001.inputs[0].hide = True
    curve_circle_001.inputs[1].hide = True
    curve_circle_001.inputs[2].hide = True
    curve_circle_001.inputs[3].hide = True
    curve_circle_001.outputs[1].hide = True
    # Resolution
    curve_circle_001.inputs[0].default_value = 16

    # node Group Input.003
    group_input_003_1 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_003_1.name = "Group Input.003"
    group_input_003_1.outputs[0].hide = True
    group_input_003_1.outputs[1].hide = True
    group_input_003_1.outputs[2].hide = True
    group_input_003_1.outputs[3].hide = True
    group_input_003_1.outputs[4].hide = True
    group_input_003_1.outputs[5].hide = True
    group_input_003_1.outputs[6].hide = True
    group_input_003_1.outputs[7].hide = True
    group_input_003_1.outputs[8].hide = True
    group_input_003_1.outputs[9].hide = True
    group_input_003_1.outputs[10].hide = True
    group_input_003_1.outputs[12].hide = True
    group_input_003_1.outputs[13].hide = True
    group_input_003_1.outputs[14].hide = True
    group_input_003_1.outputs[15].hide = True
    group_input_003_1.outputs[16].hide = True
    group_input_003_1.outputs[17].hide = True
    group_input_003_1.outputs[18].hide = True
    group_input_003_1.outputs[19].hide = True
    group_input_003_1.outputs[20].hide = True
    group_input_003_1.outputs[21].hide = True
    group_input_003_1.outputs[22].hide = True
    group_input_003_1.outputs[23].hide = True
    group_input_003_1.outputs[24].hide = True
    group_input_003_1.outputs[25].hide = True
    group_input_003_1.outputs[26].hide = True
    group_input_003_1.outputs[27].hide = True
    group_input_003_1.outputs[28].hide = True
    group_input_003_1.outputs[29].hide = True
    group_input_003_1.outputs[30].hide = True
    group_input_003_1.outputs[31].hide = True
    group_input_003_1.outputs[32].hide = True
    group_input_003_1.outputs[33].hide = True
    group_input_003_1.outputs[34].hide = True
    group_input_003_1.outputs[35].hide = True
    group_input_003_1.outputs[36].hide = True
    group_input_003_1.outputs[37].hide = True
    group_input_003_1.outputs[38].hide = True
    group_input_003_1.outputs[39].hide = True
    group_input_003_1.outputs[40].hide = True
    group_input_003_1.outputs[41].hide = True
    group_input_003_1.outputs[42].hide = True
    group_input_003_1.outputs[43].hide = True
    group_input_003_1.outputs[44].hide = True
    group_input_003_1.outputs[45].hide = True
    group_input_003_1.outputs[46].hide = True
    group_input_003_1.outputs[47].hide = True
    group_input_003_1.outputs[48].hide = True
    group_input_003_1.outputs[49].hide = True
    group_input_003_1.outputs[50].hide = True
    group_input_003_1.outputs[51].hide = True
    group_input_003_1.outputs[53].hide = True
    group_input_003_1.outputs[54].hide = True
    group_input_003_1.outputs[55].hide = True
    group_input_003_1.outputs[56].hide = True
    group_input_003_1.outputs[57].hide = True
    group_input_003_1.outputs[58].hide = True

    # node Math.008
    math_008_1 = pattern_generator.nodes.new("ShaderNodeMath")
    math_008_1.name = "Math.008"
    math_008_1.operation = "MULTIPLY"
    math_008_1.use_clamp = False
    math_008_1.inputs[2].hide = True

    # node Math.009
    math_009_1 = pattern_generator.nodes.new("ShaderNodeMath")
    math_009_1.name = "Math.009"
    math_009_1.operation = "DIVIDE"
    math_009_1.use_clamp = False
    math_009_1.inputs[1].hide = True
    math_009_1.inputs[2].hide = True
    # Value_001
    math_009_1.inputs[1].default_value = 100.0

    # node Grid.001
    grid_001 = pattern_generator.nodes.new("GeometryNodeMeshGrid")
    grid_001.name = "Grid.001"
    grid_001.inputs[2].hide = True
    grid_001.inputs[3].hide = True
    grid_001.outputs[1].hide = True
    # Vertices X
    grid_001.inputs[2].default_value = 3
    # Vertices Y
    grid_001.inputs[3].default_value = 3

    # node Group Input.020
    group_input_020_1 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_020_1.name = "Group Input.020"
    group_input_020_1.outputs[0].hide = True
    group_input_020_1.outputs[3].hide = True
    group_input_020_1.outputs[4].hide = True
    group_input_020_1.outputs[5].hide = True
    group_input_020_1.outputs[6].hide = True
    group_input_020_1.outputs[7].hide = True
    group_input_020_1.outputs[8].hide = True
    group_input_020_1.outputs[9].hide = True
    group_input_020_1.outputs[10].hide = True
    group_input_020_1.outputs[11].hide = True
    group_input_020_1.outputs[12].hide = True
    group_input_020_1.outputs[13].hide = True
    group_input_020_1.outputs[14].hide = True
    group_input_020_1.outputs[15].hide = True
    group_input_020_1.outputs[16].hide = True
    group_input_020_1.outputs[17].hide = True
    group_input_020_1.outputs[18].hide = True
    group_input_020_1.outputs[19].hide = True
    group_input_020_1.outputs[20].hide = True
    group_input_020_1.outputs[21].hide = True
    group_input_020_1.outputs[22].hide = True
    group_input_020_1.outputs[23].hide = True
    group_input_020_1.outputs[24].hide = True
    group_input_020_1.outputs[25].hide = True
    group_input_020_1.outputs[26].hide = True
    group_input_020_1.outputs[27].hide = True
    group_input_020_1.outputs[28].hide = True
    group_input_020_1.outputs[29].hide = True
    group_input_020_1.outputs[30].hide = True
    group_input_020_1.outputs[31].hide = True
    group_input_020_1.outputs[32].hide = True
    group_input_020_1.outputs[33].hide = True
    group_input_020_1.outputs[34].hide = True
    group_input_020_1.outputs[35].hide = True
    group_input_020_1.outputs[36].hide = True
    group_input_020_1.outputs[37].hide = True
    group_input_020_1.outputs[38].hide = True
    group_input_020_1.outputs[39].hide = True
    group_input_020_1.outputs[40].hide = True
    group_input_020_1.outputs[41].hide = True
    group_input_020_1.outputs[42].hide = True
    group_input_020_1.outputs[43].hide = True
    group_input_020_1.outputs[44].hide = True
    group_input_020_1.outputs[45].hide = True
    group_input_020_1.outputs[46].hide = True
    group_input_020_1.outputs[47].hide = True
    group_input_020_1.outputs[48].hide = True
    group_input_020_1.outputs[49].hide = True
    group_input_020_1.outputs[50].hide = True
    group_input_020_1.outputs[51].hide = True
    group_input_020_1.outputs[52].hide = True
    group_input_020_1.outputs[53].hide = True
    group_input_020_1.outputs[54].hide = True
    group_input_020_1.outputs[55].hide = True
    group_input_020_1.outputs[56].hide = True
    group_input_020_1.outputs[57].hide = True
    group_input_020_1.outputs[58].hide = True

    # node Math.010
    math_010 = pattern_generator.nodes.new("ShaderNodeMath")
    math_010.name = "Math.010"
    math_010.operation = "ADD"
    math_010.use_clamp = False
    math_010.inputs[1].hide = True
    math_010.inputs[2].hide = True
    # Value_001
    math_010.inputs[1].default_value = 1.0

    # node Set Position
    set_position = pattern_generator.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    set_position.inputs[1].hide = True
    set_position.inputs[2].hide = True
    # Selection
    set_position.inputs[1].default_value = True
    # Position
    set_position.inputs[2].default_value = (0.0, 0.0, 0.0)

    # node Group Input.021
    group_input_021_1 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_021_1.name = "Group Input.021"
    group_input_021_1.outputs[0].hide = True
    group_input_021_1.outputs[1].hide = True
    group_input_021_1.outputs[2].hide = True
    group_input_021_1.outputs[3].hide = True
    group_input_021_1.outputs[4].hide = True
    group_input_021_1.outputs[5].hide = True
    group_input_021_1.outputs[6].hide = True
    group_input_021_1.outputs[7].hide = True
    group_input_021_1.outputs[8].hide = True
    group_input_021_1.outputs[9].hide = True
    group_input_021_1.outputs[10].hide = True
    group_input_021_1.outputs[11].hide = True
    group_input_021_1.outputs[12].hide = True
    group_input_021_1.outputs[13].hide = True
    group_input_021_1.outputs[14].hide = True
    group_input_021_1.outputs[15].hide = True
    group_input_021_1.outputs[16].hide = True
    group_input_021_1.outputs[17].hide = True
    group_input_021_1.outputs[18].hide = True
    group_input_021_1.outputs[19].hide = True
    group_input_021_1.outputs[20].hide = True
    group_input_021_1.outputs[21].hide = True
    group_input_021_1.outputs[22].hide = True
    group_input_021_1.outputs[23].hide = True
    group_input_021_1.outputs[24].hide = True
    group_input_021_1.outputs[25].hide = True
    group_input_021_1.outputs[26].hide = True
    group_input_021_1.outputs[27].hide = True
    group_input_021_1.outputs[28].hide = True
    group_input_021_1.outputs[29].hide = True
    group_input_021_1.outputs[30].hide = True
    group_input_021_1.outputs[31].hide = True
    group_input_021_1.outputs[32].hide = True
    group_input_021_1.outputs[33].hide = True
    group_input_021_1.outputs[34].hide = True
    group_input_021_1.outputs[35].hide = True
    group_input_021_1.outputs[36].hide = True
    group_input_021_1.outputs[37].hide = True
    group_input_021_1.outputs[38].hide = True
    group_input_021_1.outputs[39].hide = True
    group_input_021_1.outputs[40].hide = True
    group_input_021_1.outputs[41].hide = True
    group_input_021_1.outputs[42].hide = True
    group_input_021_1.outputs[43].hide = True
    group_input_021_1.outputs[44].hide = True
    group_input_021_1.outputs[45].hide = True
    group_input_021_1.outputs[46].hide = True
    group_input_021_1.outputs[47].hide = True
    group_input_021_1.outputs[48].hide = True
    group_input_021_1.outputs[49].hide = True
    group_input_021_1.outputs[50].hide = True
    group_input_021_1.outputs[52].hide = True
    group_input_021_1.outputs[53].hide = True
    group_input_021_1.outputs[54].hide = True
    group_input_021_1.outputs[55].hide = True
    group_input_021_1.outputs[56].hide = True
    group_input_021_1.outputs[57].hide = True
    group_input_021_1.outputs[58].hide = True

    # node Combine XYZ.002
    combine_xyz_002 = pattern_generator.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_002.name = "Combine XYZ.002"
    combine_xyz_002.inputs[0].hide = True
    combine_xyz_002.inputs[1].hide = True
    # X
    combine_xyz_002.inputs[0].default_value = 0.0
    # Y
    combine_xyz_002.inputs[1].default_value = 0.0

    # node Math.011
    math_011 = pattern_generator.nodes.new("ShaderNodeMath")
    math_011.name = "Math.011"
    math_011.operation = "MULTIPLY"
    math_011.use_clamp = False
    math_011.inputs[1].hide = True
    math_011.inputs[2].hide = True
    # Value_001
    math_011.inputs[1].default_value = -1.0

    # node Math.012
    math_012 = pattern_generator.nodes.new("ShaderNodeMath")
    math_012.name = "Math.012"
    math_012.operation = "ADD"
    math_012.use_clamp = False
    math_012.inputs[1].hide = True
    math_012.inputs[2].hide = True
    # Value_001
    math_012.inputs[1].default_value = 1.0

    # node Math.013
    math_013 = pattern_generator.nodes.new("ShaderNodeMath")
    math_013.name = "Math.013"
    math_013.operation = "ADD"
    math_013.use_clamp = False
    math_013.inputs[1].hide = True
    math_013.inputs[2].hide = True
    # Value_001
    math_013.inputs[1].default_value = 1.0

    # node Join Geometry.002
    join_geometry_002 = pattern_generator.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_002.name = "Join Geometry.002"

    # node Switch.002
    switch_002_1 = pattern_generator.nodes.new("GeometryNodeSwitch")
    switch_002_1.name = "Switch.002"
    switch_002_1.input_type = "GEOMETRY"

    # node Group Input.022
    group_input_022_1 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_022_1.name = "Group Input.022"
    group_input_022_1.outputs[0].hide = True
    group_input_022_1.outputs[1].hide = True
    group_input_022_1.outputs[2].hide = True
    group_input_022_1.outputs[3].hide = True
    group_input_022_1.outputs[4].hide = True
    group_input_022_1.outputs[5].hide = True
    group_input_022_1.outputs[6].hide = True
    group_input_022_1.outputs[7].hide = True
    group_input_022_1.outputs[8].hide = True
    group_input_022_1.outputs[9].hide = True
    group_input_022_1.outputs[10].hide = True
    group_input_022_1.outputs[11].hide = True
    group_input_022_1.outputs[12].hide = True
    group_input_022_1.outputs[13].hide = True
    group_input_022_1.outputs[14].hide = True
    group_input_022_1.outputs[15].hide = True
    group_input_022_1.outputs[16].hide = True
    group_input_022_1.outputs[17].hide = True
    group_input_022_1.outputs[18].hide = True
    group_input_022_1.outputs[19].hide = True
    group_input_022_1.outputs[20].hide = True
    group_input_022_1.outputs[21].hide = True
    group_input_022_1.outputs[22].hide = True
    group_input_022_1.outputs[23].hide = True
    group_input_022_1.outputs[24].hide = True
    group_input_022_1.outputs[25].hide = True
    group_input_022_1.outputs[26].hide = True
    group_input_022_1.outputs[27].hide = True
    group_input_022_1.outputs[28].hide = True
    group_input_022_1.outputs[29].hide = True
    group_input_022_1.outputs[30].hide = True
    group_input_022_1.outputs[31].hide = True
    group_input_022_1.outputs[32].hide = True
    group_input_022_1.outputs[33].hide = True
    group_input_022_1.outputs[34].hide = True
    group_input_022_1.outputs[35].hide = True
    group_input_022_1.outputs[36].hide = True
    group_input_022_1.outputs[37].hide = True
    group_input_022_1.outputs[38].hide = True
    group_input_022_1.outputs[39].hide = True
    group_input_022_1.outputs[40].hide = True
    group_input_022_1.outputs[41].hide = True
    group_input_022_1.outputs[42].hide = True
    group_input_022_1.outputs[43].hide = True
    group_input_022_1.outputs[44].hide = True
    group_input_022_1.outputs[45].hide = True
    group_input_022_1.outputs[46].hide = True
    group_input_022_1.outputs[47].hide = True
    group_input_022_1.outputs[49].hide = True
    group_input_022_1.outputs[50].hide = True
    group_input_022_1.outputs[51].hide = True
    group_input_022_1.outputs[52].hide = True
    group_input_022_1.outputs[53].hide = True
    group_input_022_1.outputs[54].hide = True
    group_input_022_1.outputs[55].hide = True
    group_input_022_1.outputs[56].hide = True
    group_input_022_1.outputs[57].hide = True
    group_input_022_1.outputs[58].hide = True

    # node Frame
    frame = pattern_generator.nodes.new("NodeFrame")
    frame.label = "Using it as a Wall Decor"
    frame.name = "Frame"
    frame.label_size = 64
    frame.shrink = True

    # node Switch.003
    switch_003_1 = pattern_generator.nodes.new("GeometryNodeSwitch")
    switch_003_1.name = "Switch.003"
    switch_003_1.input_type = "GEOMETRY"

    # node Group Input.023
    group_input_023_1 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_023_1.name = "Group Input.023"
    group_input_023_1.outputs[0].hide = True
    group_input_023_1.outputs[1].hide = True
    group_input_023_1.outputs[2].hide = True
    group_input_023_1.outputs[3].hide = True
    group_input_023_1.outputs[4].hide = True
    group_input_023_1.outputs[5].hide = True
    group_input_023_1.outputs[6].hide = True
    group_input_023_1.outputs[7].hide = True
    group_input_023_1.outputs[8].hide = True
    group_input_023_1.outputs[9].hide = True
    group_input_023_1.outputs[10].hide = True
    group_input_023_1.outputs[11].hide = True
    group_input_023_1.outputs[12].hide = True
    group_input_023_1.outputs[13].hide = True
    group_input_023_1.outputs[14].hide = True
    group_input_023_1.outputs[15].hide = True
    group_input_023_1.outputs[16].hide = True
    group_input_023_1.outputs[17].hide = True
    group_input_023_1.outputs[18].hide = True
    group_input_023_1.outputs[19].hide = True
    group_input_023_1.outputs[20].hide = True
    group_input_023_1.outputs[21].hide = True
    group_input_023_1.outputs[22].hide = True
    group_input_023_1.outputs[23].hide = True
    group_input_023_1.outputs[24].hide = True
    group_input_023_1.outputs[25].hide = True
    group_input_023_1.outputs[26].hide = True
    group_input_023_1.outputs[27].hide = True
    group_input_023_1.outputs[28].hide = True
    group_input_023_1.outputs[29].hide = True
    group_input_023_1.outputs[30].hide = True
    group_input_023_1.outputs[31].hide = True
    group_input_023_1.outputs[32].hide = True
    group_input_023_1.outputs[33].hide = True
    group_input_023_1.outputs[34].hide = True
    group_input_023_1.outputs[35].hide = True
    group_input_023_1.outputs[36].hide = True
    group_input_023_1.outputs[37].hide = True
    group_input_023_1.outputs[38].hide = True
    group_input_023_1.outputs[39].hide = True
    group_input_023_1.outputs[40].hide = True
    group_input_023_1.outputs[41].hide = True
    group_input_023_1.outputs[42].hide = True
    group_input_023_1.outputs[43].hide = True
    group_input_023_1.outputs[44].hide = True
    group_input_023_1.outputs[45].hide = True
    group_input_023_1.outputs[46].hide = True
    group_input_023_1.outputs[47].hide = True
    group_input_023_1.outputs[48].hide = True
    group_input_023_1.outputs[49].hide = True
    group_input_023_1.outputs[50].hide = True
    group_input_023_1.outputs[51].hide = True
    group_input_023_1.outputs[52].hide = True
    group_input_023_1.outputs[54].hide = True
    group_input_023_1.outputs[55].hide = True
    group_input_023_1.outputs[56].hide = True
    group_input_023_1.outputs[57].hide = True
    group_input_023_1.outputs[58].hide = True

    # node Group Input.024
    group_input_024_1 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_024_1.name = "Group Input.024"
    group_input_024_1.outputs[0].hide = True
    group_input_024_1.outputs[1].hide = True
    group_input_024_1.outputs[2].hide = True
    group_input_024_1.outputs[3].hide = True
    group_input_024_1.outputs[4].hide = True
    group_input_024_1.outputs[5].hide = True
    group_input_024_1.outputs[6].hide = True
    group_input_024_1.outputs[7].hide = True
    group_input_024_1.outputs[8].hide = True
    group_input_024_1.outputs[9].hide = True
    group_input_024_1.outputs[10].hide = True
    group_input_024_1.outputs[11].hide = True
    group_input_024_1.outputs[12].hide = True
    group_input_024_1.outputs[13].hide = True
    group_input_024_1.outputs[14].hide = True
    group_input_024_1.outputs[15].hide = True
    group_input_024_1.outputs[16].hide = True
    group_input_024_1.outputs[17].hide = True
    group_input_024_1.outputs[18].hide = True
    group_input_024_1.outputs[19].hide = True
    group_input_024_1.outputs[20].hide = True
    group_input_024_1.outputs[21].hide = True
    group_input_024_1.outputs[22].hide = True
    group_input_024_1.outputs[23].hide = True
    group_input_024_1.outputs[24].hide = True
    group_input_024_1.outputs[25].hide = True
    group_input_024_1.outputs[26].hide = True
    group_input_024_1.outputs[27].hide = True
    group_input_024_1.outputs[28].hide = True
    group_input_024_1.outputs[29].hide = True
    group_input_024_1.outputs[31].hide = True
    group_input_024_1.outputs[32].hide = True
    group_input_024_1.outputs[33].hide = True
    group_input_024_1.outputs[34].hide = True
    group_input_024_1.outputs[35].hide = True
    group_input_024_1.outputs[36].hide = True
    group_input_024_1.outputs[37].hide = True
    group_input_024_1.outputs[38].hide = True
    group_input_024_1.outputs[39].hide = True
    group_input_024_1.outputs[40].hide = True
    group_input_024_1.outputs[41].hide = True
    group_input_024_1.outputs[42].hide = True
    group_input_024_1.outputs[43].hide = True
    group_input_024_1.outputs[44].hide = True
    group_input_024_1.outputs[45].hide = True
    group_input_024_1.outputs[46].hide = True
    group_input_024_1.outputs[47].hide = True
    group_input_024_1.outputs[48].hide = True
    group_input_024_1.outputs[49].hide = True
    group_input_024_1.outputs[50].hide = True
    group_input_024_1.outputs[51].hide = True
    group_input_024_1.outputs[52].hide = True
    group_input_024_1.outputs[53].hide = True
    group_input_024_1.outputs[54].hide = True
    group_input_024_1.outputs[55].hide = True
    group_input_024_1.outputs[56].hide = True
    group_input_024_1.outputs[57].hide = True
    group_input_024_1.outputs[58].hide = True

    # node Set Material.001
    set_material_001 = pattern_generator.nodes.new("GeometryNodeSetMaterial")
    set_material_001.name = "Set Material.001"
    set_material_001.inputs[1].hide = True
    # Selection
    set_material_001.inputs[1].default_value = True

    # node Group Input.025
    group_input_025_1 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_025_1.name = "Group Input.025"
    group_input_025_1.outputs[0].hide = True
    group_input_025_1.outputs[1].hide = True
    group_input_025_1.outputs[2].hide = True
    group_input_025_1.outputs[3].hide = True
    group_input_025_1.outputs[4].hide = True
    group_input_025_1.outputs[5].hide = True
    group_input_025_1.outputs[6].hide = True
    group_input_025_1.outputs[7].hide = True
    group_input_025_1.outputs[8].hide = True
    group_input_025_1.outputs[9].hide = True
    group_input_025_1.outputs[10].hide = True
    group_input_025_1.outputs[11].hide = True
    group_input_025_1.outputs[12].hide = True
    group_input_025_1.outputs[13].hide = True
    group_input_025_1.outputs[14].hide = True
    group_input_025_1.outputs[15].hide = True
    group_input_025_1.outputs[16].hide = True
    group_input_025_1.outputs[17].hide = True
    group_input_025_1.outputs[18].hide = True
    group_input_025_1.outputs[19].hide = True
    group_input_025_1.outputs[20].hide = True
    group_input_025_1.outputs[21].hide = True
    group_input_025_1.outputs[22].hide = True
    group_input_025_1.outputs[23].hide = True
    group_input_025_1.outputs[24].hide = True
    group_input_025_1.outputs[25].hide = True
    group_input_025_1.outputs[26].hide = True
    group_input_025_1.outputs[27].hide = True
    group_input_025_1.outputs[28].hide = True
    group_input_025_1.outputs[29].hide = True
    group_input_025_1.outputs[30].hide = True
    group_input_025_1.outputs[31].hide = True
    group_input_025_1.outputs[32].hide = True
    group_input_025_1.outputs[33].hide = True
    group_input_025_1.outputs[34].hide = True
    group_input_025_1.outputs[35].hide = True
    group_input_025_1.outputs[36].hide = True
    group_input_025_1.outputs[37].hide = True
    group_input_025_1.outputs[38].hide = True
    group_input_025_1.outputs[39].hide = True
    group_input_025_1.outputs[40].hide = True
    group_input_025_1.outputs[41].hide = True
    group_input_025_1.outputs[42].hide = True
    group_input_025_1.outputs[43].hide = True
    group_input_025_1.outputs[44].hide = True
    group_input_025_1.outputs[45].hide = True
    group_input_025_1.outputs[46].hide = True
    group_input_025_1.outputs[47].hide = True
    group_input_025_1.outputs[48].hide = True
    group_input_025_1.outputs[49].hide = True
    group_input_025_1.outputs[51].hide = True
    group_input_025_1.outputs[52].hide = True
    group_input_025_1.outputs[53].hide = True
    group_input_025_1.outputs[54].hide = True
    group_input_025_1.outputs[55].hide = True
    group_input_025_1.outputs[56].hide = True
    group_input_025_1.outputs[57].hide = True
    group_input_025_1.outputs[58].hide = True

    # node Set Material.002
    set_material_002 = pattern_generator.nodes.new("GeometryNodeSetMaterial")
    set_material_002.name = "Set Material.002"
    set_material_002.inputs[1].hide = True
    # Selection
    set_material_002.inputs[1].default_value = True

    # node Group Input.026
    group_input_026_1 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_026_1.name = "Group Input.026"
    group_input_026_1.outputs[0].hide = True
    group_input_026_1.outputs[1].hide = True
    group_input_026_1.outputs[2].hide = True
    group_input_026_1.outputs[3].hide = True
    group_input_026_1.outputs[4].hide = True
    group_input_026_1.outputs[5].hide = True
    group_input_026_1.outputs[6].hide = True
    group_input_026_1.outputs[7].hide = True
    group_input_026_1.outputs[8].hide = True
    group_input_026_1.outputs[9].hide = True
    group_input_026_1.outputs[10].hide = True
    group_input_026_1.outputs[11].hide = True
    group_input_026_1.outputs[12].hide = True
    group_input_026_1.outputs[13].hide = True
    group_input_026_1.outputs[14].hide = True
    group_input_026_1.outputs[15].hide = True
    group_input_026_1.outputs[16].hide = True
    group_input_026_1.outputs[17].hide = True
    group_input_026_1.outputs[18].hide = True
    group_input_026_1.outputs[19].hide = True
    group_input_026_1.outputs[20].hide = True
    group_input_026_1.outputs[21].hide = True
    group_input_026_1.outputs[22].hide = True
    group_input_026_1.outputs[23].hide = True
    group_input_026_1.outputs[24].hide = True
    group_input_026_1.outputs[25].hide = True
    group_input_026_1.outputs[26].hide = True
    group_input_026_1.outputs[27].hide = True
    group_input_026_1.outputs[28].hide = True
    group_input_026_1.outputs[29].hide = True
    group_input_026_1.outputs[30].hide = True
    group_input_026_1.outputs[31].hide = True
    group_input_026_1.outputs[32].hide = True
    group_input_026_1.outputs[33].hide = True
    group_input_026_1.outputs[34].hide = True
    group_input_026_1.outputs[35].hide = True
    group_input_026_1.outputs[36].hide = True
    group_input_026_1.outputs[37].hide = True
    group_input_026_1.outputs[38].hide = True
    group_input_026_1.outputs[39].hide = True
    group_input_026_1.outputs[40].hide = True
    group_input_026_1.outputs[41].hide = True
    group_input_026_1.outputs[42].hide = True
    group_input_026_1.outputs[43].hide = True
    group_input_026_1.outputs[44].hide = True
    group_input_026_1.outputs[45].hide = True
    group_input_026_1.outputs[46].hide = True
    group_input_026_1.outputs[47].hide = True
    group_input_026_1.outputs[48].hide = True
    group_input_026_1.outputs[49].hide = True
    group_input_026_1.outputs[50].hide = True
    group_input_026_1.outputs[51].hide = True
    group_input_026_1.outputs[52].hide = True
    group_input_026_1.outputs[53].hide = True
    group_input_026_1.outputs[55].hide = True
    group_input_026_1.outputs[56].hide = True
    group_input_026_1.outputs[57].hide = True
    group_input_026_1.outputs[58].hide = True

    # node Group Input.013
    group_input_013_1 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_013_1.name = "Group Input.013"
    group_input_013_1.outputs[0].hide = True
    group_input_013_1.outputs[1].hide = True
    group_input_013_1.outputs[2].hide = True
    group_input_013_1.outputs[3].hide = True
    group_input_013_1.outputs[4].hide = True
    group_input_013_1.outputs[5].hide = True
    group_input_013_1.outputs[6].hide = True
    group_input_013_1.outputs[7].hide = True
    group_input_013_1.outputs[8].hide = True
    group_input_013_1.outputs[9].hide = True
    group_input_013_1.outputs[10].hide = True
    group_input_013_1.outputs[11].hide = True
    group_input_013_1.outputs[12].hide = True
    group_input_013_1.outputs[13].hide = True
    group_input_013_1.outputs[14].hide = True
    group_input_013_1.outputs[15].hide = True
    group_input_013_1.outputs[16].hide = True
    group_input_013_1.outputs[17].hide = True
    group_input_013_1.outputs[18].hide = True
    group_input_013_1.outputs[19].hide = True
    group_input_013_1.outputs[20].hide = True
    group_input_013_1.outputs[21].hide = True
    group_input_013_1.outputs[22].hide = True
    group_input_013_1.outputs[23].hide = True
    group_input_013_1.outputs[24].hide = True
    group_input_013_1.outputs[25].hide = True
    group_input_013_1.outputs[26].hide = True
    group_input_013_1.outputs[27].hide = True
    group_input_013_1.outputs[28].hide = True
    group_input_013_1.outputs[29].hide = True
    group_input_013_1.outputs[30].hide = True
    group_input_013_1.outputs[31].hide = True
    group_input_013_1.outputs[32].hide = True
    group_input_013_1.outputs[33].hide = True
    group_input_013_1.outputs[34].hide = True
    group_input_013_1.outputs[35].hide = True
    group_input_013_1.outputs[36].hide = True
    group_input_013_1.outputs[37].hide = True
    group_input_013_1.outputs[38].hide = True
    group_input_013_1.outputs[39].hide = True
    group_input_013_1.outputs[40].hide = True
    group_input_013_1.outputs[41].hide = True
    group_input_013_1.outputs[42].hide = True
    group_input_013_1.outputs[43].hide = True
    group_input_013_1.outputs[44].hide = True
    group_input_013_1.outputs[45].hide = True
    group_input_013_1.outputs[46].hide = True
    group_input_013_1.outputs[47].hide = True
    group_input_013_1.outputs[48].hide = True
    group_input_013_1.outputs[50].hide = True
    group_input_013_1.outputs[51].hide = True
    group_input_013_1.outputs[52].hide = True
    group_input_013_1.outputs[53].hide = True
    group_input_013_1.outputs[54].hide = True
    group_input_013_1.outputs[55].hide = True
    group_input_013_1.outputs[56].hide = True
    group_input_013_1.outputs[57].hide = True
    group_input_013_1.outputs[58].hide = True

    # node Group Input.014
    group_input_014_1 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_014_1.name = "Group Input.014"
    group_input_014_1.outputs[0].hide = True
    group_input_014_1.outputs[1].hide = True
    group_input_014_1.outputs[2].hide = True
    group_input_014_1.outputs[3].hide = True
    group_input_014_1.outputs[4].hide = True
    group_input_014_1.outputs[5].hide = True
    group_input_014_1.outputs[6].hide = True
    group_input_014_1.outputs[8].hide = True
    group_input_014_1.outputs[9].hide = True
    group_input_014_1.outputs[10].hide = True
    group_input_014_1.outputs[11].hide = True
    group_input_014_1.outputs[12].hide = True
    group_input_014_1.outputs[13].hide = True
    group_input_014_1.outputs[14].hide = True
    group_input_014_1.outputs[15].hide = True
    group_input_014_1.outputs[16].hide = True
    group_input_014_1.outputs[17].hide = True
    group_input_014_1.outputs[18].hide = True
    group_input_014_1.outputs[19].hide = True
    group_input_014_1.outputs[20].hide = True
    group_input_014_1.outputs[21].hide = True
    group_input_014_1.outputs[22].hide = True
    group_input_014_1.outputs[23].hide = True
    group_input_014_1.outputs[24].hide = True
    group_input_014_1.outputs[25].hide = True
    group_input_014_1.outputs[26].hide = True
    group_input_014_1.outputs[27].hide = True
    group_input_014_1.outputs[28].hide = True
    group_input_014_1.outputs[29].hide = True
    group_input_014_1.outputs[30].hide = True
    group_input_014_1.outputs[31].hide = True
    group_input_014_1.outputs[32].hide = True
    group_input_014_1.outputs[33].hide = True
    group_input_014_1.outputs[34].hide = True
    group_input_014_1.outputs[35].hide = True
    group_input_014_1.outputs[36].hide = True
    group_input_014_1.outputs[37].hide = True
    group_input_014_1.outputs[38].hide = True
    group_input_014_1.outputs[39].hide = True
    group_input_014_1.outputs[40].hide = True
    group_input_014_1.outputs[41].hide = True
    group_input_014_1.outputs[42].hide = True
    group_input_014_1.outputs[43].hide = True
    group_input_014_1.outputs[44].hide = True
    group_input_014_1.outputs[45].hide = True
    group_input_014_1.outputs[46].hide = True
    group_input_014_1.outputs[47].hide = True
    group_input_014_1.outputs[48].hide = True
    group_input_014_1.outputs[49].hide = True
    group_input_014_1.outputs[50].hide = True
    group_input_014_1.outputs[51].hide = True
    group_input_014_1.outputs[52].hide = True
    group_input_014_1.outputs[53].hide = True
    group_input_014_1.outputs[54].hide = True
    group_input_014_1.outputs[55].hide = True
    group_input_014_1.outputs[56].hide = True
    group_input_014_1.outputs[57].hide = True
    group_input_014_1.outputs[58].hide = True

    # node Combine XYZ.003
    combine_xyz_003 = pattern_generator.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_003.name = "Combine XYZ.003"
    combine_xyz_003.inputs[0].hide = True
    combine_xyz_003.inputs[1].hide = True
    # X
    combine_xyz_003.inputs[0].default_value = 0.0
    # Y
    combine_xyz_003.inputs[1].default_value = 0.0

    # node Math.005
    math_005_1 = pattern_generator.nodes.new("ShaderNodeMath")
    math_005_1.name = "Math.005"
    math_005_1.operation = "MULTIPLY"
    math_005_1.use_clamp = False
    math_005_1.inputs[0].hide = True
    math_005_1.inputs[2].hide = True
    # Value
    math_005_1.inputs[0].default_value = 1.5707963705062866

    # node Switch.004
    switch_004 = pattern_generator.nodes.new("GeometryNodeSwitch")
    switch_004.name = "Switch.004"
    switch_004.input_type = "VECTOR"

    # node Group Input.015
    group_input_015_1 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_015_1.name = "Group Input.015"
    group_input_015_1.outputs[0].hide = True
    group_input_015_1.outputs[1].hide = True
    group_input_015_1.outputs[2].hide = True
    group_input_015_1.outputs[3].hide = True
    group_input_015_1.outputs[4].hide = True
    group_input_015_1.outputs[5].hide = True
    group_input_015_1.outputs[7].hide = True
    group_input_015_1.outputs[8].hide = True
    group_input_015_1.outputs[9].hide = True
    group_input_015_1.outputs[10].hide = True
    group_input_015_1.outputs[11].hide = True
    group_input_015_1.outputs[12].hide = True
    group_input_015_1.outputs[13].hide = True
    group_input_015_1.outputs[14].hide = True
    group_input_015_1.outputs[15].hide = True
    group_input_015_1.outputs[16].hide = True
    group_input_015_1.outputs[17].hide = True
    group_input_015_1.outputs[18].hide = True
    group_input_015_1.outputs[19].hide = True
    group_input_015_1.outputs[20].hide = True
    group_input_015_1.outputs[21].hide = True
    group_input_015_1.outputs[22].hide = True
    group_input_015_1.outputs[23].hide = True
    group_input_015_1.outputs[24].hide = True
    group_input_015_1.outputs[25].hide = True
    group_input_015_1.outputs[26].hide = True
    group_input_015_1.outputs[27].hide = True
    group_input_015_1.outputs[28].hide = True
    group_input_015_1.outputs[29].hide = True
    group_input_015_1.outputs[30].hide = True
    group_input_015_1.outputs[31].hide = True
    group_input_015_1.outputs[32].hide = True
    group_input_015_1.outputs[33].hide = True
    group_input_015_1.outputs[34].hide = True
    group_input_015_1.outputs[35].hide = True
    group_input_015_1.outputs[36].hide = True
    group_input_015_1.outputs[37].hide = True
    group_input_015_1.outputs[38].hide = True
    group_input_015_1.outputs[39].hide = True
    group_input_015_1.outputs[40].hide = True
    group_input_015_1.outputs[41].hide = True
    group_input_015_1.outputs[42].hide = True
    group_input_015_1.outputs[43].hide = True
    group_input_015_1.outputs[44].hide = True
    group_input_015_1.outputs[45].hide = True
    group_input_015_1.outputs[46].hide = True
    group_input_015_1.outputs[47].hide = True
    group_input_015_1.outputs[48].hide = True
    group_input_015_1.outputs[49].hide = True
    group_input_015_1.outputs[50].hide = True
    group_input_015_1.outputs[51].hide = True
    group_input_015_1.outputs[52].hide = True
    group_input_015_1.outputs[53].hide = True
    group_input_015_1.outputs[54].hide = True
    group_input_015_1.outputs[55].hide = True
    group_input_015_1.outputs[56].hide = True
    group_input_015_1.outputs[57].hide = True
    group_input_015_1.outputs[58].hide = True

    # node Switch.005
    switch_005 = pattern_generator.nodes.new("GeometryNodeSwitch")
    switch_005.name = "Switch.005"
    switch_005.input_type = "FLOAT"

    # node Random Value.005
    random_value_005_1 = pattern_generator.nodes.new("FunctionNodeRandomValue")
    random_value_005_1.name = "Random Value.005"
    random_value_005_1.data_type = "FLOAT"
    random_value_005_1.inputs[0].hide = True
    random_value_005_1.inputs[1].hide = True
    random_value_005_1.inputs[2].hide = True
    random_value_005_1.inputs[3].hide = True
    random_value_005_1.inputs[4].hide = True
    random_value_005_1.inputs[5].hide = True
    random_value_005_1.inputs[6].hide = True
    random_value_005_1.inputs[7].hide = True
    random_value_005_1.outputs[0].hide = True
    random_value_005_1.outputs[2].hide = True
    random_value_005_1.outputs[3].hide = True
    # Min_001
    random_value_005_1.inputs[2].default_value = 0.0
    # Max_001
    random_value_005_1.inputs[3].default_value = 1.0
    # ID
    random_value_005_1.inputs[7].default_value = 0

    # node Group Input.027
    group_input_027_1 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_027_1.name = "Group Input.027"
    group_input_027_1.outputs[0].hide = True
    group_input_027_1.outputs[1].hide = True
    group_input_027_1.outputs[2].hide = True
    group_input_027_1.outputs[3].hide = True
    group_input_027_1.outputs[4].hide = True
    group_input_027_1.outputs[5].hide = True
    group_input_027_1.outputs[6].hide = True
    group_input_027_1.outputs[7].hide = True
    group_input_027_1.outputs[8].hide = True
    group_input_027_1.outputs[9].hide = True
    group_input_027_1.outputs[10].hide = True
    group_input_027_1.outputs[11].hide = True
    group_input_027_1.outputs[13].hide = True
    group_input_027_1.outputs[14].hide = True
    group_input_027_1.outputs[15].hide = True
    group_input_027_1.outputs[16].hide = True
    group_input_027_1.outputs[17].hide = True
    group_input_027_1.outputs[18].hide = True
    group_input_027_1.outputs[19].hide = True
    group_input_027_1.outputs[20].hide = True
    group_input_027_1.outputs[21].hide = True
    group_input_027_1.outputs[22].hide = True
    group_input_027_1.outputs[23].hide = True
    group_input_027_1.outputs[24].hide = True
    group_input_027_1.outputs[25].hide = True
    group_input_027_1.outputs[26].hide = True
    group_input_027_1.outputs[27].hide = True
    group_input_027_1.outputs[28].hide = True
    group_input_027_1.outputs[29].hide = True
    group_input_027_1.outputs[30].hide = True
    group_input_027_1.outputs[31].hide = True
    group_input_027_1.outputs[32].hide = True
    group_input_027_1.outputs[33].hide = True
    group_input_027_1.outputs[34].hide = True
    group_input_027_1.outputs[35].hide = True
    group_input_027_1.outputs[36].hide = True
    group_input_027_1.outputs[37].hide = True
    group_input_027_1.outputs[38].hide = True
    group_input_027_1.outputs[39].hide = True
    group_input_027_1.outputs[40].hide = True
    group_input_027_1.outputs[41].hide = True
    group_input_027_1.outputs[42].hide = True
    group_input_027_1.outputs[43].hide = True
    group_input_027_1.outputs[44].hide = True
    group_input_027_1.outputs[45].hide = True
    group_input_027_1.outputs[46].hide = True
    group_input_027_1.outputs[47].hide = True
    group_input_027_1.outputs[48].hide = True
    group_input_027_1.outputs[49].hide = True
    group_input_027_1.outputs[50].hide = True
    group_input_027_1.outputs[51].hide = True
    group_input_027_1.outputs[52].hide = True
    group_input_027_1.outputs[53].hide = True
    group_input_027_1.outputs[54].hide = True
    group_input_027_1.outputs[55].hide = True
    group_input_027_1.outputs[56].hide = True
    group_input_027_1.outputs[57].hide = True
    group_input_027_1.outputs[58].hide = True

    # node Math.015
    math_015 = pattern_generator.nodes.new("ShaderNodeMath")
    math_015.name = "Math.015"
    math_015.operation = "MULTIPLY"
    math_015.use_clamp = False
    math_015.inputs[2].hide = True

    # node Random Value.006
    random_value_006_1 = pattern_generator.nodes.new("FunctionNodeRandomValue")
    random_value_006_1.name = "Random Value.006"
    random_value_006_1.data_type = "INT"
    random_value_006_1.inputs[0].hide = True
    random_value_006_1.inputs[1].hide = True
    random_value_006_1.inputs[2].hide = True
    random_value_006_1.inputs[3].hide = True
    random_value_006_1.inputs[4].hide = True
    random_value_006_1.inputs[5].hide = True
    random_value_006_1.inputs[6].hide = True
    random_value_006_1.inputs[7].hide = True
    random_value_006_1.outputs[0].hide = True
    random_value_006_1.outputs[1].hide = True
    random_value_006_1.outputs[3].hide = True
    # Min_002
    random_value_006_1.inputs[4].default_value = 0
    # Max_002
    random_value_006_1.inputs[5].default_value = 100
    # ID
    random_value_006_1.inputs[7].default_value = 0

    # node Math.016
    math_016 = pattern_generator.nodes.new("ShaderNodeMath")
    math_016.name = "Math.016"
    math_016.operation = "SUBTRACT"
    math_016.use_clamp = True
    math_016.inputs[0].hide = True
    math_016.inputs[2].hide = True
    # Value
    math_016.inputs[0].default_value = 1.0

    # node Math.017
    math_017 = pattern_generator.nodes.new("ShaderNodeMath")
    math_017.name = "Math.017"
    math_017.operation = "MULTIPLY"
    math_017.use_clamp = False
    math_017.inputs[2].hide = True

    # node Math.018
    math_018 = pattern_generator.nodes.new("ShaderNodeMath")
    math_018.name = "Math.018"
    math_018.operation = "SUBTRACT"
    math_018.use_clamp = False
    math_018.inputs[2].hide = True

    # node Frame.002
    frame_002 = pattern_generator.nodes.new("NodeFrame")
    frame_002.label = "Curve Trimming"
    frame_002.name = "Frame.002"
    frame_002.label_size = 64
    frame_002.shrink = True

    # node Merge by Distance.001
    merge_by_distance_001 = pattern_generator.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance_001.name = "Merge by Distance.001"
    merge_by_distance_001.mode = "ALL"
    merge_by_distance_001.inputs[1].hide = True
    merge_by_distance_001.inputs[2].hide = True
    # Selection
    merge_by_distance_001.inputs[1].default_value = True
    # Distance
    merge_by_distance_001.inputs[2].default_value = 0.0010000000474974513

    # node Switch.006
    switch_006_1 = pattern_generator.nodes.new("GeometryNodeSwitch")
    switch_006_1.name = "Switch.006"
    switch_006_1.input_type = "GEOMETRY"

    # node Group Input.029
    group_input_029_1 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_029_1.name = "Group Input.029"
    group_input_029_1.outputs[0].hide = True
    group_input_029_1.outputs[1].hide = True
    group_input_029_1.outputs[2].hide = True
    group_input_029_1.outputs[3].hide = True
    group_input_029_1.outputs[4].hide = True
    group_input_029_1.outputs[5].hide = True
    group_input_029_1.outputs[6].hide = True
    group_input_029_1.outputs[7].hide = True
    group_input_029_1.outputs[8].hide = True
    group_input_029_1.outputs[9].hide = True
    group_input_029_1.outputs[10].hide = True
    group_input_029_1.outputs[11].hide = True
    group_input_029_1.outputs[12].hide = True
    group_input_029_1.outputs[13].hide = True
    group_input_029_1.outputs[15].hide = True
    group_input_029_1.outputs[16].hide = True
    group_input_029_1.outputs[17].hide = True
    group_input_029_1.outputs[18].hide = True
    group_input_029_1.outputs[19].hide = True
    group_input_029_1.outputs[20].hide = True
    group_input_029_1.outputs[21].hide = True
    group_input_029_1.outputs[22].hide = True
    group_input_029_1.outputs[23].hide = True
    group_input_029_1.outputs[24].hide = True
    group_input_029_1.outputs[25].hide = True
    group_input_029_1.outputs[26].hide = True
    group_input_029_1.outputs[27].hide = True
    group_input_029_1.outputs[28].hide = True
    group_input_029_1.outputs[29].hide = True
    group_input_029_1.outputs[30].hide = True
    group_input_029_1.outputs[31].hide = True
    group_input_029_1.outputs[32].hide = True
    group_input_029_1.outputs[33].hide = True
    group_input_029_1.outputs[34].hide = True
    group_input_029_1.outputs[35].hide = True
    group_input_029_1.outputs[36].hide = True
    group_input_029_1.outputs[37].hide = True
    group_input_029_1.outputs[38].hide = True
    group_input_029_1.outputs[39].hide = True
    group_input_029_1.outputs[40].hide = True
    group_input_029_1.outputs[41].hide = True
    group_input_029_1.outputs[42].hide = True
    group_input_029_1.outputs[43].hide = True
    group_input_029_1.outputs[44].hide = True
    group_input_029_1.outputs[45].hide = True
    group_input_029_1.outputs[46].hide = True
    group_input_029_1.outputs[47].hide = True
    group_input_029_1.outputs[48].hide = True
    group_input_029_1.outputs[49].hide = True
    group_input_029_1.outputs[50].hide = True
    group_input_029_1.outputs[51].hide = True
    group_input_029_1.outputs[52].hide = True
    group_input_029_1.outputs[53].hide = True
    group_input_029_1.outputs[54].hide = True
    group_input_029_1.outputs[55].hide = True
    group_input_029_1.outputs[56].hide = True
    group_input_029_1.outputs[57].hide = True
    group_input_029_1.outputs[58].hide = True

    # node Curve to Mesh.004
    curve_to_mesh_004 = pattern_generator.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh_004.name = "Curve to Mesh.004"
    curve_to_mesh_004.inputs[1].hide = True
    curve_to_mesh_004.inputs[2].hide = True
    # Fill Caps
    curve_to_mesh_004.inputs[2].default_value = False

    # node Mesh to Curve.001
    mesh_to_curve_001 = pattern_generator.nodes.new("GeometryNodeMeshToCurve")
    mesh_to_curve_001.name = "Mesh to Curve.001"
    mesh_to_curve_001.inputs[1].hide = True
    # Selection
    mesh_to_curve_001.inputs[1].default_value = True

    # node Realize Instances.002
    realize_instances_002 = pattern_generator.nodes.new("GeometryNodeRealizeInstances")
    realize_instances_002.name = "Realize Instances.002"
    realize_instances_002.inputs[1].hide = True
    realize_instances_002.inputs[2].hide = True
    realize_instances_002.inputs[3].hide = True
    # Selection
    realize_instances_002.inputs[1].default_value = True
    # Realize All
    realize_instances_002.inputs[2].default_value = True
    # Depth
    realize_instances_002.inputs[3].default_value = 0

    # node Merge by Distance.003
    merge_by_distance_003 = pattern_generator.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance_003.name = "Merge by Distance.003"
    merge_by_distance_003.mode = "ALL"
    merge_by_distance_003.inputs[1].hide = True
    merge_by_distance_003.inputs[2].hide = True
    # Selection
    merge_by_distance_003.inputs[1].default_value = True
    # Distance
    merge_by_distance_003.inputs[2].default_value = 0.0010000000474974513

    # node Switch.009
    switch_009_1 = pattern_generator.nodes.new("GeometryNodeSwitch")
    switch_009_1.name = "Switch.009"
    switch_009_1.input_type = "GEOMETRY"

    # node Group Input.034
    group_input_034 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_034.name = "Group Input.034"
    group_input_034.outputs[0].hide = True
    group_input_034.outputs[1].hide = True
    group_input_034.outputs[2].hide = True
    group_input_034.outputs[3].hide = True
    group_input_034.outputs[4].hide = True
    group_input_034.outputs[5].hide = True
    group_input_034.outputs[6].hide = True
    group_input_034.outputs[7].hide = True
    group_input_034.outputs[8].hide = True
    group_input_034.outputs[9].hide = True
    group_input_034.outputs[10].hide = True
    group_input_034.outputs[11].hide = True
    group_input_034.outputs[12].hide = True
    group_input_034.outputs[13].hide = True
    group_input_034.outputs[15].hide = True
    group_input_034.outputs[16].hide = True
    group_input_034.outputs[17].hide = True
    group_input_034.outputs[18].hide = True
    group_input_034.outputs[19].hide = True
    group_input_034.outputs[20].hide = True
    group_input_034.outputs[21].hide = True
    group_input_034.outputs[22].hide = True
    group_input_034.outputs[23].hide = True
    group_input_034.outputs[24].hide = True
    group_input_034.outputs[25].hide = True
    group_input_034.outputs[26].hide = True
    group_input_034.outputs[27].hide = True
    group_input_034.outputs[28].hide = True
    group_input_034.outputs[29].hide = True
    group_input_034.outputs[30].hide = True
    group_input_034.outputs[31].hide = True
    group_input_034.outputs[32].hide = True
    group_input_034.outputs[33].hide = True
    group_input_034.outputs[34].hide = True
    group_input_034.outputs[35].hide = True
    group_input_034.outputs[36].hide = True
    group_input_034.outputs[37].hide = True
    group_input_034.outputs[38].hide = True
    group_input_034.outputs[39].hide = True
    group_input_034.outputs[40].hide = True
    group_input_034.outputs[41].hide = True
    group_input_034.outputs[42].hide = True
    group_input_034.outputs[43].hide = True
    group_input_034.outputs[44].hide = True
    group_input_034.outputs[45].hide = True
    group_input_034.outputs[46].hide = True
    group_input_034.outputs[47].hide = True
    group_input_034.outputs[48].hide = True
    group_input_034.outputs[49].hide = True
    group_input_034.outputs[50].hide = True
    group_input_034.outputs[51].hide = True
    group_input_034.outputs[52].hide = True
    group_input_034.outputs[53].hide = True
    group_input_034.outputs[54].hide = True
    group_input_034.outputs[55].hide = True
    group_input_034.outputs[56].hide = True
    group_input_034.outputs[57].hide = True
    group_input_034.outputs[58].hide = True

    # node Geometry to Instance
    geometry_to_instance = pattern_generator.nodes.new("GeometryNodeGeometryToInstance")
    geometry_to_instance.name = "Geometry to Instance"

    # node Store Named Attribute.001
    store_named_attribute_001 = pattern_generator.nodes.new(
        "GeometryNodeStoreNamedAttribute"
    )
    store_named_attribute_001.name = "Store Named Attribute.001"
    store_named_attribute_001.data_type = "FLOAT"
    store_named_attribute_001.domain = "POINT"
    store_named_attribute_001.inputs[1].hide = True
    store_named_attribute_001.inputs[2].hide = True
    # Selection
    store_named_attribute_001.inputs[1].default_value = True
    # Name
    store_named_attribute_001.inputs[2].default_value = "Emission Stenght"

    # node Group Input.038
    group_input_038 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_038.name = "Group Input.038"
    group_input_038.outputs[0].hide = True
    group_input_038.outputs[1].hide = True
    group_input_038.outputs[2].hide = True
    group_input_038.outputs[3].hide = True
    group_input_038.outputs[4].hide = True
    group_input_038.outputs[5].hide = True
    group_input_038.outputs[6].hide = True
    group_input_038.outputs[7].hide = True
    group_input_038.outputs[8].hide = True
    group_input_038.outputs[9].hide = True
    group_input_038.outputs[10].hide = True
    group_input_038.outputs[11].hide = True
    group_input_038.outputs[12].hide = True
    group_input_038.outputs[13].hide = True
    group_input_038.outputs[14].hide = True
    group_input_038.outputs[15].hide = True
    group_input_038.outputs[16].hide = True
    group_input_038.outputs[17].hide = True
    group_input_038.outputs[18].hide = True
    group_input_038.outputs[19].hide = True
    group_input_038.outputs[20].hide = True
    group_input_038.outputs[21].hide = True
    group_input_038.outputs[22].hide = True
    group_input_038.outputs[23].hide = True
    group_input_038.outputs[24].hide = True
    group_input_038.outputs[25].hide = True
    group_input_038.outputs[26].hide = True
    group_input_038.outputs[27].hide = True
    group_input_038.outputs[28].hide = True
    group_input_038.outputs[29].hide = True
    group_input_038.outputs[30].hide = True
    group_input_038.outputs[32].hide = True
    group_input_038.outputs[33].hide = True
    group_input_038.outputs[34].hide = True
    group_input_038.outputs[35].hide = True
    group_input_038.outputs[36].hide = True
    group_input_038.outputs[37].hide = True
    group_input_038.outputs[38].hide = True
    group_input_038.outputs[39].hide = True
    group_input_038.outputs[40].hide = True
    group_input_038.outputs[41].hide = True
    group_input_038.outputs[42].hide = True
    group_input_038.outputs[43].hide = True
    group_input_038.outputs[44].hide = True
    group_input_038.outputs[45].hide = True
    group_input_038.outputs[46].hide = True
    group_input_038.outputs[47].hide = True
    group_input_038.outputs[48].hide = True
    group_input_038.outputs[49].hide = True
    group_input_038.outputs[50].hide = True
    group_input_038.outputs[51].hide = True
    group_input_038.outputs[52].hide = True
    group_input_038.outputs[53].hide = True
    group_input_038.outputs[54].hide = True
    group_input_038.outputs[55].hide = True
    group_input_038.outputs[56].hide = True
    group_input_038.outputs[57].hide = True
    group_input_038.outputs[58].hide = True

    # node Curve to Mesh.005
    curve_to_mesh_005 = pattern_generator.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh_005.name = "Curve to Mesh.005"
    curve_to_mesh_005.inputs[1].hide = True
    curve_to_mesh_005.inputs[2].hide = True
    # Fill Caps
    curve_to_mesh_005.inputs[2].default_value = False

    # node Realize Instances.008
    realize_instances_008 = pattern_generator.nodes.new("GeometryNodeRealizeInstances")
    realize_instances_008.name = "Realize Instances.008"
    realize_instances_008.inputs[1].hide = True
    realize_instances_008.inputs[2].hide = True
    realize_instances_008.inputs[3].hide = True
    # Selection
    realize_instances_008.inputs[1].default_value = True
    # Realize All
    realize_instances_008.inputs[2].default_value = True
    # Depth
    realize_instances_008.inputs[3].default_value = 0

    # node Attribute Statistic.003
    attribute_statistic_003 = pattern_generator.nodes.new(
        "GeometryNodeAttributeStatistic"
    )
    attribute_statistic_003.name = "Attribute Statistic.003"
    attribute_statistic_003.data_type = "FLOAT"
    attribute_statistic_003.domain = "POINT"
    attribute_statistic_003.inputs[1].hide = True
    attribute_statistic_003.outputs[0].hide = True
    attribute_statistic_003.outputs[1].hide = True
    attribute_statistic_003.outputs[2].hide = True
    attribute_statistic_003.outputs[3].hide = True
    attribute_statistic_003.outputs[4].hide = True
    attribute_statistic_003.outputs[6].hide = True
    attribute_statistic_003.outputs[7].hide = True
    # Selection
    attribute_statistic_003.inputs[1].default_value = True

    # node Position.003
    position_003 = pattern_generator.nodes.new("GeometryNodeInputPosition")
    position_003.name = "Position.003"

    # node Separate XYZ.001
    separate_xyz_001 = pattern_generator.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_001.name = "Separate XYZ.001"
    separate_xyz_001.outputs[1].hide = True
    separate_xyz_001.outputs[2].hide = True

    # node Math.024
    math_024 = pattern_generator.nodes.new("ShaderNodeMath")
    math_024.name = "Math.024"
    math_024.operation = "CEIL"
    math_024.use_clamp = False
    math_024.inputs[1].hide = True
    math_024.inputs[2].hide = True

    # node Math.025
    math_025 = pattern_generator.nodes.new("ShaderNodeMath")
    math_025.label = "Size X"
    math_025.name = "Math.025"
    math_025.operation = "ADD"
    math_025.use_clamp = False
    math_025.inputs[1].hide = True
    math_025.inputs[2].hide = True
    # Value_001
    math_025.inputs[1].default_value = 2.0

    # node Math.026
    math_026 = pattern_generator.nodes.new("ShaderNodeMath")
    math_026.label = "Size Y"
    math_026.name = "Math.026"
    math_026.operation = "ADD"
    math_026.use_clamp = False
    math_026.inputs[1].hide = True
    math_026.inputs[2].hide = True
    # Value_001
    math_026.inputs[1].default_value = 2.0

    # node Math.027
    math_027 = pattern_generator.nodes.new("ShaderNodeMath")
    math_027.name = "Math.027"
    math_027.operation = "ADD"
    math_027.use_clamp = False
    math_027.inputs[1].hide = True
    math_027.inputs[2].hide = True
    # Value_001
    math_027.inputs[1].default_value = 1.0

    # node Math.028
    math_028 = pattern_generator.nodes.new("ShaderNodeMath")
    math_028.name = "Math.028"
    math_028.operation = "ADD"
    math_028.use_clamp = False
    math_028.inputs[1].hide = True
    math_028.inputs[2].hide = True
    # Value_001
    math_028.inputs[1].default_value = 1.0

    # node Grid.002
    grid_002 = pattern_generator.nodes.new("GeometryNodeMeshGrid")
    grid_002.name = "Grid.002"
    grid_002.outputs[1].hide = True

    # node String to Curves.003
    string_to_curves_003 = pattern_generator.nodes.new("GeometryNodeStringToCurves")
    string_to_curves_003.name = "String to Curves.003"
    string_to_curves_003.align_x = "CENTER"
    string_to_curves_003.align_y = "MIDDLE"
    string_to_curves_003.overflow = "OVERFLOW"
    string_to_curves_003.pivot_mode = "BOTTOM_LEFT"
    string_to_curves_003.inputs[3].hide = True
    string_to_curves_003.inputs[4].hide = True
    string_to_curves_003.inputs[5].hide = True
    string_to_curves_003.inputs[6].hide = True
    string_to_curves_003.outputs[1].hide = True
    string_to_curves_003.outputs[2].hide = True
    string_to_curves_003.outputs[3].hide = True
    # Word Spacing
    string_to_curves_003.inputs[3].default_value = 1.0
    # Line Spacing
    string_to_curves_003.inputs[4].default_value = 1.0
    # Text Box Width
    string_to_curves_003.inputs[5].default_value = 0.0

    # node Fill Curve.002
    fill_curve_002 = pattern_generator.nodes.new("GeometryNodeFillCurve")
    fill_curve_002.name = "Fill Curve.002"
    fill_curve_002.mode = "NGONS"
    fill_curve_002.inputs[1].hide = True
    # Group ID
    fill_curve_002.inputs[1].default_value = 0

    # node Group Input.044
    group_input_044 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_044.name = "Group Input.044"
    group_input_044.outputs[0].hide = True
    group_input_044.outputs[1].hide = True
    group_input_044.outputs[2].hide = True
    group_input_044.outputs[3].hide = True
    group_input_044.outputs[4].hide = True
    group_input_044.outputs[5].hide = True
    group_input_044.outputs[6].hide = True
    group_input_044.outputs[7].hide = True
    group_input_044.outputs[8].hide = True
    group_input_044.outputs[9].hide = True
    group_input_044.outputs[10].hide = True
    group_input_044.outputs[11].hide = True
    group_input_044.outputs[12].hide = True
    group_input_044.outputs[13].hide = True
    group_input_044.outputs[14].hide = True
    group_input_044.outputs[15].hide = True
    group_input_044.outputs[16].hide = True
    group_input_044.outputs[17].hide = True
    group_input_044.outputs[18].hide = True
    group_input_044.outputs[19].hide = True
    group_input_044.outputs[20].hide = True
    group_input_044.outputs[21].hide = True
    group_input_044.outputs[22].hide = True
    group_input_044.outputs[23].hide = True
    group_input_044.outputs[24].hide = True
    group_input_044.outputs[26].hide = True
    group_input_044.outputs[27].hide = True
    group_input_044.outputs[28].hide = True
    group_input_044.outputs[29].hide = True
    group_input_044.outputs[30].hide = True
    group_input_044.outputs[31].hide = True
    group_input_044.outputs[32].hide = True
    group_input_044.outputs[33].hide = True
    group_input_044.outputs[34].hide = True
    group_input_044.outputs[35].hide = True
    group_input_044.outputs[36].hide = True
    group_input_044.outputs[37].hide = True
    group_input_044.outputs[38].hide = True
    group_input_044.outputs[39].hide = True
    group_input_044.outputs[40].hide = True
    group_input_044.outputs[41].hide = True
    group_input_044.outputs[42].hide = True
    group_input_044.outputs[43].hide = True
    group_input_044.outputs[44].hide = True
    group_input_044.outputs[45].hide = True
    group_input_044.outputs[46].hide = True
    group_input_044.outputs[47].hide = True
    group_input_044.outputs[48].hide = True
    group_input_044.outputs[49].hide = True
    group_input_044.outputs[50].hide = True
    group_input_044.outputs[51].hide = True
    group_input_044.outputs[52].hide = True
    group_input_044.outputs[53].hide = True
    group_input_044.outputs[54].hide = True
    group_input_044.outputs[55].hide = True
    group_input_044.outputs[56].hide = True
    group_input_044.outputs[57].hide = True
    group_input_044.outputs[58].hide = True

    # node Group Input.045
    group_input_045 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_045.name = "Group Input.045"
    group_input_045.outputs[0].hide = True
    group_input_045.outputs[1].hide = True
    group_input_045.outputs[2].hide = True
    group_input_045.outputs[3].hide = True
    group_input_045.outputs[4].hide = True
    group_input_045.outputs[5].hide = True
    group_input_045.outputs[6].hide = True
    group_input_045.outputs[7].hide = True
    group_input_045.outputs[8].hide = True
    group_input_045.outputs[9].hide = True
    group_input_045.outputs[10].hide = True
    group_input_045.outputs[11].hide = True
    group_input_045.outputs[12].hide = True
    group_input_045.outputs[13].hide = True
    group_input_045.outputs[14].hide = True
    group_input_045.outputs[15].hide = True
    group_input_045.outputs[16].hide = True
    group_input_045.outputs[17].hide = True
    group_input_045.outputs[18].hide = True
    group_input_045.outputs[19].hide = True
    group_input_045.outputs[20].hide = True
    group_input_045.outputs[21].hide = True
    group_input_045.outputs[22].hide = True
    group_input_045.outputs[23].hide = True
    group_input_045.outputs[24].hide = True
    group_input_045.outputs[25].hide = True
    group_input_045.outputs[27].hide = True
    group_input_045.outputs[28].hide = True
    group_input_045.outputs[29].hide = True
    group_input_045.outputs[30].hide = True
    group_input_045.outputs[31].hide = True
    group_input_045.outputs[32].hide = True
    group_input_045.outputs[33].hide = True
    group_input_045.outputs[34].hide = True
    group_input_045.outputs[35].hide = True
    group_input_045.outputs[36].hide = True
    group_input_045.outputs[37].hide = True
    group_input_045.outputs[38].hide = True
    group_input_045.outputs[39].hide = True
    group_input_045.outputs[40].hide = True
    group_input_045.outputs[41].hide = True
    group_input_045.outputs[42].hide = True
    group_input_045.outputs[43].hide = True
    group_input_045.outputs[44].hide = True
    group_input_045.outputs[45].hide = True
    group_input_045.outputs[46].hide = True
    group_input_045.outputs[47].hide = True
    group_input_045.outputs[48].hide = True
    group_input_045.outputs[49].hide = True
    group_input_045.outputs[50].hide = True
    group_input_045.outputs[51].hide = True
    group_input_045.outputs[52].hide = True
    group_input_045.outputs[53].hide = True
    group_input_045.outputs[54].hide = True
    group_input_045.outputs[55].hide = True
    group_input_045.outputs[56].hide = True
    group_input_045.outputs[57].hide = True
    group_input_045.outputs[58].hide = True

    # node Group Input.046
    group_input_046 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_046.name = "Group Input.046"
    group_input_046.outputs[0].hide = True
    group_input_046.outputs[1].hide = True
    group_input_046.outputs[2].hide = True
    group_input_046.outputs[3].hide = True
    group_input_046.outputs[4].hide = True
    group_input_046.outputs[5].hide = True
    group_input_046.outputs[6].hide = True
    group_input_046.outputs[7].hide = True
    group_input_046.outputs[8].hide = True
    group_input_046.outputs[9].hide = True
    group_input_046.outputs[10].hide = True
    group_input_046.outputs[11].hide = True
    group_input_046.outputs[12].hide = True
    group_input_046.outputs[13].hide = True
    group_input_046.outputs[14].hide = True
    group_input_046.outputs[15].hide = True
    group_input_046.outputs[16].hide = True
    group_input_046.outputs[17].hide = True
    group_input_046.outputs[18].hide = True
    group_input_046.outputs[19].hide = True
    group_input_046.outputs[20].hide = True
    group_input_046.outputs[21].hide = True
    group_input_046.outputs[22].hide = True
    group_input_046.outputs[23].hide = True
    group_input_046.outputs[25].hide = True
    group_input_046.outputs[26].hide = True
    group_input_046.outputs[27].hide = True
    group_input_046.outputs[28].hide = True
    group_input_046.outputs[29].hide = True
    group_input_046.outputs[30].hide = True
    group_input_046.outputs[31].hide = True
    group_input_046.outputs[32].hide = True
    group_input_046.outputs[33].hide = True
    group_input_046.outputs[34].hide = True
    group_input_046.outputs[35].hide = True
    group_input_046.outputs[36].hide = True
    group_input_046.outputs[37].hide = True
    group_input_046.outputs[38].hide = True
    group_input_046.outputs[39].hide = True
    group_input_046.outputs[40].hide = True
    group_input_046.outputs[41].hide = True
    group_input_046.outputs[42].hide = True
    group_input_046.outputs[43].hide = True
    group_input_046.outputs[44].hide = True
    group_input_046.outputs[45].hide = True
    group_input_046.outputs[46].hide = True
    group_input_046.outputs[47].hide = True
    group_input_046.outputs[48].hide = True
    group_input_046.outputs[49].hide = True
    group_input_046.outputs[50].hide = True
    group_input_046.outputs[51].hide = True
    group_input_046.outputs[52].hide = True
    group_input_046.outputs[53].hide = True
    group_input_046.outputs[54].hide = True
    group_input_046.outputs[55].hide = True
    group_input_046.outputs[56].hide = True
    group_input_046.outputs[57].hide = True
    group_input_046.outputs[58].hide = True

    # node Math.029
    math_029 = pattern_generator.nodes.new("ShaderNodeMath")
    math_029.name = "Math.029"
    math_029.operation = "ADD"
    math_029.use_clamp = False
    math_029.inputs[1].hide = True
    math_029.inputs[2].hide = True
    # Value_001
    math_029.inputs[1].default_value = 1.0

    # node Attribute Statistic.006
    attribute_statistic_006 = pattern_generator.nodes.new(
        "GeometryNodeAttributeStatistic"
    )
    attribute_statistic_006.name = "Attribute Statistic.006"
    attribute_statistic_006.data_type = "FLOAT"
    attribute_statistic_006.domain = "POINT"
    attribute_statistic_006.inputs[1].hide = True
    attribute_statistic_006.outputs[0].hide = True
    attribute_statistic_006.outputs[1].hide = True
    attribute_statistic_006.outputs[2].hide = True
    attribute_statistic_006.outputs[3].hide = True
    attribute_statistic_006.outputs[4].hide = True
    attribute_statistic_006.outputs[6].hide = True
    attribute_statistic_006.outputs[7].hide = True
    # Selection
    attribute_statistic_006.inputs[1].default_value = True

    # node Position.006
    position_006 = pattern_generator.nodes.new("GeometryNodeInputPosition")
    position_006.name = "Position.006"

    # node Separate XYZ.002
    separate_xyz_002 = pattern_generator.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_002.name = "Separate XYZ.002"
    separate_xyz_002.outputs[0].hide = True
    separate_xyz_002.outputs[2].hide = True

    # node Math.030
    math_030 = pattern_generator.nodes.new("ShaderNodeMath")
    math_030.name = "Math.030"
    math_030.operation = "CEIL"
    math_030.use_clamp = False
    math_030.inputs[1].hide = True
    math_030.inputs[2].hide = True

    # node Scale Instances
    scale_instances = pattern_generator.nodes.new("GeometryNodeScaleInstances")
    scale_instances.name = "Scale Instances"
    scale_instances.inputs[1].hide = True
    scale_instances.inputs[3].hide = True
    scale_instances.inputs[4].hide = True
    # Selection
    scale_instances.inputs[1].default_value = True
    # Center
    scale_instances.inputs[3].default_value = (0.0, 0.0, 0.0)
    # Local Space
    scale_instances.inputs[4].default_value = False

    # node Group Input.037
    group_input_037 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_037.name = "Group Input.037"
    group_input_037.outputs[0].hide = True
    group_input_037.outputs[1].hide = True
    group_input_037.outputs[2].hide = True
    group_input_037.outputs[3].hide = True
    group_input_037.outputs[4].hide = True
    group_input_037.outputs[5].hide = True
    group_input_037.outputs[6].hide = True
    group_input_037.outputs[7].hide = True
    group_input_037.outputs[8].hide = True
    group_input_037.outputs[9].hide = True
    group_input_037.outputs[10].hide = True
    group_input_037.outputs[11].hide = True
    group_input_037.outputs[12].hide = True
    group_input_037.outputs[13].hide = True
    group_input_037.outputs[14].hide = True
    group_input_037.outputs[15].hide = True
    group_input_037.outputs[16].hide = True
    group_input_037.outputs[17].hide = True
    group_input_037.outputs[18].hide = True
    group_input_037.outputs[19].hide = True
    group_input_037.outputs[20].hide = True
    group_input_037.outputs[21].hide = True
    group_input_037.outputs[22].hide = True
    group_input_037.outputs[23].hide = True
    group_input_037.outputs[24].hide = True
    group_input_037.outputs[25].hide = True
    group_input_037.outputs[26].hide = True
    group_input_037.outputs[28].hide = True
    group_input_037.outputs[29].hide = True
    group_input_037.outputs[30].hide = True
    group_input_037.outputs[31].hide = True
    group_input_037.outputs[32].hide = True
    group_input_037.outputs[33].hide = True
    group_input_037.outputs[34].hide = True
    group_input_037.outputs[35].hide = True
    group_input_037.outputs[36].hide = True
    group_input_037.outputs[37].hide = True
    group_input_037.outputs[38].hide = True
    group_input_037.outputs[39].hide = True
    group_input_037.outputs[40].hide = True
    group_input_037.outputs[41].hide = True
    group_input_037.outputs[42].hide = True
    group_input_037.outputs[43].hide = True
    group_input_037.outputs[44].hide = True
    group_input_037.outputs[45].hide = True
    group_input_037.outputs[46].hide = True
    group_input_037.outputs[47].hide = True
    group_input_037.outputs[48].hide = True
    group_input_037.outputs[49].hide = True
    group_input_037.outputs[50].hide = True
    group_input_037.outputs[51].hide = True
    group_input_037.outputs[52].hide = True
    group_input_037.outputs[53].hide = True
    group_input_037.outputs[54].hide = True
    group_input_037.outputs[55].hide = True
    group_input_037.outputs[56].hide = True
    group_input_037.outputs[57].hide = True
    group_input_037.outputs[58].hide = True

    # node Named Attribute.001
    named_attribute_001 = pattern_generator.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_001.name = "Named Attribute.001"
    named_attribute_001.data_type = "FLOAT"
    named_attribute_001.inputs[0].hide = True
    named_attribute_001.outputs[1].hide = True
    # Name
    named_attribute_001.inputs[0].default_value = "value_not_deleted"

    # node Join Geometry.005
    join_geometry_005 = pattern_generator.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_005.name = "Join Geometry.005"

    # node Delete Geometry.005
    delete_geometry_005 = pattern_generator.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_005.name = "Delete Geometry.005"
    delete_geometry_005.domain = "POINT"
    delete_geometry_005.mode = "ALL"

    # node Named Attribute.002
    named_attribute_002 = pattern_generator.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_002.name = "Named Attribute.002"
    named_attribute_002.data_type = "FLOAT"
    named_attribute_002.inputs[0].hide = True
    named_attribute_002.outputs[1].hide = True
    # Name
    named_attribute_002.inputs[0].default_value = "value_not_deleted"

    # node Boolean Math.001
    boolean_math_001_1 = pattern_generator.nodes.new("FunctionNodeBooleanMath")
    boolean_math_001_1.name = "Boolean Math.001"
    boolean_math_001_1.operation = "NOT"
    boolean_math_001_1.inputs[1].hide = True

    # node Delete Geometry.006
    delete_geometry_006 = pattern_generator.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_006.name = "Delete Geometry.006"
    delete_geometry_006.domain = "POINT"
    delete_geometry_006.mode = "ALL"

    # node Random Value.007
    random_value_007_1 = pattern_generator.nodes.new("FunctionNodeRandomValue")
    random_value_007_1.name = "Random Value.007"
    random_value_007_1.data_type = "FLOAT"
    random_value_007_1.inputs[0].hide = True
    random_value_007_1.inputs[1].hide = True
    random_value_007_1.inputs[2].hide = True
    random_value_007_1.inputs[3].hide = True
    random_value_007_1.inputs[4].hide = True
    random_value_007_1.inputs[5].hide = True
    random_value_007_1.inputs[6].hide = True
    random_value_007_1.inputs[7].hide = True
    random_value_007_1.outputs[0].hide = True
    random_value_007_1.outputs[2].hide = True
    random_value_007_1.outputs[3].hide = True
    # Min_001
    random_value_007_1.inputs[2].default_value = 0.0
    # Max_001
    random_value_007_1.inputs[3].default_value = 1.0
    # ID
    random_value_007_1.inputs[7].default_value = 0

    # node Math.031
    math_031 = pattern_generator.nodes.new("ShaderNodeMath")
    math_031.name = "Math.031"
    math_031.operation = "MULTIPLY"
    math_031.use_clamp = False
    math_031.inputs[2].hide = True

    # node Random Value.008
    random_value_008_1 = pattern_generator.nodes.new("FunctionNodeRandomValue")
    random_value_008_1.name = "Random Value.008"
    random_value_008_1.data_type = "INT"
    random_value_008_1.inputs[0].hide = True
    random_value_008_1.inputs[1].hide = True
    random_value_008_1.inputs[2].hide = True
    random_value_008_1.inputs[3].hide = True
    random_value_008_1.inputs[4].hide = True
    random_value_008_1.inputs[5].hide = True
    random_value_008_1.inputs[6].hide = True
    random_value_008_1.inputs[7].hide = True
    random_value_008_1.outputs[0].hide = True
    random_value_008_1.outputs[1].hide = True
    random_value_008_1.outputs[3].hide = True
    # Min_002
    random_value_008_1.inputs[4].default_value = 0
    # Max_002
    random_value_008_1.inputs[5].default_value = 100
    # ID
    random_value_008_1.inputs[7].default_value = 0

    # node Group Input.042
    group_input_042 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_042.name = "Group Input.042"
    group_input_042.outputs[0].hide = True
    group_input_042.outputs[1].hide = True
    group_input_042.outputs[2].hide = True
    group_input_042.outputs[3].hide = True
    group_input_042.outputs[4].hide = True
    group_input_042.outputs[5].hide = True
    group_input_042.outputs[6].hide = True
    group_input_042.outputs[7].hide = True
    group_input_042.outputs[8].hide = True
    group_input_042.outputs[9].hide = True
    group_input_042.outputs[10].hide = True
    group_input_042.outputs[11].hide = True
    group_input_042.outputs[12].hide = True
    group_input_042.outputs[14].hide = True
    group_input_042.outputs[15].hide = True
    group_input_042.outputs[16].hide = True
    group_input_042.outputs[17].hide = True
    group_input_042.outputs[18].hide = True
    group_input_042.outputs[19].hide = True
    group_input_042.outputs[20].hide = True
    group_input_042.outputs[21].hide = True
    group_input_042.outputs[22].hide = True
    group_input_042.outputs[23].hide = True
    group_input_042.outputs[24].hide = True
    group_input_042.outputs[25].hide = True
    group_input_042.outputs[26].hide = True
    group_input_042.outputs[27].hide = True
    group_input_042.outputs[28].hide = True
    group_input_042.outputs[29].hide = True
    group_input_042.outputs[30].hide = True
    group_input_042.outputs[31].hide = True
    group_input_042.outputs[32].hide = True
    group_input_042.outputs[33].hide = True
    group_input_042.outputs[34].hide = True
    group_input_042.outputs[35].hide = True
    group_input_042.outputs[36].hide = True
    group_input_042.outputs[37].hide = True
    group_input_042.outputs[38].hide = True
    group_input_042.outputs[39].hide = True
    group_input_042.outputs[40].hide = True
    group_input_042.outputs[41].hide = True
    group_input_042.outputs[42].hide = True
    group_input_042.outputs[43].hide = True
    group_input_042.outputs[44].hide = True
    group_input_042.outputs[45].hide = True
    group_input_042.outputs[46].hide = True
    group_input_042.outputs[47].hide = True
    group_input_042.outputs[48].hide = True
    group_input_042.outputs[49].hide = True
    group_input_042.outputs[50].hide = True
    group_input_042.outputs[51].hide = True
    group_input_042.outputs[52].hide = True
    group_input_042.outputs[53].hide = True
    group_input_042.outputs[54].hide = True
    group_input_042.outputs[55].hide = True
    group_input_042.outputs[56].hide = True
    group_input_042.outputs[57].hide = True
    group_input_042.outputs[58].hide = True

    # node Switch.010
    switch_010_1 = pattern_generator.nodes.new("GeometryNodeSwitch")
    switch_010_1.name = "Switch.010"
    switch_010_1.input_type = "FLOAT"

    # node Random Value.009
    random_value_009_1 = pattern_generator.nodes.new("FunctionNodeRandomValue")
    random_value_009_1.name = "Random Value.009"
    random_value_009_1.data_type = "FLOAT"
    random_value_009_1.inputs[0].hide = True
    random_value_009_1.inputs[1].hide = True
    random_value_009_1.inputs[2].hide = True
    random_value_009_1.inputs[3].hide = True
    random_value_009_1.inputs[4].hide = True
    random_value_009_1.inputs[5].hide = True
    random_value_009_1.inputs[6].hide = True
    random_value_009_1.inputs[7].hide = True
    random_value_009_1.outputs[0].hide = True
    random_value_009_1.outputs[2].hide = True
    random_value_009_1.outputs[3].hide = True
    # Min_001
    random_value_009_1.inputs[2].default_value = 0.0
    # Max_001
    random_value_009_1.inputs[3].default_value = 1.0
    # ID
    random_value_009_1.inputs[7].default_value = 0

    # node Math.033
    math_033 = pattern_generator.nodes.new("ShaderNodeMath")
    math_033.name = "Math.033"
    math_033.operation = "SUBTRACT"
    math_033.use_clamp = False
    math_033.inputs[0].hide = True
    math_033.inputs[2].hide = True
    # Value
    math_033.inputs[0].default_value = 1.0

    # node Math.034
    math_034 = pattern_generator.nodes.new("ShaderNodeMath")
    math_034.name = "Math.034"
    math_034.operation = "MULTIPLY"
    math_034.use_clamp = False
    math_034.inputs[2].hide = True

    # node Math.035
    math_035 = pattern_generator.nodes.new("ShaderNodeMath")
    math_035.name = "Math.035"
    math_035.operation = "ADD"
    math_035.use_clamp = False
    math_035.inputs[2].hide = True

    # node Math.036
    math_036 = pattern_generator.nodes.new("ShaderNodeMath")
    math_036.name = "Math.036"
    math_036.operation = "MULTIPLY"
    math_036.use_clamp = False
    math_036.inputs[2].hide = True

    # node Group Input.043
    group_input_043 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_043.name = "Group Input.043"
    group_input_043.outputs[0].hide = True
    group_input_043.outputs[1].hide = True
    group_input_043.outputs[2].hide = True
    group_input_043.outputs[3].hide = True
    group_input_043.outputs[4].hide = True
    group_input_043.outputs[5].hide = True
    group_input_043.outputs[6].hide = True
    group_input_043.outputs[7].hide = True
    group_input_043.outputs[8].hide = True
    group_input_043.outputs[9].hide = True
    group_input_043.outputs[10].hide = True
    group_input_043.outputs[11].hide = True
    group_input_043.outputs[12].hide = True
    group_input_043.outputs[14].hide = True
    group_input_043.outputs[15].hide = True
    group_input_043.outputs[16].hide = True
    group_input_043.outputs[17].hide = True
    group_input_043.outputs[18].hide = True
    group_input_043.outputs[19].hide = True
    group_input_043.outputs[20].hide = True
    group_input_043.outputs[21].hide = True
    group_input_043.outputs[22].hide = True
    group_input_043.outputs[23].hide = True
    group_input_043.outputs[24].hide = True
    group_input_043.outputs[25].hide = True
    group_input_043.outputs[26].hide = True
    group_input_043.outputs[27].hide = True
    group_input_043.outputs[28].hide = True
    group_input_043.outputs[29].hide = True
    group_input_043.outputs[30].hide = True
    group_input_043.outputs[31].hide = True
    group_input_043.outputs[32].hide = True
    group_input_043.outputs[33].hide = True
    group_input_043.outputs[34].hide = True
    group_input_043.outputs[35].hide = True
    group_input_043.outputs[36].hide = True
    group_input_043.outputs[37].hide = True
    group_input_043.outputs[38].hide = True
    group_input_043.outputs[39].hide = True
    group_input_043.outputs[40].hide = True
    group_input_043.outputs[41].hide = True
    group_input_043.outputs[42].hide = True
    group_input_043.outputs[43].hide = True
    group_input_043.outputs[44].hide = True
    group_input_043.outputs[45].hide = True
    group_input_043.outputs[46].hide = True
    group_input_043.outputs[47].hide = True
    group_input_043.outputs[48].hide = True
    group_input_043.outputs[49].hide = True
    group_input_043.outputs[50].hide = True
    group_input_043.outputs[51].hide = True
    group_input_043.outputs[52].hide = True
    group_input_043.outputs[53].hide = True
    group_input_043.outputs[54].hide = True
    group_input_043.outputs[55].hide = True
    group_input_043.outputs[56].hide = True
    group_input_043.outputs[57].hide = True
    group_input_043.outputs[58].hide = True

    # node Switch.011
    switch_011_1 = pattern_generator.nodes.new("GeometryNodeSwitch")
    switch_011_1.name = "Switch.011"
    switch_011_1.input_type = "FLOAT"

    # node Math.032
    math_032 = pattern_generator.nodes.new("ShaderNodeMath")
    math_032.name = "Math.032"
    math_032.operation = "SUBTRACT"
    math_032.use_clamp = False
    math_032.inputs[0].hide = True
    math_032.inputs[2].hide = True
    # Value
    math_032.inputs[0].default_value = 1.0

    # node Math.037
    math_037 = pattern_generator.nodes.new("ShaderNodeMath")
    math_037.name = "Math.037"
    math_037.operation = "SUBTRACT"
    math_037.use_clamp = False
    math_037.inputs[2].hide = True

    # node Math.038
    math_038 = pattern_generator.nodes.new("ShaderNodeMath")
    math_038.name = "Math.038"
    math_038.operation = "ABSOLUTE"
    math_038.use_clamp = False
    math_038.inputs[1].hide = True
    math_038.inputs[2].hide = True

    # node Group Output.001
    group_output_001 = pattern_generator.nodes.new("NodeGroupOutput")
    group_output_001.name = "Group Output.001"
    group_output_001.is_active_output = True
    group_output_001.inputs[1].hide = True

    # node Merge by Distance
    merge_by_distance = pattern_generator.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance.name = "Merge by Distance"
    merge_by_distance.mode = "ALL"

    # node Group Input.050
    group_input_050 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_050.name = "Group Input.050"
    group_input_050.outputs[0].hide = True
    group_input_050.outputs[1].hide = True
    group_input_050.outputs[2].hide = True
    group_input_050.outputs[3].hide = True
    group_input_050.outputs[4].hide = True
    group_input_050.outputs[5].hide = True
    group_input_050.outputs[6].hide = True
    group_input_050.outputs[7].hide = True
    group_input_050.outputs[8].hide = True
    group_input_050.outputs[9].hide = True
    group_input_050.outputs[10].hide = True
    group_input_050.outputs[11].hide = True
    group_input_050.outputs[12].hide = True
    group_input_050.outputs[13].hide = True
    group_input_050.outputs[14].hide = True
    group_input_050.outputs[15].hide = True
    group_input_050.outputs[16].hide = True
    group_input_050.outputs[17].hide = True
    group_input_050.outputs[18].hide = True
    group_input_050.outputs[19].hide = True
    group_input_050.outputs[20].hide = True
    group_input_050.outputs[22].hide = True
    group_input_050.outputs[23].hide = True
    group_input_050.outputs[24].hide = True
    group_input_050.outputs[25].hide = True
    group_input_050.outputs[26].hide = True
    group_input_050.outputs[27].hide = True
    group_input_050.outputs[28].hide = True
    group_input_050.outputs[29].hide = True
    group_input_050.outputs[30].hide = True
    group_input_050.outputs[31].hide = True
    group_input_050.outputs[32].hide = True
    group_input_050.outputs[33].hide = True
    group_input_050.outputs[34].hide = True
    group_input_050.outputs[35].hide = True
    group_input_050.outputs[36].hide = True
    group_input_050.outputs[37].hide = True
    group_input_050.outputs[38].hide = True
    group_input_050.outputs[39].hide = True
    group_input_050.outputs[40].hide = True
    group_input_050.outputs[41].hide = True
    group_input_050.outputs[42].hide = True
    group_input_050.outputs[43].hide = True
    group_input_050.outputs[44].hide = True
    group_input_050.outputs[45].hide = True
    group_input_050.outputs[46].hide = True
    group_input_050.outputs[47].hide = True
    group_input_050.outputs[48].hide = True
    group_input_050.outputs[49].hide = True
    group_input_050.outputs[50].hide = True
    group_input_050.outputs[51].hide = True
    group_input_050.outputs[52].hide = True
    group_input_050.outputs[53].hide = True
    group_input_050.outputs[54].hide = True
    group_input_050.outputs[55].hide = True
    group_input_050.outputs[56].hide = True
    group_input_050.outputs[57].hide = True
    group_input_050.outputs[58].hide = True

    # node Group Input.051
    group_input_051 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_051.name = "Group Input.051"
    group_input_051.outputs[0].hide = True
    group_input_051.outputs[1].hide = True
    group_input_051.outputs[2].hide = True
    group_input_051.outputs[3].hide = True
    group_input_051.outputs[4].hide = True
    group_input_051.outputs[5].hide = True
    group_input_051.outputs[6].hide = True
    group_input_051.outputs[7].hide = True
    group_input_051.outputs[8].hide = True
    group_input_051.outputs[9].hide = True
    group_input_051.outputs[10].hide = True
    group_input_051.outputs[11].hide = True
    group_input_051.outputs[12].hide = True
    group_input_051.outputs[13].hide = True
    group_input_051.outputs[14].hide = True
    group_input_051.outputs[15].hide = True
    group_input_051.outputs[16].hide = True
    group_input_051.outputs[17].hide = True
    group_input_051.outputs[18].hide = True
    group_input_051.outputs[21].hide = True
    group_input_051.outputs[22].hide = True
    group_input_051.outputs[23].hide = True
    group_input_051.outputs[24].hide = True
    group_input_051.outputs[25].hide = True
    group_input_051.outputs[26].hide = True
    group_input_051.outputs[27].hide = True
    group_input_051.outputs[28].hide = True
    group_input_051.outputs[29].hide = True
    group_input_051.outputs[30].hide = True
    group_input_051.outputs[31].hide = True
    group_input_051.outputs[32].hide = True
    group_input_051.outputs[33].hide = True
    group_input_051.outputs[34].hide = True
    group_input_051.outputs[35].hide = True
    group_input_051.outputs[36].hide = True
    group_input_051.outputs[37].hide = True
    group_input_051.outputs[38].hide = True
    group_input_051.outputs[39].hide = True
    group_input_051.outputs[40].hide = True
    group_input_051.outputs[41].hide = True
    group_input_051.outputs[42].hide = True
    group_input_051.outputs[43].hide = True
    group_input_051.outputs[44].hide = True
    group_input_051.outputs[45].hide = True
    group_input_051.outputs[46].hide = True
    group_input_051.outputs[47].hide = True
    group_input_051.outputs[48].hide = True
    group_input_051.outputs[49].hide = True
    group_input_051.outputs[50].hide = True
    group_input_051.outputs[51].hide = True
    group_input_051.outputs[52].hide = True
    group_input_051.outputs[53].hide = True
    group_input_051.outputs[54].hide = True
    group_input_051.outputs[55].hide = True
    group_input_051.outputs[56].hide = True
    group_input_051.outputs[57].hide = True
    group_input_051.outputs[58].hide = True

    # node Random Value.010
    random_value_010 = pattern_generator.nodes.new("FunctionNodeRandomValue")
    random_value_010.name = "Random Value.010"
    random_value_010.data_type = "BOOLEAN"
    random_value_010.inputs[0].hide = True
    random_value_010.inputs[1].hide = True
    random_value_010.inputs[2].hide = True
    random_value_010.inputs[3].hide = True
    random_value_010.inputs[4].hide = True
    random_value_010.inputs[5].hide = True
    random_value_010.inputs[7].hide = True
    random_value_010.outputs[0].hide = True
    random_value_010.outputs[1].hide = True
    random_value_010.outputs[2].hide = True
    # ID
    random_value_010.inputs[7].default_value = 0

    # node Merge by Distance.002
    merge_by_distance_002 = pattern_generator.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance_002.name = "Merge by Distance.002"
    merge_by_distance_002.mode = "ALL"
    merge_by_distance_002.inputs[1].hide = True
    merge_by_distance_002.inputs[2].hide = True
    # Selection
    merge_by_distance_002.inputs[1].default_value = True
    # Distance
    merge_by_distance_002.inputs[2].default_value = 0.0010000000474974513

    # node Image Texture
    image_texture_1 = pattern_generator.nodes.new("GeometryNodeImageTexture")
    image_texture_1.name = "Image Texture"
    image_texture_1.extension = "CLIP"
    image_texture_1.interpolation = "Linear"
    image_texture_1.inputs[2].hide = True
    image_texture_1.outputs[1].hide = True
    # Frame
    image_texture_1.inputs[2].default_value = 0

    # node Position.005
    position_005 = pattern_generator.nodes.new("GeometryNodeInputPosition")
    position_005.name = "Position.005"

    # node Image Info
    image_info = pattern_generator.nodes.new("GeometryNodeImageInfo")
    image_info.name = "Image Info"
    image_info.inputs[1].hide = True
    image_info.outputs[2].hide = True
    image_info.outputs[3].hide = True
    image_info.outputs[4].hide = True
    # Frame
    image_info.inputs[1].default_value = 0

    # node Vector Math.002
    vector_math_002_1 = pattern_generator.nodes.new("ShaderNodeVectorMath")
    vector_math_002_1.name = "Vector Math.002"
    vector_math_002_1.operation = "SCALE"
    vector_math_002_1.inputs[1].hide = True
    vector_math_002_1.inputs[2].hide = True
    vector_math_002_1.outputs[1].hide = True

    # node Math.039
    math_039 = pattern_generator.nodes.new("ShaderNodeMath")
    math_039.name = "Math.039"
    math_039.operation = "DIVIDE"
    math_039.use_clamp = False
    math_039.inputs[0].hide = True
    math_039.inputs[2].hide = True
    # Value
    math_039.inputs[0].default_value = 1.0

    # node Math.040
    math_040 = pattern_generator.nodes.new("ShaderNodeMath")
    math_040.name = "Math.040"
    math_040.operation = "DIVIDE"
    math_040.use_clamp = False
    math_040.inputs[0].hide = True
    math_040.inputs[2].hide = True
    # Value
    math_040.inputs[0].default_value = 1.0

    # node Combine XYZ.007
    combine_xyz_007 = pattern_generator.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_007.name = "Combine XYZ.007"
    combine_xyz_007.inputs[2].hide = True
    # Z
    combine_xyz_007.inputs[2].default_value = 1.0

    # node Vector Math.004
    vector_math_004 = pattern_generator.nodes.new("ShaderNodeVectorMath")
    vector_math_004.name = "Vector Math.004"
    vector_math_004.operation = "MULTIPLY"
    vector_math_004.inputs[2].hide = True
    vector_math_004.inputs[3].hide = True
    vector_math_004.outputs[1].hide = True

    # node Vector Math.005
    vector_math_005 = pattern_generator.nodes.new("ShaderNodeVectorMath")
    vector_math_005.name = "Vector Math.005"
    vector_math_005.operation = "ADD"
    vector_math_005.inputs[1].hide = True
    vector_math_005.inputs[2].hide = True
    vector_math_005.inputs[3].hide = True
    vector_math_005.outputs[1].hide = True
    # Vector_001
    vector_math_005.inputs[1].default_value = (0.5, 0.5, 0.5)

    # node Math.043
    math_043 = pattern_generator.nodes.new("ShaderNodeMath")
    math_043.name = "Math.043"
    math_043.operation = "DIVIDE"
    math_043.use_clamp = False
    math_043.inputs[1].hide = True
    math_043.inputs[2].hide = True
    # Value_001
    math_043.inputs[1].default_value = 0.026399999856948853

    # node Math.044
    math_044 = pattern_generator.nodes.new("ShaderNodeMath")
    math_044.name = "Math.044"
    math_044.operation = "DIVIDE"
    math_044.use_clamp = False
    math_044.inputs[1].hide = True
    math_044.inputs[2].hide = True
    # Value_001
    math_044.inputs[1].default_value = 0.026399999856948853

    # node Math.041
    math_041 = pattern_generator.nodes.new("ShaderNodeMath")
    math_041.name = "Math.041"
    math_041.operation = "MULTIPLY"
    math_041.use_clamp = False
    math_041.inputs[2].hide = True

    # node Group Input.052
    group_input_052 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_052.name = "Group Input.052"
    group_input_052.outputs[0].hide = True
    group_input_052.outputs[2].hide = True
    group_input_052.outputs[3].hide = True
    group_input_052.outputs[4].hide = True
    group_input_052.outputs[5].hide = True
    group_input_052.outputs[6].hide = True
    group_input_052.outputs[7].hide = True
    group_input_052.outputs[8].hide = True
    group_input_052.outputs[9].hide = True
    group_input_052.outputs[10].hide = True
    group_input_052.outputs[11].hide = True
    group_input_052.outputs[12].hide = True
    group_input_052.outputs[13].hide = True
    group_input_052.outputs[14].hide = True
    group_input_052.outputs[15].hide = True
    group_input_052.outputs[16].hide = True
    group_input_052.outputs[17].hide = True
    group_input_052.outputs[18].hide = True
    group_input_052.outputs[19].hide = True
    group_input_052.outputs[20].hide = True
    group_input_052.outputs[21].hide = True
    group_input_052.outputs[22].hide = True
    group_input_052.outputs[23].hide = True
    group_input_052.outputs[24].hide = True
    group_input_052.outputs[25].hide = True
    group_input_052.outputs[26].hide = True
    group_input_052.outputs[27].hide = True
    group_input_052.outputs[28].hide = True
    group_input_052.outputs[29].hide = True
    group_input_052.outputs[30].hide = True
    group_input_052.outputs[31].hide = True
    group_input_052.outputs[32].hide = True
    group_input_052.outputs[33].hide = True
    group_input_052.outputs[34].hide = True
    group_input_052.outputs[35].hide = True
    group_input_052.outputs[36].hide = True
    group_input_052.outputs[37].hide = True
    group_input_052.outputs[38].hide = True
    group_input_052.outputs[39].hide = True
    group_input_052.outputs[40].hide = True
    group_input_052.outputs[41].hide = True
    group_input_052.outputs[42].hide = True
    group_input_052.outputs[43].hide = True
    group_input_052.outputs[44].hide = True
    group_input_052.outputs[45].hide = True
    group_input_052.outputs[46].hide = True
    group_input_052.outputs[47].hide = True
    group_input_052.outputs[48].hide = True
    group_input_052.outputs[49].hide = True
    group_input_052.outputs[50].hide = True
    group_input_052.outputs[51].hide = True
    group_input_052.outputs[52].hide = True
    group_input_052.outputs[53].hide = True
    group_input_052.outputs[54].hide = True
    group_input_052.outputs[55].hide = True
    group_input_052.outputs[56].hide = True
    group_input_052.outputs[57].hide = True
    group_input_052.outputs[58].hide = True

    # node Math.042
    math_042 = pattern_generator.nodes.new("ShaderNodeMath")
    math_042.name = "Math.042"
    math_042.operation = "DIVIDE"
    math_042.use_clamp = False
    math_042.inputs[0].hide = True
    math_042.inputs[2].hide = True
    # Value
    math_042.inputs[0].default_value = 1.0

    # node Frame.005
    frame_005 = pattern_generator.nodes.new("NodeFrame")
    frame_005.label = "Curve Creation"
    frame_005.name = "Frame.005"
    frame_005.label_size = 20
    frame_005.shrink = True

    # node Frame.006
    frame_006 = pattern_generator.nodes.new("NodeFrame")
    frame_006.label = "Image Progression"
    frame_006.name = "Frame.006"
    frame_006.label_size = 20
    frame_006.shrink = True

    # node Frame.007
    frame_007 = pattern_generator.nodes.new("NodeFrame")
    frame_007.label = "Creating Size"
    frame_007.name = "Frame.007"
    frame_007.label_size = 20
    frame_007.shrink = True

    # node Group Input.049
    group_input_049 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_049.name = "Group Input.049"
    group_input_049.outputs[0].hide = True
    group_input_049.outputs[1].hide = True
    group_input_049.outputs[2].hide = True
    group_input_049.outputs[3].hide = True
    group_input_049.outputs[4].hide = True
    group_input_049.outputs[5].hide = True
    group_input_049.outputs[6].hide = True
    group_input_049.outputs[7].hide = True
    group_input_049.outputs[8].hide = True
    group_input_049.outputs[9].hide = True
    group_input_049.outputs[10].hide = True
    group_input_049.outputs[11].hide = True
    group_input_049.outputs[12].hide = True
    group_input_049.outputs[13].hide = True
    group_input_049.outputs[14].hide = True
    group_input_049.outputs[15].hide = True
    group_input_049.outputs[16].hide = True
    group_input_049.outputs[17].hide = True
    group_input_049.outputs[18].hide = True
    group_input_049.outputs[19].hide = True
    group_input_049.outputs[20].hide = True
    group_input_049.outputs[21].hide = True
    group_input_049.outputs[23].hide = True
    group_input_049.outputs[24].hide = True
    group_input_049.outputs[25].hide = True
    group_input_049.outputs[26].hide = True
    group_input_049.outputs[27].hide = True
    group_input_049.outputs[28].hide = True
    group_input_049.outputs[29].hide = True
    group_input_049.outputs[30].hide = True
    group_input_049.outputs[31].hide = True
    group_input_049.outputs[32].hide = True
    group_input_049.outputs[33].hide = True
    group_input_049.outputs[34].hide = True
    group_input_049.outputs[35].hide = True
    group_input_049.outputs[36].hide = True
    group_input_049.outputs[37].hide = True
    group_input_049.outputs[38].hide = True
    group_input_049.outputs[39].hide = True
    group_input_049.outputs[40].hide = True
    group_input_049.outputs[41].hide = True
    group_input_049.outputs[42].hide = True
    group_input_049.outputs[43].hide = True
    group_input_049.outputs[44].hide = True
    group_input_049.outputs[45].hide = True
    group_input_049.outputs[46].hide = True
    group_input_049.outputs[47].hide = True
    group_input_049.outputs[48].hide = True
    group_input_049.outputs[49].hide = True
    group_input_049.outputs[50].hide = True
    group_input_049.outputs[51].hide = True
    group_input_049.outputs[52].hide = True
    group_input_049.outputs[53].hide = True
    group_input_049.outputs[54].hide = True
    group_input_049.outputs[55].hide = True
    group_input_049.outputs[56].hide = True
    group_input_049.outputs[57].hide = True
    group_input_049.outputs[58].hide = True

    # node Group.001
    group_001 = pattern_generator.nodes.new("GeometryNodeGroup")
    group_001.name = "Group.001"
    group_001.node_tree = method_calculation_node_group()

    # node Subdivide Mesh
    subdivide_mesh = pattern_generator.nodes.new("GeometryNodeSubdivideMesh")
    subdivide_mesh.name = "Subdivide Mesh"

    # node Group Input.028
    group_input_028_1 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_028_1.name = "Group Input.028"
    group_input_028_1.outputs[0].hide = True
    group_input_028_1.outputs[1].hide = True
    group_input_028_1.outputs[2].hide = True
    group_input_028_1.outputs[3].hide = True
    group_input_028_1.outputs[4].hide = True
    group_input_028_1.outputs[5].hide = True
    group_input_028_1.outputs[6].hide = True
    group_input_028_1.outputs[7].hide = True
    group_input_028_1.outputs[8].hide = True
    group_input_028_1.outputs[9].hide = True
    group_input_028_1.outputs[10].hide = True
    group_input_028_1.outputs[11].hide = True
    group_input_028_1.outputs[12].hide = True
    group_input_028_1.outputs[13].hide = True
    group_input_028_1.outputs[14].hide = True
    group_input_028_1.outputs[15].hide = True
    group_input_028_1.outputs[16].hide = True
    group_input_028_1.outputs[17].hide = True
    group_input_028_1.outputs[18].hide = True
    group_input_028_1.outputs[19].hide = True
    group_input_028_1.outputs[20].hide = True
    group_input_028_1.outputs[21].hide = True
    group_input_028_1.outputs[22].hide = True
    group_input_028_1.outputs[23].hide = True
    group_input_028_1.outputs[24].hide = True
    group_input_028_1.outputs[25].hide = True
    group_input_028_1.outputs[26].hide = True
    group_input_028_1.outputs[27].hide = True
    group_input_028_1.outputs[28].hide = True
    group_input_028_1.outputs[30].hide = True
    group_input_028_1.outputs[31].hide = True
    group_input_028_1.outputs[32].hide = True
    group_input_028_1.outputs[33].hide = True
    group_input_028_1.outputs[34].hide = True
    group_input_028_1.outputs[35].hide = True
    group_input_028_1.outputs[36].hide = True
    group_input_028_1.outputs[37].hide = True
    group_input_028_1.outputs[38].hide = True
    group_input_028_1.outputs[39].hide = True
    group_input_028_1.outputs[40].hide = True
    group_input_028_1.outputs[41].hide = True
    group_input_028_1.outputs[42].hide = True
    group_input_028_1.outputs[43].hide = True
    group_input_028_1.outputs[44].hide = True
    group_input_028_1.outputs[45].hide = True
    group_input_028_1.outputs[46].hide = True
    group_input_028_1.outputs[47].hide = True
    group_input_028_1.outputs[48].hide = True
    group_input_028_1.outputs[49].hide = True
    group_input_028_1.outputs[50].hide = True
    group_input_028_1.outputs[51].hide = True
    group_input_028_1.outputs[52].hide = True
    group_input_028_1.outputs[53].hide = True
    group_input_028_1.outputs[54].hide = True
    group_input_028_1.outputs[55].hide = True
    group_input_028_1.outputs[56].hide = True
    group_input_028_1.outputs[57].hide = True
    group_input_028_1.outputs[58].hide = True

    # node Vector Math.003
    vector_math_003_1 = pattern_generator.nodes.new("ShaderNodeVectorMath")
    vector_math_003_1.name = "Vector Math.003"
    vector_math_003_1.operation = "SCALE"
    vector_math_003_1.inputs[1].hide = True
    vector_math_003_1.inputs[2].hide = True
    vector_math_003_1.outputs[1].hide = True

    # node Group Input.047
    group_input_047 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_047.name = "Group Input.047"
    group_input_047.outputs[0].hide = True
    group_input_047.outputs[1].hide = True
    group_input_047.outputs[2].hide = True
    group_input_047.outputs[3].hide = True
    group_input_047.outputs[4].hide = True
    group_input_047.outputs[5].hide = True
    group_input_047.outputs[6].hide = True
    group_input_047.outputs[7].hide = True
    group_input_047.outputs[8].hide = True
    group_input_047.outputs[9].hide = True
    group_input_047.outputs[10].hide = True
    group_input_047.outputs[11].hide = True
    group_input_047.outputs[12].hide = True
    group_input_047.outputs[13].hide = True
    group_input_047.outputs[14].hide = True
    group_input_047.outputs[15].hide = True
    group_input_047.outputs[16].hide = True
    group_input_047.outputs[17].hide = True
    group_input_047.outputs[18].hide = True
    group_input_047.outputs[19].hide = True
    group_input_047.outputs[20].hide = True
    group_input_047.outputs[21].hide = True
    group_input_047.outputs[22].hide = True
    group_input_047.outputs[23].hide = True
    group_input_047.outputs[24].hide = True
    group_input_047.outputs[25].hide = True
    group_input_047.outputs[26].hide = True
    group_input_047.outputs[28].hide = True
    group_input_047.outputs[29].hide = True
    group_input_047.outputs[30].hide = True
    group_input_047.outputs[31].hide = True
    group_input_047.outputs[32].hide = True
    group_input_047.outputs[33].hide = True
    group_input_047.outputs[34].hide = True
    group_input_047.outputs[35].hide = True
    group_input_047.outputs[36].hide = True
    group_input_047.outputs[37].hide = True
    group_input_047.outputs[38].hide = True
    group_input_047.outputs[39].hide = True
    group_input_047.outputs[40].hide = True
    group_input_047.outputs[41].hide = True
    group_input_047.outputs[42].hide = True
    group_input_047.outputs[43].hide = True
    group_input_047.outputs[44].hide = True
    group_input_047.outputs[45].hide = True
    group_input_047.outputs[46].hide = True
    group_input_047.outputs[47].hide = True
    group_input_047.outputs[48].hide = True
    group_input_047.outputs[49].hide = True
    group_input_047.outputs[50].hide = True
    group_input_047.outputs[51].hide = True
    group_input_047.outputs[52].hide = True
    group_input_047.outputs[53].hide = True
    group_input_047.outputs[54].hide = True
    group_input_047.outputs[55].hide = True
    group_input_047.outputs[56].hide = True
    group_input_047.outputs[57].hide = True
    group_input_047.outputs[58].hide = True

    # node Delete Geometry.002
    delete_geometry_002 = pattern_generator.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_002.name = "Delete Geometry.002"
    delete_geometry_002.domain = "POINT"
    delete_geometry_002.mode = "ALL"

    # node Boolean Math.002
    boolean_math_002 = pattern_generator.nodes.new("FunctionNodeBooleanMath")
    boolean_math_002.name = "Boolean Math.002"
    boolean_math_002.operation = "NOT"
    boolean_math_002.inputs[1].hide = True

    # node Group.005
    group_005 = pattern_generator.nodes.new("GeometryNodeGroup")
    group_005.name = "Group.005"
    group_005.node_tree = method_calculation_node_group()

    # node Group Input.035
    group_input_035 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_035.name = "Group Input.035"
    group_input_035.outputs[0].hide = True
    group_input_035.outputs[1].hide = True
    group_input_035.outputs[2].hide = True
    group_input_035.outputs[3].hide = True
    group_input_035.outputs[4].hide = True
    group_input_035.outputs[5].hide = True
    group_input_035.outputs[6].hide = True
    group_input_035.outputs[7].hide = True
    group_input_035.outputs[8].hide = True
    group_input_035.outputs[9].hide = True
    group_input_035.outputs[10].hide = True
    group_input_035.outputs[11].hide = True
    group_input_035.outputs[12].hide = True
    group_input_035.outputs[13].hide = True
    group_input_035.outputs[14].hide = True
    group_input_035.outputs[15].hide = True
    group_input_035.outputs[16].hide = True
    group_input_035.outputs[17].hide = True
    group_input_035.outputs[18].hide = True
    group_input_035.outputs[19].hide = True
    group_input_035.outputs[20].hide = True
    group_input_035.outputs[21].hide = True
    group_input_035.outputs[22].hide = True
    group_input_035.outputs[24].hide = True
    group_input_035.outputs[25].hide = True
    group_input_035.outputs[26].hide = True
    group_input_035.outputs[27].hide = True
    group_input_035.outputs[28].hide = True
    group_input_035.outputs[29].hide = True
    group_input_035.outputs[30].hide = True
    group_input_035.outputs[31].hide = True
    group_input_035.outputs[32].hide = True
    group_input_035.outputs[33].hide = True
    group_input_035.outputs[34].hide = True
    group_input_035.outputs[35].hide = True
    group_input_035.outputs[36].hide = True
    group_input_035.outputs[37].hide = True
    group_input_035.outputs[38].hide = True
    group_input_035.outputs[39].hide = True
    group_input_035.outputs[40].hide = True
    group_input_035.outputs[41].hide = True
    group_input_035.outputs[42].hide = True
    group_input_035.outputs[43].hide = True
    group_input_035.outputs[44].hide = True
    group_input_035.outputs[45].hide = True
    group_input_035.outputs[46].hide = True
    group_input_035.outputs[47].hide = True
    group_input_035.outputs[48].hide = True
    group_input_035.outputs[49].hide = True
    group_input_035.outputs[50].hide = True
    group_input_035.outputs[51].hide = True
    group_input_035.outputs[52].hide = True
    group_input_035.outputs[53].hide = True
    group_input_035.outputs[54].hide = True
    group_input_035.outputs[55].hide = True
    group_input_035.outputs[56].hide = True
    group_input_035.outputs[57].hide = True
    group_input_035.outputs[58].hide = True

    # node Switch.012
    switch_012 = pattern_generator.nodes.new("GeometryNodeSwitch")
    switch_012.name = "Switch.012"
    switch_012.input_type = "GEOMETRY"

    # node Group Input.036
    group_input_036 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_036.name = "Group Input.036"
    group_input_036.outputs[0].hide = True
    group_input_036.outputs[1].hide = True
    group_input_036.outputs[2].hide = True
    group_input_036.outputs[3].hide = True
    group_input_036.outputs[4].hide = True
    group_input_036.outputs[5].hide = True
    group_input_036.outputs[6].hide = True
    group_input_036.outputs[7].hide = True
    group_input_036.outputs[8].hide = True
    group_input_036.outputs[9].hide = True
    group_input_036.outputs[10].hide = True
    group_input_036.outputs[11].hide = True
    group_input_036.outputs[12].hide = True
    group_input_036.outputs[13].hide = True
    group_input_036.outputs[15].hide = True
    group_input_036.outputs[16].hide = True
    group_input_036.outputs[17].hide = True
    group_input_036.outputs[18].hide = True
    group_input_036.outputs[19].hide = True
    group_input_036.outputs[20].hide = True
    group_input_036.outputs[21].hide = True
    group_input_036.outputs[22].hide = True
    group_input_036.outputs[23].hide = True
    group_input_036.outputs[24].hide = True
    group_input_036.outputs[25].hide = True
    group_input_036.outputs[26].hide = True
    group_input_036.outputs[27].hide = True
    group_input_036.outputs[28].hide = True
    group_input_036.outputs[29].hide = True
    group_input_036.outputs[30].hide = True
    group_input_036.outputs[31].hide = True
    group_input_036.outputs[32].hide = True
    group_input_036.outputs[33].hide = True
    group_input_036.outputs[34].hide = True
    group_input_036.outputs[35].hide = True
    group_input_036.outputs[36].hide = True
    group_input_036.outputs[37].hide = True
    group_input_036.outputs[38].hide = True
    group_input_036.outputs[39].hide = True
    group_input_036.outputs[40].hide = True
    group_input_036.outputs[41].hide = True
    group_input_036.outputs[42].hide = True
    group_input_036.outputs[43].hide = True
    group_input_036.outputs[44].hide = True
    group_input_036.outputs[45].hide = True
    group_input_036.outputs[46].hide = True
    group_input_036.outputs[47].hide = True
    group_input_036.outputs[48].hide = True
    group_input_036.outputs[49].hide = True
    group_input_036.outputs[50].hide = True
    group_input_036.outputs[51].hide = True
    group_input_036.outputs[52].hide = True
    group_input_036.outputs[53].hide = True
    group_input_036.outputs[54].hide = True
    group_input_036.outputs[55].hide = True
    group_input_036.outputs[56].hide = True
    group_input_036.outputs[57].hide = True
    group_input_036.outputs[58].hide = True

    # node Geometry to Instance.001
    geometry_to_instance_001 = pattern_generator.nodes.new(
        "GeometryNodeGeometryToInstance"
    )
    geometry_to_instance_001.name = "Geometry to Instance.001"

    # node Set Position.001
    set_position_001 = pattern_generator.nodes.new("GeometryNodeSetPosition")
    set_position_001.name = "Set Position.001"
    set_position_001.inputs[1].hide = True
    set_position_001.inputs[3].hide = True
    # Selection
    set_position_001.inputs[1].default_value = True
    # Offset
    set_position_001.inputs[3].default_value = (0.0, 0.0, 0.0)

    # node Position.002
    position_002 = pattern_generator.nodes.new("GeometryNodeInputPosition")
    position_002.name = "Position.002"

    # node Attribute Statistic.001
    attribute_statistic_001 = pattern_generator.nodes.new(
        "GeometryNodeAttributeStatistic"
    )
    attribute_statistic_001.name = "Attribute Statistic.001"
    attribute_statistic_001.data_type = "FLOAT_VECTOR"
    attribute_statistic_001.domain = "POINT"
    attribute_statistic_001.inputs[1].hide = True
    attribute_statistic_001.outputs[1].hide = True
    attribute_statistic_001.outputs[2].hide = True
    attribute_statistic_001.outputs[3].hide = True
    attribute_statistic_001.outputs[4].hide = True
    attribute_statistic_001.outputs[5].hide = True
    attribute_statistic_001.outputs[6].hide = True
    attribute_statistic_001.outputs[7].hide = True
    # Selection
    attribute_statistic_001.inputs[1].default_value = True

    # node Vector Math.006
    vector_math_006 = pattern_generator.nodes.new("ShaderNodeVectorMath")
    vector_math_006.name = "Vector Math.006"
    vector_math_006.operation = "SUBTRACT"
    vector_math_006.inputs[2].hide = True
    vector_math_006.inputs[3].hide = True
    vector_math_006.outputs[1].hide = True

    # node Vector Rotate
    vector_rotate = pattern_generator.nodes.new("ShaderNodeVectorRotate")
    vector_rotate.name = "Vector Rotate"
    vector_rotate.invert = False
    vector_rotate.rotation_type = "AXIS_ANGLE"
    vector_rotate.inputs[1].hide = True
    vector_rotate.inputs[2].hide = True
    vector_rotate.inputs[3].hide = True
    vector_rotate.inputs[4].hide = True
    # Center
    vector_rotate.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Axis
    vector_rotate.inputs[2].default_value = (0.0, 0.0, 1.0)
    # Angle
    vector_rotate.inputs[3].default_value = 3.1415927410125732

    # node Realize Instances.004
    realize_instances_004 = pattern_generator.nodes.new("GeometryNodeRealizeInstances")
    realize_instances_004.name = "Realize Instances.004"
    realize_instances_004.inputs[1].hide = True
    realize_instances_004.inputs[2].hide = True
    realize_instances_004.inputs[3].hide = True
    # Selection
    realize_instances_004.inputs[1].default_value = True
    # Realize All
    realize_instances_004.inputs[2].default_value = True
    # Depth
    realize_instances_004.inputs[3].default_value = 0

    # node Compare.004
    compare_004_1 = pattern_generator.nodes.new("FunctionNodeCompare")
    compare_004_1.name = "Compare.004"
    compare_004_1.data_type = "FLOAT"
    compare_004_1.mode = "ELEMENT"
    compare_004_1.operation = "GREATER_THAN"
    compare_004_1.inputs[1].hide = True
    compare_004_1.inputs[2].hide = True
    compare_004_1.inputs[3].hide = True
    compare_004_1.inputs[4].hide = True
    compare_004_1.inputs[5].hide = True
    compare_004_1.inputs[6].hide = True
    compare_004_1.inputs[7].hide = True
    compare_004_1.inputs[8].hide = True
    compare_004_1.inputs[9].hide = True
    compare_004_1.inputs[10].hide = True
    compare_004_1.inputs[11].hide = True
    compare_004_1.inputs[12].hide = True
    # B
    compare_004_1.inputs[1].default_value = 0.0

    # node Group Input.048
    group_input_048 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_048.name = "Group Input.048"
    group_input_048.outputs[0].hide = True
    group_input_048.outputs[1].hide = True
    group_input_048.outputs[2].hide = True
    group_input_048.outputs[3].hide = True
    group_input_048.outputs[4].hide = True
    group_input_048.outputs[5].hide = True
    group_input_048.outputs[6].hide = True
    group_input_048.outputs[7].hide = True
    group_input_048.outputs[8].hide = True
    group_input_048.outputs[9].hide = True
    group_input_048.outputs[10].hide = True
    group_input_048.outputs[11].hide = True
    group_input_048.outputs[12].hide = True
    group_input_048.outputs[13].hide = True
    group_input_048.outputs[14].hide = True
    group_input_048.outputs[15].hide = True
    group_input_048.outputs[16].hide = True
    group_input_048.outputs[17].hide = True
    group_input_048.outputs[18].hide = True
    group_input_048.outputs[19].hide = True
    group_input_048.outputs[20].hide = True
    group_input_048.outputs[21].hide = True
    group_input_048.outputs[22].hide = True
    group_input_048.outputs[23].hide = True
    group_input_048.outputs[24].hide = True
    group_input_048.outputs[25].hide = True
    group_input_048.outputs[26].hide = True
    group_input_048.outputs[27].hide = True
    group_input_048.outputs[29].hide = True
    group_input_048.outputs[30].hide = True
    group_input_048.outputs[31].hide = True
    group_input_048.outputs[32].hide = True
    group_input_048.outputs[33].hide = True
    group_input_048.outputs[34].hide = True
    group_input_048.outputs[35].hide = True
    group_input_048.outputs[36].hide = True
    group_input_048.outputs[37].hide = True
    group_input_048.outputs[38].hide = True
    group_input_048.outputs[39].hide = True
    group_input_048.outputs[40].hide = True
    group_input_048.outputs[41].hide = True
    group_input_048.outputs[42].hide = True
    group_input_048.outputs[43].hide = True
    group_input_048.outputs[44].hide = True
    group_input_048.outputs[45].hide = True
    group_input_048.outputs[46].hide = True
    group_input_048.outputs[47].hide = True
    group_input_048.outputs[48].hide = True
    group_input_048.outputs[49].hide = True
    group_input_048.outputs[50].hide = True
    group_input_048.outputs[51].hide = True
    group_input_048.outputs[52].hide = True
    group_input_048.outputs[53].hide = True
    group_input_048.outputs[54].hide = True
    group_input_048.outputs[55].hide = True
    group_input_048.outputs[56].hide = True
    group_input_048.outputs[57].hide = True
    group_input_048.outputs[58].hide = True

    # node Group Input.054
    group_input_054 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_054.name = "Group Input.054"
    group_input_054.outputs[0].hide = True
    group_input_054.outputs[1].hide = True
    group_input_054.outputs[2].hide = True
    group_input_054.outputs[3].hide = True
    group_input_054.outputs[4].hide = True
    group_input_054.outputs[5].hide = True
    group_input_054.outputs[6].hide = True
    group_input_054.outputs[7].hide = True
    group_input_054.outputs[8].hide = True
    group_input_054.outputs[9].hide = True
    group_input_054.outputs[10].hide = True
    group_input_054.outputs[11].hide = True
    group_input_054.outputs[12].hide = True
    group_input_054.outputs[13].hide = True
    group_input_054.outputs[14].hide = True
    group_input_054.outputs[15].hide = True
    group_input_054.outputs[16].hide = True
    group_input_054.outputs[17].hide = True
    group_input_054.outputs[18].hide = True
    group_input_054.outputs[19].hide = True
    group_input_054.outputs[20].hide = True
    group_input_054.outputs[21].hide = True
    group_input_054.outputs[22].hide = True
    group_input_054.outputs[23].hide = True
    group_input_054.outputs[24].hide = True
    group_input_054.outputs[25].hide = True
    group_input_054.outputs[26].hide = True
    group_input_054.outputs[27].hide = True
    group_input_054.outputs[29].hide = True
    group_input_054.outputs[30].hide = True
    group_input_054.outputs[31].hide = True
    group_input_054.outputs[32].hide = True
    group_input_054.outputs[33].hide = True
    group_input_054.outputs[34].hide = True
    group_input_054.outputs[35].hide = True
    group_input_054.outputs[36].hide = True
    group_input_054.outputs[37].hide = True
    group_input_054.outputs[38].hide = True
    group_input_054.outputs[39].hide = True
    group_input_054.outputs[40].hide = True
    group_input_054.outputs[41].hide = True
    group_input_054.outputs[42].hide = True
    group_input_054.outputs[43].hide = True
    group_input_054.outputs[44].hide = True
    group_input_054.outputs[45].hide = True
    group_input_054.outputs[46].hide = True
    group_input_054.outputs[47].hide = True
    group_input_054.outputs[48].hide = True
    group_input_054.outputs[49].hide = True
    group_input_054.outputs[50].hide = True
    group_input_054.outputs[51].hide = True
    group_input_054.outputs[52].hide = True
    group_input_054.outputs[53].hide = True
    group_input_054.outputs[54].hide = True
    group_input_054.outputs[55].hide = True
    group_input_054.outputs[56].hide = True
    group_input_054.outputs[57].hide = True
    group_input_054.outputs[58].hide = True

    # node Switch.013
    switch_013 = pattern_generator.nodes.new("GeometryNodeSwitch")
    switch_013.name = "Switch.013"
    switch_013.input_type = "GEOMETRY"

    # node Compare.005
    compare_005_2 = pattern_generator.nodes.new("FunctionNodeCompare")
    compare_005_2.label = "String"
    compare_005_2.name = "Compare.005"
    compare_005_2.data_type = "STRING"
    compare_005_2.mode = "ELEMENT"
    compare_005_2.operation = "EQUAL"
    compare_005_2.inputs[0].hide = True
    compare_005_2.inputs[1].hide = True
    compare_005_2.inputs[2].hide = True
    compare_005_2.inputs[3].hide = True
    compare_005_2.inputs[4].hide = True
    compare_005_2.inputs[5].hide = True
    compare_005_2.inputs[6].hide = True
    compare_005_2.inputs[7].hide = True
    compare_005_2.inputs[9].hide = True
    compare_005_2.inputs[10].hide = True
    compare_005_2.inputs[11].hide = True
    compare_005_2.inputs[12].hide = True
    # B_STR
    compare_005_2.inputs[9].default_value = "String"

    # node Compare.006
    compare_006_1 = pattern_generator.nodes.new("FunctionNodeCompare")
    compare_006_1.label = "Image"
    compare_006_1.name = "Compare.006"
    compare_006_1.data_type = "STRING"
    compare_006_1.mode = "ELEMENT"
    compare_006_1.operation = "EQUAL"
    compare_006_1.inputs[0].hide = True
    compare_006_1.inputs[1].hide = True
    compare_006_1.inputs[2].hide = True
    compare_006_1.inputs[3].hide = True
    compare_006_1.inputs[4].hide = True
    compare_006_1.inputs[5].hide = True
    compare_006_1.inputs[6].hide = True
    compare_006_1.inputs[7].hide = True
    compare_006_1.inputs[9].hide = True
    compare_006_1.inputs[10].hide = True
    compare_006_1.inputs[11].hide = True
    compare_006_1.inputs[12].hide = True
    # B_STR
    compare_006_1.inputs[9].default_value = "Image"

    # node Switch.014
    switch_014 = pattern_generator.nodes.new("GeometryNodeSwitch")
    switch_014.name = "Switch.014"
    switch_014.input_type = "GEOMETRY"

    # node Group Input.055
    group_input_055 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_055.name = "Group Input.055"
    group_input_055.outputs[0].hide = True
    group_input_055.outputs[1].hide = True
    group_input_055.outputs[2].hide = True
    group_input_055.outputs[3].hide = True
    group_input_055.outputs[4].hide = True
    group_input_055.outputs[5].hide = True
    group_input_055.outputs[6].hide = True
    group_input_055.outputs[7].hide = True
    group_input_055.outputs[8].hide = True
    group_input_055.outputs[9].hide = True
    group_input_055.outputs[10].hide = True
    group_input_055.outputs[11].hide = True
    group_input_055.outputs[12].hide = True
    group_input_055.outputs[13].hide = True
    group_input_055.outputs[14].hide = True
    group_input_055.outputs[15].hide = True
    group_input_055.outputs[16].hide = True
    group_input_055.outputs[17].hide = True
    group_input_055.outputs[18].hide = True
    group_input_055.outputs[19].hide = True
    group_input_055.outputs[20].hide = True
    group_input_055.outputs[21].hide = True
    group_input_055.outputs[23].hide = True
    group_input_055.outputs[24].hide = True
    group_input_055.outputs[25].hide = True
    group_input_055.outputs[26].hide = True
    group_input_055.outputs[27].hide = True
    group_input_055.outputs[28].hide = True
    group_input_055.outputs[29].hide = True
    group_input_055.outputs[30].hide = True
    group_input_055.outputs[31].hide = True
    group_input_055.outputs[32].hide = True
    group_input_055.outputs[33].hide = True
    group_input_055.outputs[34].hide = True
    group_input_055.outputs[35].hide = True
    group_input_055.outputs[36].hide = True
    group_input_055.outputs[37].hide = True
    group_input_055.outputs[38].hide = True
    group_input_055.outputs[39].hide = True
    group_input_055.outputs[40].hide = True
    group_input_055.outputs[41].hide = True
    group_input_055.outputs[42].hide = True
    group_input_055.outputs[43].hide = True
    group_input_055.outputs[44].hide = True
    group_input_055.outputs[45].hide = True
    group_input_055.outputs[46].hide = True
    group_input_055.outputs[47].hide = True
    group_input_055.outputs[48].hide = True
    group_input_055.outputs[49].hide = True
    group_input_055.outputs[50].hide = True
    group_input_055.outputs[51].hide = True
    group_input_055.outputs[52].hide = True
    group_input_055.outputs[53].hide = True
    group_input_055.outputs[54].hide = True
    group_input_055.outputs[55].hide = True
    group_input_055.outputs[56].hide = True
    group_input_055.outputs[57].hide = True
    group_input_055.outputs[58].hide = True

    # node Switch.015
    switch_015 = pattern_generator.nodes.new("GeometryNodeSwitch")
    switch_015.name = "Switch.015"
    switch_015.input_type = "GEOMETRY"

    # node Compare.007
    compare_007_1 = pattern_generator.nodes.new("FunctionNodeCompare")
    compare_007_1.label = "String"
    compare_007_1.name = "Compare.007"
    compare_007_1.data_type = "STRING"
    compare_007_1.mode = "ELEMENT"
    compare_007_1.operation = "EQUAL"
    compare_007_1.inputs[0].hide = True
    compare_007_1.inputs[1].hide = True
    compare_007_1.inputs[2].hide = True
    compare_007_1.inputs[3].hide = True
    compare_007_1.inputs[4].hide = True
    compare_007_1.inputs[5].hide = True
    compare_007_1.inputs[6].hide = True
    compare_007_1.inputs[7].hide = True
    compare_007_1.inputs[9].hide = True
    compare_007_1.inputs[10].hide = True
    compare_007_1.inputs[11].hide = True
    compare_007_1.inputs[12].hide = True
    # B_STR
    compare_007_1.inputs[9].default_value = "String"

    # node Compare.008
    compare_008_1 = pattern_generator.nodes.new("FunctionNodeCompare")
    compare_008_1.label = "Image"
    compare_008_1.name = "Compare.008"
    compare_008_1.data_type = "STRING"
    compare_008_1.mode = "ELEMENT"
    compare_008_1.operation = "EQUAL"
    compare_008_1.inputs[0].hide = True
    compare_008_1.inputs[1].hide = True
    compare_008_1.inputs[2].hide = True
    compare_008_1.inputs[3].hide = True
    compare_008_1.inputs[4].hide = True
    compare_008_1.inputs[5].hide = True
    compare_008_1.inputs[6].hide = True
    compare_008_1.inputs[7].hide = True
    compare_008_1.inputs[9].hide = True
    compare_008_1.inputs[10].hide = True
    compare_008_1.inputs[11].hide = True
    compare_008_1.inputs[12].hide = True
    # B_STR
    compare_008_1.inputs[9].default_value = "Image"

    # node Switch.016
    switch_016 = pattern_generator.nodes.new("GeometryNodeSwitch")
    switch_016.name = "Switch.016"
    switch_016.input_type = "GEOMETRY"

    # node Compare.009
    compare_009 = pattern_generator.nodes.new("FunctionNodeCompare")
    compare_009.name = "Compare.009"
    compare_009.data_type = "STRING"
    compare_009.mode = "ELEMENT"
    compare_009.operation = "EQUAL"
    compare_009.inputs[0].hide = True
    compare_009.inputs[1].hide = True
    compare_009.inputs[2].hide = True
    compare_009.inputs[3].hide = True
    compare_009.inputs[4].hide = True
    compare_009.inputs[5].hide = True
    compare_009.inputs[6].hide = True
    compare_009.inputs[7].hide = True
    compare_009.inputs[9].hide = True
    compare_009.inputs[10].hide = True
    compare_009.inputs[11].hide = True
    compare_009.inputs[12].hide = True
    # B_STR
    compare_009.inputs[9].default_value = "Method 1"

    # node Switch.017
    switch_017 = pattern_generator.nodes.new("GeometryNodeSwitch")
    switch_017.name = "Switch.017"
    switch_017.input_type = "GEOMETRY"

    # node Switch.018
    switch_018 = pattern_generator.nodes.new("GeometryNodeSwitch")
    switch_018.name = "Switch.018"
    switch_018.input_type = "GEOMETRY"

    # node Group Input.033
    group_input_033 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_033.name = "Group Input.033"
    group_input_033.outputs[0].hide = True
    group_input_033.outputs[1].hide = True
    group_input_033.outputs[2].hide = True
    group_input_033.outputs[3].hide = True
    group_input_033.outputs[4].hide = True
    group_input_033.outputs[5].hide = True
    group_input_033.outputs[6].hide = True
    group_input_033.outputs[7].hide = True
    group_input_033.outputs[8].hide = True
    group_input_033.outputs[9].hide = True
    group_input_033.outputs[10].hide = True
    group_input_033.outputs[11].hide = True
    group_input_033.outputs[12].hide = True
    group_input_033.outputs[13].hide = True
    group_input_033.outputs[14].hide = True
    group_input_033.outputs[15].hide = True
    group_input_033.outputs[16].hide = True
    group_input_033.outputs[17].hide = True
    group_input_033.outputs[18].hide = True
    group_input_033.outputs[19].hide = True
    group_input_033.outputs[20].hide = True
    group_input_033.outputs[21].hide = True
    group_input_033.outputs[22].hide = True
    group_input_033.outputs[23].hide = True
    group_input_033.outputs[24].hide = True
    group_input_033.outputs[25].hide = True
    group_input_033.outputs[26].hide = True
    group_input_033.outputs[27].hide = True
    group_input_033.outputs[28].hide = True
    group_input_033.outputs[29].hide = True
    group_input_033.outputs[30].hide = True
    group_input_033.outputs[31].hide = True
    group_input_033.outputs[32].hide = True
    group_input_033.outputs[33].hide = True
    group_input_033.outputs[34].hide = True
    group_input_033.outputs[35].hide = True
    group_input_033.outputs[36].hide = True
    group_input_033.outputs[37].hide = True
    group_input_033.outputs[38].hide = True
    group_input_033.outputs[39].hide = True
    group_input_033.outputs[40].hide = True
    group_input_033.outputs[41].hide = True
    group_input_033.outputs[42].hide = True
    group_input_033.outputs[43].hide = True
    group_input_033.outputs[44].hide = True
    group_input_033.outputs[45].hide = True
    group_input_033.outputs[46].hide = True
    group_input_033.outputs[47].hide = True
    group_input_033.outputs[48].hide = True
    group_input_033.outputs[49].hide = True
    group_input_033.outputs[50].hide = True
    group_input_033.outputs[51].hide = True
    group_input_033.outputs[52].hide = True
    group_input_033.outputs[53].hide = True
    group_input_033.outputs[54].hide = True
    group_input_033.outputs[56].hide = True
    group_input_033.outputs[57].hide = True
    group_input_033.outputs[58].hide = True

    # node Named Attribute
    named_attribute_1 = pattern_generator.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_1.name = "Named Attribute"
    named_attribute_1.data_type = "FLOAT"
    named_attribute_1.inputs[0].hide = True
    named_attribute_1.outputs[1].hide = True
    # Name
    named_attribute_1.inputs[0].default_value = "value_not_deleted"

    # node Group.002
    group_002 = pattern_generator.nodes.new("GeometryNodeGroup")
    group_002.name = "Group.002"
    group_002.node_tree = subset_curve_node_group()

    # node Switch.019
    switch_019 = pattern_generator.nodes.new("GeometryNodeSwitch")
    switch_019.name = "Switch.019"
    switch_019.input_type = "GEOMETRY"

    # node Group Input.056
    group_input_056 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_056.name = "Group Input.056"
    group_input_056.outputs[0].hide = True
    group_input_056.outputs[1].hide = True
    group_input_056.outputs[2].hide = True
    group_input_056.outputs[3].hide = True
    group_input_056.outputs[4].hide = True
    group_input_056.outputs[5].hide = True
    group_input_056.outputs[6].hide = True
    group_input_056.outputs[7].hide = True
    group_input_056.outputs[8].hide = True
    group_input_056.outputs[9].hide = True
    group_input_056.outputs[10].hide = True
    group_input_056.outputs[11].hide = True
    group_input_056.outputs[12].hide = True
    group_input_056.outputs[13].hide = True
    group_input_056.outputs[14].hide = True
    group_input_056.outputs[15].hide = True
    group_input_056.outputs[16].hide = True
    group_input_056.outputs[17].hide = True
    group_input_056.outputs[18].hide = True
    group_input_056.outputs[19].hide = True
    group_input_056.outputs[20].hide = True
    group_input_056.outputs[21].hide = True
    group_input_056.outputs[22].hide = True
    group_input_056.outputs[23].hide = True
    group_input_056.outputs[24].hide = True
    group_input_056.outputs[25].hide = True
    group_input_056.outputs[26].hide = True
    group_input_056.outputs[27].hide = True
    group_input_056.outputs[28].hide = True
    group_input_056.outputs[29].hide = True
    group_input_056.outputs[30].hide = True
    group_input_056.outputs[31].hide = True
    group_input_056.outputs[32].hide = True
    group_input_056.outputs[33].hide = True
    group_input_056.outputs[34].hide = True
    group_input_056.outputs[35].hide = True
    group_input_056.outputs[36].hide = True
    group_input_056.outputs[37].hide = True
    group_input_056.outputs[38].hide = True
    group_input_056.outputs[39].hide = True
    group_input_056.outputs[40].hide = True
    group_input_056.outputs[41].hide = True
    group_input_056.outputs[42].hide = True
    group_input_056.outputs[43].hide = True
    group_input_056.outputs[44].hide = True
    group_input_056.outputs[45].hide = True
    group_input_056.outputs[46].hide = True
    group_input_056.outputs[47].hide = True
    group_input_056.outputs[48].hide = True
    group_input_056.outputs[49].hide = True
    group_input_056.outputs[50].hide = True
    group_input_056.outputs[51].hide = True
    group_input_056.outputs[52].hide = True
    group_input_056.outputs[53].hide = True
    group_input_056.outputs[54].hide = True
    group_input_056.outputs[56].hide = True
    group_input_056.outputs[57].hide = True
    group_input_056.outputs[58].hide = True

    # node Switch.007
    switch_007_1 = pattern_generator.nodes.new("GeometryNodeSwitch")
    switch_007_1.name = "Switch.007"
    switch_007_1.input_type = "GEOMETRY"

    # node Curve to Mesh.006
    curve_to_mesh_006 = pattern_generator.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh_006.name = "Curve to Mesh.006"
    curve_to_mesh_006.inputs[1].hide = True
    curve_to_mesh_006.inputs[2].hide = True
    # Fill Caps
    curve_to_mesh_006.inputs[2].default_value = False

    # node Store Named Attribute.002
    store_named_attribute_002_1 = pattern_generator.nodes.new(
        "GeometryNodeStoreNamedAttribute"
    )
    store_named_attribute_002_1.name = "Store Named Attribute.002"
    store_named_attribute_002_1.data_type = "FLOAT"
    store_named_attribute_002_1.domain = "POINT"
    store_named_attribute_002_1.inputs[1].hide = True
    store_named_attribute_002_1.inputs[2].hide = True
    store_named_attribute_002_1.inputs[3].hide = True
    # Selection
    store_named_attribute_002_1.inputs[1].default_value = True
    # Name
    store_named_attribute_002_1.inputs[2].default_value = "value_not_deleted"
    # Value
    store_named_attribute_002_1.inputs[3].default_value = 0.0

    # node Realize Instances.005
    realize_instances_005 = pattern_generator.nodes.new("GeometryNodeRealizeInstances")
    realize_instances_005.name = "Realize Instances.005"
    realize_instances_005.inputs[1].hide = True
    realize_instances_005.inputs[2].hide = True
    realize_instances_005.inputs[3].hide = True
    # Selection
    realize_instances_005.inputs[1].default_value = True
    # Realize All
    realize_instances_005.inputs[2].default_value = True
    # Depth
    realize_instances_005.inputs[3].default_value = 0

    # node Delete Geometry.004
    delete_geometry_004_1 = pattern_generator.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_004_1.name = "Delete Geometry.004"
    delete_geometry_004_1.domain = "EDGE"
    delete_geometry_004_1.mode = "ALL"

    # node Compare.011
    compare_011 = pattern_generator.nodes.new("FunctionNodeCompare")
    compare_011.name = "Compare.011"
    compare_011.data_type = "INT"
    compare_011.mode = "ELEMENT"
    compare_011.operation = "GREATER_THAN"
    compare_011.inputs[0].hide = True
    compare_011.inputs[1].hide = True
    compare_011.inputs[3].hide = True
    compare_011.inputs[4].hide = True
    compare_011.inputs[5].hide = True
    compare_011.inputs[6].hide = True
    compare_011.inputs[7].hide = True
    compare_011.inputs[8].hide = True
    compare_011.inputs[9].hide = True
    compare_011.inputs[10].hide = True
    compare_011.inputs[11].hide = True
    compare_011.inputs[12].hide = True
    # B_INT
    compare_011.inputs[3].default_value = 1

    # node Edge Neighbors
    edge_neighbors = pattern_generator.nodes.new("GeometryNodeInputMeshEdgeNeighbors")
    edge_neighbors.name = "Edge Neighbors"

    # node Group Input.057
    group_input_057 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_057.name = "Group Input.057"
    group_input_057.outputs[0].hide = True
    group_input_057.outputs[1].hide = True
    group_input_057.outputs[2].hide = True
    group_input_057.outputs[3].hide = True
    group_input_057.outputs[4].hide = True
    group_input_057.outputs[5].hide = True
    group_input_057.outputs[6].hide = True
    group_input_057.outputs[7].hide = True
    group_input_057.outputs[8].hide = True
    group_input_057.outputs[9].hide = True
    group_input_057.outputs[10].hide = True
    group_input_057.outputs[11].hide = True
    group_input_057.outputs[12].hide = True
    group_input_057.outputs[13].hide = True
    group_input_057.outputs[14].hide = True
    group_input_057.outputs[15].hide = True
    group_input_057.outputs[16].hide = True
    group_input_057.outputs[17].hide = True
    group_input_057.outputs[18].hide = True
    group_input_057.outputs[19].hide = True
    group_input_057.outputs[20].hide = True
    group_input_057.outputs[21].hide = True
    group_input_057.outputs[23].hide = True
    group_input_057.outputs[24].hide = True
    group_input_057.outputs[25].hide = True
    group_input_057.outputs[26].hide = True
    group_input_057.outputs[27].hide = True
    group_input_057.outputs[28].hide = True
    group_input_057.outputs[29].hide = True
    group_input_057.outputs[30].hide = True
    group_input_057.outputs[31].hide = True
    group_input_057.outputs[32].hide = True
    group_input_057.outputs[33].hide = True
    group_input_057.outputs[34].hide = True
    group_input_057.outputs[35].hide = True
    group_input_057.outputs[36].hide = True
    group_input_057.outputs[37].hide = True
    group_input_057.outputs[38].hide = True
    group_input_057.outputs[39].hide = True
    group_input_057.outputs[40].hide = True
    group_input_057.outputs[41].hide = True
    group_input_057.outputs[42].hide = True
    group_input_057.outputs[43].hide = True
    group_input_057.outputs[44].hide = True
    group_input_057.outputs[45].hide = True
    group_input_057.outputs[46].hide = True
    group_input_057.outputs[47].hide = True
    group_input_057.outputs[48].hide = True
    group_input_057.outputs[49].hide = True
    group_input_057.outputs[50].hide = True
    group_input_057.outputs[51].hide = True
    group_input_057.outputs[52].hide = True
    group_input_057.outputs[53].hide = True
    group_input_057.outputs[54].hide = True
    group_input_057.outputs[55].hide = True
    group_input_057.outputs[56].hide = True
    group_input_057.outputs[57].hide = True
    group_input_057.outputs[58].hide = True

    # node Switch.020
    switch_020 = pattern_generator.nodes.new("GeometryNodeSwitch")
    switch_020.name = "Switch.020"
    switch_020.input_type = "GEOMETRY"

    # node Compare.012
    compare_012 = pattern_generator.nodes.new("FunctionNodeCompare")
    compare_012.label = "String"
    compare_012.name = "Compare.012"
    compare_012.data_type = "STRING"
    compare_012.mode = "ELEMENT"
    compare_012.operation = "EQUAL"
    compare_012.inputs[0].hide = True
    compare_012.inputs[1].hide = True
    compare_012.inputs[2].hide = True
    compare_012.inputs[3].hide = True
    compare_012.inputs[4].hide = True
    compare_012.inputs[5].hide = True
    compare_012.inputs[6].hide = True
    compare_012.inputs[7].hide = True
    compare_012.inputs[9].hide = True
    compare_012.inputs[10].hide = True
    compare_012.inputs[11].hide = True
    compare_012.inputs[12].hide = True
    # B_STR
    compare_012.inputs[9].default_value = "String"

    # node Compare.013
    compare_013 = pattern_generator.nodes.new("FunctionNodeCompare")
    compare_013.label = "Image"
    compare_013.name = "Compare.013"
    compare_013.data_type = "STRING"
    compare_013.mode = "ELEMENT"
    compare_013.operation = "EQUAL"
    compare_013.inputs[0].hide = True
    compare_013.inputs[1].hide = True
    compare_013.inputs[2].hide = True
    compare_013.inputs[3].hide = True
    compare_013.inputs[4].hide = True
    compare_013.inputs[5].hide = True
    compare_013.inputs[6].hide = True
    compare_013.inputs[7].hide = True
    compare_013.inputs[9].hide = True
    compare_013.inputs[10].hide = True
    compare_013.inputs[11].hide = True
    compare_013.inputs[12].hide = True
    # B_STR
    compare_013.inputs[9].default_value = "Image"

    # node Switch.021
    switch_021 = pattern_generator.nodes.new("GeometryNodeSwitch")
    switch_021.name = "Switch.021"
    switch_021.input_type = "GEOMETRY"

    # node Blur Attribute
    blur_attribute = pattern_generator.nodes.new("GeometryNodeBlurAttribute")
    blur_attribute.name = "Blur Attribute"
    blur_attribute.data_type = "FLOAT_VECTOR"
    blur_attribute.inputs[2].hide = True
    # Weight
    blur_attribute.inputs[2].default_value = 1.0

    # node Position.001
    position_001 = pattern_generator.nodes.new("GeometryNodeInputPosition")
    position_001.name = "Position.001"

    # node Set Position.002
    set_position_002 = pattern_generator.nodes.new("GeometryNodeSetPosition")
    set_position_002.name = "Set Position.002"
    set_position_002.inputs[1].hide = True
    set_position_002.inputs[3].hide = True
    # Selection
    set_position_002.inputs[1].default_value = True
    # Offset
    set_position_002.inputs[3].default_value = (0.0, 0.0, 0.0)

    # node Group Input.058
    group_input_058 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_058.name = "Group Input.058"
    group_input_058.outputs[0].hide = True
    group_input_058.outputs[1].hide = True
    group_input_058.outputs[2].hide = True
    group_input_058.outputs[3].hide = True
    group_input_058.outputs[4].hide = True
    group_input_058.outputs[5].hide = True
    group_input_058.outputs[6].hide = True
    group_input_058.outputs[7].hide = True
    group_input_058.outputs[8].hide = True
    group_input_058.outputs[9].hide = True
    group_input_058.outputs[10].hide = True
    group_input_058.outputs[11].hide = True
    group_input_058.outputs[12].hide = True
    group_input_058.outputs[13].hide = True
    group_input_058.outputs[14].hide = True
    group_input_058.outputs[15].hide = True
    group_input_058.outputs[16].hide = True
    group_input_058.outputs[17].hide = True
    group_input_058.outputs[18].hide = True
    group_input_058.outputs[19].hide = True
    group_input_058.outputs[20].hide = True
    group_input_058.outputs[21].hide = True
    group_input_058.outputs[22].hide = True
    group_input_058.outputs[23].hide = True
    group_input_058.outputs[24].hide = True
    group_input_058.outputs[25].hide = True
    group_input_058.outputs[26].hide = True
    group_input_058.outputs[27].hide = True
    group_input_058.outputs[28].hide = True
    group_input_058.outputs[30].hide = True
    group_input_058.outputs[31].hide = True
    group_input_058.outputs[32].hide = True
    group_input_058.outputs[33].hide = True
    group_input_058.outputs[34].hide = True
    group_input_058.outputs[35].hide = True
    group_input_058.outputs[36].hide = True
    group_input_058.outputs[37].hide = True
    group_input_058.outputs[38].hide = True
    group_input_058.outputs[39].hide = True
    group_input_058.outputs[40].hide = True
    group_input_058.outputs[41].hide = True
    group_input_058.outputs[42].hide = True
    group_input_058.outputs[43].hide = True
    group_input_058.outputs[44].hide = True
    group_input_058.outputs[45].hide = True
    group_input_058.outputs[46].hide = True
    group_input_058.outputs[47].hide = True
    group_input_058.outputs[48].hide = True
    group_input_058.outputs[49].hide = True
    group_input_058.outputs[50].hide = True
    group_input_058.outputs[51].hide = True
    group_input_058.outputs[52].hide = True
    group_input_058.outputs[53].hide = True
    group_input_058.outputs[54].hide = True
    group_input_058.outputs[55].hide = True
    group_input_058.outputs[56].hide = True
    group_input_058.outputs[57].hide = True
    group_input_058.outputs[58].hide = True

    # node Compare.014
    compare_014 = pattern_generator.nodes.new("FunctionNodeCompare")
    compare_014.name = "Compare.014"
    compare_014.data_type = "INT"
    compare_014.mode = "ELEMENT"
    compare_014.operation = "GREATER_THAN"
    compare_014.inputs[1].hide = True
    compare_014.inputs[3].hide = True
    compare_014.inputs[4].hide = True
    compare_014.inputs[5].hide = True
    compare_014.inputs[6].hide = True
    compare_014.inputs[7].hide = True
    compare_014.inputs[8].hide = True
    compare_014.inputs[9].hide = True
    compare_014.inputs[10].hide = True
    compare_014.inputs[11].hide = True
    compare_014.inputs[12].hide = True
    # B_INT
    compare_014.inputs[3].default_value = 8

    # node Switch.022
    switch_022 = pattern_generator.nodes.new("GeometryNodeSwitch")
    switch_022.name = "Switch.022"
    switch_022.input_type = "INT"
    switch_022.inputs[2].hide = True
    # True
    switch_022.inputs[2].default_value = 8

    # node Group Input.059
    group_input_059 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_059.name = "Group Input.059"
    group_input_059.outputs[0].hide = True
    group_input_059.outputs[1].hide = True
    group_input_059.outputs[2].hide = True
    group_input_059.outputs[3].hide = True
    group_input_059.outputs[4].hide = True
    group_input_059.outputs[5].hide = True
    group_input_059.outputs[6].hide = True
    group_input_059.outputs[7].hide = True
    group_input_059.outputs[8].hide = True
    group_input_059.outputs[9].hide = True
    group_input_059.outputs[10].hide = True
    group_input_059.outputs[11].hide = True
    group_input_059.outputs[12].hide = True
    group_input_059.outputs[13].hide = True
    group_input_059.outputs[14].hide = True
    group_input_059.outputs[15].hide = True
    group_input_059.outputs[16].hide = True
    group_input_059.outputs[17].hide = True
    group_input_059.outputs[18].hide = True
    group_input_059.outputs[19].hide = True
    group_input_059.outputs[20].hide = True
    group_input_059.outputs[21].hide = True
    group_input_059.outputs[22].hide = True
    group_input_059.outputs[23].hide = True
    group_input_059.outputs[24].hide = True
    group_input_059.outputs[25].hide = True
    group_input_059.outputs[26].hide = True
    group_input_059.outputs[27].hide = True
    group_input_059.outputs[28].hide = True
    group_input_059.outputs[29].hide = True
    group_input_059.outputs[30].hide = True
    group_input_059.outputs[31].hide = True
    group_input_059.outputs[32].hide = True
    group_input_059.outputs[33].hide = True
    group_input_059.outputs[34].hide = True
    group_input_059.outputs[35].hide = True
    group_input_059.outputs[36].hide = True
    group_input_059.outputs[37].hide = True
    group_input_059.outputs[38].hide = True
    group_input_059.outputs[39].hide = True
    group_input_059.outputs[40].hide = True
    group_input_059.outputs[41].hide = True
    group_input_059.outputs[42].hide = True
    group_input_059.outputs[43].hide = True
    group_input_059.outputs[44].hide = True
    group_input_059.outputs[45].hide = True
    group_input_059.outputs[46].hide = True
    group_input_059.outputs[47].hide = True
    group_input_059.outputs[48].hide = True
    group_input_059.outputs[49].hide = True
    group_input_059.outputs[50].hide = True
    group_input_059.outputs[51].hide = True
    group_input_059.outputs[52].hide = True
    group_input_059.outputs[53].hide = True
    group_input_059.outputs[54].hide = True
    group_input_059.outputs[55].hide = True
    group_input_059.outputs[58].hide = True

    # node Switch.023
    switch_023 = pattern_generator.nodes.new("GeometryNodeSwitch")
    switch_023.name = "Switch.023"
    switch_023.input_type = "GEOMETRY"

    # node Join Geometry.003
    join_geometry_003 = pattern_generator.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_003.name = "Join Geometry.003"

    # node Bake
    bake_1 = pattern_generator.nodes.new("GeometryNodeBake")
    bake_1.name = "Bake"
    bake_1.active_index = 0
    bake_1.bake_items.clear()
    bake_1.bake_items.new("GEOMETRY", "Geometry")
    bake_1.bake_items[0].attribute_domain = "POINT"

    # node Store Named Attribute.003
    store_named_attribute_003 = pattern_generator.nodes.new(
        "GeometryNodeStoreNamedAttribute"
    )
    store_named_attribute_003.name = "Store Named Attribute.003"
    store_named_attribute_003.data_type = "FLOAT_VECTOR"
    store_named_attribute_003.domain = "CURVE"
    store_named_attribute_003.inputs[1].hide = True
    # Selection
    store_named_attribute_003.inputs[1].default_value = True

    # node Group.003
    group_003 = pattern_generator.nodes.new("GeometryNodeGroup")
    group_003.name = "Group.003"
    group_003.node_tree = colorpalette_node_group()

    # node Group Input.039
    group_input_039 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_039.name = "Group Input.039"
    group_input_039.outputs[0].hide = True
    group_input_039.outputs[1].hide = True
    group_input_039.outputs[2].hide = True
    group_input_039.outputs[3].hide = True
    group_input_039.outputs[4].hide = True
    group_input_039.outputs[5].hide = True
    group_input_039.outputs[6].hide = True
    group_input_039.outputs[7].hide = True
    group_input_039.outputs[8].hide = True
    group_input_039.outputs[9].hide = True
    group_input_039.outputs[10].hide = True
    group_input_039.outputs[11].hide = True
    group_input_039.outputs[12].hide = True
    group_input_039.outputs[13].hide = True
    group_input_039.outputs[14].hide = True
    group_input_039.outputs[15].hide = True
    group_input_039.outputs[16].hide = True
    group_input_039.outputs[17].hide = True
    group_input_039.outputs[18].hide = True
    group_input_039.outputs[19].hide = True
    group_input_039.outputs[20].hide = True
    group_input_039.outputs[21].hide = True
    group_input_039.outputs[22].hide = True
    group_input_039.outputs[23].hide = True
    group_input_039.outputs[24].hide = True
    group_input_039.outputs[25].hide = True
    group_input_039.outputs[26].hide = True
    group_input_039.outputs[27].hide = True
    group_input_039.outputs[28].hide = True
    group_input_039.outputs[29].hide = True
    group_input_039.outputs[30].hide = True
    group_input_039.outputs[31].hide = True
    group_input_039.outputs[32].hide = True
    group_input_039.outputs[41].hide = True
    group_input_039.outputs[43].hide = True
    group_input_039.outputs[48].hide = True
    group_input_039.outputs[49].hide = True
    group_input_039.outputs[50].hide = True
    group_input_039.outputs[51].hide = True
    group_input_039.outputs[52].hide = True
    group_input_039.outputs[53].hide = True
    group_input_039.outputs[54].hide = True
    group_input_039.outputs[55].hide = True
    group_input_039.outputs[56].hide = True
    group_input_039.outputs[57].hide = True
    group_input_039.outputs[58].hide = True

    # node Group Input.041
    group_input_041 = pattern_generator.nodes.new("NodeGroupInput")
    group_input_041.name = "Group Input.041"
    group_input_041.outputs[0].hide = True
    group_input_041.outputs[1].hide = True
    group_input_041.outputs[2].hide = True
    group_input_041.outputs[3].hide = True
    group_input_041.outputs[4].hide = True
    group_input_041.outputs[5].hide = True
    group_input_041.outputs[6].hide = True
    group_input_041.outputs[7].hide = True
    group_input_041.outputs[8].hide = True
    group_input_041.outputs[9].hide = True
    group_input_041.outputs[10].hide = True
    group_input_041.outputs[11].hide = True
    group_input_041.outputs[12].hide = True
    group_input_041.outputs[13].hide = True
    group_input_041.outputs[14].hide = True
    group_input_041.outputs[15].hide = True
    group_input_041.outputs[16].hide = True
    group_input_041.outputs[17].hide = True
    group_input_041.outputs[18].hide = True
    group_input_041.outputs[19].hide = True
    group_input_041.outputs[20].hide = True
    group_input_041.outputs[21].hide = True
    group_input_041.outputs[22].hide = True
    group_input_041.outputs[23].hide = True
    group_input_041.outputs[24].hide = True
    group_input_041.outputs[25].hide = True
    group_input_041.outputs[26].hide = True
    group_input_041.outputs[27].hide = True
    group_input_041.outputs[28].hide = True
    group_input_041.outputs[29].hide = True
    group_input_041.outputs[30].hide = True
    group_input_041.outputs[31].hide = True
    group_input_041.outputs[33].hide = True
    group_input_041.outputs[34].hide = True
    group_input_041.outputs[35].hide = True
    group_input_041.outputs[36].hide = True
    group_input_041.outputs[37].hide = True
    group_input_041.outputs[38].hide = True
    group_input_041.outputs[39].hide = True
    group_input_041.outputs[40].hide = True
    group_input_041.outputs[41].hide = True
    group_input_041.outputs[42].hide = True
    group_input_041.outputs[43].hide = True
    group_input_041.outputs[44].hide = True
    group_input_041.outputs[45].hide = True
    group_input_041.outputs[46].hide = True
    group_input_041.outputs[47].hide = True
    group_input_041.outputs[48].hide = True
    group_input_041.outputs[49].hide = True
    group_input_041.outputs[50].hide = True
    group_input_041.outputs[51].hide = True
    group_input_041.outputs[52].hide = True
    group_input_041.outputs[53].hide = True
    group_input_041.outputs[54].hide = True
    group_input_041.outputs[55].hide = True
    group_input_041.outputs[56].hide = True
    group_input_041.outputs[57].hide = True
    group_input_041.outputs[58].hide = True

    # node Named Attribute.003
    named_attribute_003 = pattern_generator.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_003.name = "Named Attribute.003"
    named_attribute_003.data_type = "INT"
    # Name
    named_attribute_003.inputs[0].default_value = "Index_island"

    # node Store Named Attribute
    store_named_attribute = pattern_generator.nodes.new(
        "GeometryNodeStoreNamedAttribute"
    )
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.data_type = "INT"
    store_named_attribute.domain = "EDGE"
    # Selection
    store_named_attribute.inputs[1].default_value = True
    # Name
    store_named_attribute.inputs[2].default_value = "Index_island"

    # node Mesh Island
    mesh_island_1 = pattern_generator.nodes.new("GeometryNodeInputMeshIsland")
    mesh_island_1.name = "Mesh Island"

    # node Named Attribute.004
    named_attribute_004 = pattern_generator.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_004.name = "Named Attribute.004"
    named_attribute_004.data_type = "INT"
    # Name
    named_attribute_004.inputs[0].default_value = "id_not"

    # node Reroute
    reroute_3 = pattern_generator.nodes.new("NodeReroute")
    reroute_3.name = "Reroute"
    # node Reroute.001
    reroute_001_3 = pattern_generator.nodes.new("NodeReroute")
    reroute_001_3.name = "Reroute.001"
    # node Reroute.002
    reroute_002_3 = pattern_generator.nodes.new("NodeReroute")
    reroute_002_3.name = "Reroute.002"
    # node Reroute.003
    reroute_003_3 = pattern_generator.nodes.new("NodeReroute")
    reroute_003_3.name = "Reroute.003"
    # node Reroute.004
    reroute_004_3 = pattern_generator.nodes.new("NodeReroute")
    reroute_004_3.name = "Reroute.004"
    # node Reroute.005
    reroute_005_3 = pattern_generator.nodes.new("NodeReroute")
    reroute_005_3.name = "Reroute.005"
    # node Reroute.006
    reroute_006_3 = pattern_generator.nodes.new("NodeReroute")
    reroute_006_3.name = "Reroute.006"
    # node Reroute.007
    reroute_007_2 = pattern_generator.nodes.new("NodeReroute")
    reroute_007_2.name = "Reroute.007"
    # node Reroute.008
    reroute_008_2 = pattern_generator.nodes.new("NodeReroute")
    reroute_008_2.name = "Reroute.008"
    # node Reroute.009
    reroute_009_2 = pattern_generator.nodes.new("NodeReroute")
    reroute_009_2.name = "Reroute.009"
    # node Reroute.010
    reroute_010_2 = pattern_generator.nodes.new("NodeReroute")
    reroute_010_2.name = "Reroute.010"
    # node Reroute.011
    reroute_011_1 = pattern_generator.nodes.new("NodeReroute")
    reroute_011_1.name = "Reroute.011"
    # node Reroute.012
    reroute_012 = pattern_generator.nodes.new("NodeReroute")
    reroute_012.name = "Reroute.012"
    # node Reroute.013
    reroute_013 = pattern_generator.nodes.new("NodeReroute")
    reroute_013.name = "Reroute.013"
    # node Reroute.014
    reroute_014 = pattern_generator.nodes.new("NodeReroute")
    reroute_014.name = "Reroute.014"
    # node Reroute.015
    reroute_015 = pattern_generator.nodes.new("NodeReroute")
    reroute_015.name = "Reroute.015"
    # node Reroute.016
    reroute_016 = pattern_generator.nodes.new("NodeReroute")
    reroute_016.name = "Reroute.016"
    # node Reroute.017
    reroute_017 = pattern_generator.nodes.new("NodeReroute")
    reroute_017.name = "Reroute.017"
    # node Reroute.018
    reroute_018 = pattern_generator.nodes.new("NodeReroute")
    reroute_018.name = "Reroute.018"
    # node Reroute.019
    reroute_019 = pattern_generator.nodes.new("NodeReroute")
    reroute_019.name = "Reroute.019"
    # node Reroute.020
    reroute_020 = pattern_generator.nodes.new("NodeReroute")
    reroute_020.name = "Reroute.020"
    # node Reroute.021
    reroute_021 = pattern_generator.nodes.new("NodeReroute")
    reroute_021.name = "Reroute.021"
    # node Reroute.022
    reroute_022 = pattern_generator.nodes.new("NodeReroute")
    reroute_022.name = "Reroute.022"
    # node Reroute.023
    reroute_023 = pattern_generator.nodes.new("NodeReroute")
    reroute_023.name = "Reroute.023"
    # node Reroute.024
    reroute_024 = pattern_generator.nodes.new("NodeReroute")
    reroute_024.name = "Reroute.024"
    # node Reroute.025
    reroute_025 = pattern_generator.nodes.new("NodeReroute")
    reroute_025.name = "Reroute.025"
    # node Reroute.026
    reroute_026 = pattern_generator.nodes.new("NodeReroute")
    reroute_026.name = "Reroute.026"
    # node Reroute.027
    reroute_027 = pattern_generator.nodes.new("NodeReroute")
    reroute_027.name = "Reroute.027"
    # node Reroute.028
    reroute_028 = pattern_generator.nodes.new("NodeReroute")
    reroute_028.name = "Reroute.028"
    # node Reroute.029
    reroute_029 = pattern_generator.nodes.new("NodeReroute")
    reroute_029.name = "Reroute.029"
    # node Reroute.030
    reroute_030 = pattern_generator.nodes.new("NodeReroute")
    reroute_030.name = "Reroute.030"
    # node Reroute.031
    reroute_031 = pattern_generator.nodes.new("NodeReroute")
    reroute_031.name = "Reroute.031"
    # node Reroute.032
    reroute_032 = pattern_generator.nodes.new("NodeReroute")
    reroute_032.name = "Reroute.032"
    # node Reroute.033
    reroute_033 = pattern_generator.nodes.new("NodeReroute")
    reroute_033.name = "Reroute.033"
    # node Reroute.034
    reroute_034 = pattern_generator.nodes.new("NodeReroute")
    reroute_034.name = "Reroute.034"
    # node Reroute.035
    reroute_035 = pattern_generator.nodes.new("NodeReroute")
    reroute_035.name = "Reroute.035"
    # node Reroute.036
    reroute_036 = pattern_generator.nodes.new("NodeReroute")
    reroute_036.name = "Reroute.036"
    # node Reroute.037
    reroute_037 = pattern_generator.nodes.new("NodeReroute")
    reroute_037.name = "Reroute.037"
    # node Reroute.038
    reroute_038 = pattern_generator.nodes.new("NodeReroute")
    reroute_038.name = "Reroute.038"
    # node Reroute.039
    reroute_039 = pattern_generator.nodes.new("NodeReroute")
    reroute_039.name = "Reroute.039"
    # node Reroute.040
    reroute_040 = pattern_generator.nodes.new("NodeReroute")
    reroute_040.name = "Reroute.040"
    # node Reroute.041
    reroute_041 = pattern_generator.nodes.new("NodeReroute")
    reroute_041.name = "Reroute.041"
    # node Reroute.042
    reroute_042 = pattern_generator.nodes.new("NodeReroute")
    reroute_042.name = "Reroute.042"
    # node Reroute.043
    reroute_043 = pattern_generator.nodes.new("NodeReroute")
    reroute_043.name = "Reroute.043"
    # node Reroute.044
    reroute_044 = pattern_generator.nodes.new("NodeReroute")
    reroute_044.name = "Reroute.044"
    # node Reroute.045
    reroute_045 = pattern_generator.nodes.new("NodeReroute")
    reroute_045.name = "Reroute.045"
    # node Reroute.046
    reroute_046 = pattern_generator.nodes.new("NodeReroute")
    reroute_046.name = "Reroute.046"
    # node Reroute.047
    reroute_047 = pattern_generator.nodes.new("NodeReroute")
    reroute_047.name = "Reroute.047"
    # node Reroute.048
    reroute_048 = pattern_generator.nodes.new("NodeReroute")
    reroute_048.name = "Reroute.048"
    # node Reroute.049
    reroute_049 = pattern_generator.nodes.new("NodeReroute")
    reroute_049.name = "Reroute.049"
    # node Reroute.050
    reroute_050 = pattern_generator.nodes.new("NodeReroute")
    reroute_050.name = "Reroute.050"
    # node Reroute.051
    reroute_051 = pattern_generator.nodes.new("NodeReroute")
    reroute_051.name = "Reroute.051"
    # node Reroute.052
    reroute_052 = pattern_generator.nodes.new("NodeReroute")
    reroute_052.name = "Reroute.052"
    # node Reroute.053
    reroute_053 = pattern_generator.nodes.new("NodeReroute")
    reroute_053.name = "Reroute.053"
    # node Reroute.054
    reroute_054 = pattern_generator.nodes.new("NodeReroute")
    reroute_054.name = "Reroute.054"
    # node Reroute.055
    reroute_055 = pattern_generator.nodes.new("NodeReroute")
    reroute_055.name = "Reroute.055"
    # node Reroute.056
    reroute_056 = pattern_generator.nodes.new("NodeReroute")
    reroute_056.name = "Reroute.056"
    # node Reroute.057
    reroute_057 = pattern_generator.nodes.new("NodeReroute")
    reroute_057.name = "Reroute.057"
    # node Reroute.058
    reroute_058 = pattern_generator.nodes.new("NodeReroute")
    reroute_058.name = "Reroute.058"
    # node Reroute.059
    reroute_059 = pattern_generator.nodes.new("NodeReroute")
    reroute_059.name = "Reroute.059"
    # node Reroute.060
    reroute_060 = pattern_generator.nodes.new("NodeReroute")
    reroute_060.name = "Reroute.060"
    # node Reroute.061
    reroute_061 = pattern_generator.nodes.new("NodeReroute")
    reroute_061.name = "Reroute.061"
    # node Reroute.062
    reroute_062 = pattern_generator.nodes.new("NodeReroute")
    reroute_062.name = "Reroute.062"
    # node Reroute.063
    reroute_063 = pattern_generator.nodes.new("NodeReroute")
    reroute_063.name = "Reroute.063"
    # node Reroute.064
    reroute_064 = pattern_generator.nodes.new("NodeReroute")
    reroute_064.name = "Reroute.064"
    # node Reroute.065
    reroute_065 = pattern_generator.nodes.new("NodeReroute")
    reroute_065.name = "Reroute.065"
    # node Reroute.066
    reroute_066 = pattern_generator.nodes.new("NodeReroute")
    reroute_066.name = "Reroute.066"

    # Set parents
    group_input_3.parent = frame_007
    arc.parent = frame_005
    instance_on_points.parent = frame_005
    points.parent = frame_005
    index_1.parent = frame_005
    map_range_1.parent = frame_005
    math_2.parent = frame_005
    transform_geometry.parent = frame_005
    join_geometry_1.parent = frame_005
    grid.parent = frame_007
    math_001_1.parent = frame_007
    transform_geometry_001.parent = frame_007
    math_002_1.parent = frame_005
    realize_instances.parent = frame_005
    curve_to_mesh.parent = frame_005
    delete_geometry.parent = frame_005
    position_1.parent = frame_005
    vector_math.parent = frame_005
    compare_1.parent = frame_005
    math_003_1.parent = frame_005
    math_004_1.parent = frame_005
    random_value_001_1.parent = frame_005
    combine_xyz.parent = frame_005
    realize_instances_001.parent = frame_005
    curve_to_mesh_002.parent = frame_005
    resample_curve.parent = frame_005
    resample_curve_001.parent = frame_005
    group_input_004_1.parent = frame_005
    group_input_005_1.parent = frame_005
    group_input_006_1.parent = frame_005
    group_input_007_1.parent = frame_005
    group_input_008_1.parent = frame_005
    group_input_009_1.parent = frame_005
    group_input_011_1.parent = frame_005
    group_input_012_1.parent = frame_005
    random_value_1.parent = frame_002
    group_input_016_1.parent = frame_002
    group_input_017_1.parent = frame_002
    random_value_002_1.parent = frame_002
    math_006_1.parent = frame_002
    switch_2.parent = frame_002
    group_input_018_1.parent = frame_002
    group_input_019_1.parent = frame_002
    compare_001_2.parent = frame_002
    compare_002_2.parent = frame_002
    boolean_math_1.parent = frame_002
    random_value_003_1.parent = frame_002
    curve_to_mesh_003.parent = frame
    curve_circle_001.parent = frame
    group_input_003_1.parent = frame
    math_008_1.parent = frame
    math_009_1.parent = frame
    grid_001.parent = frame
    group_input_020_1.parent = frame
    math_010.parent = frame_007
    set_position.parent = frame
    group_input_021_1.parent = frame
    combine_xyz_002.parent = frame
    math_011.parent = frame
    math_012.parent = frame
    math_013.parent = frame
    join_geometry_002.parent = frame
    switch_003_1.parent = frame
    group_input_023_1.parent = frame
    set_material_001.parent = frame
    group_input_025_1.parent = frame
    set_material_002.parent = frame
    group_input_026_1.parent = frame
    group_input_014_1.parent = frame_005
    combine_xyz_003.parent = frame_005
    math_005_1.parent = frame_005
    switch_004.parent = frame_005
    group_input_015_1.parent = frame_005
    switch_005.parent = frame_002
    random_value_005_1.parent = frame_002
    group_input_027_1.parent = frame_002
    math_015.parent = frame_002
    random_value_006_1.parent = frame_002
    math_016.parent = frame_002
    math_017.parent = frame_002
    math_018.parent = frame_002
    curve_to_mesh_005.parent = frame_007
    realize_instances_008.parent = frame_007
    attribute_statistic_003.parent = frame_007
    position_003.parent = frame_007
    separate_xyz_001.parent = frame_007
    math_024.parent = frame_007
    math_025.parent = frame_007
    math_026.parent = frame_007
    math_027.parent = frame_007
    math_028.parent = frame_007
    grid_002.parent = frame_007
    attribute_statistic_006.parent = frame_007
    position_006.parent = frame_007
    separate_xyz_002.parent = frame_007
    math_030.parent = frame_007
    random_value_007_1.parent = frame_002
    math_031.parent = frame_002
    random_value_008_1.parent = frame_002
    group_input_042.parent = frame_002
    switch_010_1.parent = frame_002
    random_value_009_1.parent = frame_002
    math_033.parent = frame_002
    math_034.parent = frame_002
    math_035.parent = frame_002
    math_036.parent = frame_002
    group_input_043.parent = frame_002
    switch_011_1.parent = frame_002
    math_032.parent = frame_002
    math_037.parent = frame_002
    math_038.parent = frame_002
    image_texture_1.parent = frame_006
    position_005.parent = frame_006
    image_info.parent = frame_006
    vector_math_002_1.parent = frame_006
    math_039.parent = frame_006
    math_040.parent = frame_006
    combine_xyz_007.parent = frame_006
    vector_math_004.parent = frame_006
    vector_math_005.parent = frame_006
    math_043.parent = frame_006
    math_044.parent = frame_006
    math_041.parent = frame_006
    group_input_052.parent = frame_006
    math_042.parent = frame_006
    subdivide_mesh.parent = frame_006
    group_input_028_1.parent = frame_006
    vector_math_003_1.parent = frame_006
    group_input_047.parent = frame_006
    delete_geometry_002.parent = frame_006
    boolean_math_002.parent = frame_006
    compare_004_1.parent = frame_006
    group_input_048.parent = frame_006
    group_input_054.parent = frame_006
    compare_014.parent = frame_006
    switch_022.parent = frame_006
    reroute_3.parent = frame_007
    reroute_001_3.parent = frame_007
    reroute_002_3.parent = frame_005
    reroute_003_3.parent = frame_005
    reroute_004_3.parent = frame_005
    reroute_005_3.parent = frame_002
    reroute_006_3.parent = frame_002
    reroute_007_2.parent = frame_002
    reroute_008_2.parent = frame_002
    reroute_009_2.parent = frame_002
    reroute_010_2.parent = frame_002
    reroute_011_1.parent = frame
    reroute_014.parent = frame_006
    reroute_015.parent = frame_006
    reroute_022.parent = frame_002
    reroute_023.parent = frame_002
    reroute_024.parent = frame_002
    reroute_025.parent = frame_002
    reroute_028.parent = frame_005
    reroute_029.parent = frame_002
    reroute_030.parent = frame_002
    reroute_031.parent = frame_002
    reroute_032.parent = frame_002
    reroute_038.parent = frame_002
    reroute_039.parent = frame_006
    reroute_040.parent = frame_002
    reroute_041.parent = frame_002
    reroute_042.parent = frame_002
    reroute_043.parent = frame_002
    reroute_044.parent = frame_007
    reroute_045.parent = frame_007
    reroute_046.parent = frame_007

    # Set locations
    group_input_3.location = (-1060.3836669921875, 1004.48779296875)
    set_material.location = (9467.759765625, 508.3438720703125)
    arc.location = (-1477.8836669921875, 299.38775634765625)
    instance_on_points.location = (-1275.3836669921875, 426.38775634765625)
    points.location = (-1477.8836669921875, 426.38775634765625)
    index_1.location = (-1760.18359375, 146.38775634765625)
    map_range_1.location = (-1477.8836669921875, 146.38775634765625)
    math_2.location = (-1760.18359375, 46.38775634765625)
    transform_geometry.location = (-845.3836669921875, 253.38775634765625)
    join_geometry_1.location = (261.71636962890625, 167.18878173828125)
    grid.location = (-630.3836669921875, 932.48779296875)
    instance_on_points_001.location = (519.016357421875, 574.580810546875)
    math_001_1.location = (-845.3836669921875, 888.48779296875)
    transform_geometry_001.location = (-373.0836486816406, 932.48779296875)
    math_002_1.location = (-1760.18359375, -129.61224365234375)
    realize_instances.location = (-630.3836669921875, 253.38775634765625)
    curve_to_mesh.location = (-373.0836486816406, 253.38775634765625)
    delete_geometry.location = (-70.58364868164062, 253.38775634765625)
    position_1.location = (-845.3836669921875, 80.38775634765625)
    vector_math.location = (-630.3836669921875, 80.38775634765625)
    compare_1.location = (-373.0836486816406, 80.38775634765625)
    math_003_1.location = (-630.3836669921875, -70.61224365234375)
    rotate_instances.location = (746.516357421875, 287.2748718261719)
    math_004_1.location = (-373.0836486816406, -567.6122436523438)
    random_value_001_1.location = (-630.3836669921875, -567.6122436523438)
    combine_xyz.location = (-70.58364868164062, -567.6122436523438)
    curve_circle.location = (8822.759765625, 756.19775390625)
    curve_to_mesh_001.location = (9037.759765625, 781.89794921875)
    mesh_to_curve.location = (5373.6162109375, -667.1192626953125)
    realize_instances_001.location = (-373.0836486816406, 426.38775634765625)
    curve_to_mesh_002.location = (-70.58364868164062, 426.38775634765625)
    resample_curve.location = (-1060.3836669921875, 253.38775634765625)
    resample_curve_001.location = (-630.3836669921875, 426.38775634765625)
    group_input_004_1.location = (-845.3836669921875, -465.6122131347656)
    group_input_005_1.location = (-2012.68359375, -21.04901123046875)
    group_input_006_1.location = (-1760.18359375, 299.38775634765625)
    group_input_007_1.location = (-2012.68359375, -123.04901123046875)
    group_input_008_1.location = (-1760.18359375, -305.6122131347656)
    group_input_009_1.location = (-845.3836669921875, -567.6122436523438)
    group_input_010_1.location = (8607.759765625, 768.06787109375)
    group_input_011_1.location = (-1275.3836669921875, 257.38775634765625)
    group_input_012_1.location = (-845.3836669921875, 368.38775634765625)
    trim_curve.location = (6538.41650390625, -156.60772705078125)
    random_value_1.location = (4107.9765625, -1693.300048828125)
    group_input_016_1.location = (3842.976318359375, -1200.9691162109375)
    group_input_017_1.location = (4587.9765625, 172.6998291015625)
    random_value_002_1.location = (4587.9765625, 48.6998291015625)
    math_006_1.location = (4877.9765625, -841.3001098632812)
    switch_2.location = (6240.4765625, -426.458984375)
    group_input_018_1.location = (5950.4765625, -28.3001708984375)
    group_input_019_1.location = (5660.4765625, 323.6998291015625)
    compare_001_2.location = (5950.4765625, 323.6998291015625)
    switch_001_1.location = (6955.91650390625, -31.64013671875)
    compare_002_2.location = (5950.4765625, 147.6998291015625)
    boolean_math_1.location = (6240.4765625, -255.458984375)
    delete_geometry_001.location = (7170.91650390625, 315.68206787109375)
    spline_length.location = (6740.91650390625, -964.3653564453125)
    compare_003_1.location = (6955.91650390625, -964.3653564453125)
    random_value_003_1.location = (4347.9765625, 48.6998291015625)
    join_geometry_001.location = (9712.5595703125, 360.14599609375)
    instance_on_points_002.location = (8822.759765625, 381.770751953125)
    endpoint_selection.location = (8607.759765625, 471.06787109375)
    trim_curve_001.location = (8607.759765625, 644.06787109375)
    random_value_004_1.location = (8405.259765625, 542.026611328125)
    curve_line.location = (8607.759765625, 371.06787109375)
    group_input_001_1.location = (7968.41650390625, 371.06787109375)
    combine_xyz_001.location = (8405.259765625, 371.06787109375)
    math_007_1.location = (8190.25927734375, 371.06787109375)
    curve_to_mesh_003.location = (-2291.3671875, 30.810791015625)
    curve_circle_001.location = (-2506.3671875, 142.37646484375)
    group_input_003_1.location = (-3138.86767578125, 142.37646484375)
    math_008_1.location = (-2721.3671875, 142.37646484375)
    math_009_1.location = (-2923.8671875, 84.37646484375)
    grid_001.location = (-2721.3671875, -55.62353515625)
    group_input_020_1.location = (-3138.86767578125, 18.37646484375)
    math_010.location = (-845.3836669921875, 712.48779296875)
    set_position.location = (-2506.3671875, -55.62353515625)
    group_input_021_1.location = (-3138.86767578125, -443.62353515625)
    combine_xyz_002.location = (-2721.3671875, -443.62353515625)
    math_011.location = (-2923.8671875, -443.62353515625)
    math_012.location = (-2923.8671875, -91.62353515625)
    math_013.location = (-2923.8671875, -267.62353515625)
    join_geometry_002.location = (-2076.3671875, -107.4140625)
    switch_002_1.location = (9902.5595703125, 488.4993896484375)
    group_input_022_1.location = (9712.5595703125, 525.3963623046875)
    frame.location = (11329.126953125, -62.40869140625)
    switch_003_1.location = (-1861.3671875, 142.239501953125)
    group_input_023_1.location = (-2076.3671875, 141.5859375)
    group_input_024_1.location = (9252.759765625, 486.08740234375)
    set_material_001.location = (-2076.3671875, 39.5859375)
    group_input_025_1.location = (-2291.3671875, 132.810791015625)
    set_material_002.location = (-2291.3671875, -118.189208984375)
    group_input_026_1.location = (-2506.3671875, -202.62353515625)
    group_input_013_1.location = (8190.25927734375, 542.026611328125)
    group_input_014_1.location = (-630.3836669921875, -268.6122131347656)
    combine_xyz_003.location = (-70.58364868164062, -268.6122131347656)
    math_005_1.location = (-373.0836486816406, -268.6122131347656)
    switch_004.location = (261.71636962890625, 42.18878173828125)
    group_input_015_1.location = (-70.58364868164062, 57.38775634765625)
    switch_005.location = (6240.4765625, -619.458984375)
    random_value_005_1.location = (4877.9765625, -1215.300048828125)
    group_input_027_1.location = (5950.4765625, -381.30010986328125)
    math_015.location = (4357.482421875, 323.6998291015625)
    random_value_006_1.location = (4107.9765625, 323.6998291015625)
    math_016.location = (4877.9765625, -1039.300048828125)
    math_017.location = (5092.9765625, -1039.300048828125)
    math_018.location = (5370.4765625, -1141.300048828125)
    frame_002.location = (3.139892578125, 1247.1807861328125)
    merge_by_distance_001.location = (1341.516357421875, 37.96470642089844)
    switch_006_1.location = (1569.016357421875, -92.80807495117188)
    group_input_029_1.location = (1341.516357421875, 139.96470642089844)
    curve_to_mesh_004.location = (7360.91650390625, 315.68206787109375)
    mesh_to_curve_001.location = (8405.259765625, 735.3326416015625)
    realize_instances_002.location = (1151.516357421875, 37.96470642089844)
    merge_by_distance_003.location = (1341.516357421875, -113.03529357910156)
    switch_009_1.location = (3846.116455078125, -1186.4781494140625)
    group_input_034.location = (3591.31640625, -1266.679931640625)
    geometry_to_instance.location = (3581.31640625, -1426.679931640625)
    store_named_attribute_001.location = (9252.759765625, 682.08740234375)
    group_input_038.location = (9037.759765625, 628.28076171875)
    curve_to_mesh_005.location = (-1477.8836669921875, 1110.5030517578125)
    realize_instances_008.location = (-1275.3836669921875, 1110.5030517578125)
    attribute_statistic_003.location = (-1060.3836669921875, 1400.48779296875)
    position_003.location = (-1477.8836669921875, 1237.5030517578125)
    separate_xyz_001.location = (-1275.3836669921875, 1237.5030517578125)
    math_024.location = (-845.3836669921875, 1400.48779296875)
    math_025.location = (-630.3836669921875, 1400.48779296875)
    math_026.location = (-630.3836669921875, 1202.48779296875)
    math_027.location = (-373.0836486816406, 1108.48779296875)
    math_028.location = (-373.0836486816406, 1284.48779296875)
    grid_002.location = (-70.58364868164062, 1266.570556640625)
    string_to_curves_003.location = (-1785.18359375, 846.296142578125)
    fill_curve_002.location = (2731.516357421875, -1415.712158203125)
    group_input_044.location = (-2012.68359375, 766.9034423828125)
    group_input_045.location = (-2232.483642578125, 664.9034423828125)
    group_input_046.location = (-2012.68359375, 868.9034423828125)
    math_029.location = (-2012.68359375, 664.9034423828125)
    attribute_statistic_006.location = (-1060.3836669921875, 1202.48779296875)
    position_006.location = (-1477.8836669921875, 983.5030517578125)
    separate_xyz_002.location = (-1275.3836669921875, 983.5030517578125)
    math_030.location = (-845.3836669921875, 1202.48779296875)
    scale_instances.location = (949.016357421875, 118.17687225341797)
    group_input_037.location = (746.516357421875, 119.94305419921875)
    named_attribute_001.location = (5953.6162109375, -667.1193237304688)
    join_geometry_005.location = (6740.91650390625, 9.471435546875)
    delete_geometry_005.location = (6538.41650390625, 320.81341552734375)
    named_attribute_002.location = (5953.6162109375, 1836.980712890625)
    boolean_math_001_1.location = (6243.6162109375, 1836.980712890625)
    delete_geometry_006.location = (6243.6162109375, -667.1193237304688)
    random_value_007_1.location = (4877.9765625, -1542.300048828125)
    math_031.location = (5092.9765625, -1237.300048828125)
    random_value_008_1.location = (4587.9765625, -1542.300048828125)
    group_input_042.location = (5660.4765625, -1039.300048828125)
    switch_010_1.location = (5950.4765625, -541.3001098632812)
    random_value_009_1.location = (4587.9765625, 323.6998291015625)
    math_033.location = (4877.9765625, 207.6998291015625)
    math_034.location = (5092.9765625, 207.6998291015625)
    math_035.location = (5370.4765625, -188.3001708984375)
    math_036.location = (5660.4765625, -643.3001098632812)
    group_input_043.location = (5660.4765625, -541.3001098632812)
    switch_011_1.location = (5950.4765625, -188.3001708984375)
    math_032.location = (4877.9765625, -1366.300048828125)
    math_037.location = (5370.4765625, -1339.300048828125)
    math_038.location = (5660.4765625, -1339.300048828125)
    group_output_001.location = (10092.5595703125, 488.4993896484375)
    merge_by_distance.location = (7765.91650390625, 514.4326782226562)
    group_input_050.location = (7550.91650390625, -51.31793212890625)
    group_input_051.location = (7360.91650390625, 86.12921142578125)
    random_value_010.location = (7550.91650390625, 119.68206787109375)
    merge_by_distance_002.location = (7550.91650390625, 315.68206787109375)
    image_texture_1.location = (5985.5166015625, 303.544189453125)
    position_005.location = (4948.0166015625, 552.7551879882812)
    image_info.location = (3878.416259765625, 289.56787109375)
    vector_math_002_1.location = (5150.5166015625, 552.7551879882812)
    math_039.location = (4260.71630859375, 455.28778076171875)
    math_040.location = (4260.71630859375, 279.287841796875)
    combine_xyz_007.location = (4745.5166015625, 254.755126953125)
    vector_math_004.location = (5568.0166015625, 278.6915283203125)
    vector_math_005.location = (5758.0166015625, 278.6915283203125)
    math_043.location = (4518.0166015625, 455.28778076171875)
    math_044.location = (4518.0166015625, 279.287841796875)
    math_041.location = (4745.5166015625, 452.75518798828125)
    group_input_052.location = (4518.0166015625, 557.2877807617188)
    math_042.location = (4948.0166015625, 452.75518798828125)
    frame_005.location = (0.0, 0.0)
    frame_006.location = (-3999.0, -1469.0)
    frame_007.location = (0.0, 0.0)
    group_input_049.location = (3591.31640625, -741.5040893554688)
    group_001.location = (3051.31640625, -976.9976806640625)
    subdivide_mesh.location = (6503.0166015625, 537.544189453125)
    group_input_028_1.location = (5758.0166015625, 482.6915283203125)
    vector_math_003_1.location = (5340.5166015625, 552.7551879882812)
    group_input_047.location = (5150.5166015625, 379.755126953125)
    delete_geometry_002.location = (6730.5166015625, 433.99169921875)
    boolean_math_002.location = (6503.0166015625, 303.544189453125)
    group_005.location = (3051.31640625, -234.46636962890625)
    group_input_035.location = (2731.516357421875, -465.19891357421875)
    switch_012.location = (3846.116455078125, -993.4781494140625)
    group_input_036.location = (3591.31640625, -976.9976806640625)
    geometry_to_instance_001.location = (3581.31640625, -1136.9976806640625)
    set_position_001.location = (2731.516357421875, -594.5191650390625)
    position_002.location = (1759.016357421875, -433.14312744140625)
    attribute_statistic_001.location = (2036.516357421875, -329.36041259765625)
    vector_math_006.location = (2289.016357421875, -556.7040405273438)
    vector_rotate.location = (2504.016357421875, -556.7040405273438)
    realize_instances_004.location = (1759.016357421875, -92.80807495117188)
    compare_004_1.location = (6288.0166015625, 303.544189453125)
    group_input_048.location = (5758.0166015625, 380.6915283203125)
    group_input_054.location = (3625.916259765625, 289.56787109375)
    switch_013.location = (4351.1162109375, -984.210693359375)
    compare_005_2.location = (4111.1162109375, -667.1193237304688)
    compare_006_1.location = (3846.116455078125, -725.3095703125)
    switch_014.location = (4111.1162109375, -980.9057006835938)
    group_input_055.location = (-630.3836669921875, 1685.2938232421875)
    switch_015.location = (261.71636962890625, 1314.7308349609375)
    compare_007_1.location = (-70.58364868164062, 1829.5877685546875)
    compare_008_1.location = (-373.0836486816406, 1653.5877685546875)
    switch_016.location = (-70.58364868164062, 1653.5877685546875)
    compare_009.location = (3051.31640625, -465.19891357421875)
    switch_017.location = (3328.81640625, -651.96484375)
    switch_018.location = (3328.81640625, -1060.57275390625)
    group_input_033.location = (2731.516357421875, -743.5191650390625)
    named_attribute_1.location = (7765.91650390625, 321.4326171875)
    group_002.location = (7969.43798828125, 543.9261474609375)
    switch_019.location = (8190.25927734375, 735.3326416015625)
    group_input_056.location = (7969.43798828125, 714.7349853515625)
    switch_007_1.location = (4591.1162109375, -894.7996826171875)
    curve_to_mesh_006.location = (3051.31640625, -2155.51220703125)
    store_named_attribute_002_1.location = (3328.81640625, -2155.51220703125)
    realize_instances_005.location = (3591.31640625, -2155.51220703125)
    delete_geometry_004_1.location = (3051.31640625, -1632.8463134765625)
    compare_011.location = (2731.516357421875, -1566.712158203125)
    edge_neighbors.location = (2504.016357421875, -1566.712158203125)
    group_input_057.location = (3051.31640625, -1529.31201171875)
    switch_020.location = (3846.116455078125, -1379.4781494140625)
    compare_012.location = (3591.31640625, -1562.4364013671875)
    compare_013.location = (3328.81640625, -1665.1396484375)
    switch_021.location = (3591.31640625, -1756.15966796875)
    blur_attribute.location = (3051.31640625, -1972.392333984375)
    position_001.location = (2731.516357421875, -1939.571044921875)
    set_position_002.location = (3328.81640625, -1841.2933349609375)
    group_input_058.location = (2731.516357421875, -2039.571044921875)
    compare_014.location = (6035.5166015625, 537.544189453125)
    switch_022.location = (6288.0166015625, 537.544189453125)
    group_input_059.location = (4351.1162109375, -667.1193237304688)
    switch_023.location = (4881.1162109375, -667.1192626953125)
    join_geometry_003.location = (4591.1162109375, -1090.4427490234375)
    bake_1.location = (5096.1162109375, -667.1192626953125)
    store_named_attribute_003.location = (5953.6162109375, -860.3775634765625)
    group_003.location = (5663.6162109375, -1080.99365234375)
    group_input_039.location = (5373.6162109375, -931.142822265625)
    group_input_041.location = (5663.6162109375, -978.688232421875)
    named_attribute_003.location = (5373.6162109375, -1297.142822265625)
    store_named_attribute.location = (2504.016357421875, -315.32293701171875)
    mesh_island_1.location = (2289.016357421875, -398.99609375)
    named_attribute_004.location = (-2422.4833984375, 806.5496826171875)
    reroute_3.location = (-705.3836669921875, 969.163330078125)
    reroute_001_3.location = (-705.3836669921875, 947.163330078125)
    reroute_002_3.location = (-1785.18359375, 366.1634216308594)
    reroute_003_3.location = (-1785.18359375, -407.6122131347656)
    reroute_004_3.location = (-705.3836669921875, -407.6122131347656)
    reroute_005_3.location = (4107.9765625, -1542.300048828125)
    reroute_006_3.location = (4247.9765625, -1542.300048828125)
    reroute_007_2.location = (4877.9765625, 323.699951171875)
    reroute_008_2.location = (5017.9765625, 323.699951171875)
    reroute_009_2.location = (4877.9765625, 9.699951171875)
    reroute_010_2.location = (5232.9765625, 9.699951171875)
    reroute_011_1.location = (-2783.8671875, 107.30500793457031)
    reroute_012.location = (3846.116455078125, -667.1193237304688)
    reroute_013.location = (3986.116455078125, -667.1193237304688)
    reroute_014.location = (5985.5166015625, 361.544189453125)
    reroute_015.location = (6225.5166015625, 361.544189453125)
    reroute_016.location = (1986.516357421875, -664.315185546875)
    reroute_017.location = (-373.0836486816406, 1720.1634521484375)
    reroute_018.location = (3468.81640625, -1564.5841064453125)
    reroute_019.location = (4731.1162109375, -723.99853515625)
    reroute_020.location = (4351.1162109375, -1572.4781494140625)
    reroute_021.location = (6383.6162109375, -1572.4781494140625)
    reroute_022.location = (4487.9765625, -1542.300048828125)
    reroute_023.location = (5232.9765625, 323.699951171875)
    reroute_024.location = (5370.4765625, -130.300048828125)
    reroute_025.location = (5510.4765625, -130.300048828125)
    reroute_026.location = (-1477.8836669921875, -2155.51220703125)
    reroute_027.location = (2644.016357421875, -2155.51220703125)
    reroute_028.location = (-705.3836669921875, 391.1634216308594)
    reroute_029.location = (4587.9765625, -1301.1793212890625)
    reroute_030.location = (5510.4765625, 9.699951171875)
    reroute_031.location = (5660.4765625, -483.30010986328125)
    reroute_032.location = (5800.4765625, -483.30010986328125)
    reroute_033.location = (-120.5836410522461, -793.6122436523438)
    reroute_034.location = (2429.016357421875, -793.6122436523438)
    reroute_035.location = (-120.5836410522461, 1525.1634521484375)
    reroute_036.location = (-120.5836410522461, 1547.1634521484375)
    reroute_037.location = (519.016357421875, 205.1693878173828)
    reroute_038.location = (5232.9765625, 288.82080078125)
    reroute_039.location = (5480.5166015625, 219.494384765625)
    reroute_040.location = (5800.4765625, -876.1793212890625)
    reroute_041.location = (6090.4765625, -130.300048828125)
    reroute_042.location = (5800.4765625, -1176.1793212890625)
    reroute_043.location = (6090.4765625, -483.30010986328125)
    reroute_044.location = (-373.0836486816406, 1342.48779296875)
    reroute_045.location = (-233.08364868164062, 1342.48779296875)
    reroute_046.location = (-233.08364868164062, 1365.163330078125)
    reroute_047.location = (6880.91650390625, 956.9002685546875)
    reroute_048.location = (1151.516357421875, -196.54583740234375)
    reroute_049.location = (2429.016357421875, -127.80807495117188)
    reroute_050.location = (2871.516357421875, -2155.51220703125)
    reroute_051.location = (3051.31640625, -918.9976806640625)
    reroute_052.location = (3468.81640625, -918.9976806640625)
    reroute_053.location = (3581.31640625, -1099.559814453125)
    reroute_054.location = (3581.31640625, -1368.679931640625)
    reroute_055.location = (3741.31640625, -1368.679931640625)
    reroute_056.location = (3986.116455078125, -918.9976806640625)
    reroute_057.location = (4251.1162109375, -1221.559814453125)
    reroute_058.location = (4491.1162109375, -1414.559814453125)
    reroute_059.location = (5803.6162109375, -702.1193237304688)
    reroute_060.location = (6243.6162109375, -871.0178833007812)
    reroute_061.location = (6383.6162109375, -871.0178833007812)
    reroute_062.location = (6880.91650390625, -871.0178833007812)
    reroute_063.location = (7968.41650390625, 629.5740356445312)
    reroute_064.location = (8607.759765625, 826.06787109375)
    reroute_065.location = (8962.759765625, 826.06787109375)
    reroute_066.location = (9712.5595703125, 382.2157287597656)

    # Set dimensions
    group_input_3.width, group_input_3.height = 140.0, 100.0
    set_material.width, set_material.height = 140.0, 100.0
    arc.width, arc.height = 140.0, 100.0
    instance_on_points.width, instance_on_points.height = 140.0, 100.0
    points.width, points.height = 140.0, 100.0
    index_1.width, index_1.height = 140.0, 100.0
    map_range_1.width, map_range_1.height = 140.0, 100.0
    math_2.width, math_2.height = 140.0, 100.0
    transform_geometry.width, transform_geometry.height = 140.0, 100.0
    join_geometry_1.width, join_geometry_1.height = 140.0, 100.0
    grid.width, grid.height = 140.0, 100.0
    instance_on_points_001.width, instance_on_points_001.height = 140.0, 100.0
    math_001_1.width, math_001_1.height = 140.0, 100.0
    transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
    math_002_1.width, math_002_1.height = 140.0, 100.0
    realize_instances.width, realize_instances.height = 140.0, 100.0
    curve_to_mesh.width, curve_to_mesh.height = 140.0, 100.0
    delete_geometry.width, delete_geometry.height = 140.0, 100.0
    position_1.width, position_1.height = 140.0, 100.0
    vector_math.width, vector_math.height = 140.0, 100.0
    compare_1.width, compare_1.height = 140.0, 100.0
    math_003_1.width, math_003_1.height = 140.0, 100.0
    rotate_instances.width, rotate_instances.height = 140.0, 100.0
    math_004_1.width, math_004_1.height = 140.0, 100.0
    random_value_001_1.width, random_value_001_1.height = 140.0, 100.0
    combine_xyz.width, combine_xyz.height = 140.0, 100.0
    curve_circle.width, curve_circle.height = 140.0, 100.0
    curve_to_mesh_001.width, curve_to_mesh_001.height = 140.0, 100.0
    mesh_to_curve.width, mesh_to_curve.height = 140.0, 100.0
    realize_instances_001.width, realize_instances_001.height = 140.0, 100.0
    curve_to_mesh_002.width, curve_to_mesh_002.height = 140.0, 100.0
    resample_curve.width, resample_curve.height = 140.0, 100.0
    resample_curve_001.width, resample_curve_001.height = 140.0, 100.0
    group_input_004_1.width, group_input_004_1.height = 140.0, 100.0
    group_input_005_1.width, group_input_005_1.height = 140.0, 100.0
    group_input_006_1.width, group_input_006_1.height = 140.0, 100.0
    group_input_007_1.width, group_input_007_1.height = 140.0, 100.0
    group_input_008_1.width, group_input_008_1.height = 140.0, 100.0
    group_input_009_1.width, group_input_009_1.height = 140.0, 100.0
    group_input_010_1.width, group_input_010_1.height = 140.0, 100.0
    group_input_011_1.width, group_input_011_1.height = 140.0, 100.0
    group_input_012_1.width, group_input_012_1.height = 140.0, 100.0
    trim_curve.width, trim_curve.height = 140.0, 100.0
    random_value_1.width, random_value_1.height = 140.0, 100.0
    group_input_016_1.width, group_input_016_1.height = 140.0, 100.0
    group_input_017_1.width, group_input_017_1.height = 140.0, 100.0
    random_value_002_1.width, random_value_002_1.height = 140.0, 100.0
    math_006_1.width, math_006_1.height = 140.0, 100.0
    switch_2.width, switch_2.height = 140.0, 100.0
    group_input_018_1.width, group_input_018_1.height = 140.0, 100.0
    group_input_019_1.width, group_input_019_1.height = 140.0, 100.0
    compare_001_2.width, compare_001_2.height = 140.0, 100.0
    switch_001_1.width, switch_001_1.height = 140.0, 100.0
    compare_002_2.width, compare_002_2.height = 140.0, 100.0
    boolean_math_1.width, boolean_math_1.height = 140.0, 100.0
    delete_geometry_001.width, delete_geometry_001.height = 140.0, 100.0
    spline_length.width, spline_length.height = 140.0, 100.0
    compare_003_1.width, compare_003_1.height = 140.0, 100.0
    random_value_003_1.width, random_value_003_1.height = 140.0, 100.0
    join_geometry_001.width, join_geometry_001.height = 140.0, 100.0
    instance_on_points_002.width, instance_on_points_002.height = 140.0, 100.0
    endpoint_selection.width, endpoint_selection.height = 140.0, 100.0
    trim_curve_001.width, trim_curve_001.height = 140.0, 100.0
    random_value_004_1.width, random_value_004_1.height = 140.0, 100.0
    curve_line.width, curve_line.height = 140.0, 100.0
    group_input_001_1.width, group_input_001_1.height = 142.04296875, 100.0
    combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
    math_007_1.width, math_007_1.height = 140.0, 100.0
    curve_to_mesh_003.width, curve_to_mesh_003.height = 140.0, 100.0
    curve_circle_001.width, curve_circle_001.height = 140.0, 100.0
    group_input_003_1.width, group_input_003_1.height = 140.0, 100.0
    math_008_1.width, math_008_1.height = 140.0, 100.0
    math_009_1.width, math_009_1.height = 140.0, 100.0
    grid_001.width, grid_001.height = 140.0, 100.0
    group_input_020_1.width, group_input_020_1.height = 140.0, 100.0
    math_010.width, math_010.height = 140.0, 100.0
    set_position.width, set_position.height = 140.0, 100.0
    group_input_021_1.width, group_input_021_1.height = 140.0, 100.0
    combine_xyz_002.width, combine_xyz_002.height = 140.0, 100.0
    math_011.width, math_011.height = 140.0, 100.0
    math_012.width, math_012.height = 140.0, 100.0
    math_013.width, math_013.height = 140.0, 100.0
    join_geometry_002.width, join_geometry_002.height = 140.0, 100.0
    switch_002_1.width, switch_002_1.height = 140.0, 100.0
    group_input_022_1.width, group_input_022_1.height = 140.0, 100.0
    frame.width, frame.height = 1478.0, 837.0
    switch_003_1.width, switch_003_1.height = 140.0, 100.0
    group_input_023_1.width, group_input_023_1.height = 140.0, 100.0
    group_input_024_1.width, group_input_024_1.height = 140.0, 100.0
    set_material_001.width, set_material_001.height = 140.0, 100.0
    group_input_025_1.width, group_input_025_1.height = 140.0, 100.0
    set_material_002.width, set_material_002.height = 140.0, 100.0
    group_input_026_1.width, group_input_026_1.height = 140.0, 100.0
    group_input_013_1.width, group_input_013_1.height = 140.0, 100.0
    group_input_014_1.width, group_input_014_1.height = 140.0, 100.0
    combine_xyz_003.width, combine_xyz_003.height = 140.0, 100.0
    math_005_1.width, math_005_1.height = 140.0, 100.0
    switch_004.width, switch_004.height = 140.0, 100.0
    group_input_015_1.width, group_input_015_1.height = 140.0, 100.0
    switch_005.width, switch_005.height = 140.0, 100.0
    random_value_005_1.width, random_value_005_1.height = 140.0, 100.0
    group_input_027_1.width, group_input_027_1.height = 140.0, 100.0
    math_015.width, math_015.height = 120.98828125, 100.0
    random_value_006_1.width, random_value_006_1.height = 140.0, 100.0
    math_016.width, math_016.height = 140.0, 100.0
    math_017.width, math_017.height = 140.0, 100.0
    math_018.width, math_018.height = 140.0, 100.0
    frame_002.width, frame_002.height = 2598.000244140625, 2270.880859375
    merge_by_distance_001.width, merge_by_distance_001.height = 140.0, 100.0
    switch_006_1.width, switch_006_1.height = 140.0, 100.0
    group_input_029_1.width, group_input_029_1.height = 140.0, 100.0
    curve_to_mesh_004.width, curve_to_mesh_004.height = 140.0, 100.0
    mesh_to_curve_001.width, mesh_to_curve_001.height = 140.0, 100.0
    realize_instances_002.width, realize_instances_002.height = 140.0, 100.0
    merge_by_distance_003.width, merge_by_distance_003.height = 140.0, 100.0
    switch_009_1.width, switch_009_1.height = 140.0, 100.0
    group_input_034.width, group_input_034.height = 140.0, 100.0
    geometry_to_instance.width, geometry_to_instance.height = 160.0, 100.0
    store_named_attribute_001.width, store_named_attribute_001.height = 140.0, 100.0
    group_input_038.width, group_input_038.height = 140.0, 100.0
    curve_to_mesh_005.width, curve_to_mesh_005.height = 140.0, 100.0
    realize_instances_008.width, realize_instances_008.height = 140.0, 100.0
    attribute_statistic_003.width, attribute_statistic_003.height = 140.0, 100.0
    position_003.width, position_003.height = 140.0, 100.0
    separate_xyz_001.width, separate_xyz_001.height = 140.0, 100.0
    math_024.width, math_024.height = 140.0, 100.0
    math_025.width, math_025.height = 140.0, 100.0
    math_026.width, math_026.height = 140.0, 100.0
    math_027.width, math_027.height = 140.0, 100.0
    math_028.width, math_028.height = 140.0, 100.0
    grid_002.width, grid_002.height = 140.0, 100.0
    string_to_curves_003.width, string_to_curves_003.height = 190.0, 100.0
    fill_curve_002.width, fill_curve_002.height = 140.0, 100.0
    group_input_044.width, group_input_044.height = 140.0, 100.0
    group_input_045.width, group_input_045.height = 140.0, 100.0
    group_input_046.width, group_input_046.height = 140.0, 100.0
    math_029.width, math_029.height = 140.0, 100.0
    attribute_statistic_006.width, attribute_statistic_006.height = 140.0, 100.0
    position_006.width, position_006.height = 140.0, 100.0
    separate_xyz_002.width, separate_xyz_002.height = 140.0, 100.0
    math_030.width, math_030.height = 140.0, 100.0
    scale_instances.width, scale_instances.height = 140.0, 100.0
    group_input_037.width, group_input_037.height = 140.0, 100.0
    named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
    join_geometry_005.width, join_geometry_005.height = 140.0, 100.0
    delete_geometry_005.width, delete_geometry_005.height = 140.0, 100.0
    named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
    boolean_math_001_1.width, boolean_math_001_1.height = 140.0, 100.0
    delete_geometry_006.width, delete_geometry_006.height = 140.0, 100.0
    random_value_007_1.width, random_value_007_1.height = 140.0, 100.0
    math_031.width, math_031.height = 140.0, 100.0
    random_value_008_1.width, random_value_008_1.height = 140.0, 100.0
    group_input_042.width, group_input_042.height = 140.0, 100.0
    switch_010_1.width, switch_010_1.height = 140.0, 100.0
    random_value_009_1.width, random_value_009_1.height = 140.0, 100.0
    math_033.width, math_033.height = 140.0, 100.0
    math_034.width, math_034.height = 140.0, 100.0
    math_035.width, math_035.height = 140.0, 100.0
    math_036.width, math_036.height = 140.0, 100.0
    group_input_043.width, group_input_043.height = 140.0, 100.0
    switch_011_1.width, switch_011_1.height = 140.0, 100.0
    math_032.width, math_032.height = 140.0, 100.0
    math_037.width, math_037.height = 140.0, 100.0
    math_038.width, math_038.height = 140.0, 100.0
    group_output_001.width, group_output_001.height = 140.0, 100.0
    merge_by_distance.width, merge_by_distance.height = 140.0, 100.0
    group_input_050.width, group_input_050.height = 140.0, 100.0
    group_input_051.width, group_input_051.height = 140.0, 100.0
    random_value_010.width, random_value_010.height = 140.0, 100.0
    merge_by_distance_002.width, merge_by_distance_002.height = 140.0, 100.0
    image_texture_1.width, image_texture_1.height = 240.0, 100.0
    position_005.width, position_005.height = 140.0, 100.0
    image_info.width, image_info.height = 240.0, 100.0
    vector_math_002_1.width, vector_math_002_1.height = 140.0, 100.0
    math_039.width, math_039.height = 140.0, 100.0
    math_040.width, math_040.height = 140.0, 100.0
    combine_xyz_007.width, combine_xyz_007.height = 140.0, 100.0
    vector_math_004.width, vector_math_004.height = 140.0, 100.0
    vector_math_005.width, vector_math_005.height = 140.0, 100.0
    math_043.width, math_043.height = 140.0, 100.0
    math_044.width, math_044.height = 140.0, 100.0
    math_041.width, math_041.height = 140.0, 100.0
    group_input_052.width, group_input_052.height = 140.0, 100.0
    math_042.width, math_042.height = 140.0, 100.0
    frame_005.width, frame_005.height = 2475.0, 1190.0
    frame_006.width, frame_006.height = 3305.0, 474.0
    frame_007.width, frame_007.height = 1607.0, 884.0
    group_input_049.width, group_input_049.height = 140.0, 100.0
    group_001.width, group_001.height = 140.0, 100.0
    subdivide_mesh.width, subdivide_mesh.height = 140.0, 100.0
    group_input_028_1.width, group_input_028_1.height = 140.0, 100.0
    vector_math_003_1.width, vector_math_003_1.height = 140.0, 100.0
    group_input_047.width, group_input_047.height = 140.0, 100.0
    delete_geometry_002.width, delete_geometry_002.height = 140.0, 100.0
    boolean_math_002.width, boolean_math_002.height = 140.0, 100.0
    group_005.width, group_005.height = 140.0, 100.0
    group_input_035.width, group_input_035.height = 140.0, 100.0
    switch_012.width, switch_012.height = 140.0, 100.0
    group_input_036.width, group_input_036.height = 140.0, 100.0
    geometry_to_instance_001.width, geometry_to_instance_001.height = 160.0, 100.0
    set_position_001.width, set_position_001.height = 140.0, 100.0
    position_002.width, position_002.height = 140.0, 100.0
    attribute_statistic_001.width, attribute_statistic_001.height = 140.0, 100.0
    vector_math_006.width, vector_math_006.height = 140.0, 100.0
    vector_rotate.width, vector_rotate.height = 140.0, 100.0
    realize_instances_004.width, realize_instances_004.height = 140.0, 100.0
    compare_004_1.width, compare_004_1.height = 140.0, 100.0
    group_input_048.width, group_input_048.height = 140.0, 100.0
    group_input_054.width, group_input_054.height = 140.0, 100.0
    switch_013.width, switch_013.height = 140.0, 100.0
    compare_005_2.width, compare_005_2.height = 140.0, 100.0
    compare_006_1.width, compare_006_1.height = 140.0, 100.0
    switch_014.width, switch_014.height = 140.0, 100.0
    group_input_055.width, group_input_055.height = 140.0, 100.0
    switch_015.width, switch_015.height = 140.0, 100.0
    compare_007_1.width, compare_007_1.height = 140.0, 100.0
    compare_008_1.width, compare_008_1.height = 140.0, 100.0
    switch_016.width, switch_016.height = 140.0, 100.0
    compare_009.width, compare_009.height = 140.0, 100.0
    switch_017.width, switch_017.height = 140.0, 100.0
    switch_018.width, switch_018.height = 140.0, 100.0
    group_input_033.width, group_input_033.height = 140.0, 100.0
    named_attribute_1.width, named_attribute_1.height = 140.0, 100.0
    group_002.width, group_002.height = 140.0, 100.0
    switch_019.width, switch_019.height = 140.0, 100.0
    group_input_056.width, group_input_056.height = 140.0, 100.0
    switch_007_1.width, switch_007_1.height = 140.0, 100.0
    curve_to_mesh_006.width, curve_to_mesh_006.height = 140.0, 100.0
    store_named_attribute_002_1.width, store_named_attribute_002_1.height = 140.0, 100.0
    realize_instances_005.width, realize_instances_005.height = 140.0, 100.0
    delete_geometry_004_1.width, delete_geometry_004_1.height = 140.0, 100.0
    compare_011.width, compare_011.height = 140.0, 100.0
    edge_neighbors.width, edge_neighbors.height = 140.0, 100.0
    group_input_057.width, group_input_057.height = 140.0, 100.0
    switch_020.width, switch_020.height = 140.0, 100.0
    compare_012.width, compare_012.height = 140.0, 100.0
    compare_013.width, compare_013.height = 140.0, 100.0
    switch_021.width, switch_021.height = 140.0, 100.0
    blur_attribute.width, blur_attribute.height = 140.0, 100.0
    position_001.width, position_001.height = 140.0, 100.0
    set_position_002.width, set_position_002.height = 140.0, 100.0
    group_input_058.width, group_input_058.height = 140.0, 100.0
    compare_014.width, compare_014.height = 140.0, 100.0
    switch_022.width, switch_022.height = 140.0, 100.0
    group_input_059.width, group_input_059.height = 140.0, 100.0
    switch_023.width, switch_023.height = 140.0, 100.0
    join_geometry_003.width, join_geometry_003.height = 140.0, 100.0
    bake_1.width, bake_1.height = 140.0, 100.0
    store_named_attribute_003.width, store_named_attribute_003.height = 140.0, 100.0
    group_003.width, group_003.height = 140.0, 100.0
    group_input_039.width, group_input_039.height = 140.0, 100.0
    group_input_041.width, group_input_041.height = 140.0, 100.0
    named_attribute_003.width, named_attribute_003.height = 140.0, 100.0
    store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
    mesh_island_1.width, mesh_island_1.height = 140.0, 100.0
    named_attribute_004.width, named_attribute_004.height = 140.0, 100.0
    reroute_3.width, reroute_3.height = 16.0, 100.0
    reroute_001_3.width, reroute_001_3.height = 16.0, 100.0
    reroute_002_3.width, reroute_002_3.height = 16.0, 100.0
    reroute_003_3.width, reroute_003_3.height = 16.0, 100.0
    reroute_004_3.width, reroute_004_3.height = 16.0, 100.0
    reroute_005_3.width, reroute_005_3.height = 16.0, 100.0
    reroute_006_3.width, reroute_006_3.height = 16.0, 100.0
    reroute_007_2.width, reroute_007_2.height = 16.0, 100.0
    reroute_008_2.width, reroute_008_2.height = 16.0, 100.0
    reroute_009_2.width, reroute_009_2.height = 16.0, 100.0
    reroute_010_2.width, reroute_010_2.height = 16.0, 100.0
    reroute_011_1.width, reroute_011_1.height = 16.0, 100.0
    reroute_012.width, reroute_012.height = 16.0, 100.0
    reroute_013.width, reroute_013.height = 16.0, 100.0
    reroute_014.width, reroute_014.height = 16.0, 100.0
    reroute_015.width, reroute_015.height = 16.0, 100.0
    reroute_016.width, reroute_016.height = 16.0, 100.0
    reroute_017.width, reroute_017.height = 16.0, 100.0
    reroute_018.width, reroute_018.height = 16.0, 100.0
    reroute_019.width, reroute_019.height = 16.0, 100.0
    reroute_020.width, reroute_020.height = 16.0, 100.0
    reroute_021.width, reroute_021.height = 16.0, 100.0
    reroute_022.width, reroute_022.height = 16.0, 100.0
    reroute_023.width, reroute_023.height = 16.0, 100.0
    reroute_024.width, reroute_024.height = 16.0, 100.0
    reroute_025.width, reroute_025.height = 16.0, 100.0
    reroute_026.width, reroute_026.height = 16.0, 100.0
    reroute_027.width, reroute_027.height = 16.0, 100.0
    reroute_028.width, reroute_028.height = 16.0, 100.0
    reroute_029.width, reroute_029.height = 16.0, 100.0
    reroute_030.width, reroute_030.height = 16.0, 100.0
    reroute_031.width, reroute_031.height = 16.0, 100.0
    reroute_032.width, reroute_032.height = 16.0, 100.0
    reroute_033.width, reroute_033.height = 16.0, 100.0
    reroute_034.width, reroute_034.height = 16.0, 100.0
    reroute_035.width, reroute_035.height = 16.0, 100.0
    reroute_036.width, reroute_036.height = 16.0, 100.0
    reroute_037.width, reroute_037.height = 16.0, 100.0
    reroute_038.width, reroute_038.height = 16.0, 100.0
    reroute_039.width, reroute_039.height = 16.0, 100.0
    reroute_040.width, reroute_040.height = 16.0, 100.0
    reroute_041.width, reroute_041.height = 16.0, 100.0
    reroute_042.width, reroute_042.height = 16.0, 100.0
    reroute_043.width, reroute_043.height = 16.0, 100.0
    reroute_044.width, reroute_044.height = 16.0, 100.0
    reroute_045.width, reroute_045.height = 16.0, 100.0
    reroute_046.width, reroute_046.height = 16.0, 100.0
    reroute_047.width, reroute_047.height = 16.0, 100.0
    reroute_048.width, reroute_048.height = 16.0, 100.0
    reroute_049.width, reroute_049.height = 16.0, 100.0
    reroute_050.width, reroute_050.height = 16.0, 100.0
    reroute_051.width, reroute_051.height = 16.0, 100.0
    reroute_052.width, reroute_052.height = 16.0, 100.0
    reroute_053.width, reroute_053.height = 16.0, 100.0
    reroute_054.width, reroute_054.height = 16.0, 100.0
    reroute_055.width, reroute_055.height = 16.0, 100.0
    reroute_056.width, reroute_056.height = 16.0, 100.0
    reroute_057.width, reroute_057.height = 16.0, 100.0
    reroute_058.width, reroute_058.height = 16.0, 100.0
    reroute_059.width, reroute_059.height = 16.0, 100.0
    reroute_060.width, reroute_060.height = 16.0, 100.0
    reroute_061.width, reroute_061.height = 16.0, 100.0
    reroute_062.width, reroute_062.height = 16.0, 100.0
    reroute_063.width, reroute_063.height = 16.0, 100.0
    reroute_064.width, reroute_064.height = 16.0, 100.0
    reroute_065.width, reroute_065.height = 16.0, 100.0
    reroute_066.width, reroute_066.height = 16.0, 100.0

    # initialize pattern_generator links
    # vector_math.Value -> compare_1.A
    pattern_generator.links.new(vector_math.outputs[1], compare_1.inputs[0])
    # delete_geometry.Geometry -> join_geometry_1.Geometry
    pattern_generator.links.new(delete_geometry.outputs[0], join_geometry_1.inputs[0])
    # realize_instances_001.Geometry -> curve_to_mesh_002.Curve
    pattern_generator.links.new(
        realize_instances_001.outputs[0], curve_to_mesh_002.inputs[0]
    )
    # map_range_1.Result -> instance_on_points.Scale
    pattern_generator.links.new(map_range_1.outputs[0], instance_on_points.inputs[6])
    # random_value_001_1.Value -> math_004_1.Value
    pattern_generator.links.new(random_value_001_1.outputs[2], math_004_1.inputs[1])
    # position_1.Position -> vector_math.Vector
    pattern_generator.links.new(position_1.outputs[0], vector_math.inputs[0])
    # math_2.Value -> map_range_1.From Max
    pattern_generator.links.new(math_2.outputs[0], map_range_1.inputs[2])
    # math_004_1.Value -> combine_xyz.Z
    pattern_generator.links.new(math_004_1.outputs[0], combine_xyz.inputs[2])
    # math_003_1.Value -> compare_1.B
    pattern_generator.links.new(math_003_1.outputs[0], compare_1.inputs[1])
    # realize_instances.Geometry -> curve_to_mesh.Curve
    pattern_generator.links.new(realize_instances.outputs[0], curve_to_mesh.inputs[0])
    # transform_geometry.Geometry -> realize_instances.Geometry
    pattern_generator.links.new(
        transform_geometry.outputs[0], realize_instances.inputs[0]
    )
    # arc.Curve -> instance_on_points.Instance
    pattern_generator.links.new(arc.outputs[0], instance_on_points.inputs[2])
    # curve_to_mesh.Mesh -> delete_geometry.Geometry
    pattern_generator.links.new(curve_to_mesh.outputs[0], delete_geometry.inputs[0])
    # math_001_1.Value -> grid.Vertices X
    pattern_generator.links.new(math_001_1.outputs[0], grid.inputs[2])
    # math_002_1.Value -> map_range_1.To Min
    pattern_generator.links.new(math_002_1.outputs[0], map_range_1.inputs[3])
    # resample_curve.Curve -> transform_geometry.Geometry
    pattern_generator.links.new(resample_curve.outputs[0], transform_geometry.inputs[0])
    # resample_curve_001.Curve -> realize_instances_001.Geometry
    pattern_generator.links.new(
        resample_curve_001.outputs[0], realize_instances_001.inputs[0]
    )
    # join_geometry_1.Geometry -> instance_on_points_001.Instance
    pattern_generator.links.new(
        join_geometry_1.outputs[0], instance_on_points_001.inputs[2]
    )
    # points.Points -> instance_on_points.Points
    pattern_generator.links.new(points.outputs[0], instance_on_points.inputs[0])
    # grid.Mesh -> transform_geometry_001.Geometry
    pattern_generator.links.new(grid.outputs[0], transform_geometry_001.inputs[0])
    # instance_on_points.Instances -> resample_curve.Curve
    pattern_generator.links.new(instance_on_points.outputs[0], resample_curve.inputs[0])
    # group_input_004_1.Grain -> math_003_1.Value
    pattern_generator.links.new(group_input_004_1.outputs[5], math_003_1.inputs[1])
    # group_input_007_1.Offset -> math_002_1.Value
    pattern_generator.links.new(group_input_007_1.outputs[3], math_002_1.inputs[1])
    # group_input_009_1.Seed -> random_value_001_1.Seed
    pattern_generator.links.new(
        group_input_009_1.outputs[4], random_value_001_1.inputs[8]
    )
    # group_input_010_1.Resolution of Tubes -> curve_circle.Resolution
    pattern_generator.links.new(group_input_010_1.outputs[8], curve_circle.inputs[0])
    # group_input_010_1.Radius of Tubes -> curve_circle.Radius
    pattern_generator.links.new(group_input_010_1.outputs[11], curve_circle.inputs[4])
    # group_input_011_1.2nd Curve Segements -> resample_curve.Count
    pattern_generator.links.new(group_input_011_1.outputs[10], resample_curve.inputs[2])
    # group_input_012_1.1st Curve Segments -> resample_curve_001.Count
    pattern_generator.links.new(
        group_input_012_1.outputs[9], resample_curve_001.inputs[2]
    )
    # group_input_008_1.Offset -> map_range_1.To Max
    pattern_generator.links.new(group_input_008_1.outputs[3], map_range_1.inputs[4])
    # curve_circle.Curve -> curve_to_mesh_001.Profile Curve
    pattern_generator.links.new(curve_circle.outputs[0], curve_to_mesh_001.inputs[1])
    # compare_1.Result -> delete_geometry.Selection
    pattern_generator.links.new(compare_1.outputs[0], delete_geometry.inputs[1])
    # group_input_016_1.Trim - Portion -> random_value_1.Probability
    pattern_generator.links.new(group_input_016_1.outputs[16], random_value_1.inputs[6])
    # group_input_016_1.Seed - Triming -> random_value_1.Seed
    pattern_generator.links.new(group_input_016_1.outputs[15], random_value_1.inputs[8])
    # random_value_1.Value -> random_value_002_1.Probability
    pattern_generator.links.new(random_value_1.outputs[3], random_value_002_1.inputs[6])
    # group_input_018_1.Random Portion -> switch_2.Switch
    pattern_generator.links.new(group_input_018_1.outputs[12], switch_2.inputs[0])
    # group_input_019_1.From Start -> compare_001_2.A
    pattern_generator.links.new(group_input_019_1.outputs[17], compare_001_2.inputs[0])
    # compare_001_2.Result -> boolean_math_1.Boolean
    pattern_generator.links.new(compare_001_2.outputs[0], boolean_math_1.inputs[0])
    # compare_002_2.Result -> boolean_math_1.Boolean
    pattern_generator.links.new(compare_002_2.outputs[0], boolean_math_1.inputs[1])
    # spline_length.Length -> compare_003_1.A
    pattern_generator.links.new(spline_length.outputs[0], compare_003_1.inputs[0])
    # random_value_002_1.Value -> math_006_1.Value
    pattern_generator.links.new(random_value_002_1.outputs[1], math_006_1.inputs[1])
    # random_value_003_1.Value -> random_value_002_1.Seed
    pattern_generator.links.new(
        random_value_003_1.outputs[2], random_value_002_1.inputs[8]
    )
    # store_named_attribute_001.Geometry -> set_material.Geometry
    pattern_generator.links.new(
        store_named_attribute_001.outputs[0], set_material.inputs[0]
    )
    # trim_curve_001.Curve -> instance_on_points_002.Points
    pattern_generator.links.new(
        trim_curve_001.outputs[0], instance_on_points_002.inputs[0]
    )
    # endpoint_selection.Selection -> instance_on_points_002.Selection
    pattern_generator.links.new(
        endpoint_selection.outputs[0], instance_on_points_002.inputs[1]
    )
    # random_value_004_1.Value -> trim_curve_001.Start
    pattern_generator.links.new(random_value_004_1.outputs[1], trim_curve_001.inputs[2])
    # math_007_1.Value -> combine_xyz_001.Z
    pattern_generator.links.new(math_007_1.outputs[0], combine_xyz_001.inputs[2])
    # group_input_001_1.Distance -> math_007_1.Value
    pattern_generator.links.new(group_input_001_1.outputs[51], math_007_1.inputs[0])
    # combine_xyz_001.Vector -> curve_line.End
    pattern_generator.links.new(combine_xyz_001.outputs[0], curve_line.inputs[1])
    # curve_circle_001.Curve -> curve_to_mesh_003.Profile Curve
    pattern_generator.links.new(
        curve_circle_001.outputs[0], curve_to_mesh_003.inputs[1]
    )
    # math_009_1.Value -> math_008_1.Value
    pattern_generator.links.new(math_009_1.outputs[0], math_008_1.inputs[1])
    # math_008_1.Value -> curve_circle_001.Radius
    pattern_generator.links.new(math_008_1.outputs[0], curve_circle_001.inputs[4])
    # group_input_003_1.Radius (Comparing) -> math_009_1.Value
    pattern_generator.links.new(group_input_003_1.outputs[52], math_009_1.inputs[0])
    # curve_line.Curve -> instance_on_points_002.Instance
    pattern_generator.links.new(curve_line.outputs[0], instance_on_points_002.inputs[2])
    # instance_on_points_002.Instances -> curve_to_mesh_003.Curve
    pattern_generator.links.new(
        instance_on_points_002.outputs[0], curve_to_mesh_003.inputs[0]
    )
    # math_010.Value -> grid.Vertices Y
    pattern_generator.links.new(math_010.outputs[0], grid.inputs[3])
    # math_013.Value -> grid_001.Size Y
    pattern_generator.links.new(math_013.outputs[0], grid_001.inputs[1])
    # grid_001.Mesh -> set_position.Geometry
    pattern_generator.links.new(grid_001.outputs[0], set_position.inputs[0])
    # math_011.Value -> combine_xyz_002.Z
    pattern_generator.links.new(math_011.outputs[0], combine_xyz_002.inputs[2])
    # group_input_021_1.Distance -> math_011.Value
    pattern_generator.links.new(group_input_021_1.outputs[51], math_011.inputs[0])
    # combine_xyz_002.Vector -> set_position.Offset
    pattern_generator.links.new(combine_xyz_002.outputs[0], set_position.inputs[3])
    # group_input_020_1.Size X -> math_012.Value
    pattern_generator.links.new(group_input_020_1.outputs[1], math_012.inputs[0])
    # math_012.Value -> grid_001.Size X
    pattern_generator.links.new(math_012.outputs[0], grid_001.inputs[0])
    # group_input_020_1.Size Y -> math_013.Value
    pattern_generator.links.new(group_input_020_1.outputs[2], math_013.inputs[0])
    # curve_to_mesh_003.Mesh -> join_geometry_002.Geometry
    pattern_generator.links.new(
        curve_to_mesh_003.outputs[0], join_geometry_002.inputs[0]
    )
    # group_input_022_1.Prop -> switch_002_1.Switch
    pattern_generator.links.new(group_input_022_1.outputs[48], switch_002_1.inputs[0])
    # join_geometry_001.Geometry -> switch_002_1.True
    pattern_generator.links.new(join_geometry_001.outputs[0], switch_002_1.inputs[2])
    # group_input_3.Size X -> math_001_1.Value
    pattern_generator.links.new(group_input_3.outputs[1], math_001_1.inputs[0])
    # group_input_3.Size Y -> math_010.Value
    pattern_generator.links.new(group_input_3.outputs[2], math_010.inputs[0])
    # group_input_023_1.Have Back Plate -> switch_003_1.Switch
    pattern_generator.links.new(group_input_023_1.outputs[53], switch_003_1.inputs[0])
    # join_geometry_002.Geometry -> switch_003_1.True
    pattern_generator.links.new(join_geometry_002.outputs[0], switch_003_1.inputs[2])
    # set_material_001.Geometry -> switch_003_1.False
    pattern_generator.links.new(set_material_001.outputs[0], switch_003_1.inputs[1])
    # switch_003_1.Output -> join_geometry_001.Geometry
    pattern_generator.links.new(switch_003_1.outputs[0], join_geometry_001.inputs[0])
    # group_input_024_1.Material (Curves) -> set_material.Material
    pattern_generator.links.new(group_input_024_1.outputs[30], set_material.inputs[2])
    # curve_to_mesh_003.Mesh -> set_material_001.Geometry
    pattern_generator.links.new(
        curve_to_mesh_003.outputs[0], set_material_001.inputs[0]
    )
    # group_input_025_1.Material (Hangers) -> set_material_001.Material
    pattern_generator.links.new(
        group_input_025_1.outputs[50], set_material_001.inputs[2]
    )
    # set_position.Geometry -> set_material_002.Geometry
    pattern_generator.links.new(set_position.outputs[0], set_material_002.inputs[0])
    # group_input_026_1.Material (Back Plate) -> set_material_002.Material
    pattern_generator.links.new(
        group_input_026_1.outputs[54], set_material_002.inputs[2]
    )
    # group_input_013_1.Seed -> random_value_004_1.Seed
    pattern_generator.links.new(
        group_input_013_1.outputs[49], random_value_004_1.inputs[8]
    )
    # math_005_1.Value -> combine_xyz_003.Z
    pattern_generator.links.new(math_005_1.outputs[0], combine_xyz_003.inputs[2])
    # group_input_014_1.Rotation -> math_005_1.Value
    pattern_generator.links.new(group_input_014_1.outputs[7], math_005_1.inputs[1])
    # group_input_015_1.Rotation Random -> switch_004.Switch
    pattern_generator.links.new(group_input_015_1.outputs[6], switch_004.inputs[0])
    # combine_xyz.Vector -> switch_004.True
    pattern_generator.links.new(combine_xyz.outputs[0], switch_004.inputs[2])
    # group_input_005_1.Count -> math_2.Value
    pattern_generator.links.new(group_input_005_1.outputs[0], math_2.inputs[0])
    # group_input_006_1.Resolution of Tubes -> arc.Resolution
    pattern_generator.links.new(group_input_006_1.outputs[8], arc.inputs[0])
    # random_value_006_1.Value -> math_015.Value
    pattern_generator.links.new(random_value_006_1.outputs[2], math_015.inputs[1])
    # math_016.Value -> math_017.Value
    pattern_generator.links.new(math_016.outputs[0], math_017.inputs[0])
    # random_value_005_1.Value -> math_017.Value
    pattern_generator.links.new(random_value_005_1.outputs[1], math_017.inputs[1])
    # math_017.Value -> math_018.Value
    pattern_generator.links.new(math_017.outputs[0], math_018.inputs[1])
    # group_input_016_1.Seed - Triming -> random_value_006_1.Seed
    pattern_generator.links.new(
        group_input_016_1.outputs[15], random_value_006_1.inputs[8]
    )
    # group_input_017_1.From End -> math_016.Value
    pattern_generator.links.new(group_input_017_1.outputs[18], math_016.inputs[1])
    # switch_005.Output -> trim_curve.End
    pattern_generator.links.new(switch_005.outputs[0], trim_curve.inputs[3])
    # group_input_027_1.Random Portion -> switch_005.Switch
    pattern_generator.links.new(group_input_027_1.outputs[12], switch_005.inputs[0])
    # merge_by_distance_001.Geometry -> switch_006_1.False
    pattern_generator.links.new(
        merge_by_distance_001.outputs[0], switch_006_1.inputs[1]
    )
    # group_input_029_1.Every Section -> switch_006_1.Switch
    pattern_generator.links.new(group_input_029_1.outputs[14], switch_006_1.inputs[0])
    # realize_instances_002.Geometry -> merge_by_distance_001.Geometry
    pattern_generator.links.new(
        realize_instances_002.outputs[0], merge_by_distance_001.inputs[0]
    )
    # delete_geometry_001.Geometry -> curve_to_mesh_004.Curve
    pattern_generator.links.new(
        delete_geometry_001.outputs[0], curve_to_mesh_004.inputs[0]
    )
    # merge_by_distance_003.Geometry -> switch_006_1.True
    pattern_generator.links.new(
        merge_by_distance_003.outputs[0], switch_006_1.inputs[2]
    )
    # switch_001_1.Output -> delete_geometry_001.Geometry
    pattern_generator.links.new(switch_001_1.outputs[0], delete_geometry_001.inputs[0])
    # delete_geometry_006.Geometry -> trim_curve.Curve
    pattern_generator.links.new(delete_geometry_006.outputs[0], trim_curve.inputs[0])
    # group_input_034.Every Section -> switch_009_1.Switch
    pattern_generator.links.new(group_input_034.outputs[14], switch_009_1.inputs[0])
    # geometry_to_instance.Instances -> switch_009_1.True
    pattern_generator.links.new(geometry_to_instance.outputs[0], switch_009_1.inputs[2])
    # curve_to_mesh_001.Mesh -> store_named_attribute_001.Geometry
    pattern_generator.links.new(
        curve_to_mesh_001.outputs[0], store_named_attribute_001.inputs[0]
    )
    # group_input_038.Emission Stenght -> store_named_attribute_001.Value
    pattern_generator.links.new(
        group_input_038.outputs[31], store_named_attribute_001.inputs[3]
    )
    # curve_to_mesh_005.Mesh -> realize_instances_008.Geometry
    pattern_generator.links.new(
        curve_to_mesh_005.outputs[0], realize_instances_008.inputs[0]
    )
    # realize_instances_008.Geometry -> attribute_statistic_003.Geometry
    pattern_generator.links.new(
        realize_instances_008.outputs[0], attribute_statistic_003.inputs[0]
    )
    # position_003.Position -> separate_xyz_001.Vector
    pattern_generator.links.new(position_003.outputs[0], separate_xyz_001.inputs[0])
    # attribute_statistic_003.Range -> math_024.Value
    pattern_generator.links.new(attribute_statistic_003.outputs[5], math_024.inputs[0])
    # math_024.Value -> math_025.Value
    pattern_generator.links.new(math_024.outputs[0], math_025.inputs[0])
    # math_026.Value -> math_027.Value
    pattern_generator.links.new(math_026.outputs[0], math_027.inputs[0])
    # math_025.Value -> math_028.Value
    pattern_generator.links.new(math_025.outputs[0], math_028.inputs[0])
    # math_027.Value -> grid_002.Vertices Y
    pattern_generator.links.new(math_027.outputs[0], grid_002.inputs[3])
    # math_028.Value -> grid_002.Vertices X
    pattern_generator.links.new(math_028.outputs[0], grid_002.inputs[2])
    # group_input_045.Gap Between Characters -> math_029.Value
    pattern_generator.links.new(group_input_045.outputs[26], math_029.inputs[0])
    # math_029.Value -> string_to_curves_003.Character Spacing
    pattern_generator.links.new(math_029.outputs[0], string_to_curves_003.inputs[2])
    # group_input_044.String Size -> string_to_curves_003.Size
    pattern_generator.links.new(
        group_input_044.outputs[25], string_to_curves_003.inputs[1]
    )
    # position_006.Position -> separate_xyz_002.Vector
    pattern_generator.links.new(position_006.outputs[0], separate_xyz_002.inputs[0])
    # realize_instances_008.Geometry -> attribute_statistic_006.Geometry
    pattern_generator.links.new(
        realize_instances_008.outputs[0], attribute_statistic_006.inputs[0]
    )
    # math_030.Value -> math_026.Value
    pattern_generator.links.new(math_030.outputs[0], math_026.inputs[0])
    # attribute_statistic_006.Range -> math_030.Value
    pattern_generator.links.new(attribute_statistic_006.outputs[5], math_030.inputs[0])
    # separate_xyz_001.X -> attribute_statistic_003.Attribute
    pattern_generator.links.new(
        separate_xyz_001.outputs[0], attribute_statistic_003.inputs[2]
    )
    # rotate_instances.Instances -> scale_instances.Instances
    pattern_generator.links.new(rotate_instances.outputs[0], scale_instances.inputs[0])
    # group_input_037.Scale -> scale_instances.Scale
    pattern_generator.links.new(group_input_037.outputs[27], scale_instances.inputs[2])
    # scale_instances.Instances -> realize_instances_002.Geometry
    pattern_generator.links.new(
        scale_instances.outputs[0], realize_instances_002.inputs[0]
    )
    # separate_xyz_002.Y -> attribute_statistic_006.Attribute
    pattern_generator.links.new(
        separate_xyz_002.outputs[1], attribute_statistic_006.inputs[2]
    )
    # trim_curve.Curve -> join_geometry_005.Geometry
    pattern_generator.links.new(trim_curve.outputs[0], join_geometry_005.inputs[0])
    # named_attribute_002.Attribute -> boolean_math_001_1.Boolean
    pattern_generator.links.new(
        named_attribute_002.outputs[0], boolean_math_001_1.inputs[0]
    )
    # boolean_math_001_1.Boolean -> delete_geometry_005.Selection
    pattern_generator.links.new(
        boolean_math_001_1.outputs[0], delete_geometry_005.inputs[1]
    )
    # named_attribute_001.Attribute -> delete_geometry_006.Selection
    pattern_generator.links.new(
        named_attribute_001.outputs[0], delete_geometry_006.inputs[1]
    )
    # random_value_007_1.Value -> math_031.Value
    pattern_generator.links.new(random_value_007_1.outputs[1], math_031.inputs[1])
    # random_value_008_1.Value -> random_value_007_1.Seed
    pattern_generator.links.new(
        random_value_008_1.outputs[2], random_value_007_1.inputs[8]
    )
    # math_032.Value -> math_031.Value
    pattern_generator.links.new(math_032.outputs[0], math_031.inputs[0])
    # group_input_042.True Random Portion -> switch_010_1.Switch
    pattern_generator.links.new(group_input_042.outputs[13], switch_010_1.inputs[0])
    # switch_010_1.Output -> switch_005.True
    pattern_generator.links.new(switch_010_1.outputs[0], switch_005.inputs[2])
    # math_015.Value -> random_value_009_1.Seed
    pattern_generator.links.new(math_015.outputs[0], random_value_009_1.inputs[8])
    # random_value_009_1.Value -> math_033.Value
    pattern_generator.links.new(random_value_009_1.outputs[1], math_033.inputs[1])
    # math_033.Value -> math_034.Value
    pattern_generator.links.new(math_033.outputs[0], math_034.inputs[1])
    # math_034.Value -> math_035.Value
    pattern_generator.links.new(math_034.outputs[0], math_035.inputs[1])
    # math_035.Value -> math_036.Value
    pattern_generator.links.new(math_035.outputs[0], math_036.inputs[0])
    # group_input_043.True Random Portion -> switch_011_1.Switch
    pattern_generator.links.new(group_input_043.outputs[13], switch_011_1.inputs[0])
    # switch_011_1.Output -> switch_2.True
    pattern_generator.links.new(switch_011_1.outputs[0], switch_2.inputs[2])
    # math_036.Value -> switch_011_1.False
    pattern_generator.links.new(math_036.outputs[0], switch_011_1.inputs[1])
    # switch_2.Output -> trim_curve.Start
    pattern_generator.links.new(switch_2.outputs[0], trim_curve.inputs[2])
    # math_031.Value -> math_037.Value
    pattern_generator.links.new(math_031.outputs[0], math_037.inputs[1])
    # math_037.Value -> math_038.Value
    pattern_generator.links.new(math_037.outputs[0], math_038.inputs[0])
    # group_input_017_1.From End -> math_032.Value
    pattern_generator.links.new(group_input_017_1.outputs[18], math_032.inputs[1])
    # math_038.Value -> switch_010_1.True
    pattern_generator.links.new(math_038.outputs[0], switch_010_1.inputs[2])
    # group_input_017_1.From Start -> math_006_1.Value
    pattern_generator.links.new(group_input_017_1.outputs[17], math_006_1.inputs[0])
    # switch_002_1.Output -> group_output_001.Geometry
    pattern_generator.links.new(switch_002_1.outputs[0], group_output_001.inputs[0])
    # merge_by_distance_002.Geometry -> merge_by_distance.Geometry
    pattern_generator.links.new(
        merge_by_distance_002.outputs[0], merge_by_distance.inputs[0]
    )
    # group_input_050.Merge Distance -> merge_by_distance.Distance
    pattern_generator.links.new(
        group_input_050.outputs[21], merge_by_distance.inputs[2]
    )
    # group_input_051.Merge Probability -> random_value_010.Probability
    pattern_generator.links.new(group_input_051.outputs[19], random_value_010.inputs[6])
    # group_input_051.Merge Seed -> random_value_010.Seed
    pattern_generator.links.new(group_input_051.outputs[20], random_value_010.inputs[8])
    # random_value_010.Value -> merge_by_distance.Selection
    pattern_generator.links.new(
        random_value_010.outputs[3], merge_by_distance.inputs[1]
    )
    # curve_to_mesh_004.Mesh -> merge_by_distance_002.Geometry
    pattern_generator.links.new(
        curve_to_mesh_004.outputs[0], merge_by_distance_002.inputs[0]
    )
    # join_geometry_005.Geometry -> switch_001_1.False
    pattern_generator.links.new(join_geometry_005.outputs[0], switch_001_1.inputs[1])
    # vector_math_005.Vector -> image_texture_1.Vector
    pattern_generator.links.new(vector_math_005.outputs[0], image_texture_1.inputs[1])
    # position_005.Position -> vector_math_002_1.Vector
    pattern_generator.links.new(position_005.outputs[0], vector_math_002_1.inputs[0])
    # image_info.Width -> math_039.Value
    pattern_generator.links.new(image_info.outputs[0], math_039.inputs[1])
    # vector_math_003_1.Vector -> vector_math_004.Vector
    pattern_generator.links.new(vector_math_003_1.outputs[0], vector_math_004.inputs[0])
    # vector_math_004.Vector -> vector_math_005.Vector
    pattern_generator.links.new(vector_math_004.outputs[0], vector_math_005.inputs[0])
    # math_039.Value -> math_043.Value
    pattern_generator.links.new(math_039.outputs[0], math_043.inputs[0])
    # math_040.Value -> math_044.Value
    pattern_generator.links.new(math_040.outputs[0], math_044.inputs[0])
    # math_043.Value -> combine_xyz_007.X
    pattern_generator.links.new(math_043.outputs[0], combine_xyz_007.inputs[0])
    # math_044.Value -> combine_xyz_007.Y
    pattern_generator.links.new(math_044.outputs[0], combine_xyz_007.inputs[1])
    # image_info.Height -> math_040.Value
    pattern_generator.links.new(image_info.outputs[1], math_040.inputs[1])
    # math_043.Value -> math_041.Value
    pattern_generator.links.new(math_043.outputs[0], math_041.inputs[0])
    # group_input_052.Size X -> math_041.Value
    pattern_generator.links.new(group_input_052.outputs[1], math_041.inputs[1])
    # math_041.Value -> math_042.Value
    pattern_generator.links.new(math_041.outputs[0], math_042.inputs[1])
    # math_042.Value -> vector_math_002_1.Scale
    pattern_generator.links.new(math_042.outputs[0], vector_math_002_1.inputs[3])
    # index_1.Index -> map_range_1.Value
    pattern_generator.links.new(index_1.outputs[0], map_range_1.inputs[0])
    # fill_curve_002.Mesh -> group_001.Cutout Instance
    pattern_generator.links.new(fill_curve_002.outputs[0], group_001.inputs[1])
    # vector_math_002_1.Vector -> vector_math_003_1.Vector
    pattern_generator.links.new(
        vector_math_002_1.outputs[0], vector_math_003_1.inputs[0]
    )
    # group_input_047.Scale -> vector_math_003_1.Scale
    pattern_generator.links.new(
        group_input_047.outputs[27], vector_math_003_1.inputs[3]
    )
    # compare_004_1.Result -> boolean_math_002.Boolean
    pattern_generator.links.new(compare_004_1.outputs[0], boolean_math_002.inputs[0])
    # boolean_math_002.Boolean -> delete_geometry_002.Selection
    pattern_generator.links.new(
        boolean_math_002.outputs[0], delete_geometry_002.inputs[1]
    )
    # subdivide_mesh.Mesh -> delete_geometry_002.Geometry
    pattern_generator.links.new(
        subdivide_mesh.outputs[0], delete_geometry_002.inputs[0]
    )
    # group_input_036.Every Section -> switch_012.Switch
    pattern_generator.links.new(group_input_036.outputs[14], switch_012.inputs[0])
    # geometry_to_instance_001.Instances -> switch_012.True
    pattern_generator.links.new(
        geometry_to_instance_001.outputs[0], switch_012.inputs[2]
    )
    # instance_on_points_001.Instances -> rotate_instances.Instances
    pattern_generator.links.new(
        instance_on_points_001.outputs[0], rotate_instances.inputs[0]
    )
    # position_002.Position -> attribute_statistic_001.Attribute
    pattern_generator.links.new(
        position_002.outputs[0], attribute_statistic_001.inputs[2]
    )
    # attribute_statistic_001.Mean -> vector_math_006.Vector
    pattern_generator.links.new(
        attribute_statistic_001.outputs[0], vector_math_006.inputs[0]
    )
    # vector_math_006.Vector -> vector_rotate.Vector
    pattern_generator.links.new(vector_math_006.outputs[0], vector_rotate.inputs[0])
    # vector_rotate.Vector -> set_position_001.Position
    pattern_generator.links.new(vector_rotate.outputs[0], set_position_001.inputs[2])
    # compare_003_1.Result -> delete_geometry_001.Selection
    pattern_generator.links.new(compare_003_1.outputs[0], delete_geometry_001.inputs[1])
    # set_position_001.Geometry -> group_001.OG Geometry
    pattern_generator.links.new(set_position_001.outputs[0], group_001.inputs[0])
    # set_position_001.Geometry -> group_005.OG Geometry
    pattern_generator.links.new(set_position_001.outputs[0], group_005.inputs[0])
    # switch_006_1.Output -> realize_instances_004.Geometry
    pattern_generator.links.new(
        switch_006_1.outputs[0], realize_instances_004.inputs[0]
    )
    # group_input_046.String -> string_to_curves_003.String
    pattern_generator.links.new(
        group_input_046.outputs[24], string_to_curves_003.inputs[0]
    )
    # realize_instances_004.Geometry -> attribute_statistic_001.Geometry
    pattern_generator.links.new(
        realize_instances_004.outputs[0], attribute_statistic_001.inputs[0]
    )
    # image_texture_1.Color -> compare_004_1.A
    pattern_generator.links.new(image_texture_1.outputs[0], compare_004_1.inputs[0])
    # group_input_048.Image -> image_texture_1.Image
    pattern_generator.links.new(group_input_048.outputs[28], image_texture_1.inputs[0])
    # group_input_054.Image -> image_info.Image
    pattern_generator.links.new(group_input_054.outputs[28], image_info.inputs[0])
    # compare_005_2.Result -> switch_013.Switch
    pattern_generator.links.new(compare_005_2.outputs[0], switch_013.inputs[0])
    # group_input_049.Mode -> compare_006_1.A
    pattern_generator.links.new(group_input_049.outputs[22], compare_006_1.inputs[8])
    # compare_006_1.Result -> switch_014.Switch
    pattern_generator.links.new(compare_006_1.outputs[0], switch_014.inputs[0])
    # switch_012.Output -> switch_014.True
    pattern_generator.links.new(switch_012.outputs[0], switch_014.inputs[2])
    # switch_014.Output -> switch_013.False
    pattern_generator.links.new(switch_014.outputs[0], switch_013.inputs[1])
    # compare_007_1.Result -> switch_015.Switch
    pattern_generator.links.new(compare_007_1.outputs[0], switch_015.inputs[0])
    # group_input_055.Mode -> compare_008_1.A
    pattern_generator.links.new(group_input_055.outputs[22], compare_008_1.inputs[8])
    # compare_008_1.Result -> switch_016.Switch
    pattern_generator.links.new(compare_008_1.outputs[0], switch_016.inputs[0])
    # switch_016.Output -> switch_015.False
    pattern_generator.links.new(switch_016.outputs[0], switch_015.inputs[1])
    # grid_002.Mesh -> switch_015.True
    pattern_generator.links.new(grid_002.outputs[0], switch_015.inputs[2])
    # group_input_035.Method -> compare_009.A
    pattern_generator.links.new(group_input_035.outputs[23], compare_009.inputs[8])
    # compare_009.Result -> switch_017.Switch
    pattern_generator.links.new(compare_009.outputs[0], switch_017.inputs[0])
    # group_005.Method 1 -> switch_017.True
    pattern_generator.links.new(group_005.outputs[0], switch_017.inputs[2])
    # group_005.Method 2 -> switch_017.False
    pattern_generator.links.new(group_005.outputs[1], switch_017.inputs[1])
    # group_001.Method 1 -> switch_018.True
    pattern_generator.links.new(group_001.outputs[0], switch_018.inputs[2])
    # group_001.Method 2 -> switch_018.False
    pattern_generator.links.new(group_001.outputs[1], switch_018.inputs[1])
    # switch_015.Output -> instance_on_points_001.Points
    pattern_generator.links.new(switch_015.outputs[0], instance_on_points_001.inputs[0])
    # switch_018.Output -> geometry_to_instance.Geometry
    pattern_generator.links.new(switch_018.outputs[0], geometry_to_instance.inputs[0])
    # switch_017.Output -> geometry_to_instance_001.Geometry
    pattern_generator.links.new(
        switch_017.outputs[0], geometry_to_instance_001.inputs[0]
    )
    # group_input_033.Subset -> group_001.Subset
    pattern_generator.links.new(group_input_033.outputs[55], group_001.inputs[2])
    # group_input_033.Subset -> group_005.Subset
    pattern_generator.links.new(group_input_033.outputs[55], group_005.inputs[2])
    # merge_by_distance.Geometry -> group_002.Geometry
    pattern_generator.links.new(merge_by_distance.outputs[0], group_002.inputs[0])
    # named_attribute_1.Attribute -> group_002.not_to_be_deleted
    pattern_generator.links.new(named_attribute_1.outputs[0], group_002.inputs[1])
    # group_input_056.Subset -> switch_019.Switch
    pattern_generator.links.new(group_input_056.outputs[55], switch_019.inputs[0])
    # group_002.Output -> switch_019.True
    pattern_generator.links.new(group_002.outputs[0], switch_019.inputs[2])
    # switch_019.Output -> mesh_to_curve_001.Mesh
    pattern_generator.links.new(switch_019.outputs[0], mesh_to_curve_001.inputs[0])
    # curve_to_mesh_006.Mesh -> store_named_attribute_002_1.Geometry
    pattern_generator.links.new(
        curve_to_mesh_006.outputs[0], store_named_attribute_002_1.inputs[0]
    )
    # store_named_attribute_002_1.Geometry -> realize_instances_005.Geometry
    pattern_generator.links.new(
        store_named_attribute_002_1.outputs[0], realize_instances_005.inputs[0]
    )
    # switch_013.Output -> switch_007_1.False
    pattern_generator.links.new(switch_013.outputs[0], switch_007_1.inputs[1])
    # delete_geometry_002.Geometry -> delete_geometry_004_1.Geometry
    pattern_generator.links.new(
        delete_geometry_002.outputs[0], delete_geometry_004_1.inputs[0]
    )
    # compare_011.Result -> delete_geometry_004_1.Selection
    pattern_generator.links.new(compare_011.outputs[0], delete_geometry_004_1.inputs[1])
    # edge_neighbors.Face Count -> compare_011.A
    pattern_generator.links.new(edge_neighbors.outputs[0], compare_011.inputs[2])
    # compare_012.Result -> switch_020.Switch
    pattern_generator.links.new(compare_012.outputs[0], switch_020.inputs[0])
    # group_input_057.Mode -> compare_013.A
    pattern_generator.links.new(group_input_057.outputs[22], compare_013.inputs[8])
    # compare_013.Result -> switch_021.Switch
    pattern_generator.links.new(compare_013.outputs[0], switch_021.inputs[0])
    # switch_021.Output -> switch_020.False
    pattern_generator.links.new(switch_021.outputs[0], switch_020.inputs[1])
    # set_position_002.Geometry -> switch_021.True
    pattern_generator.links.new(set_position_002.outputs[0], switch_021.inputs[2])
    # realize_instances_005.Geometry -> switch_020.True
    pattern_generator.links.new(realize_instances_005.outputs[0], switch_020.inputs[2])
    # position_001.Position -> blur_attribute.Value
    pattern_generator.links.new(position_001.outputs[0], blur_attribute.inputs[0])
    # delete_geometry_004_1.Geometry -> set_position_002.Geometry
    pattern_generator.links.new(
        delete_geometry_004_1.outputs[0], set_position_002.inputs[0]
    )
    # blur_attribute.Value -> set_position_002.Position
    pattern_generator.links.new(blur_attribute.outputs[0], set_position_002.inputs[2])
    # group_input_058.Image Smoothness (Subdivision) -> blur_attribute.Iterations
    pattern_generator.links.new(group_input_058.outputs[29], blur_attribute.inputs[1])
    # group_input_028_1.Image Smoothness (Subdivision) -> compare_014.A
    pattern_generator.links.new(group_input_028_1.outputs[29], compare_014.inputs[0])
    # group_input_028_1.Image Smoothness (Subdivision) -> compare_014.A
    pattern_generator.links.new(group_input_028_1.outputs[29], compare_014.inputs[2])
    # compare_014.Result -> switch_022.Switch
    pattern_generator.links.new(compare_014.outputs[0], switch_022.inputs[0])
    # switch_022.Output -> subdivide_mesh.Level
    pattern_generator.links.new(switch_022.outputs[0], subdivide_mesh.inputs[1])
    # group_input_059.Outside -> switch_007_1.Switch
    pattern_generator.links.new(group_input_059.outputs[56], switch_007_1.inputs[0])
    # switch_013.Output -> join_geometry_003.Geometry
    pattern_generator.links.new(switch_013.outputs[0], join_geometry_003.inputs[0])
    # join_geometry_003.Geometry -> switch_023.True
    pattern_generator.links.new(join_geometry_003.outputs[0], switch_023.inputs[2])
    # switch_007_1.Output -> switch_023.False
    pattern_generator.links.new(switch_007_1.outputs[0], switch_023.inputs[1])
    # bake_1.Geometry -> mesh_to_curve.Mesh
    pattern_generator.links.new(bake_1.outputs[0], mesh_to_curve.inputs[0])
    # delete_geometry_002.Geometry -> group_005.Cutout Instance
    pattern_generator.links.new(delete_geometry_002.outputs[0], group_005.inputs[1])
    # switch_023.Output -> bake_1.Geometry
    pattern_generator.links.new(switch_023.outputs[0], bake_1.inputs[0])
    # combine_xyz_003.Vector -> switch_004.False
    pattern_generator.links.new(combine_xyz_003.outputs[0], switch_004.inputs[1])
    # string_to_curves_003.Curve Instances -> curve_to_mesh_005.Curve
    pattern_generator.links.new(
        string_to_curves_003.outputs[0], curve_to_mesh_005.inputs[0]
    )
    # mesh_to_curve_001.Curve -> trim_curve_001.Curve
    pattern_generator.links.new(mesh_to_curve_001.outputs[0], trim_curve_001.inputs[0])
    # group_003.Color -> store_named_attribute_003.Value
    pattern_generator.links.new(
        group_003.outputs[0], store_named_attribute_003.inputs[3]
    )
    # group_input_041.Color Attribute -> store_named_attribute_003.Name
    pattern_generator.links.new(
        group_input_041.outputs[32], store_named_attribute_003.inputs[2]
    )
    # group_input_039.Wave Motion -> group_003.Wave Motion
    pattern_generator.links.new(group_input_039.outputs[36], group_003.inputs[4])
    # mesh_to_curve.Curve -> group_003.Geometry
    pattern_generator.links.new(mesh_to_curve.outputs[0], group_003.inputs[0])
    # store_named_attribute_003.Geometry -> delete_geometry_006.Geometry
    pattern_generator.links.new(
        store_named_attribute_003.outputs[0], delete_geometry_006.inputs[0]
    )
    # named_attribute_003.Attribute -> group_003.Spline ID
    pattern_generator.links.new(named_attribute_003.outputs[0], group_003.inputs[14])
    # mesh_island_1.Island Index -> store_named_attribute.Value
    pattern_generator.links.new(
        mesh_island_1.outputs[0], store_named_attribute.inputs[3]
    )
    # store_named_attribute.Geometry -> set_position_001.Geometry
    pattern_generator.links.new(
        store_named_attribute.outputs[0], set_position_001.inputs[0]
    )
    # group_input_039.Animate -> group_003.Animate
    pattern_generator.links.new(group_input_039.outputs[33], group_003.inputs[1])
    # group_input_039.Animation Type -> group_003.Animation Type
    pattern_generator.links.new(group_input_039.outputs[34], group_003.inputs[2])
    # group_input_039.Color -> group_003.Colors
    pattern_generator.links.new(group_input_039.outputs[35], group_003.inputs[3])
    # group_input_039.Seed - Colors -> group_003.Seed
    pattern_generator.links.new(group_input_039.outputs[37], group_003.inputs[5])
    # group_input_039.Speed -> group_003.Speed
    pattern_generator.links.new(group_input_039.outputs[38], group_003.inputs[6])
    # group_input_039.Color Distribution -> group_003.Color - Distribution
    pattern_generator.links.new(group_input_039.outputs[39], group_003.inputs[7])
    # group_input_039.Blackness -> group_003.Blackness
    pattern_generator.links.new(group_input_039.outputs[40], group_003.inputs[8])
    # group_input_039.Image -> group_003.Image
    pattern_generator.links.new(group_input_039.outputs[42], group_003.inputs[9])
    # group_input_039.Color 1 -> group_003.Color 1
    pattern_generator.links.new(group_input_039.outputs[44], group_003.inputs[10])
    # group_input_039.Color 2 -> group_003.Color 2
    pattern_generator.links.new(group_input_039.outputs[45], group_003.inputs[11])
    # group_input_039.Color 3 -> group_003.Color 3
    pattern_generator.links.new(group_input_039.outputs[46], group_003.inputs[12])
    # group_input_039.Color 4 -> group_003.Color 4
    pattern_generator.links.new(group_input_039.outputs[47], group_003.inputs[13])
    # group_input_3.Size X -> reroute_3.Input
    pattern_generator.links.new(group_input_3.outputs[1], reroute_3.inputs[0])
    # reroute_3.Output -> grid.Size X
    pattern_generator.links.new(reroute_3.outputs[0], grid.inputs[0])
    # group_input_3.Size Y -> reroute_001_3.Input
    pattern_generator.links.new(group_input_3.outputs[2], reroute_001_3.inputs[0])
    # reroute_001_3.Output -> grid.Size Y
    pattern_generator.links.new(reroute_001_3.outputs[0], grid.inputs[1])
    # group_input_005_1.Count -> reroute_002_3.Input
    pattern_generator.links.new(group_input_005_1.outputs[0], reroute_002_3.inputs[0])
    # reroute_002_3.Output -> points.Count
    pattern_generator.links.new(reroute_002_3.outputs[0], points.inputs[0])
    # group_input_007_1.Offset -> reroute_003_3.Input
    pattern_generator.links.new(group_input_007_1.outputs[3], reroute_003_3.inputs[0])
    # reroute_003_3.Output -> reroute_004_3.Input
    pattern_generator.links.new(reroute_003_3.outputs[0], reroute_004_3.inputs[0])
    # reroute_004_3.Output -> math_003_1.Value
    pattern_generator.links.new(reroute_004_3.outputs[0], math_003_1.inputs[0])
    # group_input_016_1.Seed - Triming -> reroute_005_3.Input
    pattern_generator.links.new(group_input_016_1.outputs[15], reroute_005_3.inputs[0])
    # reroute_005_3.Output -> reroute_006_3.Input
    pattern_generator.links.new(reroute_005_3.outputs[0], reroute_006_3.inputs[0])
    # reroute_006_3.Output -> math_015.Value
    pattern_generator.links.new(reroute_006_3.outputs[0], math_015.inputs[0])
    # reroute_006_3.Output -> random_value_003_1.Seed
    pattern_generator.links.new(reroute_006_3.outputs[0], random_value_003_1.inputs[8])
    # group_input_017_1.From Start -> reroute_007_2.Input
    pattern_generator.links.new(group_input_017_1.outputs[17], reroute_007_2.inputs[0])
    # reroute_007_2.Output -> reroute_008_2.Input
    pattern_generator.links.new(reroute_007_2.outputs[0], reroute_008_2.inputs[0])
    # reroute_008_2.Output -> math_034.Value
    pattern_generator.links.new(reroute_008_2.outputs[0], math_034.inputs[0])
    # group_input_017_1.From End -> reroute_009_2.Input
    pattern_generator.links.new(group_input_017_1.outputs[18], reroute_009_2.inputs[0])
    # reroute_009_2.Output -> reroute_010_2.Input
    pattern_generator.links.new(reroute_009_2.outputs[0], reroute_010_2.inputs[0])
    # reroute_010_2.Output -> math_018.Value
    pattern_generator.links.new(reroute_010_2.outputs[0], math_018.inputs[0])
    # reroute_010_2.Output -> math_037.Value
    pattern_generator.links.new(reroute_010_2.outputs[0], math_037.inputs[0])
    # group_input_003_1.Radius of Tubes -> reroute_011_1.Input
    pattern_generator.links.new(group_input_003_1.outputs[11], reroute_011_1.inputs[0])
    # reroute_011_1.Output -> math_008_1.Value
    pattern_generator.links.new(reroute_011_1.outputs[0], math_008_1.inputs[0])
    # group_input_049.Mode -> reroute_012.Input
    pattern_generator.links.new(group_input_049.outputs[22], reroute_012.inputs[0])
    # reroute_012.Output -> reroute_013.Input
    pattern_generator.links.new(reroute_012.outputs[0], reroute_013.inputs[0])
    # reroute_013.Output -> compare_005_2.A
    pattern_generator.links.new(reroute_013.outputs[0], compare_005_2.inputs[8])
    # group_input_028_1.Image Smoothness (Subdivision) -> reroute_014.Input
    pattern_generator.links.new(group_input_028_1.outputs[29], reroute_014.inputs[0])
    # reroute_014.Output -> reroute_015.Input
    pattern_generator.links.new(reroute_014.outputs[0], reroute_015.inputs[0])
    # reroute_015.Output -> switch_022.False
    pattern_generator.links.new(reroute_015.outputs[0], switch_022.inputs[1])
    # position_002.Position -> reroute_016.Input
    pattern_generator.links.new(position_002.outputs[0], reroute_016.inputs[0])
    # reroute_016.Output -> vector_math_006.Vector
    pattern_generator.links.new(reroute_016.outputs[0], vector_math_006.inputs[1])
    # group_input_055.Mode -> reroute_017.Input
    pattern_generator.links.new(group_input_055.outputs[22], reroute_017.inputs[0])
    # reroute_017.Output -> compare_007_1.A
    pattern_generator.links.new(reroute_017.outputs[0], compare_007_1.inputs[8])
    # group_input_057.Mode -> reroute_018.Input
    pattern_generator.links.new(group_input_057.outputs[22], reroute_018.inputs[0])
    # reroute_018.Output -> compare_012.A
    pattern_generator.links.new(reroute_018.outputs[0], compare_012.inputs[8])
    # group_input_059.Both Outside and Inside -> reroute_019.Input
    pattern_generator.links.new(group_input_059.outputs[57], reroute_019.inputs[0])
    # reroute_019.Output -> switch_023.Switch
    pattern_generator.links.new(reroute_019.outputs[0], switch_023.inputs[0])
    # random_value_1.Value -> reroute_020.Input
    pattern_generator.links.new(random_value_1.outputs[3], reroute_020.inputs[0])
    # reroute_020.Output -> reroute_021.Input
    pattern_generator.links.new(reroute_020.outputs[0], reroute_021.inputs[0])
    # reroute_021.Output -> trim_curve.Selection
    pattern_generator.links.new(reroute_021.outputs[0], trim_curve.inputs[1])
    # reroute_006_3.Output -> reroute_022.Input
    pattern_generator.links.new(reroute_006_3.outputs[0], reroute_022.inputs[0])
    # reroute_022.Output -> random_value_008_1.Seed
    pattern_generator.links.new(reroute_022.outputs[0], random_value_008_1.inputs[8])
    # reroute_008_2.Output -> reroute_023.Input
    pattern_generator.links.new(reroute_008_2.outputs[0], reroute_023.inputs[0])
    # reroute_023.Output -> reroute_024.Input
    pattern_generator.links.new(reroute_023.outputs[0], reroute_024.inputs[0])
    # reroute_024.Output -> reroute_025.Input
    pattern_generator.links.new(reroute_024.outputs[0], reroute_025.inputs[0])
    # reroute_025.Output -> math_036.Value
    pattern_generator.links.new(reroute_025.outputs[0], math_036.inputs[1])
    # string_to_curves_003.Curve Instances -> reroute_026.Input
    pattern_generator.links.new(string_to_curves_003.outputs[0], reroute_026.inputs[0])
    # reroute_026.Output -> reroute_027.Input
    pattern_generator.links.new(reroute_026.outputs[0], reroute_027.inputs[0])
    # reroute_027.Output -> fill_curve_002.Curve
    pattern_generator.links.new(reroute_027.outputs[0], fill_curve_002.inputs[0])
    # instance_on_points.Instances -> reroute_028.Input
    pattern_generator.links.new(instance_on_points.outputs[0], reroute_028.inputs[0])
    # reroute_028.Output -> resample_curve_001.Curve
    pattern_generator.links.new(reroute_028.outputs[0], resample_curve_001.inputs[0])
    # math_015.Value -> reroute_029.Input
    pattern_generator.links.new(math_015.outputs[0], reroute_029.inputs[0])
    # reroute_029.Output -> random_value_005_1.Seed
    pattern_generator.links.new(reroute_029.outputs[0], random_value_005_1.inputs[8])
    # reroute_010_2.Output -> reroute_030.Input
    pattern_generator.links.new(reroute_010_2.outputs[0], reroute_030.inputs[0])
    # reroute_030.Output -> reroute_031.Input
    pattern_generator.links.new(reroute_030.outputs[0], reroute_031.inputs[0])
    # reroute_031.Output -> reroute_032.Input
    pattern_generator.links.new(reroute_031.outputs[0], reroute_032.inputs[0])
    # reroute_032.Output -> compare_002_2.A
    pattern_generator.links.new(reroute_032.outputs[0], compare_002_2.inputs[0])
    # transform_geometry_001.Geometry -> reroute_033.Input
    pattern_generator.links.new(
        transform_geometry_001.outputs[0], reroute_033.inputs[0]
    )
    # reroute_033.Output -> reroute_034.Input
    pattern_generator.links.new(reroute_033.outputs[0], reroute_034.inputs[0])
    # reroute_034.Output -> subdivide_mesh.Mesh
    pattern_generator.links.new(reroute_034.outputs[0], subdivide_mesh.inputs[0])
    # transform_geometry_001.Geometry -> reroute_035.Input
    pattern_generator.links.new(
        transform_geometry_001.outputs[0], reroute_035.inputs[0]
    )
    # reroute_035.Output -> switch_016.True
    pattern_generator.links.new(reroute_035.outputs[0], switch_016.inputs[2])
    # transform_geometry_001.Geometry -> reroute_036.Input
    pattern_generator.links.new(
        transform_geometry_001.outputs[0], reroute_036.inputs[0]
    )
    # reroute_036.Output -> switch_016.False
    pattern_generator.links.new(reroute_036.outputs[0], switch_016.inputs[1])
    # switch_004.Output -> reroute_037.Input
    pattern_generator.links.new(switch_004.outputs[0], reroute_037.inputs[0])
    # reroute_037.Output -> rotate_instances.Rotation
    pattern_generator.links.new(reroute_037.outputs[0], rotate_instances.inputs[2])
    # random_value_009_1.Value -> reroute_038.Input
    pattern_generator.links.new(random_value_009_1.outputs[1], reroute_038.inputs[0])
    # reroute_038.Output -> math_035.Value
    pattern_generator.links.new(reroute_038.outputs[0], math_035.inputs[0])
    # combine_xyz_007.Vector -> reroute_039.Input
    pattern_generator.links.new(combine_xyz_007.outputs[0], reroute_039.inputs[0])
    # reroute_039.Output -> vector_math_004.Vector
    pattern_generator.links.new(reroute_039.outputs[0], vector_math_004.inputs[1])
    # math_006_1.Value -> reroute_040.Input
    pattern_generator.links.new(math_006_1.outputs[0], reroute_040.inputs[0])
    # reroute_040.Output -> switch_011_1.True
    pattern_generator.links.new(reroute_040.outputs[0], switch_011_1.inputs[2])
    # reroute_025.Output -> reroute_041.Input
    pattern_generator.links.new(reroute_025.outputs[0], reroute_041.inputs[0])
    # reroute_041.Output -> switch_2.False
    pattern_generator.links.new(reroute_041.outputs[0], switch_2.inputs[1])
    # math_018.Value -> reroute_042.Input
    pattern_generator.links.new(math_018.outputs[0], reroute_042.inputs[0])
    # reroute_042.Output -> switch_010_1.False
    pattern_generator.links.new(reroute_042.outputs[0], switch_010_1.inputs[1])
    # reroute_032.Output -> reroute_043.Input
    pattern_generator.links.new(reroute_032.outputs[0], reroute_043.inputs[0])
    # reroute_043.Output -> switch_005.False
    pattern_generator.links.new(reroute_043.outputs[0], switch_005.inputs[1])
    # math_026.Value -> reroute_044.Input
    pattern_generator.links.new(math_026.outputs[0], reroute_044.inputs[0])
    # reroute_044.Output -> reroute_045.Input
    pattern_generator.links.new(reroute_044.outputs[0], reroute_045.inputs[0])
    # reroute_045.Output -> grid_002.Size Y
    pattern_generator.links.new(reroute_045.outputs[0], grid_002.inputs[1])
    # math_025.Value -> reroute_046.Input
    pattern_generator.links.new(math_025.outputs[0], reroute_046.inputs[0])
    # reroute_046.Output -> grid_002.Size X
    pattern_generator.links.new(reroute_046.outputs[0], grid_002.inputs[0])
    # boolean_math_1.Boolean -> reroute_047.Input
    pattern_generator.links.new(boolean_math_1.outputs[0], reroute_047.inputs[0])
    # reroute_047.Output -> switch_001_1.Switch
    pattern_generator.links.new(reroute_047.outputs[0], switch_001_1.inputs[0])
    # scale_instances.Instances -> reroute_048.Input
    pattern_generator.links.new(scale_instances.outputs[0], reroute_048.inputs[0])
    # reroute_048.Output -> merge_by_distance_003.Geometry
    pattern_generator.links.new(reroute_048.outputs[0], merge_by_distance_003.inputs[0])
    # realize_instances_004.Geometry -> reroute_049.Input
    pattern_generator.links.new(realize_instances_004.outputs[0], reroute_049.inputs[0])
    # reroute_049.Output -> store_named_attribute.Geometry
    pattern_generator.links.new(reroute_049.outputs[0], store_named_attribute.inputs[0])
    # reroute_027.Output -> reroute_050.Input
    pattern_generator.links.new(reroute_027.outputs[0], reroute_050.inputs[0])
    # reroute_050.Output -> curve_to_mesh_006.Curve
    pattern_generator.links.new(reroute_050.outputs[0], curve_to_mesh_006.inputs[0])
    # set_position_001.Geometry -> reroute_051.Input
    pattern_generator.links.new(set_position_001.outputs[0], reroute_051.inputs[0])
    # reroute_051.Output -> reroute_052.Input
    pattern_generator.links.new(reroute_051.outputs[0], reroute_052.inputs[0])
    # reroute_052.Output -> switch_021.False
    pattern_generator.links.new(reroute_052.outputs[0], switch_021.inputs[1])
    # switch_017.Output -> reroute_053.Input
    pattern_generator.links.new(switch_017.outputs[0], reroute_053.inputs[0])
    # reroute_053.Output -> switch_012.False
    pattern_generator.links.new(reroute_053.outputs[0], switch_012.inputs[1])
    # switch_018.Output -> reroute_054.Input
    pattern_generator.links.new(switch_018.outputs[0], reroute_054.inputs[0])
    # reroute_054.Output -> reroute_055.Input
    pattern_generator.links.new(reroute_054.outputs[0], reroute_055.inputs[0])
    # reroute_055.Output -> switch_009_1.False
    pattern_generator.links.new(reroute_055.outputs[0], switch_009_1.inputs[1])
    # reroute_052.Output -> reroute_056.Input
    pattern_generator.links.new(reroute_052.outputs[0], reroute_056.inputs[0])
    # reroute_056.Output -> switch_014.False
    pattern_generator.links.new(reroute_056.outputs[0], switch_014.inputs[1])
    # switch_009_1.Output -> reroute_057.Input
    pattern_generator.links.new(switch_009_1.outputs[0], reroute_057.inputs[0])
    # reroute_057.Output -> switch_013.True
    pattern_generator.links.new(reroute_057.outputs[0], switch_013.inputs[2])
    # switch_020.Output -> reroute_058.Input
    pattern_generator.links.new(switch_020.outputs[0], reroute_058.inputs[0])
    # reroute_058.Output -> switch_007_1.True
    pattern_generator.links.new(reroute_058.outputs[0], switch_007_1.inputs[2])
    # mesh_to_curve.Curve -> reroute_059.Input
    pattern_generator.links.new(mesh_to_curve.outputs[0], reroute_059.inputs[0])
    # reroute_059.Output -> store_named_attribute_003.Geometry
    pattern_generator.links.new(
        reroute_059.outputs[0], store_named_attribute_003.inputs[0]
    )
    # store_named_attribute_003.Geometry -> reroute_060.Input
    pattern_generator.links.new(
        store_named_attribute_003.outputs[0], reroute_060.inputs[0]
    )
    # reroute_060.Output -> reroute_061.Input
    pattern_generator.links.new(reroute_060.outputs[0], reroute_061.inputs[0])
    # reroute_061.Output -> delete_geometry_005.Geometry
    pattern_generator.links.new(reroute_061.outputs[0], delete_geometry_005.inputs[0])
    # reroute_061.Output -> reroute_062.Input
    pattern_generator.links.new(reroute_061.outputs[0], reroute_062.inputs[0])
    # reroute_062.Output -> switch_001_1.True
    pattern_generator.links.new(reroute_062.outputs[0], switch_001_1.inputs[2])
    # merge_by_distance.Geometry -> reroute_063.Input
    pattern_generator.links.new(merge_by_distance.outputs[0], reroute_063.inputs[0])
    # reroute_063.Output -> switch_019.False
    pattern_generator.links.new(reroute_063.outputs[0], switch_019.inputs[1])
    # mesh_to_curve_001.Curve -> reroute_064.Input
    pattern_generator.links.new(mesh_to_curve_001.outputs[0], reroute_064.inputs[0])
    # reroute_064.Output -> reroute_065.Input
    pattern_generator.links.new(reroute_064.outputs[0], reroute_065.inputs[0])
    # reroute_065.Output -> curve_to_mesh_001.Curve
    pattern_generator.links.new(reroute_065.outputs[0], curve_to_mesh_001.inputs[0])
    # set_material.Geometry -> reroute_066.Input
    pattern_generator.links.new(set_material.outputs[0], reroute_066.inputs[0])
    # reroute_066.Output -> switch_002_1.False
    pattern_generator.links.new(reroute_066.outputs[0], switch_002_1.inputs[1])
    # curve_to_mesh_002.Mesh -> join_geometry_1.Geometry
    pattern_generator.links.new(curve_to_mesh_002.outputs[0], join_geometry_1.inputs[0])
    # set_material_002.Geometry -> join_geometry_002.Geometry
    pattern_generator.links.new(
        set_material_002.outputs[0], join_geometry_002.inputs[0]
    )
    # set_material.Geometry -> join_geometry_001.Geometry
    pattern_generator.links.new(set_material.outputs[0], join_geometry_001.inputs[0])
    # delete_geometry_005.Geometry -> join_geometry_005.Geometry
    pattern_generator.links.new(
        delete_geometry_005.outputs[0], join_geometry_005.inputs[0]
    )
    # compare_009.Result -> switch_018.Switch
    pattern_generator.links.new(compare_009.outputs[0], switch_018.inputs[0])
    # reroute_058.Output -> join_geometry_003.Geometry
    pattern_generator.links.new(reroute_058.outputs[0], join_geometry_003.inputs[0])
    color_distribution_socket.default_value = "Constant"
    return pattern_generator


# initialize colorpalette node group
def colorpalette_node_group():
    name = "ColorPalette"
    while True:
        if node_group_name_exists(name, "GEOMETRY"):
            name = "ColorPalette" + str(random.randint(0, 1000))
        else:
            colorpalette = bpy.data.node_groups.new(type="GeometryNodeTree", name=name)
            break
    colorpalette.color_tag = "NONE"
    colorpalette.description = ""

    # colorpalette interface
    # Socket Color
    color_socket = colorpalette.interface.new_socket(
        name="Color", in_out="OUTPUT", socket_type="NodeSocketColor"
    )
    color_socket.default_value = (
        0.800000011920929,
        0.800000011920929,
        0.800000011920929,
        1.0,
    )
    color_socket.attribute_domain = "POINT"

    # Socket Geometry
    geometry_socket_1 = colorpalette.interface.new_socket(
        name="Geometry", in_out="INPUT", socket_type="NodeSocketGeometry"
    )
    geometry_socket_1.attribute_domain = "POINT"

    # Socket Animate
    animate_socket = colorpalette.interface.new_socket(
        name="Animate", in_out="INPUT", socket_type="NodeSocketBool"
    )
    animate_socket.default_value = False
    animate_socket.attribute_domain = "POINT"

    # Socket Animation Type
    animation_type_socket = colorpalette.interface.new_socket(
        name="Animation Type", in_out="INPUT", socket_type="NodeSocketString"
    )
    animation_type_socket.default_value = ""
    animation_type_socket.attribute_domain = "POINT"

    # Socket Colors
    colors_socket = colorpalette.interface.new_socket(
        name="Colors", in_out="INPUT", socket_type="NodeSocketString"
    )
    colors_socket.default_value = ""
    colors_socket.attribute_domain = "POINT"

    # Socket Wave Motion
    wave_motion_socket = colorpalette.interface.new_socket(
        name="Wave Motion", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    wave_motion_socket.default_value = 0.5
    wave_motion_socket.min_value = 0.0
    wave_motion_socket.max_value = 1.0
    wave_motion_socket.subtype = "FACTOR"
    wave_motion_socket.attribute_domain = "POINT"

    # Socket Seed
    seed_socket = colorpalette.interface.new_socket(
        name="Seed", in_out="INPUT", socket_type="NodeSocketInt"
    )
    seed_socket.default_value = 0
    seed_socket.min_value = -2147483648
    seed_socket.max_value = 2147483647
    seed_socket.subtype = "NONE"
    seed_socket.attribute_domain = "POINT"

    # Socket Speed
    speed_socket = colorpalette.interface.new_socket(
        name="Speed", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    speed_socket.default_value = 1.0
    speed_socket.min_value = 0.0
    speed_socket.max_value = 3.4028234663852886e38
    speed_socket.subtype = "NONE"
    speed_socket.attribute_domain = "POINT"

    # Socket Color - Distribution
    color___distribution_socket = colorpalette.interface.new_socket(
        name="Color - Distribution", in_out="INPUT", socket_type="NodeSocketMenu"
    )
    color___distribution_socket.attribute_domain = "POINT"

    # Socket Blackness
    blackness_socket = colorpalette.interface.new_socket(
        name="Blackness", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    blackness_socket.default_value = 0.25
    blackness_socket.min_value = 0.0
    blackness_socket.max_value = 1.0
    blackness_socket.subtype = "FACTOR"
    blackness_socket.attribute_domain = "POINT"

    # Socket Image
    image_socket = colorpalette.interface.new_socket(
        name="Image", in_out="INPUT", socket_type="NodeSocketImage"
    )
    image_socket.attribute_domain = "POINT"

    # Socket Color 1
    color_1_socket = colorpalette.interface.new_socket(
        name="Color 1", in_out="INPUT", socket_type="NodeSocketColor"
    )
    color_1_socket.default_value = (0.0, 0.0, 0.0, 1.0)
    color_1_socket.attribute_domain = "POINT"

    # Socket Color 2
    color_2_socket = colorpalette.interface.new_socket(
        name="Color 2", in_out="INPUT", socket_type="NodeSocketColor"
    )
    color_2_socket.default_value = (0.0, 0.0, 0.0, 1.0)
    color_2_socket.attribute_domain = "POINT"

    # Socket Color 3
    color_3_socket = colorpalette.interface.new_socket(
        name="Color 3", in_out="INPUT", socket_type="NodeSocketColor"
    )
    color_3_socket.default_value = (0.0, 0.0, 0.0, 1.0)
    color_3_socket.attribute_domain = "POINT"

    # Socket Color 4
    color_4_socket = colorpalette.interface.new_socket(
        name="Color 4", in_out="INPUT", socket_type="NodeSocketColor"
    )
    color_4_socket.default_value = (0.0, 0.0, 0.0, 1.0)
    color_4_socket.attribute_domain = "POINT"

    # Socket Spline ID
    spline_id_socket = colorpalette.interface.new_socket(
        name="Spline ID", in_out="INPUT", socket_type="NodeSocketInt"
    )
    spline_id_socket.default_value = 0
    spline_id_socket.min_value = -2147483648
    spline_id_socket.max_value = 2147483647
    spline_id_socket.subtype = "NONE"
    spline_id_socket.attribute_domain = "POINT"

    # initialize colorpalette nodes
    # node Group Output
    group_output_2 = colorpalette.nodes.new("NodeGroupOutput")
    group_output_2.name = "Group Output"
    group_output_2.is_active_output = True
    group_output_2.inputs[1].hide = True

    # node Group Input
    group_input_2 = colorpalette.nodes.new("NodeGroupInput")
    group_input_2.name = "Group Input"
    group_input_2.outputs[0].hide = True
    group_input_2.outputs[1].hide = True
    group_input_2.outputs[2].hide = True
    group_input_2.outputs[3].hide = True
    group_input_2.outputs[4].hide = True
    group_input_2.outputs[6].hide = True
    group_input_2.outputs[7].hide = True
    group_input_2.outputs[8].hide = True
    group_input_2.outputs[9].hide = True
    group_input_2.outputs[10].hide = True
    group_input_2.outputs[11].hide = True
    group_input_2.outputs[12].hide = True
    group_input_2.outputs[13].hide = True
    group_input_2.outputs[14].hide = True
    group_input_2.outputs[15].hide = True

    # node Random Value
    random_value = colorpalette.nodes.new("FunctionNodeRandomValue")
    random_value.name = "Random Value"
    random_value.data_type = "FLOAT"
    # Min_001
    random_value.inputs[2].default_value = 0.0
    # Max_001
    random_value.inputs[3].default_value = 1.0

    # node Switch.001
    switch_001 = colorpalette.nodes.new("GeometryNodeSwitch")
    switch_001.name = "Switch.001"
    switch_001.input_type = "RGBA"

    # node Compare
    compare = colorpalette.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.data_type = "FLOAT"
    compare.mode = "ELEMENT"
    compare.operation = "LESS_THAN"
    compare.inputs[1].hide = True
    compare.inputs[2].hide = True
    compare.inputs[3].hide = True
    compare.inputs[4].hide = True
    compare.inputs[5].hide = True
    compare.inputs[6].hide = True
    compare.inputs[7].hide = True
    compare.inputs[8].hide = True
    compare.inputs[9].hide = True
    compare.inputs[10].hide = True
    compare.inputs[11].hide = True
    compare.inputs[12].hide = True
    # B
    compare.inputs[1].default_value = 0.25

    # node Random Value.001
    random_value_001 = colorpalette.nodes.new("FunctionNodeRandomValue")
    random_value_001.name = "Random Value.001"
    random_value_001.data_type = "FLOAT_VECTOR"
    random_value_001.inputs[0].hide = True
    random_value_001.inputs[1].hide = True
    random_value_001.inputs[2].hide = True
    random_value_001.inputs[3].hide = True
    random_value_001.inputs[4].hide = True
    random_value_001.inputs[5].hide = True
    random_value_001.inputs[6].hide = True
    random_value_001.outputs[1].hide = True
    random_value_001.outputs[2].hide = True
    random_value_001.outputs[3].hide = True
    # Min
    random_value_001.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Max
    random_value_001.inputs[1].default_value = (1.0, 1.0, 1.0)

    # node Compare.001
    compare_001_1 = colorpalette.nodes.new("FunctionNodeCompare")
    compare_001_1.name = "Compare.001"
    compare_001_1.data_type = "FLOAT"
    compare_001_1.mode = "ELEMENT"
    compare_001_1.operation = "GREATER_THAN"
    compare_001_1.inputs[1].hide = True
    compare_001_1.inputs[2].hide = True
    compare_001_1.inputs[3].hide = True
    compare_001_1.inputs[4].hide = True
    compare_001_1.inputs[5].hide = True
    compare_001_1.inputs[6].hide = True
    compare_001_1.inputs[7].hide = True
    compare_001_1.inputs[8].hide = True
    compare_001_1.inputs[9].hide = True
    compare_001_1.inputs[10].hide = True
    compare_001_1.inputs[11].hide = True
    compare_001_1.inputs[12].hide = True
    # B
    compare_001_1.inputs[1].default_value = 0.25

    # node Compare.002
    compare_002_1 = colorpalette.nodes.new("FunctionNodeCompare")
    compare_002_1.name = "Compare.002"
    compare_002_1.data_type = "FLOAT"
    compare_002_1.mode = "ELEMENT"
    compare_002_1.operation = "LESS_THAN"
    compare_002_1.inputs[1].hide = True
    compare_002_1.inputs[2].hide = True
    compare_002_1.inputs[3].hide = True
    compare_002_1.inputs[4].hide = True
    compare_002_1.inputs[5].hide = True
    compare_002_1.inputs[6].hide = True
    compare_002_1.inputs[7].hide = True
    compare_002_1.inputs[8].hide = True
    compare_002_1.inputs[9].hide = True
    compare_002_1.inputs[10].hide = True
    compare_002_1.inputs[11].hide = True
    compare_002_1.inputs[12].hide = True
    # B
    compare_002_1.inputs[1].default_value = 0.5

    # node Boolean Math
    boolean_math = colorpalette.nodes.new("FunctionNodeBooleanMath")
    boolean_math.name = "Boolean Math"
    boolean_math.operation = "AND"

    # node Switch.002
    switch_002 = colorpalette.nodes.new("GeometryNodeSwitch")
    switch_002.name = "Switch.002"
    switch_002.input_type = "RGBA"

    # node Random Value.002
    random_value_002 = colorpalette.nodes.new("FunctionNodeRandomValue")
    random_value_002.name = "Random Value.002"
    random_value_002.data_type = "FLOAT_VECTOR"
    random_value_002.inputs[0].hide = True
    random_value_002.inputs[1].hide = True
    random_value_002.inputs[2].hide = True
    random_value_002.inputs[3].hide = True
    random_value_002.inputs[4].hide = True
    random_value_002.inputs[5].hide = True
    random_value_002.inputs[6].hide = True
    random_value_002.outputs[1].hide = True
    random_value_002.outputs[2].hide = True
    random_value_002.outputs[3].hide = True
    # Min
    random_value_002.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Max
    random_value_002.inputs[1].default_value = (1.0, 1.0, 1.0)

    # node Compare.003
    compare_003 = colorpalette.nodes.new("FunctionNodeCompare")
    compare_003.name = "Compare.003"
    compare_003.data_type = "FLOAT"
    compare_003.mode = "ELEMENT"
    compare_003.operation = "GREATER_THAN"
    compare_003.inputs[1].hide = True
    compare_003.inputs[2].hide = True
    compare_003.inputs[3].hide = True
    compare_003.inputs[4].hide = True
    compare_003.inputs[5].hide = True
    compare_003.inputs[6].hide = True
    compare_003.inputs[7].hide = True
    compare_003.inputs[8].hide = True
    compare_003.inputs[9].hide = True
    compare_003.inputs[10].hide = True
    compare_003.inputs[11].hide = True
    compare_003.inputs[12].hide = True
    # B
    compare_003.inputs[1].default_value = 0.5

    # node Compare.004
    compare_004 = colorpalette.nodes.new("FunctionNodeCompare")
    compare_004.name = "Compare.004"
    compare_004.data_type = "FLOAT"
    compare_004.mode = "ELEMENT"
    compare_004.operation = "LESS_THAN"
    compare_004.inputs[1].hide = True
    compare_004.inputs[2].hide = True
    compare_004.inputs[3].hide = True
    compare_004.inputs[4].hide = True
    compare_004.inputs[5].hide = True
    compare_004.inputs[6].hide = True
    compare_004.inputs[7].hide = True
    compare_004.inputs[8].hide = True
    compare_004.inputs[9].hide = True
    compare_004.inputs[10].hide = True
    compare_004.inputs[11].hide = True
    compare_004.inputs[12].hide = True
    # B
    compare_004.inputs[1].default_value = 0.75

    # node Boolean Math.001
    boolean_math_001 = colorpalette.nodes.new("FunctionNodeBooleanMath")
    boolean_math_001.name = "Boolean Math.001"
    boolean_math_001.operation = "AND"

    # node Switch.003
    switch_003 = colorpalette.nodes.new("GeometryNodeSwitch")
    switch_003.name = "Switch.003"
    switch_003.input_type = "RGBA"

    # node Random Value.003
    random_value_003 = colorpalette.nodes.new("FunctionNodeRandomValue")
    random_value_003.name = "Random Value.003"
    random_value_003.data_type = "FLOAT_VECTOR"
    random_value_003.inputs[0].hide = True
    random_value_003.inputs[1].hide = True
    random_value_003.inputs[2].hide = True
    random_value_003.inputs[3].hide = True
    random_value_003.inputs[4].hide = True
    random_value_003.inputs[5].hide = True
    random_value_003.inputs[6].hide = True
    random_value_003.outputs[1].hide = True
    random_value_003.outputs[2].hide = True
    random_value_003.outputs[3].hide = True
    # Min
    random_value_003.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Max
    random_value_003.inputs[1].default_value = (1.0, 1.0, 1.0)

    # node Random Value.004
    random_value_004 = colorpalette.nodes.new("FunctionNodeRandomValue")
    random_value_004.name = "Random Value.004"
    random_value_004.data_type = "FLOAT_VECTOR"
    random_value_004.inputs[0].hide = True
    random_value_004.inputs[1].hide = True
    random_value_004.inputs[2].hide = True
    random_value_004.inputs[3].hide = True
    random_value_004.inputs[4].hide = True
    random_value_004.inputs[5].hide = True
    random_value_004.inputs[6].hide = True
    random_value_004.outputs[1].hide = True
    random_value_004.outputs[2].hide = True
    random_value_004.outputs[3].hide = True
    # Min
    random_value_004.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Max
    random_value_004.inputs[1].default_value = (1.0, 1.0, 1.0)

    # node Random Value.005
    random_value_005 = colorpalette.nodes.new("FunctionNodeRandomValue")
    random_value_005.name = "Random Value.005"
    random_value_005.data_type = "INT"
    random_value_005.inputs[0].hide = True
    random_value_005.inputs[1].hide = True
    random_value_005.inputs[2].hide = True
    random_value_005.inputs[3].hide = True
    random_value_005.inputs[4].hide = True
    random_value_005.inputs[5].hide = True
    random_value_005.inputs[6].hide = True
    random_value_005.inputs[8].hide = True
    random_value_005.outputs[0].hide = True
    random_value_005.outputs[1].hide = True
    random_value_005.outputs[3].hide = True
    # Min_002
    random_value_005.inputs[4].default_value = 0
    # Max_002
    random_value_005.inputs[5].default_value = 100
    # Seed
    random_value_005.inputs[8].default_value = 1

    # node Math
    math_1 = colorpalette.nodes.new("ShaderNodeMath")
    math_1.name = "Math"
    math_1.operation = "MULTIPLY"
    math_1.use_clamp = False
    math_1.inputs[2].hide = True

    # node Math.001
    math_001 = colorpalette.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = "MULTIPLY"
    math_001.use_clamp = False
    math_001.inputs[2].hide = True

    # node Random Value.006
    random_value_006 = colorpalette.nodes.new("FunctionNodeRandomValue")
    random_value_006.name = "Random Value.006"
    random_value_006.data_type = "INT"
    random_value_006.inputs[0].hide = True
    random_value_006.inputs[1].hide = True
    random_value_006.inputs[2].hide = True
    random_value_006.inputs[3].hide = True
    random_value_006.inputs[4].hide = True
    random_value_006.inputs[5].hide = True
    random_value_006.inputs[6].hide = True
    random_value_006.inputs[8].hide = True
    random_value_006.outputs[0].hide = True
    random_value_006.outputs[1].hide = True
    random_value_006.outputs[3].hide = True
    # Min_002
    random_value_006.inputs[4].default_value = 0
    # Max_002
    random_value_006.inputs[5].default_value = 100
    # Seed
    random_value_006.inputs[8].default_value = 2

    # node Math.002
    math_002 = colorpalette.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = "MULTIPLY"
    math_002.use_clamp = False
    math_002.inputs[2].hide = True

    # node Random Value.007
    random_value_007 = colorpalette.nodes.new("FunctionNodeRandomValue")
    random_value_007.name = "Random Value.007"
    random_value_007.data_type = "INT"
    random_value_007.inputs[0].hide = True
    random_value_007.inputs[1].hide = True
    random_value_007.inputs[2].hide = True
    random_value_007.inputs[3].hide = True
    random_value_007.inputs[4].hide = True
    random_value_007.inputs[5].hide = True
    random_value_007.inputs[6].hide = True
    random_value_007.inputs[8].hide = True
    random_value_007.outputs[0].hide = True
    random_value_007.outputs[1].hide = True
    random_value_007.outputs[3].hide = True
    # Min_002
    random_value_007.inputs[4].default_value = 0
    # Max_002
    random_value_007.inputs[5].default_value = 100
    # Seed
    random_value_007.inputs[8].default_value = 3

    # node Map Range
    map_range = colorpalette.nodes.new("ShaderNodeMapRange")
    map_range.name = "Map Range"
    map_range.clamp = True
    map_range.data_type = "FLOAT_VECTOR"
    map_range.interpolation_type = "LINEAR"
    map_range.inputs[1].hide = True
    map_range.inputs[2].hide = True
    map_range.inputs[3].hide = True
    map_range.inputs[4].hide = True
    map_range.inputs[5].hide = True
    map_range.inputs[7].hide = True
    map_range.inputs[8].hide = True
    map_range.inputs[9].hide = True
    map_range.inputs[10].hide = True
    map_range.inputs[11].hide = True
    map_range.outputs[0].hide = True
    # From_Min_FLOAT3
    map_range.inputs[7].default_value = (0.0, 0.0, 0.0)
    # From_Max_FLOAT3
    map_range.inputs[8].default_value = (1.0, 1.0, 1.0)
    # To_Min_FLOAT3
    map_range.inputs[9].default_value = (0.0, 0.0, 0.0)
    # To_Max_FLOAT3
    map_range.inputs[10].default_value = (1.0, 1.0, 1.0)

    # node Group Input.001
    group_input_001 = colorpalette.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.outputs[0].hide = True
    group_input_001.outputs[1].hide = True
    group_input_001.outputs[2].hide = True
    group_input_001.outputs[3].hide = True
    group_input_001.outputs[4].hide = True
    group_input_001.outputs[5].hide = True
    group_input_001.outputs[6].hide = True
    group_input_001.outputs[8].hide = True
    group_input_001.outputs[9].hide = True
    group_input_001.outputs[10].hide = True
    group_input_001.outputs[11].hide = True
    group_input_001.outputs[12].hide = True
    group_input_001.outputs[13].hide = True
    group_input_001.outputs[14].hide = True
    group_input_001.outputs[15].hide = True

    # node Menu Switch
    menu_switch = colorpalette.nodes.new("GeometryNodeMenuSwitch")
    menu_switch.name = "Menu Switch"
    menu_switch.active_index = 3
    menu_switch.data_type = "RGBA"
    menu_switch.enum_items.clear()
    menu_switch.enum_items.new("Constant")
    menu_switch.enum_items[0].description = ""
    menu_switch.enum_items.new("Linear")
    menu_switch.enum_items[1].description = ""
    menu_switch.enum_items.new("Ease")
    menu_switch.enum_items[2].description = ""
    menu_switch.enum_items.new("B-Spline")
    menu_switch.enum_items[3].description = ""
    menu_switch.inputs[5].hide = True

    # node Map Range.001
    map_range_001 = colorpalette.nodes.new("ShaderNodeMapRange")
    map_range_001.name = "Map Range.001"
    map_range_001.clamp = True
    map_range_001.data_type = "FLOAT_VECTOR"
    map_range_001.interpolation_type = "SMOOTHSTEP"
    map_range_001.inputs[1].hide = True
    map_range_001.inputs[2].hide = True
    map_range_001.inputs[3].hide = True
    map_range_001.inputs[4].hide = True
    map_range_001.inputs[5].hide = True
    map_range_001.inputs[7].hide = True
    map_range_001.inputs[8].hide = True
    map_range_001.inputs[9].hide = True
    map_range_001.inputs[10].hide = True
    map_range_001.inputs[11].hide = True
    map_range_001.outputs[0].hide = True
    # From_Min_FLOAT3
    map_range_001.inputs[7].default_value = (0.0, 0.0, 0.0)
    # From_Max_FLOAT3
    map_range_001.inputs[8].default_value = (1.0, 1.0, 1.0)
    # To_Min_FLOAT3
    map_range_001.inputs[9].default_value = (0.0, 0.0, 0.0)
    # To_Max_FLOAT3
    map_range_001.inputs[10].default_value = (1.0, 1.0, 1.0)

    # node Map Range.002
    map_range_002 = colorpalette.nodes.new("ShaderNodeMapRange")
    map_range_002.name = "Map Range.002"
    map_range_002.clamp = True
    map_range_002.data_type = "FLOAT_VECTOR"
    map_range_002.interpolation_type = "SMOOTHERSTEP"
    map_range_002.inputs[1].hide = True
    map_range_002.inputs[2].hide = True
    map_range_002.inputs[3].hide = True
    map_range_002.inputs[4].hide = True
    map_range_002.inputs[5].hide = True
    map_range_002.inputs[7].hide = True
    map_range_002.inputs[8].hide = True
    map_range_002.inputs[9].hide = True
    map_range_002.inputs[10].hide = True
    map_range_002.inputs[11].hide = True
    map_range_002.outputs[0].hide = True
    # From_Min_FLOAT3
    map_range_002.inputs[7].default_value = (0.0, 0.0, 0.0)
    # From_Max_FLOAT3
    map_range_002.inputs[8].default_value = (1.0, 1.0, 1.0)
    # To_Min_FLOAT3
    map_range_002.inputs[9].default_value = (0.0, 0.0, 0.0)
    # To_Max_FLOAT3
    map_range_002.inputs[10].default_value = (1.0, 1.0, 1.0)

    # node Image Texture
    image_texture = colorpalette.nodes.new("GeometryNodeImageTexture")
    image_texture.name = "Image Texture"
    image_texture.extension = "REPEAT"
    image_texture.interpolation = "Cubic"
    image_texture.inputs[2].hide = True
    image_texture.outputs[1].hide = True
    # Frame
    image_texture.inputs[2].default_value = 1

    # node Position
    position = colorpalette.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"

    # node Group Input.003
    group_input_003 = colorpalette.nodes.new("NodeGroupInput")
    group_input_003.name = "Group Input.003"
    group_input_003.outputs[0].hide = True
    group_input_003.outputs[1].hide = True
    group_input_003.outputs[2].hide = True
    group_input_003.outputs[3].hide = True
    group_input_003.outputs[4].hide = True
    group_input_003.outputs[5].hide = True
    group_input_003.outputs[6].hide = True
    group_input_003.outputs[7].hide = True
    group_input_003.outputs[8].hide = True
    group_input_003.outputs[10].hide = True
    group_input_003.outputs[11].hide = True
    group_input_003.outputs[12].hide = True
    group_input_003.outputs[13].hide = True
    group_input_003.outputs[14].hide = True
    group_input_003.outputs[15].hide = True

    # node Group Input.004
    group_input_004 = colorpalette.nodes.new("NodeGroupInput")
    group_input_004.name = "Group Input.004"
    group_input_004.outputs[0].hide = True
    group_input_004.outputs[1].hide = True
    group_input_004.outputs[2].hide = True
    group_input_004.outputs[3].hide = True
    group_input_004.outputs[4].hide = True
    group_input_004.outputs[5].hide = True
    group_input_004.outputs[7].hide = True
    group_input_004.outputs[8].hide = True
    group_input_004.outputs[9].hide = True
    group_input_004.outputs[10].hide = True
    group_input_004.outputs[11].hide = True
    group_input_004.outputs[12].hide = True
    group_input_004.outputs[13].hide = True
    group_input_004.outputs[14].hide = True
    group_input_004.outputs[15].hide = True

    # node Scene Time
    scene_time = colorpalette.nodes.new("GeometryNodeInputSceneTime")
    scene_time.name = "Scene Time"
    scene_time.outputs[1].hide = True

    # node Math.004
    math_004 = colorpalette.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.operation = "MULTIPLY"
    math_004.use_clamp = False
    math_004.inputs[2].hide = True

    # node Math.005
    math_005 = colorpalette.nodes.new("ShaderNodeMath")
    math_005.name = "Math.005"
    math_005.operation = "TRUNC"
    math_005.use_clamp = False
    math_005.inputs[1].hide = True
    math_005.inputs[2].hide = True

    # node Group Input.005
    group_input_005 = colorpalette.nodes.new("NodeGroupInput")
    group_input_005.name = "Group Input.005"
    group_input_005.outputs[0].hide = True
    group_input_005.outputs[1].hide = True
    group_input_005.outputs[2].hide = True
    group_input_005.outputs[3].hide = True
    group_input_005.outputs[4].hide = True
    group_input_005.outputs[5].hide = True
    group_input_005.outputs[6].hide = True
    group_input_005.outputs[7].hide = True
    group_input_005.outputs[9].hide = True
    group_input_005.outputs[10].hide = True
    group_input_005.outputs[11].hide = True
    group_input_005.outputs[12].hide = True
    group_input_005.outputs[13].hide = True
    group_input_005.outputs[14].hide = True
    group_input_005.outputs[15].hide = True

    # node Group Input.006
    group_input_006 = colorpalette.nodes.new("NodeGroupInput")
    group_input_006.name = "Group Input.006"
    group_input_006.outputs[0].hide = True
    group_input_006.outputs[1].hide = True
    group_input_006.outputs[2].hide = True
    group_input_006.outputs[3].hide = True
    group_input_006.outputs[4].hide = True
    group_input_006.outputs[5].hide = True
    group_input_006.outputs[6].hide = True
    group_input_006.outputs[7].hide = True
    group_input_006.outputs[8].hide = True
    group_input_006.outputs[9].hide = True
    group_input_006.outputs[11].hide = True
    group_input_006.outputs[12].hide = True
    group_input_006.outputs[13].hide = True
    group_input_006.outputs[14].hide = True
    group_input_006.outputs[15].hide = True

    # node Group Input.007
    group_input_007 = colorpalette.nodes.new("NodeGroupInput")
    group_input_007.name = "Group Input.007"
    group_input_007.outputs[0].hide = True
    group_input_007.outputs[1].hide = True
    group_input_007.outputs[2].hide = True
    group_input_007.outputs[3].hide = True
    group_input_007.outputs[4].hide = True
    group_input_007.outputs[5].hide = True
    group_input_007.outputs[6].hide = True
    group_input_007.outputs[7].hide = True
    group_input_007.outputs[8].hide = True
    group_input_007.outputs[9].hide = True
    group_input_007.outputs[10].hide = True
    group_input_007.outputs[12].hide = True
    group_input_007.outputs[13].hide = True
    group_input_007.outputs[14].hide = True
    group_input_007.outputs[15].hide = True

    # node Switch.006
    switch_006 = colorpalette.nodes.new("GeometryNodeSwitch")
    switch_006.name = "Switch.006"
    switch_006.input_type = "RGBA"

    # node Group Input.008
    group_input_008 = colorpalette.nodes.new("NodeGroupInput")
    group_input_008.name = "Group Input.008"
    group_input_008.outputs[0].hide = True
    group_input_008.outputs[1].hide = True
    group_input_008.outputs[2].hide = True
    group_input_008.outputs[3].hide = True
    group_input_008.outputs[4].hide = True
    group_input_008.outputs[5].hide = True
    group_input_008.outputs[6].hide = True
    group_input_008.outputs[7].hide = True
    group_input_008.outputs[8].hide = True
    group_input_008.outputs[9].hide = True
    group_input_008.outputs[10].hide = True
    group_input_008.outputs[11].hide = True
    group_input_008.outputs[13].hide = True
    group_input_008.outputs[14].hide = True
    group_input_008.outputs[15].hide = True

    # node Switch.007
    switch_007 = colorpalette.nodes.new("GeometryNodeSwitch")
    switch_007.name = "Switch.007"
    switch_007.input_type = "RGBA"

    # node Math.003
    math_003 = colorpalette.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.operation = "MULTIPLY"
    math_003.use_clamp = False
    math_003.inputs[2].hide = True

    # node Random Value.009
    random_value_009 = colorpalette.nodes.new("FunctionNodeRandomValue")
    random_value_009.name = "Random Value.009"
    random_value_009.data_type = "INT"
    random_value_009.inputs[0].hide = True
    random_value_009.inputs[1].hide = True
    random_value_009.inputs[2].hide = True
    random_value_009.inputs[3].hide = True
    random_value_009.inputs[4].hide = True
    random_value_009.inputs[5].hide = True
    random_value_009.inputs[6].hide = True
    random_value_009.inputs[8].hide = True
    random_value_009.outputs[0].hide = True
    random_value_009.outputs[1].hide = True
    random_value_009.outputs[3].hide = True
    # Min_002
    random_value_009.inputs[4].default_value = 0
    # Max_002
    random_value_009.inputs[5].default_value = 100
    # Seed
    random_value_009.inputs[8].default_value = 4

    # node Group Input.009
    group_input_009 = colorpalette.nodes.new("NodeGroupInput")
    group_input_009.name = "Group Input.009"
    group_input_009.outputs[0].hide = True
    group_input_009.outputs[1].hide = True
    group_input_009.outputs[2].hide = True
    group_input_009.outputs[3].hide = True
    group_input_009.outputs[4].hide = True
    group_input_009.outputs[5].hide = True
    group_input_009.outputs[6].hide = True
    group_input_009.outputs[7].hide = True
    group_input_009.outputs[8].hide = True
    group_input_009.outputs[9].hide = True
    group_input_009.outputs[10].hide = True
    group_input_009.outputs[11].hide = True
    group_input_009.outputs[12].hide = True
    group_input_009.outputs[14].hide = True
    group_input_009.outputs[15].hide = True

    # node Switch.008
    switch_008 = colorpalette.nodes.new("GeometryNodeSwitch")
    switch_008.name = "Switch.008"
    switch_008.input_type = "RGBA"

    # node Group Input.010
    group_input_010 = colorpalette.nodes.new("NodeGroupInput")
    group_input_010.name = "Group Input.010"
    group_input_010.outputs[0].hide = True
    group_input_010.outputs[2].hide = True
    group_input_010.outputs[3].hide = True
    group_input_010.outputs[4].hide = True
    group_input_010.outputs[5].hide = True
    group_input_010.outputs[6].hide = True
    group_input_010.outputs[7].hide = True
    group_input_010.outputs[8].hide = True
    group_input_010.outputs[9].hide = True
    group_input_010.outputs[10].hide = True
    group_input_010.outputs[11].hide = True
    group_input_010.outputs[12].hide = True
    group_input_010.outputs[13].hide = True
    group_input_010.outputs[14].hide = True
    group_input_010.outputs[15].hide = True

    # node Group Input.012
    group_input_012 = colorpalette.nodes.new("NodeGroupInput")
    group_input_012.name = "Group Input.012"
    group_input_012.outputs[0].hide = True
    group_input_012.outputs[1].hide = True
    group_input_012.outputs[2].hide = True
    group_input_012.outputs[3].hide = True
    group_input_012.outputs[4].hide = True
    group_input_012.outputs[5].hide = True
    group_input_012.outputs[6].hide = True
    group_input_012.outputs[7].hide = True
    group_input_012.outputs[9].hide = True
    group_input_012.outputs[10].hide = True
    group_input_012.outputs[11].hide = True
    group_input_012.outputs[12].hide = True
    group_input_012.outputs[13].hide = True
    group_input_012.outputs[14].hide = True
    group_input_012.outputs[15].hide = True

    # node Vector Math.001
    vector_math_001 = colorpalette.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.operation = "SCALE"
    vector_math_001.inputs[1].hide = True
    vector_math_001.inputs[2].hide = True
    vector_math_001.outputs[1].hide = True

    # node Random Value.011
    random_value_011 = colorpalette.nodes.new("FunctionNodeRandomValue")
    random_value_011.name = "Random Value.011"
    random_value_011.data_type = "BOOLEAN"
    # Seed
    random_value_011.inputs[8].default_value = 0

    # node Switch
    switch_1 = colorpalette.nodes.new("GeometryNodeSwitch")
    switch_1.name = "Switch"
    switch_1.input_type = "VECTOR"

    # node Random Value.012
    random_value_012 = colorpalette.nodes.new("FunctionNodeRandomValue")
    random_value_012.name = "Random Value.012"
    random_value_012.data_type = "BOOLEAN"
    random_value_012.inputs[0].hide = True
    random_value_012.inputs[1].hide = True
    random_value_012.inputs[2].hide = True
    random_value_012.inputs[3].hide = True
    random_value_012.inputs[4].hide = True
    random_value_012.inputs[5].hide = True
    random_value_012.outputs[0].hide = True
    random_value_012.outputs[1].hide = True
    random_value_012.outputs[2].hide = True

    # node Vector Math.002
    vector_math_002 = colorpalette.nodes.new("ShaderNodeVectorMath")
    vector_math_002.name = "Vector Math.002"
    vector_math_002.operation = "SCALE"
    vector_math_002.inputs[1].hide = True
    vector_math_002.inputs[2].hide = True
    vector_math_002.outputs[1].hide = True

    # node Curve of Point
    curve_of_point = colorpalette.nodes.new("GeometryNodeCurveOfPoint")
    curve_of_point.name = "Curve of Point"
    curve_of_point.outputs[0].hide = True

    # node Index
    index = colorpalette.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"

    # node Compare.005
    compare_005_1 = colorpalette.nodes.new("FunctionNodeCompare")
    compare_005_1.name = "Compare.005"
    compare_005_1.data_type = "FLOAT"
    compare_005_1.mode = "ELEMENT"
    compare_005_1.operation = "LESS_EQUAL"
    compare_005_1.inputs[3].hide = True
    compare_005_1.inputs[4].hide = True
    compare_005_1.inputs[5].hide = True
    compare_005_1.inputs[6].hide = True
    compare_005_1.inputs[7].hide = True
    compare_005_1.inputs[8].hide = True
    compare_005_1.inputs[9].hide = True
    compare_005_1.inputs[10].hide = True
    compare_005_1.inputs[11].hide = True
    compare_005_1.inputs[12].hide = True

    # node Group Input.002
    group_input_002 = colorpalette.nodes.new("NodeGroupInput")
    group_input_002.name = "Group Input.002"
    group_input_002.outputs[0].hide = True
    group_input_002.outputs[1].hide = True
    group_input_002.outputs[3].hide = True
    group_input_002.outputs[4].hide = True
    group_input_002.outputs[5].hide = True
    group_input_002.outputs[6].hide = True
    group_input_002.outputs[7].hide = True
    group_input_002.outputs[8].hide = True
    group_input_002.outputs[9].hide = True
    group_input_002.outputs[10].hide = True
    group_input_002.outputs[11].hide = True
    group_input_002.outputs[12].hide = True
    group_input_002.outputs[13].hide = True
    group_input_002.outputs[14].hide = True
    group_input_002.outputs[15].hide = True

    # node Group Input.011
    group_input_011 = colorpalette.nodes.new("NodeGroupInput")
    group_input_011.name = "Group Input.011"
    group_input_011.outputs[0].hide = True
    group_input_011.outputs[1].hide = True
    group_input_011.outputs[2].hide = True
    group_input_011.outputs[3].hide = True
    group_input_011.outputs[4].hide = True
    group_input_011.outputs[5].hide = True
    group_input_011.outputs[6].hide = True
    group_input_011.outputs[7].hide = True
    group_input_011.outputs[9].hide = True
    group_input_011.outputs[10].hide = True
    group_input_011.outputs[11].hide = True
    group_input_011.outputs[12].hide = True
    group_input_011.outputs[13].hide = True
    group_input_011.outputs[14].hide = True
    group_input_011.outputs[15].hide = True

    # node Math.006
    math_006 = colorpalette.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.operation = "MULTIPLY"
    math_006.use_clamp = False
    math_006.inputs[2].hide = True

    # node Random Value.013
    random_value_013 = colorpalette.nodes.new("FunctionNodeRandomValue")
    random_value_013.name = "Random Value.013"
    random_value_013.data_type = "BOOLEAN"
    random_value_013.inputs[0].hide = True
    random_value_013.inputs[1].hide = True
    random_value_013.inputs[2].hide = True
    random_value_013.inputs[3].hide = True
    random_value_013.inputs[4].hide = True
    random_value_013.inputs[5].hide = True
    random_value_013.outputs[0].hide = True
    random_value_013.outputs[1].hide = True
    random_value_013.outputs[2].hide = True

    # node Math.007
    math_007 = colorpalette.nodes.new("ShaderNodeMath")
    math_007.name = "Math.007"
    math_007.operation = "ADD"
    math_007.use_clamp = False
    math_007.inputs[1].hide = True
    math_007.inputs[2].hide = True
    # Value_001
    math_007.inputs[1].default_value = 1.0

    # node Math.008
    math_008 = colorpalette.nodes.new("ShaderNodeMath")
    math_008.name = "Math.008"
    math_008.operation = "DIVIDE"
    math_008.use_clamp = False
    math_008.inputs[2].hide = True

    # node Group Input.013
    group_input_013 = colorpalette.nodes.new("NodeGroupInput")
    group_input_013.name = "Group Input.013"
    group_input_013.outputs[0].hide = True
    group_input_013.outputs[1].hide = True
    group_input_013.outputs[2].hide = True
    group_input_013.outputs[3].hide = True
    group_input_013.outputs[4].hide = True
    group_input_013.outputs[5].hide = True
    group_input_013.outputs[7].hide = True
    group_input_013.outputs[8].hide = True
    group_input_013.outputs[9].hide = True
    group_input_013.outputs[10].hide = True
    group_input_013.outputs[11].hide = True
    group_input_013.outputs[12].hide = True
    group_input_013.outputs[13].hide = True
    group_input_013.outputs[14].hide = True
    group_input_013.outputs[15].hide = True

    # node Group Input.014
    group_input_014 = colorpalette.nodes.new("NodeGroupInput")
    group_input_014.name = "Group Input.014"
    group_input_014.outputs[0].hide = True
    group_input_014.outputs[1].hide = True
    group_input_014.outputs[2].hide = True
    group_input_014.outputs[3].hide = True
    group_input_014.outputs[4].hide = True
    group_input_014.outputs[5].hide = True
    group_input_014.outputs[7].hide = True
    group_input_014.outputs[8].hide = True
    group_input_014.outputs[9].hide = True
    group_input_014.outputs[10].hide = True
    group_input_014.outputs[11].hide = True
    group_input_014.outputs[12].hide = True
    group_input_014.outputs[13].hide = True
    group_input_014.outputs[14].hide = True
    group_input_014.outputs[15].hide = True

    # node Attribute Statistic
    attribute_statistic_1 = colorpalette.nodes.new("GeometryNodeAttributeStatistic")
    attribute_statistic_1.name = "Attribute Statistic"
    attribute_statistic_1.data_type = "FLOAT"
    attribute_statistic_1.domain = "CURVE"
    attribute_statistic_1.inputs[1].hide = True
    attribute_statistic_1.outputs[0].hide = True
    attribute_statistic_1.outputs[1].hide = True
    attribute_statistic_1.outputs[2].hide = True
    attribute_statistic_1.outputs[3].hide = True
    attribute_statistic_1.outputs[5].hide = True
    attribute_statistic_1.outputs[6].hide = True
    attribute_statistic_1.outputs[7].hide = True
    # Selection
    attribute_statistic_1.inputs[1].default_value = True

    # node Group Input.015
    group_input_015 = colorpalette.nodes.new("NodeGroupInput")
    group_input_015.name = "Group Input.015"
    group_input_015.outputs[1].hide = True
    group_input_015.outputs[2].hide = True
    group_input_015.outputs[3].hide = True
    group_input_015.outputs[5].hide = True
    group_input_015.outputs[6].hide = True
    group_input_015.outputs[7].hide = True
    group_input_015.outputs[8].hide = True
    group_input_015.outputs[9].hide = True
    group_input_015.outputs[10].hide = True
    group_input_015.outputs[11].hide = True
    group_input_015.outputs[12].hide = True
    group_input_015.outputs[13].hide = True
    group_input_015.outputs[14].hide = True
    group_input_015.outputs[15].hide = True

    # node Math.009
    math_009 = colorpalette.nodes.new("ShaderNodeMath")
    math_009.name = "Math.009"
    math_009.operation = "MULTIPLY"
    math_009.use_clamp = False
    math_009.inputs[2].hide = True

    # node Random Value.008
    random_value_008 = colorpalette.nodes.new("FunctionNodeRandomValue")
    random_value_008.name = "Random Value.008"
    random_value_008.data_type = "FLOAT_VECTOR"
    random_value_008.inputs[0].hide = True
    random_value_008.inputs[1].hide = True
    random_value_008.inputs[2].hide = True
    random_value_008.inputs[3].hide = True
    random_value_008.inputs[4].hide = True
    random_value_008.inputs[5].hide = True
    random_value_008.inputs[6].hide = True
    random_value_008.outputs[1].hide = True
    random_value_008.outputs[2].hide = True
    random_value_008.outputs[3].hide = True
    # Min
    random_value_008.inputs[0].default_value = (-10.0, -10.0, -10.0)
    # Max
    random_value_008.inputs[1].default_value = (10.0, 10.0, 10.0)

    # node Group Input.016
    group_input_016 = colorpalette.nodes.new("NodeGroupInput")
    group_input_016.name = "Group Input.016"
    group_input_016.outputs[0].hide = True
    group_input_016.outputs[1].hide = True
    group_input_016.outputs[2].hide = True
    group_input_016.outputs[3].hide = True
    group_input_016.outputs[4].hide = True
    group_input_016.outputs[6].hide = True
    group_input_016.outputs[7].hide = True
    group_input_016.outputs[8].hide = True
    group_input_016.outputs[9].hide = True
    group_input_016.outputs[10].hide = True
    group_input_016.outputs[11].hide = True
    group_input_016.outputs[12].hide = True
    group_input_016.outputs[13].hide = True
    group_input_016.outputs[14].hide = True
    group_input_016.outputs[15].hide = True

    # node Vector Math.003
    vector_math_003 = colorpalette.nodes.new("ShaderNodeVectorMath")
    vector_math_003.name = "Vector Math.003"
    vector_math_003.operation = "ADD"
    vector_math_003.inputs[2].hide = True
    vector_math_003.inputs[3].hide = True
    vector_math_003.outputs[1].hide = True

    # node Compare.006
    compare_006 = colorpalette.nodes.new("FunctionNodeCompare")
    compare_006.name = "Compare.006"
    compare_006.data_type = "STRING"
    compare_006.mode = "ELEMENT"
    compare_006.operation = "EQUAL"
    compare_006.inputs[0].hide = True
    compare_006.inputs[1].hide = True
    compare_006.inputs[2].hide = True
    compare_006.inputs[3].hide = True
    compare_006.inputs[4].hide = True
    compare_006.inputs[5].hide = True
    compare_006.inputs[6].hide = True
    compare_006.inputs[7].hide = True
    compare_006.inputs[9].hide = True
    compare_006.inputs[10].hide = True
    compare_006.inputs[11].hide = True
    compare_006.inputs[12].hide = True
    # B_STR
    compare_006.inputs[9].default_value = "Random"

    # node Switch.009
    switch_009 = colorpalette.nodes.new("GeometryNodeSwitch")
    switch_009.name = "Switch.009"
    switch_009.input_type = "FLOAT"

    # node Group Input.017
    group_input_017 = colorpalette.nodes.new("NodeGroupInput")
    group_input_017.name = "Group Input.017"
    group_input_017.outputs[0].hide = True
    group_input_017.outputs[1].hide = True
    group_input_017.outputs[2].hide = True
    group_input_017.outputs[4].hide = True
    group_input_017.outputs[5].hide = True
    group_input_017.outputs[6].hide = True
    group_input_017.outputs[7].hide = True
    group_input_017.outputs[8].hide = True
    group_input_017.outputs[9].hide = True
    group_input_017.outputs[10].hide = True
    group_input_017.outputs[11].hide = True
    group_input_017.outputs[12].hide = True
    group_input_017.outputs[13].hide = True
    group_input_017.outputs[14].hide = True
    group_input_017.outputs[15].hide = True

    # node Compare.007
    compare_007 = colorpalette.nodes.new("FunctionNodeCompare")
    compare_007.name = "Compare.007"
    compare_007.data_type = "STRING"
    compare_007.mode = "ELEMENT"
    compare_007.operation = "EQUAL"
    compare_007.inputs[0].hide = True
    compare_007.inputs[1].hide = True
    compare_007.inputs[2].hide = True
    compare_007.inputs[3].hide = True
    compare_007.inputs[4].hide = True
    compare_007.inputs[5].hide = True
    compare_007.inputs[6].hide = True
    compare_007.inputs[7].hide = True
    compare_007.inputs[9].hide = True
    compare_007.inputs[10].hide = True
    compare_007.inputs[11].hide = True
    compare_007.inputs[12].hide = True
    # B_STR
    compare_007.inputs[9].default_value = "Custom"

    # node Compare.008
    compare_008 = colorpalette.nodes.new("FunctionNodeCompare")
    compare_008.name = "Compare.008"
    compare_008.data_type = "STRING"
    compare_008.mode = "ELEMENT"
    compare_008.operation = "EQUAL"
    compare_008.inputs[0].hide = True
    compare_008.inputs[1].hide = True
    compare_008.inputs[2].hide = True
    compare_008.inputs[3].hide = True
    compare_008.inputs[4].hide = True
    compare_008.inputs[5].hide = True
    compare_008.inputs[6].hide = True
    compare_008.inputs[7].hide = True
    compare_008.inputs[9].hide = True
    compare_008.inputs[10].hide = True
    compare_008.inputs[11].hide = True
    compare_008.inputs[12].hide = True
    # B_STR
    compare_008.inputs[9].default_value = "Image"

    # node Switch.010
    switch_010 = colorpalette.nodes.new("GeometryNodeSwitch")
    switch_010.name = "Switch.010"
    switch_010.input_type = "RGBA"

    # node Switch.011
    switch_011 = colorpalette.nodes.new("GeometryNodeSwitch")
    switch_011.name = "Switch.011"
    switch_011.input_type = "RGBA"



    # node Group Input.018
    group_input_018 = colorpalette.nodes.new("NodeGroupInput")
    group_input_018.name = "Group Input.018"
    group_input_018.outputs[0].hide = True
    group_input_018.outputs[1].hide = True
    group_input_018.outputs[2].hide = True
    group_input_018.outputs[3].hide = True
    group_input_018.outputs[4].hide = True
    group_input_018.outputs[5].hide = True
    group_input_018.outputs[6].hide = True
    group_input_018.outputs[7].hide = True
    group_input_018.outputs[8].hide = True
    group_input_018.outputs[9].hide = True
    group_input_018.outputs[10].hide = True
    group_input_018.outputs[11].hide = True
    group_input_018.outputs[12].hide = True
    group_input_018.outputs[13].hide = True
    group_input_018.outputs[15].hide = True

    # node Group Input.019
    group_input_019 = colorpalette.nodes.new("NodeGroupInput")
    group_input_019.name = "Group Input.019"
    group_input_019.outputs[0].hide = True
    group_input_019.outputs[1].hide = True
    group_input_019.outputs[2].hide = True
    group_input_019.outputs[3].hide = True
    group_input_019.outputs[4].hide = True
    group_input_019.outputs[5].hide = True
    group_input_019.outputs[6].hide = True
    group_input_019.outputs[7].hide = True
    group_input_019.outputs[8].hide = True
    group_input_019.outputs[9].hide = True
    group_input_019.outputs[10].hide = True
    group_input_019.outputs[11].hide = True
    group_input_019.outputs[12].hide = True
    group_input_019.outputs[13].hide = True
    group_input_019.outputs[15].hide = True

    # node Group Input.020
    group_input_020 = colorpalette.nodes.new("NodeGroupInput")
    group_input_020.name = "Group Input.020"
    group_input_020.outputs[0].hide = True
    group_input_020.outputs[1].hide = True
    group_input_020.outputs[2].hide = True
    group_input_020.outputs[3].hide = True
    group_input_020.outputs[4].hide = True
    group_input_020.outputs[5].hide = True
    group_input_020.outputs[6].hide = True
    group_input_020.outputs[7].hide = True
    group_input_020.outputs[8].hide = True
    group_input_020.outputs[9].hide = True
    group_input_020.outputs[10].hide = True
    group_input_020.outputs[11].hide = True
    group_input_020.outputs[12].hide = True
    group_input_020.outputs[13].hide = True
    group_input_020.outputs[15].hide = True

    # node Group Input.021
    group_input_021 = colorpalette.nodes.new("NodeGroupInput")
    group_input_021.name = "Group Input.021"
    group_input_021.outputs[0].hide = True
    group_input_021.outputs[1].hide = True
    group_input_021.outputs[2].hide = True
    group_input_021.outputs[3].hide = True
    group_input_021.outputs[4].hide = True
    group_input_021.outputs[5].hide = True
    group_input_021.outputs[6].hide = True
    group_input_021.outputs[7].hide = True
    group_input_021.outputs[8].hide = True
    group_input_021.outputs[9].hide = True
    group_input_021.outputs[10].hide = True
    group_input_021.outputs[11].hide = True
    group_input_021.outputs[12].hide = True
    group_input_021.outputs[13].hide = True
    group_input_021.outputs[15].hide = True

    # node Group Input.022
    group_input_022 = colorpalette.nodes.new("NodeGroupInput")
    group_input_022.name = "Group Input.022"
    group_input_022.outputs[0].hide = True
    group_input_022.outputs[1].hide = True
    group_input_022.outputs[2].hide = True
    group_input_022.outputs[3].hide = True
    group_input_022.outputs[4].hide = True
    group_input_022.outputs[5].hide = True
    group_input_022.outputs[6].hide = True
    group_input_022.outputs[7].hide = True
    group_input_022.outputs[8].hide = True
    group_input_022.outputs[9].hide = True
    group_input_022.outputs[10].hide = True
    group_input_022.outputs[11].hide = True
    group_input_022.outputs[12].hide = True
    group_input_022.outputs[13].hide = True
    group_input_022.outputs[15].hide = True

    # node Group Input.023
    group_input_023 = colorpalette.nodes.new("NodeGroupInput")
    group_input_023.name = "Group Input.023"
    group_input_023.outputs[0].hide = True
    group_input_023.outputs[1].hide = True
    group_input_023.outputs[2].hide = True
    group_input_023.outputs[3].hide = True
    group_input_023.outputs[4].hide = True
    group_input_023.outputs[5].hide = True
    group_input_023.outputs[6].hide = True
    group_input_023.outputs[7].hide = True
    group_input_023.outputs[8].hide = True
    group_input_023.outputs[9].hide = True
    group_input_023.outputs[10].hide = True
    group_input_023.outputs[11].hide = True
    group_input_023.outputs[12].hide = True
    group_input_023.outputs[13].hide = True
    group_input_023.outputs[15].hide = True

    # node Group Input.024
    group_input_024 = colorpalette.nodes.new("NodeGroupInput")
    group_input_024.name = "Group Input.024"
    group_input_024.outputs[0].hide = True
    group_input_024.outputs[1].hide = True
    group_input_024.outputs[2].hide = True
    group_input_024.outputs[3].hide = True
    group_input_024.outputs[4].hide = True
    group_input_024.outputs[5].hide = True
    group_input_024.outputs[6].hide = True
    group_input_024.outputs[7].hide = True
    group_input_024.outputs[8].hide = True
    group_input_024.outputs[9].hide = True
    group_input_024.outputs[10].hide = True
    group_input_024.outputs[11].hide = True
    group_input_024.outputs[12].hide = True
    group_input_024.outputs[13].hide = True
    group_input_024.outputs[15].hide = True

    # node Group Input.025
    group_input_025 = colorpalette.nodes.new("NodeGroupInput")
    group_input_025.name = "Group Input.025"
    group_input_025.outputs[0].hide = True
    group_input_025.outputs[1].hide = True
    group_input_025.outputs[2].hide = True
    group_input_025.outputs[3].hide = True
    group_input_025.outputs[4].hide = True
    group_input_025.outputs[5].hide = True
    group_input_025.outputs[6].hide = True
    group_input_025.outputs[7].hide = True
    group_input_025.outputs[8].hide = True
    group_input_025.outputs[9].hide = True
    group_input_025.outputs[10].hide = True
    group_input_025.outputs[11].hide = True
    group_input_025.outputs[12].hide = True
    group_input_025.outputs[13].hide = True
    group_input_025.outputs[15].hide = True

    # node Group Input.026
    group_input_026 = colorpalette.nodes.new("NodeGroupInput")
    group_input_026.name = "Group Input.026"
    group_input_026.outputs[0].hide = True
    group_input_026.outputs[1].hide = True
    group_input_026.outputs[2].hide = True
    group_input_026.outputs[3].hide = True
    group_input_026.outputs[4].hide = True
    group_input_026.outputs[5].hide = True
    group_input_026.outputs[6].hide = True
    group_input_026.outputs[7].hide = True
    group_input_026.outputs[8].hide = True
    group_input_026.outputs[9].hide = True
    group_input_026.outputs[10].hide = True
    group_input_026.outputs[11].hide = True
    group_input_026.outputs[12].hide = True
    group_input_026.outputs[13].hide = True
    group_input_026.outputs[15].hide = True

    # node Group Input.027
    group_input_027 = colorpalette.nodes.new("NodeGroupInput")
    group_input_027.name = "Group Input.027"
    group_input_027.outputs[0].hide = True
    group_input_027.outputs[1].hide = True
    group_input_027.outputs[2].hide = True
    group_input_027.outputs[3].hide = True
    group_input_027.outputs[4].hide = True
    group_input_027.outputs[5].hide = True
    group_input_027.outputs[6].hide = True
    group_input_027.outputs[7].hide = True
    group_input_027.outputs[8].hide = True
    group_input_027.outputs[9].hide = True
    group_input_027.outputs[10].hide = True
    group_input_027.outputs[11].hide = True
    group_input_027.outputs[12].hide = True
    group_input_027.outputs[13].hide = True
    group_input_027.outputs[15].hide = True

    # node Group Input.028
    group_input_028 = colorpalette.nodes.new("NodeGroupInput")
    group_input_028.name = "Group Input.028"
    group_input_028.outputs[0].hide = True
    group_input_028.outputs[1].hide = True
    group_input_028.outputs[2].hide = True
    group_input_028.outputs[3].hide = True
    group_input_028.outputs[4].hide = True
    group_input_028.outputs[5].hide = True
    group_input_028.outputs[6].hide = True
    group_input_028.outputs[7].hide = True
    group_input_028.outputs[8].hide = True
    group_input_028.outputs[9].hide = True
    group_input_028.outputs[10].hide = True
    group_input_028.outputs[11].hide = True
    group_input_028.outputs[12].hide = True
    group_input_028.outputs[13].hide = True
    group_input_028.outputs[15].hide = True

    # node Reroute
    reroute_2 = colorpalette.nodes.new("NodeReroute")
    reroute_2.name = "Reroute"
    # node Reroute.001
    reroute_001_2 = colorpalette.nodes.new("NodeReroute")
    reroute_001_2.name = "Reroute.001"
    # node Reroute.002
    reroute_002_2 = colorpalette.nodes.new("NodeReroute")
    reroute_002_2.name = "Reroute.002"
    # node Reroute.003
    reroute_003_2 = colorpalette.nodes.new("NodeReroute")
    reroute_003_2.name = "Reroute.003"
    # node Reroute.004
    reroute_004_2 = colorpalette.nodes.new("NodeReroute")
    reroute_004_2.name = "Reroute.004"
    # node Reroute.005
    reroute_005_2 = colorpalette.nodes.new("NodeReroute")
    reroute_005_2.name = "Reroute.005"
    # node Reroute.006
    reroute_006_2 = colorpalette.nodes.new("NodeReroute")
    reroute_006_2.name = "Reroute.006"
    # node Reroute.007
    reroute_007_1 = colorpalette.nodes.new("NodeReroute")
    reroute_007_1.name = "Reroute.007"
    # node Reroute.008
    reroute_008_1 = colorpalette.nodes.new("NodeReroute")
    reroute_008_1.name = "Reroute.008"
    # node Reroute.009
    reroute_009_1 = colorpalette.nodes.new("NodeReroute")
    reroute_009_1.name = "Reroute.009"
    # node Reroute.010
    reroute_010_1 = colorpalette.nodes.new("NodeReroute")
    reroute_010_1.name = "Reroute.010"
    # node Group Input.029
    group_input_029 = colorpalette.nodes.new("NodeGroupInput")
    group_input_029.name = "Group Input.029"
    group_input_029.outputs[0].hide = True
    group_input_029.outputs[1].hide = True
    group_input_029.outputs[2].hide = True
    group_input_029.outputs[3].hide = True
    group_input_029.outputs[4].hide = True
    group_input_029.outputs[5].hide = True
    group_input_029.outputs[6].hide = True
    group_input_029.outputs[7].hide = True
    group_input_029.outputs[8].hide = True
    group_input_029.outputs[9].hide = True
    group_input_029.outputs[10].hide = True
    group_input_029.outputs[11].hide = True
    group_input_029.outputs[12].hide = True
    group_input_029.outputs[13].hide = True
    group_input_029.outputs[15].hide = True

    # node Group Input.030
    group_input_030 = colorpalette.nodes.new("NodeGroupInput")
    group_input_030.name = "Group Input.030"
    group_input_030.outputs[0].hide = True
    group_input_030.outputs[1].hide = True
    group_input_030.outputs[2].hide = True
    group_input_030.outputs[3].hide = True
    group_input_030.outputs[4].hide = True
    group_input_030.outputs[5].hide = True
    group_input_030.outputs[6].hide = True
    group_input_030.outputs[7].hide = True
    group_input_030.outputs[8].hide = True
    group_input_030.outputs[9].hide = True
    group_input_030.outputs[10].hide = True
    group_input_030.outputs[11].hide = True
    group_input_030.outputs[12].hide = True
    group_input_030.outputs[13].hide = True
    group_input_030.outputs[15].hide = True

    # node Reroute.011
    reroute_011 = colorpalette.nodes.new("NodeReroute")
    reroute_011.name = "Reroute.011"

    # Set locations
    group_output_2.location = (2693.85107421875, -1830.119384765625)
    group_input_2.location = (-236.14886474609375, -137.119384765625)
    random_value.location = (41.35113525390625, 460.380615234375)
    switch_001.location = (1366.35107421875, -181.619384765625)
    compare.location = (1076.35107421875, 753.380615234375)
    random_value_001.location = (331.35113525390625, -1310.119384765625)
    compare_001_1.location = (331.35113525390625, 695.380615234375)
    compare_002_1.location = (331.35113525390625, 519.380615234375)
    boolean_math.location = (608.8511352539062, 607.380615234375)
    switch_002.location = (1076.35107421875, -181.619384765625)
    random_value_002.location = (331.35113525390625, -1010.119384765625)
    compare_003.location = (331.35113525390625, 343.380615234375)
    compare_004.location = (331.35113525390625, 167.380615234375)
    boolean_math_001.location = (608.8511352539062, 255.380615234375)
    switch_003.location = (848.8511352539062, -273.619384765625)
    random_value_003.location = (331.35113525390625, -296.119384765625)
    random_value_004.location = (331.35113525390625, -8.619384765625)
    random_value_005.location = (-236.14886474609375, -1361.119384765625)
    math_1.location = (41.35113525390625, -1361.119384765625)
    math_001.location = (41.35113525390625, -1061.119384765625)
    random_value_006.location = (-236.14886474609375, -1061.119384765625)
    math_002.location = (41.35113525390625, -385.619384765625)
    random_value_007.location = (-236.14886474609375, 38.380615234375)
    map_range.location = (2288.85107421875, -1910.119384765625)
    group_input_001.location = (2288.85107421875, -1750.119384765625)
    menu_switch.location = (2503.85107421875, -1830.119384765625)
    map_range_001.location = (2288.85107421875, -2111.119384765625)
    map_range_002.location = (2288.85107421875, -2287.119384765625)
    image_texture.location = (1316.35107421875, -1486.619384765625)
    position.location = (848.8511352539062, -1487.619384765625)
    group_input_003.location = (1076.35107421875, -1435.619384765625)
    group_input_004.location = (608.8511352539062, -2538.119384765625)
    scene_time.location = (608.8511352539062, -2640.119384765625)
    math_004.location = (848.8511352539062, -2589.119384765625)
    math_005.location = (1076.35107421875, -2589.119384765625)
    group_input_005.location = (1076.35107421875, -2385.119384765625)
    group_input_006.location = (331.35113525390625, -1544.119384765625)
    group_input_007.location = (331.35113525390625, -1195.619384765625)
    switch_006.location = (608.8511352539062, -1010.119384765625)
    group_input_008.location = (331.35113525390625, -908.119384765625)
    switch_007.location = (608.8511352539062, -543.619384765625)
    math_003.location = (41.35113525390625, -685.619384765625)
    random_value_009.location = (-236.14886474609375, -685.619384765625)
    group_input_009.location = (331.35113525390625, -181.619384765625)
    switch_008.location = (608.8511352539062, -181.619384765625)
    group_input_010.location = (1883.85107421875, -2027.619384765625)
    group_input_012.location = (1366.35107421875, 913.380615234375)
    vector_math_001.location = (1883.85107421875, -2129.619384765625)
    random_value_011.location = (1656.35107421875, 913.380615234375)
    switch_1.location = (2073.85107421875, -2082.119384765625)
    random_value_012.location = (1366.35107421875, -2487.119384765625)
    vector_math_002.location = (1883.85107421875, -2302.619384765625)
    curve_of_point.location = (1076.35107421875, -1892.119384765625)
    index.location = (-426.14886474609375, -1705.119384765625)
    compare_005_1.location = (848.8511352539062, -1892.119384765625)
    group_input_002.location = (1076.35107421875, -1753.119384765625)
    group_input_011.location = (848.8511352539062, -2090.119384765625)
    math_006.location = (1366.35107421875, -2104.119384765625)
    random_value_013.location = (1076.35107421875, -2192.119384765625)
    math_007.location = (-236.14886474609375, -1705.119384765625)
    math_008.location = (41.35113525390625, -1793.119384765625)
    group_input_013.location = (-236.14886474609375, -1881.119384765625)
    group_input_014.location = (848.8511352539062, -2390.619384765625)
    attribute_statistic_1.location = (331.35113525390625, -1892.119384765625)
    group_input_015.location = (41.35113525390625, -1991.119384765625)
    math_009.location = (608.8511352539062, -1991.119384765625)
    random_value_008.location = (848.8511352539062, -1587.619384765625)
    group_input_016.location = (608.8511352539062, -1638.619384765625)
    vector_math_003.location = (1076.35107421875, -1537.619384765625)
    compare_006.location = (1366.35107421875, -1753.119384765625)
    switch_009.location = (1656.35107421875, -2302.619384765625)
    group_input_017.location = (41.35113525390625, 72.880615234375)
    compare_007.location = (331.35113525390625, -469.119384765625)
    compare_008.location = (1366.35107421875, 811.380615234375)
    switch_010.location = (1656.35107421875, -181.619384765625)
    switch_011.location = (608.8511352539062, -1310.119384765625)
    group_input_018.location = (-426.14886474609375, 38.380615234375)
    group_input_019.location = (-426.14886474609375, -685.619384765625)
    group_input_020.location = (41.35113525390625, -283.619384765625)
    group_input_021.location = (41.35113525390625, -583.619384765625)
    group_input_022.location = (-426.14886474609375, -1061.119384765625)
    group_input_023.location = (41.35113525390625, -959.119384765625)
    group_input_024.location = (-426.14886474609375, -1361.119384765625)
    group_input_025.location = (41.35113525390625, -1259.119384765625)
    group_input_026.location = (848.8511352539062, -2192.119384765625)
    group_input_027.location = (1076.35107421875, -2487.119384765625)
    group_input_028.location = (608.8511352539062, -1536.619384765625)
    reroute_2.location = (331.35113525390625, -2122.213623046875)
    reroute_001_2.location = (331.35113525390625, 811.380615234375)
    reroute_002_2.location = (1216.35107421875, 811.380615234375)
    reroute_003_2.location = (331.35113525390625, 753.380615234375)
    reroute_004_2.location = (988.8511352539062, 753.380615234375)
    reroute_005_2.location = (748.8511352539062, -1828.213623046875)
    reroute_006_2.location = (988.8511352539062, 572.786376953125)
    reroute_007_1.location = (988.8511352539062, -1045.213623046875)
    reroute_008_1.location = (1216.35107421875, -1344.713623046875)
    reroute_009_1.location = (2288.85107421875, -1852.119384765625)
    reroute_010_1.location = (2428.85107421875, -1852.119384765625)
    group_input_029.location = (1459.29931640625, 1016.361083984375)
    group_input_030.location = (-311.8929443359375, 473.4652099609375)
    reroute_011.location = (0.11743736267089844, 214.52769470214844)

    # Set dimensions
    group_output_2.width, group_output_2.height = 140.0, 100.0
    group_input_2.width, group_input_2.height = 140.0, 100.0
    random_value.width, random_value.height = 140.0, 100.0
    switch_001.width, switch_001.height = 140.0, 100.0
    compare.width, compare.height = 140.0, 100.0
    random_value_001.width, random_value_001.height = 140.0, 100.0
    compare_001_1.width, compare_001_1.height = 140.0, 100.0
    compare_002_1.width, compare_002_1.height = 140.0, 100.0
    boolean_math.width, boolean_math.height = 140.0, 100.0
    switch_002.width, switch_002.height = 140.0, 100.0
    random_value_002.width, random_value_002.height = 140.0, 100.0
    compare_003.width, compare_003.height = 140.0, 100.0
    compare_004.width, compare_004.height = 140.0, 100.0
    boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
    switch_003.width, switch_003.height = 140.0, 100.0
    random_value_003.width, random_value_003.height = 140.0, 100.0
    random_value_004.width, random_value_004.height = 140.0, 100.0
    random_value_005.width, random_value_005.height = 140.0, 100.0
    math_1.width, math_1.height = 140.0, 100.0
    math_001.width, math_001.height = 140.0, 100.0
    random_value_006.width, random_value_006.height = 140.0, 100.0
    math_002.width, math_002.height = 140.0, 100.0
    random_value_007.width, random_value_007.height = 140.0, 100.0
    map_range.width, map_range.height = 140.0, 100.0
    group_input_001.width, group_input_001.height = 140.0, 100.0
    menu_switch.width, menu_switch.height = 140.0, 100.0
    map_range_001.width, map_range_001.height = 140.0, 100.0
    map_range_002.width, map_range_002.height = 140.0, 100.0
    image_texture.width, image_texture.height = 240.0, 100.0
    position.width, position.height = 140.0, 100.0
    group_input_003.width, group_input_003.height = 140.0, 100.0
    group_input_004.width, group_input_004.height = 140.0, 100.0
    scene_time.width, scene_time.height = 140.0, 100.0
    math_004.width, math_004.height = 140.0, 100.0
    math_005.width, math_005.height = 140.0, 100.0
    group_input_005.width, group_input_005.height = 140.0, 100.0
    group_input_006.width, group_input_006.height = 140.0, 100.0
    group_input_007.width, group_input_007.height = 140.0, 100.0
    switch_006.width, switch_006.height = 140.0, 100.0
    group_input_008.width, group_input_008.height = 140.0, 100.0
    switch_007.width, switch_007.height = 140.0, 100.0
    math_003.width, math_003.height = 140.0, 100.0
    random_value_009.width, random_value_009.height = 140.0, 100.0
    group_input_009.width, group_input_009.height = 140.0, 100.0
    switch_008.width, switch_008.height = 140.0, 100.0
    group_input_010.width, group_input_010.height = 140.0, 100.0
    group_input_012.width, group_input_012.height = 140.0, 100.0
    vector_math_001.width, vector_math_001.height = 140.0, 100.0
    random_value_011.width, random_value_011.height = 140.0, 100.0
    switch_1.width, switch_1.height = 140.0, 100.0
    random_value_012.width, random_value_012.height = 140.0, 100.0
    vector_math_002.width, vector_math_002.height = 140.0, 100.0
    curve_of_point.width, curve_of_point.height = 140.0, 100.0
    index.width, index.height = 140.0, 100.0
    compare_005_1.width, compare_005_1.height = 140.0, 100.0
    group_input_002.width, group_input_002.height = 140.0, 100.0
    group_input_011.width, group_input_011.height = 140.0, 100.0
    math_006.width, math_006.height = 140.0, 100.0
    random_value_013.width, random_value_013.height = 140.0, 100.0
    math_007.width, math_007.height = 140.0, 100.0
    math_008.width, math_008.height = 140.0, 100.0
    group_input_013.width, group_input_013.height = 140.0, 100.0
    group_input_014.width, group_input_014.height = 140.0, 100.0
    attribute_statistic_1.width, attribute_statistic_1.height = 140.0, 100.0
    group_input_015.width, group_input_015.height = 140.0, 100.0
    math_009.width, math_009.height = 140.0, 100.0
    random_value_008.width, random_value_008.height = 140.0, 100.0
    group_input_016.width, group_input_016.height = 140.0, 100.0
    vector_math_003.width, vector_math_003.height = 140.0, 100.0
    compare_006.width, compare_006.height = 140.0, 100.0
    switch_009.width, switch_009.height = 140.0, 100.0
    group_input_017.width, group_input_017.height = 140.0, 100.0
    compare_007.width, compare_007.height = 140.0, 100.0
    compare_008.width, compare_008.height = 140.0, 100.0
    switch_010.width, switch_010.height = 140.0, 100.0
    switch_011.width, switch_011.height = 140.0, 100.0
    group_input_018.width, group_input_018.height = 140.0, 100.0
    group_input_019.width, group_input_019.height = 140.0, 100.0
    group_input_020.width, group_input_020.height = 140.0, 100.0
    group_input_021.width, group_input_021.height = 140.0, 100.0
    group_input_022.width, group_input_022.height = 140.0, 100.0
    group_input_023.width, group_input_023.height = 140.0, 100.0
    group_input_024.width, group_input_024.height = 140.0, 100.0
    group_input_025.width, group_input_025.height = 140.0, 100.0
    group_input_026.width, group_input_026.height = 140.0, 100.0
    group_input_027.width, group_input_027.height = 140.0, 100.0
    group_input_028.width, group_input_028.height = 140.0, 100.0
    reroute_2.width, reroute_2.height = 16.0, 100.0
    reroute_001_2.width, reroute_001_2.height = 16.0, 100.0
    reroute_002_2.width, reroute_002_2.height = 16.0, 100.0
    reroute_003_2.width, reroute_003_2.height = 16.0, 100.0
    reroute_004_2.width, reroute_004_2.height = 16.0, 100.0
    reroute_005_2.width, reroute_005_2.height = 16.0, 100.0
    reroute_006_2.width, reroute_006_2.height = 16.0, 100.0
    reroute_007_1.width, reroute_007_1.height = 16.0, 100.0
    reroute_008_1.width, reroute_008_1.height = 16.0, 100.0
    reroute_009_1.width, reroute_009_1.height = 16.0, 100.0
    reroute_010_1.width, reroute_010_1.height = 16.0, 100.0
    group_input_029.width, group_input_029.height = 140.0, 100.0
    group_input_030.width, group_input_030.height = 140.0, 100.0
    reroute_011.width, reroute_011.height = 16.0, 100.0

    # initialize colorpalette links
    # compare.Result -> switch_001.Switch
    colorpalette.links.new(compare.outputs[0], switch_001.inputs[0])
    # boolean_math_001.Boolean -> switch_003.Switch
    colorpalette.links.new(boolean_math_001.outputs[0], switch_003.inputs[0])
    # switch_003.Output -> switch_002.False
    colorpalette.links.new(switch_003.outputs[0], switch_002.inputs[1])
    # switch_002.Output -> switch_001.False
    colorpalette.links.new(switch_002.outputs[0], switch_001.inputs[1])
    # random_value_005.Value -> math_1.Value
    colorpalette.links.new(random_value_005.outputs[2], math_1.inputs[1])
    # math_1.Value -> random_value_001.Seed
    colorpalette.links.new(math_1.outputs[0], random_value_001.inputs[8])
    # math_001.Value -> random_value_002.Seed
    colorpalette.links.new(math_001.outputs[0], random_value_002.inputs[8])
    # random_value_007.Value -> math_002.Value
    colorpalette.links.new(random_value_007.outputs[2], math_002.inputs[1])
    # random_value.Value -> compare_001_1.A
    colorpalette.links.new(random_value.outputs[1], compare_001_1.inputs[0])
    # random_value.Value -> compare_003.A
    colorpalette.links.new(random_value.outputs[1], compare_003.inputs[0])
    # random_value.Value -> compare_004.A
    colorpalette.links.new(random_value.outputs[1], compare_004.inputs[0])
    # random_value.Value -> compare_002_1.A
    colorpalette.links.new(random_value.outputs[1], compare_002_1.inputs[0])
    # switch_001.Output -> map_range.Value
    colorpalette.links.new(switch_001.outputs[0], map_range.inputs[0])
    # group_input_001.Color - Distribution -> menu_switch.Menu
    colorpalette.links.new(group_input_001.outputs[7], menu_switch.inputs[0])
    # map_range.Vector -> menu_switch.Linear
    colorpalette.links.new(map_range.outputs[1], menu_switch.inputs[2])
    # switch_001.Output -> map_range_001.Value
    colorpalette.links.new(switch_001.outputs[0], map_range_001.inputs[0])
    # map_range_001.Vector -> menu_switch.Ease
    colorpalette.links.new(map_range_001.outputs[1], menu_switch.inputs[3])
    # switch_001.Output -> map_range_002.Value
    colorpalette.links.new(switch_001.outputs[0], map_range_002.inputs[0])
    # map_range_002.Vector -> menu_switch.B-Spline
    colorpalette.links.new(map_range_002.outputs[1], menu_switch.inputs[4])
    # random_value_006.Value -> math_001.Value
    colorpalette.links.new(random_value_006.outputs[2], math_001.inputs[1])
    # compare_004.Result -> boolean_math_001.Boolean
    colorpalette.links.new(compare_004.outputs[0], boolean_math_001.inputs[1])
    # compare_003.Result -> boolean_math_001.Boolean
    colorpalette.links.new(compare_003.outputs[0], boolean_math_001.inputs[0])
    # compare_002_1.Result -> boolean_math.Boolean
    colorpalette.links.new(compare_002_1.outputs[0], boolean_math.inputs[1])
    # compare_001_1.Result -> boolean_math.Boolean
    colorpalette.links.new(compare_001_1.outputs[0], boolean_math.inputs[0])
    # math_002.Value -> random_value_004.Seed
    colorpalette.links.new(math_002.outputs[0], random_value_004.inputs[8])
    # vector_math_003.Vector -> image_texture.Vector
    colorpalette.links.new(vector_math_003.outputs[0], image_texture.inputs[1])
    # group_input_003.Image -> image_texture.Image
    colorpalette.links.new(group_input_003.outputs[9], image_texture.inputs[0])
    # group_input_004.Speed -> math_004.Value
    colorpalette.links.new(group_input_004.outputs[6], math_004.inputs[0])
    # scene_time.Seconds -> math_004.Value
    colorpalette.links.new(scene_time.outputs[0], math_004.inputs[1])
    # math_004.Value -> math_005.Value
    colorpalette.links.new(math_004.outputs[0], math_005.inputs[0])
    # random_value_002.Value -> switch_006.False
    colorpalette.links.new(random_value_002.outputs[0], switch_006.inputs[1])
    # group_input_007.Color 2 -> switch_006.True
    colorpalette.links.new(group_input_007.outputs[11], switch_006.inputs[2])
    # random_value_009.Value -> math_003.Value
    colorpalette.links.new(random_value_009.outputs[2], math_003.inputs[1])
    # group_input_2.Seed -> math_003.Value
    colorpalette.links.new(group_input_2.outputs[5], math_003.inputs[0])
    # math_003.Value -> random_value_003.Seed
    colorpalette.links.new(math_003.outputs[0], random_value_003.inputs[8])
    # random_value_003.Value -> switch_007.False
    colorpalette.links.new(random_value_003.outputs[0], switch_007.inputs[1])
    # switch_007.Output -> switch_003.True
    colorpalette.links.new(switch_007.outputs[0], switch_003.inputs[2])
    # group_input_008.Color 3 -> switch_007.True
    colorpalette.links.new(group_input_008.outputs[12], switch_007.inputs[2])
    # random_value_004.Value -> switch_008.False
    colorpalette.links.new(random_value_004.outputs[0], switch_008.inputs[1])
    # group_input_009.Color 4 -> switch_008.True
    colorpalette.links.new(group_input_009.outputs[13], switch_008.inputs[2])
    # switch_008.Output -> switch_003.False
    colorpalette.links.new(switch_008.outputs[0], switch_003.inputs[1])
    # group_input_2.Seed -> math_002.Value
    colorpalette.links.new(group_input_2.outputs[5], math_002.inputs[0])
    # random_value_011.Value -> vector_math_001.Scale
    colorpalette.links.new(random_value_011.outputs[3], vector_math_001.inputs[3])
    # group_input_010.Animate -> switch_1.Switch
    colorpalette.links.new(group_input_010.outputs[1], switch_1.inputs[0])
    # vector_math_001.Vector -> switch_1.False
    colorpalette.links.new(vector_math_001.outputs[0], switch_1.inputs[1])
    # group_input_005.Blackness -> random_value_012.Probability
    colorpalette.links.new(group_input_005.outputs[8], random_value_012.inputs[6])
    # vector_math_002.Vector -> switch_1.True
    colorpalette.links.new(vector_math_002.outputs[0], switch_1.inputs[2])
    # index.Index -> compare_005_1.A
    colorpalette.links.new(index.outputs[0], compare_005_1.inputs[2])
    # compare_005_1.Result -> curve_of_point.Point Index
    colorpalette.links.new(compare_005_1.outputs[0], curve_of_point.inputs[0])
    # curve_of_point.Index in Curve -> math_006.Value
    colorpalette.links.new(curve_of_point.outputs[1], math_006.inputs[0])
    # group_input_011.Blackness -> random_value_013.Probability
    colorpalette.links.new(group_input_011.outputs[8], random_value_013.inputs[6])
    # random_value_013.Value -> math_006.Value
    colorpalette.links.new(random_value_013.outputs[3], math_006.inputs[1])
    # index.Index -> math_007.Value
    colorpalette.links.new(index.outputs[0], math_007.inputs[0])
    # math_007.Value -> math_008.Value
    colorpalette.links.new(math_007.outputs[0], math_008.inputs[0])
    # group_input_013.Speed -> math_008.Value
    colorpalette.links.new(group_input_013.outputs[6], math_008.inputs[1])
    # group_input_014.Speed -> random_value_013.Seed
    colorpalette.links.new(group_input_014.outputs[6], random_value_013.inputs[8])
    # math_005.Value -> random_value_012.Seed
    colorpalette.links.new(math_005.outputs[0], random_value_012.inputs[8])
    # switch_1.Output -> map_range_002.Vector
    colorpalette.links.new(switch_1.outputs[0], map_range_002.inputs[6])
    # switch_1.Output -> map_range.Vector
    colorpalette.links.new(switch_1.outputs[0], map_range.inputs[6])
    # switch_1.Output -> map_range_001.Vector
    colorpalette.links.new(switch_1.outputs[0], map_range_001.inputs[6])
    # group_input_015.Geometry -> attribute_statistic_1.Geometry
    colorpalette.links.new(group_input_015.outputs[0], attribute_statistic_1.inputs[0])
    # attribute_statistic_1.Max -> math_009.Value
    colorpalette.links.new(attribute_statistic_1.outputs[4], math_009.inputs[0])
    # math_009.Value -> compare_005_1.B
    colorpalette.links.new(math_009.outputs[0], compare_005_1.inputs[1])
    # math_008.Value -> attribute_statistic_1.Attribute
    colorpalette.links.new(math_008.outputs[0], attribute_statistic_1.inputs[2])
    # group_input_012.Blackness -> random_value_011.Probability
    colorpalette.links.new(group_input_012.outputs[8], random_value_011.inputs[6])
    # position.Position -> vector_math_003.Vector
    colorpalette.links.new(position.outputs[0], vector_math_003.inputs[0])
    # random_value_008.Value -> vector_math_003.Vector
    colorpalette.links.new(random_value_008.outputs[0], vector_math_003.inputs[1])
    # group_input_016.Seed -> random_value_008.Seed
    colorpalette.links.new(group_input_016.outputs[5], random_value_008.inputs[8])
    # group_input_002.Animation Type -> compare_006.A
    colorpalette.links.new(group_input_002.outputs[2], compare_006.inputs[8])
    # compare_006.Result -> switch_009.Switch
    colorpalette.links.new(compare_006.outputs[0], switch_009.inputs[0])
    # random_value_012.Value -> switch_009.True
    colorpalette.links.new(random_value_012.outputs[3], switch_009.inputs[2])
    # math_006.Value -> switch_009.False
    colorpalette.links.new(math_006.outputs[0], switch_009.inputs[1])
    # switch_009.Output -> vector_math_002.Scale
    colorpalette.links.new(switch_009.outputs[0], vector_math_002.inputs[3])
    # group_input_017.Colors -> compare_007.A
    colorpalette.links.new(group_input_017.outputs[3], compare_007.inputs[8])
    # compare_007.Result -> switch_011.Switch
    colorpalette.links.new(compare_007.outputs[0], switch_011.inputs[0])
    # compare_008.Result -> switch_010.Switch
    colorpalette.links.new(compare_008.outputs[0], switch_010.inputs[0])
    # image_texture.Color -> switch_010.True
    colorpalette.links.new(image_texture.outputs[0], switch_010.inputs[2])
    # group_input_006.Color 1 -> switch_011.True
    colorpalette.links.new(group_input_006.outputs[10], switch_011.inputs[2])
    # random_value_001.Value -> switch_011.False
    colorpalette.links.new(random_value_001.outputs[0], switch_011.inputs[1])
    # group_input_2.Seed -> math_1.Value
    colorpalette.links.new(group_input_2.outputs[5], math_1.inputs[0])
    # switch_010.Output -> vector_math_001.Vector
    colorpalette.links.new(switch_010.outputs[0], vector_math_001.inputs[0])
    # switch_010.Output -> vector_math_002.Vector
    colorpalette.links.new(switch_010.outputs[0], vector_math_002.inputs[0])
    # switch_001.Output -> switch_010.False
    colorpalette.links.new(switch_001.outputs[0], switch_010.inputs[1])
    # compare_007.Result -> switch_006.Switch
    colorpalette.links.new(compare_007.outputs[0], switch_006.inputs[0])
    # compare_007.Result -> switch_007.Switch
    colorpalette.links.new(compare_007.outputs[0], switch_007.inputs[0])
    # compare_007.Result -> switch_008.Switch
    colorpalette.links.new(compare_007.outputs[0], switch_008.inputs[0])
    # group_input_2.Seed -> math_001.Value
    colorpalette.links.new(group_input_2.outputs[5], math_001.inputs[0])
    # menu_switch.Output -> group_output_2.Color
    colorpalette.links.new(menu_switch.outputs[0], group_output_2.inputs[0])
    # group_input_018.Spline ID -> random_value_007.ID
    colorpalette.links.new(group_input_018.outputs[14], random_value_007.inputs[7])
    # group_input_019.Spline ID -> random_value_009.ID
    colorpalette.links.new(group_input_019.outputs[14], random_value_009.inputs[7])
    # group_input_020.Spline ID -> random_value_004.ID
    colorpalette.links.new(group_input_020.outputs[14], random_value_004.inputs[7])
    # group_input_021.Spline ID -> random_value_003.ID
    colorpalette.links.new(group_input_021.outputs[14], random_value_003.inputs[7])
    # group_input_022.Spline ID -> random_value_006.ID
    colorpalette.links.new(group_input_022.outputs[14], random_value_006.inputs[7])
    # group_input_023.Spline ID -> random_value_002.ID
    colorpalette.links.new(group_input_023.outputs[14], random_value_002.inputs[7])
    # group_input_024.Spline ID -> random_value_005.ID
    colorpalette.links.new(group_input_024.outputs[14], random_value_005.inputs[7])
    # group_input_025.Spline ID -> random_value_001.ID
    colorpalette.links.new(group_input_025.outputs[14], random_value_001.inputs[7])
    # group_input_026.Spline ID -> random_value_013.ID
    colorpalette.links.new(group_input_026.outputs[14], random_value_013.inputs[7])
    # group_input_027.Spline ID -> random_value_012.ID
    colorpalette.links.new(group_input_027.outputs[14], random_value_012.inputs[7])
    # group_input_028.Spline ID -> random_value_008.ID
    colorpalette.links.new(group_input_028.outputs[14], random_value_008.inputs[7])
    # group_input_015.Wave Motion -> reroute_2.Input
    colorpalette.links.new(group_input_015.outputs[4], reroute_2.inputs[0])
    # reroute_2.Output -> math_009.Value
    colorpalette.links.new(reroute_2.outputs[0], math_009.inputs[1])
    # group_input_017.Colors -> reroute_001_2.Input
    colorpalette.links.new(group_input_017.outputs[3], reroute_001_2.inputs[0])
    # reroute_001_2.Output -> reroute_002_2.Input
    colorpalette.links.new(reroute_001_2.outputs[0], reroute_002_2.inputs[0])
    # reroute_002_2.Output -> compare_008.A
    colorpalette.links.new(reroute_002_2.outputs[0], compare_008.inputs[8])
    # random_value.Value -> reroute_003_2.Input
    colorpalette.links.new(random_value.outputs[1], reroute_003_2.inputs[0])
    # reroute_003_2.Output -> reroute_004_2.Input
    colorpalette.links.new(reroute_003_2.outputs[0], reroute_004_2.inputs[0])
    # reroute_004_2.Output -> compare.A
    colorpalette.links.new(reroute_004_2.outputs[0], compare.inputs[0])
    # math_008.Value -> reroute_005_2.Input
    colorpalette.links.new(math_008.outputs[0], reroute_005_2.inputs[0])
    # reroute_005_2.Output -> compare_005_1.A
    colorpalette.links.new(reroute_005_2.outputs[0], compare_005_1.inputs[0])
    # boolean_math.Boolean -> reroute_006_2.Input
    colorpalette.links.new(boolean_math.outputs[0], reroute_006_2.inputs[0])
    # reroute_006_2.Output -> switch_002.Switch
    colorpalette.links.new(reroute_006_2.outputs[0], switch_002.inputs[0])
    # switch_006.Output -> reroute_007_1.Input
    colorpalette.links.new(switch_006.outputs[0], reroute_007_1.inputs[0])
    # reroute_007_1.Output -> switch_002.True
    colorpalette.links.new(reroute_007_1.outputs[0], switch_002.inputs[2])
    # switch_011.Output -> reroute_008_1.Input
    colorpalette.links.new(switch_011.outputs[0], reroute_008_1.inputs[0])
    # reroute_008_1.Output -> switch_001.True
    colorpalette.links.new(reroute_008_1.outputs[0], switch_001.inputs[2])
    # switch_1.Output -> reroute_009_1.Input
    colorpalette.links.new(switch_1.outputs[0], reroute_009_1.inputs[0])
    # reroute_009_1.Output -> reroute_010_1.Input
    colorpalette.links.new(reroute_009_1.outputs[0], reroute_010_1.inputs[0])
    # reroute_010_1.Output -> menu_switch.Constant
    colorpalette.links.new(reroute_010_1.outputs[0], menu_switch.inputs[1])
    # group_input_029.Spline ID -> random_value_011.ID
    colorpalette.links.new(group_input_029.outputs[14], random_value_011.inputs[7])
    # group_input_030.Spline ID -> random_value.ID
    colorpalette.links.new(group_input_030.outputs[14], random_value.inputs[7])
    # group_input_2.Seed -> reroute_011.Input
    colorpalette.links.new(group_input_2.outputs[5], reroute_011.inputs[0])
    # reroute_011.Output -> random_value.Seed
    colorpalette.links.new(reroute_011.outputs[0], random_value.inputs[8])
    color___distribution_socket.default_value = "Constant"
    return colorpalette
