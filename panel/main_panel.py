import bpy


class Main(bpy.types.Panel):
    bl_idname = "OBJECT_PT_pattern_generator"
    bl_label = "Pattern Generator"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Pattern Generator"
    bl_context = "objectmode"

    def draw(self, context):
        layout = self.layout
        layout.operator(
            "object.start_pattern_generator_operator", text="Generate Pattern"
        )
        try:
            modifier = context.object.modifiers[context.object["node_tree_name"]]
        except Exception:
            modifier = False
        if not modifier:
            layout.label(text="Please Generate Pattern")
