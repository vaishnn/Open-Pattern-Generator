import bpy
from ..some_scripts.some_func import get_nodes


def update_count_sizeandshape(self, context):
    value = self.count_sizeandshape
    context.object.modifiers[context.object["node_tree_name"]]["Socket_2"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_size_x_sizeandshape(self, context):
    value = self.size_x_sizeandshape
    context.object.modifiers[context.object["node_tree_name"]]["Socket_3"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_size_y_sizeandshape(self, context):
    value = self.size_y_sizeandshape
    context.object.modifiers[context.object["node_tree_name"]]["Socket_4"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_offset_sizeandshape(self, context):
    value = self.offset_sizeandshape
    context.object.modifiers[context.object["node_tree_name"]]["Socket_5"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_seed_sizeandshape(self, context):
    value = self.seed_sizeandshape
    context.object.modifiers[context.object["node_tree_name"]]["Socket_6"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_grain_sizeandshape(self, context):
    value = self.grain_sizeandshape
    context.object.modifiers[context.object["node_tree_name"]]["Socket_7"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_rotation_random_sizeandshape(self, context):
    value = self.rotation_random_sizeandshape
    context.object.modifiers[context.object["node_tree_name"]]["Socket_8"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_rotation_sizeandshape(self, context):
    value = self.rotation_sizeandshape
    context.object.modifiers[context.object["node_tree_name"]]["Socket_9"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_resolution_of_tubes_curves(self, context):
    value = self.resolution_of_tubes_curves
    context.object.modifiers[context.object["node_tree_name"]]["Socket_11"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_1st_curve_segments_curves(self, context):
    value = self.first_curve_segments_curves
    context.object.modifiers[context.object["node_tree_name"]]["Socket_12"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_2nd_curve_segments_curves(self, context):
    value = self.second_curve_segments_curves
    context.object.modifiers[context.object["node_tree_name"]]["Socket_13"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_radius_of_tubes_curves(self, context):
    value = self.radius_of_tubes_curves
    context.object.modifiers[context.object["node_tree_name"]]["Socket_14"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_random_portion_curve_trimming(self, context):
    value = self.random_portion_curve_trimming
    context.object.modifiers[context.object["node_tree_name"]]["Socket_16"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_true_random_portion_curve_trimming(self, context):
    value = self.true_random_portion_curve_trimming
    context.object.modifiers[context.object["node_tree_name"]]["Socket_17"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_every_section_curve_trimming(self, context):
    value = self.every_section_curve_trimming
    context.object.modifiers[context.object["node_tree_name"]]["Socket_18"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_seed_trimming_curve_trimming(self, context):
    value = self.seed_trimming_curve_trimming
    context.object.modifiers[context.object["node_tree_name"]]["Socket_19"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_trim_portion_curve_trimming(self, context):
    value = self.trim_portion_curve_trimming
    context.object.modifiers[context.object["node_tree_name"]]["Socket_20"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_from_start_curve_trimming(self, context):
    value = self.from_start_curve_trimming
    context.object.modifiers[context.object["node_tree_name"]]["Socket_21"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_from_end_curve_trimming(self, context):
    value = self.from_end_curve_trimming
    context.object.modifiers[context.object["node_tree_name"]]["Socket_22"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_merge_probability_merge(self, context):
    value = self.merge_probability_merge
    context.object.modifiers[context.object["node_tree_name"]]["Socket_24"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_merge_seed_merge(self, context):
    value = self.merge_seed_merge
    context.object.modifiers[context.object["node_tree_name"]]["Socket_25"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_merge_distance_merge(self, context):
    value = self.merge_distance_merge
    context.object.modifiers[context.object["node_tree_name"]]["Socket_26"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_mode_custom_model(self, context):
    value = self.mode_custom_model
    context.object.modifiers[context.object["node_tree_name"]]["Socket_28"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_method_custom_model(self, context):
    value = self.method_custom_model
    context.object.modifiers[context.object["node_tree_name"]]["Socket_29"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_string_custom_model(self, context):
    value = self.string_custom_model
    context.object.modifiers[context.object["node_tree_name"]]["Socket_30"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_string_size_custom_model(self, context):
    value = self.string_size_custom_model
    context.object.modifiers[context.object["node_tree_name"]]["Socket_31"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_gap_between_characters_custom_model(self, context):
    value = self.gap_between_characters_custom_model
    context.object.modifiers[context.object["node_tree_name"]]["Socket_32"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_scale_custom_model(self, context):
    value = self.scale_custom_model
    context.object.modifiers[context.object["node_tree_name"]]["Socket_33"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_image_custom_model(self, context):
    value = self.image_custom_model
    context.object.modifiers[context.object["node_tree_name"]]["Socket_34"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_image_smoothness__subdivision__custom_model(self, context):
    value = self.image_smoothness__subdivision__custom_model
    context.object.modifiers[context.object["node_tree_name"]]["Socket_35"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_subset_curves_custom_model(self, context):
    value = self.subset_curves_custom_model
    if value is True:
        context.object.modifiers[context.object["node_tree_name"]]["Socket_29"] = (
            "Method 2"
        )
    context.object.modifiers[context.object["node_tree_name"]]["Socket_62"] = value
    bpy.context.view_layer.update()


def update_emission_stenght_color(self, context):
    value = self.emission_stenght_color
    context.object.modifiers[context.object["node_tree_name"]]["Socket_38"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_color_color(self, context):
    value = self.color_color
    context.object.modifiers[context.object["node_tree_name"]]["Socket_42"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_seed___colors_color(self, context):
    value = self.seed___colors_color
    context.object.modifiers[context.object["node_tree_name"]]["Socket_44"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_color_1_color(self, context):
    value = self.color_1_color
    context.object.modifiers[context.object["node_tree_name"]]["Socket_49"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_color_2_color(self, context):
    value = self.color_2_color
    context.object.modifiers[context.object["node_tree_name"]]["Socket_50"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_color_3_color(self, context):
    value = self.color_3_color
    context.object.modifiers[context.object["node_tree_name"]]["Socket_51"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_color_4_color(self, context):
    value = self.color_4_color
    context.object.modifiers[context.object["node_tree_name"]]["Socket_52"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_image_color(self, context):
    value = self.image_color
    context.object.modifiers[context.object["node_tree_name"]]["Socket_48"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_animate_color(self, context):
    value = self.animate_color
    if value is False:
        context.object.modifiers[context.object["node_tree_name"]]["Socket_43"] = 1000
    context.object.modifiers[context.object["node_tree_name"]]["Socket_40"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_animation_type_color(self, context):
    value = self.animation_type_color
    if value == "Random":
        context.object.modifiers[context.object["node_tree_name"]]["Socket_43"] = 1000
    context.object.modifiers[context.object["node_tree_name"]]["Socket_41"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_wave_motion_color(self, context):
    value = self.wave_motion_color
    context.object.modifiers[context.object["node_tree_name"]]["Socket_43"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_speed_color(self, context):
    value = self.speed_color
    context.object.modifiers[context.object["node_tree_name"]]["Socket_45"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_gradient_color(self, context):
    value = self.gradient_color
    context.object.modifiers[context.object["node_tree_name"]]["Socket_47"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_prop_as_prop(self, context):
    value = self.prop_as_prop
    context.object.modifiers[context.object["node_tree_name"]]["Socket_54"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_seed_as_prop(self, context):
    value = self.seed_as_prop
    context.object.modifiers[context.object["node_tree_name"]]["Socket_55"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_material__hangers__as_prop(self, context):
    value = self.material__hangers__as_prop
    context.object.modifiers[context.object["node_tree_name"]]["Socket_56"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_distance_as_prop(self, context):
    value = self.distance_as_prop
    context.object.modifiers[context.object["node_tree_name"]]["Socket_57"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_radius__comparing__as_prop(self, context):
    value = self.radius__comparing__as_prop
    context.object.modifiers[context.object["node_tree_name"]]["Socket_58"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_have_back_plate_as_prop(self, context):
    value = self.have_back_plate_as_prop
    context.object.modifiers[context.object["node_tree_name"]]["Socket_59"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_material__back_plate__as_prop(self, context):
    value = self.material__back_plate__as_prop
    context.object.modifiers[context.object["node_tree_name"]]["Socket_60"] = value
    bpy.context.view_layer.update()  # Redraw viewport if necessary


def update_outline(self, context):
    value = self.outline
    if value is False:
        context.object.modifiers[context.object["node_tree_name"]]["Socket_64"] = False
    context.object.modifiers[context.object["node_tree_name"]]["Socket_63"] = value
    bpy.context.view_layer.update()


def update_both_outline_and_inside(self, context):
    value = self.both_outline_and_inside
    context.object.modifiers[context.object["node_tree_name"]]["Socket_64"] = value
    bpy.context.view_layer.update()


def update_font(self, context):
    value = self.font
    ob = context.object
    _, nodes = get_nodes(ob, "STRING_TO_CURVES")
    print(nodes)
    nodes.font = bpy.data.fonts.load(value)
