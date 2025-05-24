import bpy
from ..some_scripts.some_func import get_nodes


class SizeAndShape_SubPanel(bpy.types.Panel):
    bl_label = "Size and Shape"
    bl_space_type = "VIEW_3D"  # Correct space type
    bl_region_type = "UI"
    bl_category = "Pattern generator"  # Or your category
    bl_description = "To Control Size and Shape of the curves"
    bl_idname = "OBJECT_PT_sizeandshape_subpanel"
    bl_parent_id = "OBJECT_PT_pattern_generator"  # Important: Link to the main panel
    bl_options = {"DEFAULT_CLOSED"}  # Optional: Start closed

    @classmethod
    def poll(cls, context):
        """This method determines if the panel should be displayed."""
        obj = context.object
        if (
            obj is None or obj.type != "MESH"
        ):  # Check if an object is selected and if its type is MESH
            return False
        if context.object.outline is True:
            return False

        # Check for obj["node_tree_name"] Geometry Nodes modifier
        try:
            modifier = context.object.modifiers[context.object["node_tree_name"]]
        except Exception:
            modifier = None
        return modifier is not None  # Only show panel if modifier exists

    def draw(self, context):
        layout = self.layout
        layout.label(text="Change Size and Shape of Curves")
        layout.prop(context.object, "count_sizeandshape", text="Count")
        layout.prop(context.object, "size_x_sizeandshape", text="Size X")
        layout.prop(context.object, "size_y_sizeandshape", text="Size Y")
        layout.prop(context.object, "offset_sizeandshape", text="Offset")
        layout.prop(context.object, "seed_sizeandshape", text="Seed")
        layout.prop(context.object, "grain_sizeandshape", text="Grain")
        layout.prop(
            context.object, "rotation_random_sizeandshape", text="Rotation Random"
        )
        layout.prop(context.object, "rotation_sizeandshape", text="Rotation")


class Curves_SubPanel(bpy.types.Panel):
    bl_label = "Curves"
    bl_space_type = "VIEW_3D"  # Correct space type
    bl_region_type = "UI"
    bl_category = "Pattern generator"  # Or your category
    bl_description = "To Control Resolution of the curves, for artistic effect"
    bl_idname = "OBJECT_PT_curves_subpanel"
    bl_parent_id = "OBJECT_PT_pattern_generator"  # Important: Link to the main panel
    bl_options = {"DEFAULT_CLOSED"}  # Optional: Start closed

    @classmethod
    def poll(cls, context):
        """This method determines if the panel should be displayed."""
        obj = context.object
        if (
            obj is None or obj.type != "MESH"
        ):  # Check if an object is selected and if its type is MESH
            return False
        # Check for obj["node_tree_name"] Geometry Nodes modifier
        try:
            modifier = context.object.modifiers[context.object["node_tree_name"]]
        except Exception:
            modifier = None
        return modifier is not None  # Only show panel if modifier exists

    def draw(self, context):
        layout = self.layout
        layout.label(text="Change Resolution for Optimization and Stylish Look")
        layout.prop(
            context.object, "resolution_of_tubes_curves", text="Resolution of Tubes"
        )
        if (
            context.object.outline is True
            and context.object.both_outline_and_inside is False
        ):
            pass
        elif (
            context.object.outline is True
            and context.object.both_outline_and_inside is True
        ):
            layout.prop(
                context.object, "first_curve_segments_curves", text="1st Curve Segments"
            )
            layout.prop(
                context.object,
                "second_curve_segments_curves",
                text="2nd Curve Segements",
            )
        else:
            layout.prop(
                context.object, "first_curve_segments_curves", text="1st Curve Segments"
            )
            layout.prop(
                context.object,
                "second_curve_segments_curves",
                text="2nd Curve Segements",
            )
        layout.prop(context.object, "radius_of_tubes_curves", text="Radius of Tubes")


class CurveTrimming_SubPanel(bpy.types.Panel):
    bl_label = "Curve Trimming"
    bl_space_type = "VIEW_3D"  # Correct space type
    bl_region_type = "UI"
    bl_category = "Pattern generator"  # Or your category
    bl_description = "To Trim curves, for artistic effect"
    bl_idname = "OBJECT_PT_curvestrimming_subpanel"
    bl_parent_id = "OBJECT_PT_pattern_generator"  # Important: Link to the main panel
    bl_options = {"DEFAULT_CLOSED"}  # Optional: Start closed

    @classmethod
    def poll(cls, context):
        """This method determines if the panel should be displayed."""
        obj = context.object
        if (
            obj is None or obj.type != "MESH"
        ):  # Check if an object is selected and if its type is MESH
            return False

        # Check for obj["node_tree_name"] Geometry Nodes modifier
        try:
            modifier = context.object.modifiers[context.object["node_tree_name"]]
        except Exception:
            modifier = None
        return modifier is not None  # Only show panel if modifier exists

    def draw(self, context):
        layout = self.layout
        layout.label(text="To Trim Curves")
        layout.prop(
            context.object, "random_portion_curve_trimming", text="Random Portion"
        )
        layout.prop(
            context.object,
            "true_random_portion_curve_trimming",
            text="True Random Portion",
        )
        layout.prop(
            context.object, "every_section_curve_trimming", text="Every Section"
        )
        layout.prop(context.object, "seed_trimming_curve_trimming", text="Seed")
        layout.prop(
            context.object, "trim_portion_curve_trimming", text="Trim - Percentage"
        )
        layout.prop(context.object, "from_start_curve_trimming", text="From Start")
        layout.prop(context.object, "from_end_curve_trimming", text="From End")


class Merge_SubPanel(bpy.types.Panel):
    bl_label = "Merge"
    bl_space_type = "VIEW_3D"  # Correct space type
    bl_region_type = "UI"
    bl_category = "Pattern generator"  # Or your category
    bl_description = "To merge the curves, for artistic effect"
    bl_idname = "OBJECT_PT_merge_subpanel"
    bl_parent_id = "OBJECT_PT_pattern_generator"  # Important: Link to the main panel
    bl_options = {"DEFAULT_CLOSED"}  # Optional: Start closed

    @classmethod
    def poll(cls, context):
        """This method determines if the panel should be displayed."""
        obj = context.object
        if (
            obj is None or obj.type != "MESH"
        ):  # Check if an object is selected and if its type is MESH
            return False

        # Check for obj["node_tree_name"] Geometry Nodes modifier
        try:
            modifier = context.object.modifiers[context.object["node_tree_name"]]
        except Exception:
            modifier = None
        return modifier is not None  # Only show panel if modifier exists

    def draw(self, context):
        layout = self.layout
        layout.label(text="For Merging Curves After Trimming Gives Artistic Look")
        layout.prop(context.object, "merge_probability_merge", text="Merge Probability")
        layout.prop(context.object, "merge_seed_merge", text="Merge Seed")
        layout.prop(context.object, "merge_distance_merge", text="Merge Distance")


class CustomModel_SubPanel(bpy.types.Panel):
    bl_label = "Custom Model"
    bl_space_type = "VIEW_3D"  # Correct space type
    bl_region_type = "UI"
    bl_category = "Pattern generator"  # Or your category
    bl_description = (
        "To have string effect and logo effect of the curves, for artistic effect"
    )
    bl_idname = "OBJECT_PT_custommodel_subpanel"
    bl_parent_id = "OBJECT_PT_pattern_generator"  # Important: Link to the main panel
    bl_options = {"DEFAULT_CLOSED"}  # Optional: Start closed

    @classmethod
    def poll(cls, context):
        """This method determines if the panel should be displayed."""
        obj = context.object
        if (
            obj is None or obj.type != "MESH"
        ):  # Check if an object is selected and if its type is MESH
            return False

        # Check for obj["node_tree_name"] Geometry Nodes modifier
        try:
            modifier = context.object.modifiers[context.object["node_tree_name"]]
        except Exception:
            modifier = None
        return modifier is not None  # Only show panel if modifier exists

    def draw(self, context):
        layout = self.layout
        layout.label(text="All About Creating Something Custom")
        layout.prop(context.object, "mode_custom_model", text="Mode")
        if context.object.mode_custom_model == "String":
            layout.prop(context.object, "outline", text="Outline")
            layout.prop(context.object, "font", text="Font")
            if context.object.outline is True:
                layout.prop(
                    context.object,
                    "both_outline_and_inside",
                    text="Both Outline and Inside",
                )
                if context.object.both_outline_and_inside is False:
                    layout.prop(context.object, "string_custom_model", text="String")
                    layout.prop(
                        context.object,
                        "gap_between_characters_custom_model",
                        text="Gap Between Characters",
                    )
                else:
                    if context.object.subset_curves_custom_model is False:
                        layout.prop(
                            context.object, "method_custom_model", text="Method"
                        )
                    layout.prop(context.object, "string_custom_model", text="String")
                    layout.prop(
                        context.object,
                        "subset_curves_custom_model",
                        text="Subset Curves",
                    )
                    layout.prop(
                        context.object, "string_size_custom_model", text="String Size"
                    )
                    layout.prop(
                        context.object,
                        "gap_between_characters_custom_model",
                        text="Gap Between Characters",
                    )
                    layout.prop(context.object, "scale_custom_model", text="Scale")
            else:
                if context.object.subset_curves_custom_model is False:
                    layout.prop(context.object, "method_custom_model", text="Method")
                layout.prop(context.object, "string_custom_model", text="String")
                layout.prop(
                    context.object, "subset_curves_custom_model", text="Subset Curves"
                )
                layout.prop(
                    context.object, "string_size_custom_model", text="String Size"
                )
                layout.prop(
                    context.object,
                    "gap_between_characters_custom_model",
                    text="Gap Between Characters",
                )
                layout.prop(context.object, "scale_custom_model", text="Scale")
        if context.object.mode_custom_model == "Image":
            layout.prop(context.object, "outline", text="Outline")
            layout.prop(
                context.object,
                "both_outline_and_inside",
                text="Both Outline and Inside",
            )
            layout.prop(context.object, "image_custom_model", text="Image")
            if context.object.outline is True:
                if context.object.both_outline_and_inside is False:
                    layout.prop(
                        context.object,
                        "image_smoothness__subdivision__custom_model",
                        text="Image Smoothness (Subdivision)",
                    )
                    pass
                else:
                    if context.object.subset_curves_custom_model is False:
                        layout.prop(
                            context.object, "method_custom_model", text="Method"
                        )
                    layout.prop(
                        context.object,
                        "subset_curves_custom_model",
                        text="Subset Curves",
                    )
                    layout.prop(
                        context.object,
                        "image_smoothness__subdivision__custom_model",
                        text="Image Smoothness (Subdivision)",
                    )
                    layout.prop(context.object, "scale_custom_model", text="Scale")
            else:
                if context.object.subset_curves_custom_model is False:
                    layout.prop(context.object, "method_custom_model", text="Method")
                layout.prop(
                    context.object, "subset_curves_custom_model", text="Subset Curves"
                )
                layout.prop(
                    context.object,
                    "image_smoothness__subdivision__custom_model",
                    text="Image Smoothness (Subdivision)",
                )
                layout.prop(context.object, "scale_custom_model", text="Scale")


class baking_custom_SubPanel(bpy.types.Panel):
    bl_label = "Baking"
    bl_space_type = "VIEW_3D"  # Correct space type
    bl_region_type = "UI"
    bl_category = "Pattern generator"  # Or your category
    bl_description = "It bakes the shape and size and random portion and Custom Model for optimizing the workflow"
    bl_idname = "OBJECT_PT_baking_subpanel"
    bl_parent_id = "OBJECT_PT_pattern_generator"  # Important: Link to the main panel
    bl_options = {"DEFAULT_CLOSED"}  # Optional: Start closed

    @classmethod
    def poll(cls, context):
        """This method determines if the panel should be displayed."""
        obj = context.object
        if (
            obj is None or obj.type != "MESH"
        ):  # Check if an object is selected and if its type is MESH
            return False

        # Check for obj["node_tree_name"] Geometry Nodes modifier
        try:
            modifier = context.object.modifiers[context.object["node_tree_name"]]
        except Exception:
            modifier = None
        return modifier is not None  # Only show panel if modifier exists

    def draw(self, context):
        layout = self.layout
        obj = context.object
        if bpy.data.filepath:
            if not obj:
                layout.label(text="No active object")
                return

            bake_modifiers, _ = get_nodes(obj, "BAKE")

            if not bake_modifiers:
                layout.label(text="No Geometry Nodes modifiers with Bake nodes found.")
                return

            for md in bake_modifiers:
                box = layout.box()
                row = box.row()
                # row.label(text=md.name, icon='NODETREE')

                if not hasattr(md, "bake_directory"):
                    md.bake_directory = bpy.props.StringProperty(
                        name="Bake Directory", subtype="DIR_PATH", default=""
                    )

                row = box.row()

                row = box.row()
                row.label(text="Bake Path")
                row.prop(md, "bake_directory", text="")

                bake_node_amounts = len(md.bakes)

                for i in range(bake_node_amounts):
                    row = box.row(align=True)
                    label = "Pattern Bake"
                    row.label(text=label)
                    row.operator("object.ml_modifier_bake", text="Bake")
                    row.operator(
                        "object.ml_modifier_bake_delete_single", text="", icon="TRASH"
                    ).bake_id = i
        else:
            layout.label(text="Save the File First")


class color_SubPanel(bpy.types.Panel):
    bl_label = "Color"
    bl_space_type = "VIEW_3D"  # Correct space type
    bl_region_type = "UI"
    bl_category = "Pattern generator"  # Or your category
    bl_description = "To Control colors of the curves"
    bl_idname = "OBJECT_PT_color_subpanel"
    bl_parent_id = "OBJECT_PT_pattern_generator"  # Important: Link to the main panel
    bl_options = {"DEFAULT_CLOSED"}  # Optional: Start closed

    @classmethod
    def poll(cls, context):
        """This method determines if the panel should be displayed."""
        obj = context.object
        if (
            obj is None or obj.type != "MESH"
        ):  # Check if an object is selected and if its type is MESH
            return False

        # Check for obj["node_tree_name"] Geometry Nodes modifier
        try:
            modifier = context.object.modifiers[context.object["node_tree_name"]]
        except Exception:
            modifier = None
        return modifier is not None  # Only show panel if modifier exists

    def draw(self, context):
        layout = self.layout
        layout.label(text="All Abouts Colors")
        layout.prop(context.object, "emission_stenght_color", text="Emission Stenght")
        layout.prop(context.object, "color_color", text="Color")
        if context.object.color_color == "Random":
            layout.prop(context.object, "seed___colors_color", text="Seed")
        elif context.object.color_color == "Custom":
            layout.prop(context.object, "color_1_color", text="Color 1")
            layout.prop(context.object, "color_2_color", text="Color 2")
            layout.prop(context.object, "color_3_color", text="Color 3")
            layout.prop(context.object, "color_4_color", text="Color 4")
            layout.prop(context.object, "seed___colors_color", text="Seed")
        elif context.object.color_color == "Image":
            layout.prop(context.object, "image_color", text="Image")
            layout.prop(context.object, "seed___colors_color", text="Seed")
        layout.prop(context.object, "animate_color", text="Animate")
        if context.object.animate_color is True:
            layout.prop(context.object, "animation_type_color", text="Animation Type")
            if context.object.animation_type_color == "Wave":
                layout.prop(context.object, "wave_motion_color", text="Wave Motion")
                layout.prop(context.object, "gradient_color", text="Gradient")
            elif context.object.animation_type_color == "Random":
                layout.prop(context.object, "speed_color", text="Speed")
                layout.prop(context.object, "gradient_color", text="Gradient")
        else:
            layout.prop(context.object, "gradient_color", text="Gradient")


class AsProp_SubPanel(bpy.types.Panel):
    bl_label = "As Hangable Prop"
    bl_space_type = "VIEW_3D"  # Correct space type
    bl_region_type = "UI"
    bl_category = "Pattern generator"  # Or your category
    bl_description = "To have hanging cylinders in the back of the curves"
    bl_idname = "OBJECT_PT_asprop_subpanel"
    bl_parent_id = "OBJECT_PT_pattern_generator"  # Important: Link to the main panel
    bl_options = {"DEFAULT_CLOSED"}  # Optional: Start closed

    @classmethod
    def poll(cls, context):
        """This method determines if the panel should be displayed."""
        obj = context.object
        if (
            obj is None or obj.type != "MESH"
        ):  # Check if an object is selected and if its type is MESH
            return False

        # Check for obj["node_tree_name"] Geometry Nodes modifier
        try:
            modifier = context.object.modifiers[context.object["node_tree_name"]]
        except Exception:
            modifier = None
        return modifier is not None  # Only show panel if modifier exists

    def draw(self, context):
        layout = self.layout
        layout.label(text="Using it as a Prop in an Atmosphere")
        layout.prop(context.object, "prop_as_prop", text="Prop")
        if context.object.prop_as_prop is True:
            layout.prop(context.object, "seed_as_prop", text="Seed")
            layout.prop(
                context.object, "material__hangers__as_prop", text="Material (Hangers)"
            )
            layout.prop(context.object, "distance_as_prop", text="Distance")
            layout.prop(
                context.object, "radius__comparing__as_prop", text="Radius (Comparing)"
            )
            layout.prop(
                context.object, "have_back_plate_as_prop", text="Have Back Plate"
            )
            if context.object.have_back_plate_as_prop is True:
                layout.prop(
                    context.object,
                    "material__back_plate__as_prop",
                    text="Material (Back Plate)",
                )
