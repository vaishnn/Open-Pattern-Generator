import bpy
import random


def neon_node_group():
    matname = "Neon"
    while True:
        _is_neon_present = matname in bpy.data.materials
        if not _is_neon_present:
            mat = bpy.data.materials.new(name=matname)
            matname = matname
            break
        else:
            matname = "Neon" + str(random.randint(100, 1000))
    mat.use_nodes = True
    neon = mat.node_tree
    # start with a clean node tree
    for node in neon.nodes:
        neon.nodes.remove(node)
    neon.color_tag = "NONE"
    neon.description = ""
    material_output = neon.nodes.new("ShaderNodeOutputMaterial")
    material_output.name = "Material Output"
    material_output.is_active_output = True
    material_output.target = "ALL"
    # Displacement
    material_output.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Thickness
    material_output.inputs[3].default_value = 0.0
    # node Attribute
    attribute = neon.nodes.new("ShaderNodeAttribute")
    attribute.name = "Attribute"
    attribute.attribute_name = "S"
    attribute.attribute_type = "GEOMETRY"
    # node Principled BSDF
    principled_bsdf = neon.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf.name = "Principled BSDF"
    principled_bsdf.distribution = "MULTI_GGX"
    principled_bsdf.subsurface_method = "RANDOM_WALK_SKIN"
    # Base Color
    principled_bsdf.inputs[0].default_value = (
        0.800000011920929,
        0.800000011920929,
        0.800000011920929,
        1.0,
    )
    # Metallic
    principled_bsdf.inputs[1].default_value = 0.0
    # Roughness
    principled_bsdf.inputs[2].default_value = 0.5
    # IOR
    principled_bsdf.inputs[3].default_value = 1.5
    # Alpha
    principled_bsdf.inputs[4].default_value = 1.0
    # Normal
    principled_bsdf.inputs[5].default_value = (0.0, 0.0, 0.0)
    # Subsurface Weight
    principled_bsdf.inputs[7].default_value = 0.0
    # Subsurface Radius
    principled_bsdf.inputs[8].default_value = (
        1.0,
        0.20000000298023224,
        0.10000000149011612,
    )
    # Subsurface Scale
    principled_bsdf.inputs[9].default_value = 0.05000000074505806
    # Subsurface IOR
    principled_bsdf.inputs[10].default_value = 1.399999976158142
    # Subsurface Anisotropy
    principled_bsdf.inputs[11].default_value = 0.0
    # Specular IOR Level
    principled_bsdf.inputs[12].default_value = 0.581818163394928
    # Specular Tint
    principled_bsdf.inputs[13].default_value = (1.0, 1.0, 1.0, 1.0)
    # Anisotropic
    principled_bsdf.inputs[14].default_value = 0.0
    # Anisotropic Rotation
    principled_bsdf.inputs[15].default_value = 0.0
    # Tangent
    principled_bsdf.inputs[16].default_value = (0.0, 0.0, 0.0)
    # Transmission Weight
    principled_bsdf.inputs[17].default_value = 0.0
    # Coat Weight
    principled_bsdf.inputs[18].default_value = 1.0
    # Coat Roughness
    principled_bsdf.inputs[19].default_value = 0.0
    # Coat IOR
    principled_bsdf.inputs[20].default_value = 4.0
    # Coat Tint
    principled_bsdf.inputs[21].default_value = (1.0, 1.0, 1.0, 1.0)
    # Coat Normal
    principled_bsdf.inputs[22].default_value = (0.0, 0.0, 0.0)
    # Sheen Weight
    principled_bsdf.inputs[23].default_value = 0.0
    # Sheen Roughness
    principled_bsdf.inputs[24].default_value = 0.0
    # Sheen Tint
    principled_bsdf.inputs[25].default_value = (1.0, 1.0, 1.0, 1.0)
    # Thin Film Thickness
    principled_bsdf.inputs[28].default_value = 0.0
    # Thin Film IOR
    principled_bsdf.inputs[29].default_value = 1.3300000429153442
    # node Attribute.001
    attribute_001 = neon.nodes.new("ShaderNodeAttribute")
    attribute_001.name = "Attribute.001"
    attribute_001.attribute_name = "Emission Stenght"
    attribute_001.attribute_type = "GEOMETRY"
    # Set locations
    material_output.location = (-270.58349609375, 115.82111358642578)
    attribute.location = (-750.58349609375, 115.82111358642578)
    principled_bsdf.location = (-560.58349609375, 115.82111358642578)
    attribute_001.location = (-816.3646240234375, -732.2822265625)
    # Set dimensions
    material_output.width, material_output.height = 140.0, 100.0
    attribute.width, attribute.height = 140.0, 100.0
    principled_bsdf.width, principled_bsdf.height = 240.0, 100.0
    attribute_001.width, attribute_001.height = 140.0, 100.0
    # initialize neon links
    # principled_bsdf.BSDF -> material_output.Surface
    neon.links.new(principled_bsdf.outputs[0], material_output.inputs[0])
    # attribute.Color -> principled_bsdf.Emission Color
    neon.links.new(attribute.outputs[0], principled_bsdf.inputs[26])
    # attribute_001.Fac -> principled_bsdf.Emission Strength
    neon.links.new(attribute_001.outputs[2], principled_bsdf.inputs[27])
    # mat = bpy.data.materials["Neon"]
    return bpy.data.materials[matname]
