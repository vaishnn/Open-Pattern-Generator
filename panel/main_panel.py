import bpy
class Main(bpy.types.Panel):
    bl_idname = "OBJECT_PT_open_pattern_generator"
    bl_label ="Open Pattern Generator"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Open Pattern Generator"
    bl_context = "objectmode" 
    
    def draw(self, context):
        layout = self.layout
        layout.operator("object.start_open_pattern_generator_operator", text = "Generate Pattern")
        try:
            modifier = next((mod for mod in context.object.modifiers if mod.type == 'NODES' and mod.name == "Creating curves"), None)
        except AttributeError:
            modifier = False
        if not modifier:
            layout.label(text="Please Generate Pattern")
