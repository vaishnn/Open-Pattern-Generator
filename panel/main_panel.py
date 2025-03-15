import bpy
class Main(bpy.types.Panel):
    bl_idname = "OBJECT_PT_dreamscape"
    bl_label ="DreamScape Generator"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "DreamScape Generator"
    bl_context = "objectmode" 
    
    def draw(self, context):
        layout = self.layout
        layout.operator("object.start_operator", text = "Generate DreamScape")
        try:
            modifier = next((mod for mod in context.object.modifiers if mod.type == 'NODES' and mod.name == "Creating curves"), None)
        except AttributeError:
            modifier = False
        if not modifier:
            layout.label(text="Please Generate DreamScape")
