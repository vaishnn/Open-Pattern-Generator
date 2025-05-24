import bpy
from .nodes import material, geonode


class StartOperator(bpy.types.Operator):
    bl_idname = "object.start_pattern_generator_operator"
    bl_label = "Generate Pattern"
    bl_description = "Generate Dreamscape to show the controls and other Properties"
    bl_options = {"REGISTER", "UNDO"}  # So that you can undo the operation.

    def execute(self, context):
        node_tree, node_tree_name = geonode.creating_curves_node_group()
        print(node_tree_name)
        bpy.ops.mesh.primitive_plane_add(
            size=2,
            enter_editmode=False,
            align="WORLD",
            location=(0, 0, 0),
            scale=(1, 1, 1),
        )
        obj = context.object
        obj["node_tree_name"] = node_tree_name
        node_tree = bpy.data.node_groups.get(node_tree_name)
        modifier = obj.modifiers.get("GeometryNodes")
        if modifier is None:
            modifier = obj.modifiers.new(name=node_tree_name, type="NODES")

        # Assign the node tree to the modifier
        if (
            modifier.node_group is None or modifier.node_group.name != node_tree_name
        ):  # prevent assigning the same node tree multiple times.
            modifier.node_group = node_tree
            # Put your operation code here
            print("Operator executed!")  # Replace with your actual operation.
        obj.modifiers[node_tree_name]["Socket_37"] = material.neon_node_group()
        return {"FINISHED"}


class OBJECT_OT_GeometryNodeBake(bpy.types.Operator):
    """Bakes a specific bake node within a Geometry Nodes modifier"""

    bl_idname = "object.ml_modifier_bake"
    bl_label = "Bake Modifier"
    bl_options = {"REGISTER", "UNDO"}

    bake_id: bpy.props.IntProperty(name="Bake_ID", default=0)  # type: ignore

    def execute(self, context):
        ob = context.active_object
        if not ob:
            return False

        md = ob.modifiers[ob["node_tree_name"]]

        if bpy.data.is_saved:
            try:
                with context.temp_override(id=ob):
                    bpy.ops.object.geometry_node_bake_single(
                        session_uid=int(md.id_data.session_uid),
                        modifier_name=str(md.name),
                        bake_id=int(md.bakes[self.bake_id].bake_id),
                    )
            except RuntimeError as e:
                self.report({"ERROR"}, str(e))
                return {"CANCELLED"}

        md.show_viewport = True
        return {"FINISHED"}


class OBJECT_OT_GeometryNodeBakeDeleteSingle(bpy.types.Operator):
    bl_idname = "object.ml_modifier_bake_delete_single"
    bl_label = "Delete Single Bake"
    bl_description = "Delete a specific bake result from a Geometry Nodes modifier"
    bl_options = {"REGISTER", "UNDO"}

    bake_id: bpy.props.IntProperty(name="Bake_ID", default=0)  # type: ignore

    def execute(self, context):
        ob = context.active_object
        if not ob:
            return False

        md = ob.modifiers[ob["node_tree_name"]]
        with context.temp_override(id=ob):
            bpy.ops.object.geometry_node_bake_delete_single(
                session_uid=int(md.id_data.session_uid),
                modifier_name=str(md.name),
                bake_id=int(md.bakes[self.bake_id].bake_id),
            )
        return {"FINISHED"}
