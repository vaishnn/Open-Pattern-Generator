import bpy
class SizeAndShape_SubPanel(bpy.types.Panel):
    bl_label = "Size and Shape"
    bl_space_type = 'VIEW_3D'  # Correct space type
    bl_region_type = 'UI'
    bl_category = "DreamScape Generator" # Or your category
    bl_description = "To Control Size and Shape of the curves"
    bl_idname = "OBJECT_PT_sizeandshape_subpanel"
    bl_parent_id = "OBJECT_PT_dreamscape" # Important: Link to the main panel
    bl_options = {'DEFAULT_CLOSED'} # Optional: Start closed

    @classmethod
    def poll(cls, context):
        """This method determines if the panel should be displayed."""
        obj = context.object
        if obj is None or obj.type != 'MESH':  # Check if an object is selected and if its type is MESH
            return False

        # Check for "Creating curves" Geometry Nodes modifier
        modifier = next((mod for mod in obj.modifiers if mod.type == 'NODES' and mod.name == "Creating curves"), None)
        return modifier is not None  # Only show panel if modifier exists
    
    def draw(self, context):
        try:
            modifier = next((mod for mod in context.object.modifiers if mod.type == 'NODES' and mod.name == "Creating curves"), None)
        except AttributeError:
            modifier = False
        if modifier:
            layout = self.layout
            layout.label(text="Change Size and Shape of Curves")
            layout.prop(context.object, "count_sizeandshape", text="Count")
            layout.prop(context.object, "size_sizeandshape", text = "Size")
            layout.prop(context.object, "offset_sizeandshape", text = "Offset")
            layout.prop(context.object, "seed_sizeandshape", text = "Seed")
            layout.prop(context.object, "grain_sizeandshape", text = "Grain")

class Curves_SubPanel(bpy.types.Panel):
    bl_label = "Curves"
    bl_space_type = 'VIEW_3D'  # Correct space type
    bl_region_type = 'UI'
    bl_category = "DreamScape Generator" # Or your category
    bl_description = "To Control Resolution of the curves, for artistic effect"
    bl_idname = "OBJECT_PT_curves_subpanel"
    bl_parent_id = "OBJECT_PT_dreamscape" # Important: Link to the main panel
    bl_options = {'DEFAULT_CLOSED'} # Optional: Start closed

    @classmethod
    def poll(cls, context):
        """This method determines if the panel should be displayed."""
        obj = context.object
        if obj is None or obj.type != 'MESH':  # Check if an object is selected and if its type is MESH
            return False

        # Check for "Creating curves" Geometry Nodes modifier
        modifier = next((mod for mod in obj.modifiers if mod.type == 'NODES' and mod.name == "Creating curves"), None)
        return modifier is not None  # Only show panel if modifier exists
    
    def draw(self, context):
        try:
            modifier = next((mod for mod in context.object.modifiers if mod.type == 'NODES' and mod.name == "Creating curves"), None)
        except AttributeError:
            modifier = False
        if modifier:
            layout = self.layout
            layout.label(text="Change Resolution for Optimization and Stylish Look")
            layout.prop(context.object, "resolution_of_curves_curves", text="Resolution of Curves")
            layout.prop(context.object, "resolution_of_tubes_curves", text="Resolution of Tubes")
            layout.prop(context.object, "first_curve_segments_curves", text="1st Curve Segments")
            layout.prop(context.object, "second_curve_segments_curves", text="2nd Curve Segements")
            layout.prop(context.object, "radius_of_tubes_curves", text="Radius of Tubes")