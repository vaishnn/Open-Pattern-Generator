import bpy
from ..nodes import geonode, material

class StartOperator(bpy.types.Operator):
    
    bl_idname = "object.start_operator"
    bl_label = "Generate DreamScape"
    bl_description = "Generate Dreamscape to show the controls and other Properties"
    bl_options = {'REGISTER', 'UNDO'} #So that you can undo the operation.
    def execute(self, context):
        node_tree = geonode.creating_curves_node_group()
        node_tree_name = "Creating curves"
        bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        obj = context.object
        node_tree = bpy.data.node_groups.get(node_tree_name)
        modifier = obj.modifiers.get("GeometryNodes")
        if modifier is None:
            modifier = obj.modifiers.new(name="Creating curves", type='NODES')

        # Assign the node tree to the modifier
        if modifier.node_group is None or modifier.node_group.name != node_tree_name: # prevent assigning the same node tree multiple times.
            modifier.node_group = node_tree
            # Put your operation code here
            print("Operator executed!")  # Replace with your actual operation.
        obj.modifiers["Creating curves"]["Socket_11"] = material.neon_node_group()
        return {'FINISHED'}