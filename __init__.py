import bpy

# from . import nodes
# from .nodes import material, geonode
from .panel import main_panel, sub_panels
from .properties import delete_properties, update_properties
from .operators import (
    StartOperator,
    OBJECT_OT_GeometryNodeBake,
    OBJECT_OT_GeometryNodeBakeDeleteSingle,
)


classes = [
    main_panel.Main,
    sub_panels.SizeAndShape_SubPanel,
    sub_panels.Curves_SubPanel,
    sub_panels.CurveTrimming_SubPanel,
    sub_panels.Merge_SubPanel,
    sub_panels.CustomModel_SubPanel,
    sub_panels.color_SubPanel,
    sub_panels.AsProp_SubPanel,
    sub_panels.baking_custom_SubPanel,
    StartOperator,
    OBJECT_OT_GeometryNodeBake,
    OBJECT_OT_GeometryNodeBakeDeleteSingle,
]


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
