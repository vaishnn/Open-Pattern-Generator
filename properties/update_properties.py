import bpy
from .update_properties_func import (
    update_1st_curve_segments_curves,
    update_2nd_curve_segments_curves,
    update_animate_color,
    update_animation_type_color,
    update_both_outline_and_inside,
    update_color_1_color,
    update_color_2_color,
    update_color_3_color,
    update_color_4_color,
    update_color_color,
    update_count_sizeandshape,
    update_distance_as_prop,
    update_emission_stenght_color,
    update_every_section_curve_trimming,
    update_from_end_curve_trimming,
    update_from_start_curve_trimming,
    update_gap_between_characters_custom_model,
    update_grain_sizeandshape,
    update_gradient_color,
    update_have_back_plate_as_prop,
    update_image_color,
    update_image_custom_model,
    update_image_smoothness__subdivision__custom_model,
    update_material__back_plate__as_prop,
    update_material__hangers__as_prop,
    update_merge_distance_merge,
    update_merge_probability_merge,
    update_merge_seed_merge,
    update_method_custom_model,
    update_mode_custom_model,
    update_offset_sizeandshape,
    update_outline,
    update_prop_as_prop,
    update_radius__comparing__as_prop,
    update_radius_of_tubes_curves,
    update_random_portion_curve_trimming,
    update_resolution_of_tubes_curves,
    update_rotation_random_sizeandshape,
    update_rotation_sizeandshape,
    update_scale_custom_model,
    update_seed___colors_color,
    update_seed_as_prop,
    update_seed_sizeandshape,
    update_seed_trimming_curve_trimming,
    update_size_x_sizeandshape,
    update_size_y_sizeandshape,
    update_speed_color,
    update_string_custom_model,
    update_string_size_custom_model,
    update_subset_curves_custom_model,
    update_trim_portion_curve_trimming,
    update_true_random_portion_curve_trimming,
    update_wave_motion_color,
    update_font,
)


def property_update():
    bpy.types.Object.count_sizeandshape = bpy.props.IntProperty(
        name="Count",
        update=update_count_sizeandshape,  # Assign the update function
        default=15,
        min=1,
        max=1000,
    )
    bpy.types.Object.size_x_sizeandshape = bpy.props.IntProperty(
        name="Size X",
        update=update_size_x_sizeandshape,  # Assign the update function
        default=5,
        min=1,
        max=1000,
    )
    bpy.types.Object.size_y_sizeandshape = bpy.props.IntProperty(
        name="Size Y",
        update=update_size_y_sizeandshape,  # Assign the update function
        default=5,
        min=1,
        max=1000,
    )
    bpy.types.Object.offset_sizeandshape = bpy.props.FloatProperty(
        name="Offset",
        update=update_offset_sizeandshape,  # Assign the update function
        default=0.83,
        min=0.5,
        max=1,
    )
    bpy.types.Object.seed_sizeandshape = bpy.props.IntProperty(
        name="Seed",
        update=update_seed_sizeandshape,  # Assign the update function
        default=0,
        min=-1000,
        max=1000,
    )
    bpy.types.Object.grain_sizeandshape = bpy.props.FloatProperty(
        name="Grain",
        update=update_grain_sizeandshape,  # Assign the update function
        default=0.98,
        min=0,
        max=1,
    )
    bpy.types.Object.rotation_random_sizeandshape = bpy.props.BoolProperty(
        name="Random Rotation",
        default=True,
        update=update_rotation_random_sizeandshape,  # Assign the update function
    )
    bpy.types.Object.rotation_sizeandshape = bpy.props.IntProperty(
        name="Rotation",
        update=update_rotation_sizeandshape,  # Assign the update function
        default=0,
        min=0,
        max=3,
    )
    bpy.types.Object.resolution_of_tubes_curves = bpy.props.IntProperty(
        name="Resolution of Tubes",
        update=update_resolution_of_tubes_curves,  # Assign the update function
        default=16,
        min=2,
        max=512,
    )
    bpy.types.Object.first_curve_segments_curves = bpy.props.IntProperty(
        name="1st Curve Segments",
        update=update_1st_curve_segments_curves,  # Assign the update function
        default=10,
        min=2,
        max=512,
    )
    bpy.types.Object.second_curve_segments_curves = bpy.props.IntProperty(
        name="2nd Curve Segements",
        update=update_2nd_curve_segments_curves,  # Assign the update function
        default=10,
        min=2,
        max=512,
    )
    bpy.types.Object.radius_of_tubes_curves = bpy.props.FloatProperty(
        name="Radius of Tubes",
        update=update_radius_of_tubes_curves,  # Assign the update function
        min=0.0001,
        max=100,
        default=0.01,
    )
    bpy.types.Object.random_portion_curve_trimming = bpy.props.BoolProperty(
        name="Random Portion",
        default=True,
        update=update_random_portion_curve_trimming,  # Assign the update function
    )
    bpy.types.Object.true_random_portion_curve_trimming = bpy.props.BoolProperty(
        name="True Random Portion",
        default=False,
        update=update_true_random_portion_curve_trimming,  # Assign the update function
    )
    bpy.types.Object.every_section_curve_trimming = bpy.props.BoolProperty(
        name="Every Section",
        default=False,
        update=update_every_section_curve_trimming,  # Assign the update function
    )
    bpy.types.Object.seed_trimming_curve_trimming = bpy.props.IntProperty(
        name="Seed",
        update=update_seed_trimming_curve_trimming,  # Assign the update function
        default=0,
        min=-1000,
        max=1000,
    )
    bpy.types.Object.trim_portion_curve_trimming = bpy.props.FloatProperty(
        name="Trim - Percentage",
        update=update_trim_portion_curve_trimming,  # Assign the update function
        default=0.5,
        min=0,
        max=1,
    )
    bpy.types.Object.from_start_curve_trimming = bpy.props.FloatProperty(
        name="From Start",
        update=update_from_start_curve_trimming,  # Assign the update function
        default=0,
        min=0,
        max=1,
    )
    bpy.types.Object.from_end_curve_trimming = bpy.props.FloatProperty(
        name="From End",
        update=update_from_end_curve_trimming,  # Assign the update function
        default=1,
        min=0,
        max=1,
    )
    bpy.types.Object.merge_probability_merge = bpy.props.FloatProperty(
        name="Merge Probability",
        update=update_merge_probability_merge,  # Assign the update function
        default=0.0,
        min=0,
        max=1,
    )
    bpy.types.Object.merge_seed_merge = bpy.props.IntProperty(
        name="Merge Seed",
        update=update_merge_seed_merge,  # Assign the update function
        default=0,
        min=-1000,
        max=1000,
    )
    bpy.types.Object.merge_distance_merge = bpy.props.FloatProperty(
        name="Merge Distance",
        update=update_merge_distance_merge,  # Assign the update function
        default=0.0,
        min=0,
        max=10000,
    )
    bpy.types.Object.mode_custom_model = bpy.props.EnumProperty(
        name="Mode",
        items=[
            ("String", "String", "For Forming String Out of No-where"),
            ("Image", "Image", "For Creating image out of no where"),
            ("None", "None", "For Base"),
        ],
        update=update_mode_custom_model,  # Assign the update function
        default="None",
    )
    bpy.types.Object.method_custom_model = bpy.props.EnumProperty(
        name="Method",
        items=[
            ("Method 1", "Method 1", "For Dissolving"),
            ("Method 2", "Method 2", "For Revealing"),
        ],
        update=update_method_custom_model,  # Assign the update function
        default="Method 2",
    )
    bpy.types.Object.string_custom_model = bpy.props.StringProperty(
        name="String",
        update=update_string_custom_model,  # Assign the update function
        default="",
    )
    bpy.types.Object.string_size_custom_model = bpy.props.FloatProperty(
        name="String Size",
        update=update_string_size_custom_model,  # Assign the update function
        default=2,
        min=0,
        max=100,
    )
    bpy.types.Object.gap_between_characters_custom_model = bpy.props.FloatProperty(
        name="Gap Between Characters",
        update=update_gap_between_characters_custom_model,  # Assign the update function
        default=0,
        min=0,
        max=100,
    )
    bpy.types.Object.scale_custom_model = bpy.props.FloatProperty(
        name="Scale",
        update=update_scale_custom_model,  # Assign the update function
        default=1,
        min=0,
        max=100,
    )
    bpy.types.Object.subset_curves_custom_model = bpy.props.BoolProperty(
        name="Subset Curves", update=update_subset_curves_custom_model, default=False
    )
    bpy.types.Object.image_custom_model = bpy.props.PointerProperty(
        type=bpy.types.Image,
        name="Image",
        update=update_image_custom_model,  # Assign the update function
    )
    bpy.types.Object.image_smoothness__subdivision__custom_model = bpy.props.IntProperty(
        name="Image Smoothness (Subdivision)",
        update=update_image_smoothness__subdivision__custom_model,  # Assign the update function
        default=4,
        min=0,
        max=64,
    )
    bpy.types.Object.emission_stenght_color = bpy.props.FloatProperty(
        name="Emission Stenght",
        update=update_emission_stenght_color,  # Assign the update function
        default=1.0,
        min=0,
        max=1000,
    )
    bpy.types.Object.color_color = bpy.props.EnumProperty(
        name="Color",
        items=[
            ("Random", "Random", "For Random Colors"),
            ("Custom", "Custom", "For Custom Colors"),
            ("Image", "Image", "For Image Colors"),
        ],
        update=update_color_color,  # Assign the update function
        default="Random",
    )
    bpy.types.Object.seed___colors_color = bpy.props.IntProperty(
        name="Seed",
        update=update_seed___colors_color,  # Assign the update function
        default=0,
        min=-1000,
        max=1000,
    )
    bpy.types.Object.color_1_color = bpy.props.FloatVectorProperty(
        subtype="COLOR",
        name="Color 1",
        update=update_color_1_color,  # Assign the update function
        default=(0.0, 0.0, 0.0, 1.0),
        size=4,  # Size 4 for RGBA
        min=0.0,
        max=1.0,
    )
    bpy.types.Object.color_2_color = bpy.props.FloatVectorProperty(
        subtype="COLOR",
        name="Color 2",
        update=update_color_2_color,  # Assign the update function
        default=(0.0, 0.0, 0.0, 1.0),
        size=4,  # Size 4 for RGBA
        min=0.0,
        max=1.0,
    )
    bpy.types.Object.color_3_color = bpy.props.FloatVectorProperty(
        subtype="COLOR",
        name="Color 3",
        update=update_color_3_color,  # Assign the update function
        default=(0.0, 0.0, 0.0, 1.0),
        size=4,  # Size 4 for RGBA
        min=0.0,
        max=1.0,
    )
    bpy.types.Object.color_4_color = bpy.props.FloatVectorProperty(
        subtype="COLOR",
        name="Color 4",
        update=update_color_4_color,  # Assign the update function
        default=(0.0, 0.0, 0.0, 1.0),
        size=4,  # Size 4 for RGBA
        min=0.0,
        max=1.0,
    )
    bpy.types.Object.image_color = bpy.props.PointerProperty(
        type=bpy.types.Image,
        name="Image",
        update=update_image_color,  # Assign the update function
    )
    bpy.types.Object.animate_color = bpy.props.BoolProperty(
        name="Animate",
        default=False,
        update=update_animate_color,  # Assign the update function
    )
    bpy.types.Object.animation_type_color = bpy.props.EnumProperty(
        name="Animation Type",
        items=[
            ("Wave", "Wave", "For Wave Animation"),
            ("Random", "Random", "For Random Animation"),
        ],
        update=update_animation_type_color,  # Assign the update function
        default="Wave",
    )
    bpy.types.Object.wave_motion_color = bpy.props.FloatProperty(
        name="Wave Motion",
        update=update_wave_motion_color,  # Assign the update function
        default=1000.0,
        min=0.0,
        max=1000,
    )
    bpy.types.Object.speed_color = bpy.props.FloatProperty(
        name="Speed",
        update=update_speed_color,  # Assign the update function
        default=2.0,
        min=0.0,
        max=1000.0,
    )
    bpy.types.Object.gradient_color = bpy.props.FloatProperty(
        name="Gradient",
        update=update_gradient_color,  # Assign the update function
        default=1.0,
        min=0.0,
        max=1.0,
    )
    bpy.types.Object.prop_as_prop = bpy.props.BoolProperty(
        name="Prop",
        default=False,
        update=update_prop_as_prop,  # Assign the update function
    )
    bpy.types.Object.seed_as_prop = bpy.props.IntProperty(
        name="Seed",
        update=update_seed_as_prop,  # Assign the update function
        default=0,
        min=-1000,
        max=1000,
    )
    bpy.types.Object.material__hangers__as_prop = bpy.props.PointerProperty(
        type=bpy.types.Material,
        name="Material (Hangers)",
        update=update_material__hangers__as_prop,  # Assign the update function
    )
    bpy.types.Object.distance_as_prop = bpy.props.FloatProperty(
        name="Distance",
        update=update_distance_as_prop,  # Assign the update function
        default=0.0,
        min=0.0,
        max=1000.0,
    )
    bpy.types.Object.radius__comparing__as_prop = bpy.props.FloatProperty(
        name="Radius (Comparing)",
        update=update_radius__comparing__as_prop,  # Assign the update function
        default=50.0,
        min=0.0,
        max=100.0,
    )
    bpy.types.Object.have_back_plate_as_prop = bpy.props.BoolProperty(
        name="Have Back Plate",
        default=False,
        update=update_have_back_plate_as_prop,  # Assign the update function
    )
    bpy.types.Object.material__back_plate__as_prop = bpy.props.PointerProperty(
        type=bpy.types.Material,
        name="Material (Back Plate)",
        update=update_material__back_plate__as_prop,  # Assign the update function
    )
    bpy.types.Object.outline = bpy.props.BoolProperty(
        name="Outline", default=False, update=update_outline
    )
    bpy.types.Object.both_outline_and_inside = bpy.props.BoolProperty(
        name="Both Outline and Inside",
        default=False,
        update=update_both_outline_and_inside,
    )
    bpy.types.Object.font = bpy.props.StringProperty(
        name="Font",
        description="Select a font",
        subtype="FILE_PATH",
        update=update_font,
    )
