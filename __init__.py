import bpy
# from . import nodes
# from .nodes import material, geonode
from .panel import main_panel, sub_panels
from .properties import delete_properties,update_properties
from .operators import StartOperator


classes = [main_panel.Main, sub_panels.SizeAndShape_SubPanel, sub_panels.Curves_SubPanel, StartOperator.StartOperator]
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    # bpy.types.OBJECT_PT_dreamscape.my_bool = bpy.props.BoolProperty(default=False) # Important: Register the property
    update_properties.property_update()


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    # del bpy.types.OBJECT_PT_dreamscape.my_bool
    delete_properties.del_properties()
if __name__ == "__main__":
    register()