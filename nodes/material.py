import bpy
import random 

def nodegroup_node_group():

    nodegroup = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "NodeGroup")

    nodegroup.color_tag = 'NONE'
    nodegroup.description = ""
    

    #nodegroup interface
    #Socket BSDF
    bsdf_socket = nodegroup.interface.new_socket(name = "BSDF", in_out='OUTPUT', socket_type = 'NodeSocketShader')
    bsdf_socket.attribute_domain = 'POINT'

    #Socket Vector
    vector_socket = nodegroup.interface.new_socket(name = "Vector", in_out='INPUT', socket_type = 'NodeSocketVector')
    vector_socket.default_value = (0.0, 0.0, 0.0)
    vector_socket.min_value = -3.4028234663852886e+38
    vector_socket.max_value = 3.4028234663852886e+38
    vector_socket.subtype = 'NONE'
    vector_socket.attribute_domain = 'POINT'
    vector_socket.hide_value = True

    #Socket Seed
    seed_socket = nodegroup.interface.new_socket(name = "Seed", in_out='INPUT', socket_type = 'NodeSocketFloat')
    seed_socket.default_value = 0.0
    seed_socket.min_value = -1000.0
    seed_socket.max_value = 1000.0
    seed_socket.subtype = 'NONE'
    seed_socket.attribute_domain = 'POINT'


    #initialize nodegroup nodes
    #node Group Output
    group_output = nodegroup.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    #node Group Input
    group_input = nodegroup.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    #node Principled BSDF
    principled_bsdf = nodegroup.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf.name = "Principled BSDF"
    principled_bsdf.distribution = 'MULTI_GGX'
    principled_bsdf.subsurface_method = 'RANDOM_WALK'
    #Base Color
    principled_bsdf.inputs[0].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
    #Metallic
    principled_bsdf.inputs[1].default_value = 0.0
    #Roughness
    principled_bsdf.inputs[2].default_value = 0.5
    #IOR
    principled_bsdf.inputs[3].default_value = 1.5
    #Alpha
    principled_bsdf.inputs[4].default_value = 1.0
    #Normal
    principled_bsdf.inputs[5].default_value = (0.0, 0.0, 0.0)
    #Subsurface Weight
    principled_bsdf.inputs[7].default_value = 0.0
    #Subsurface Radius
    principled_bsdf.inputs[8].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
    #Subsurface Scale
    principled_bsdf.inputs[9].default_value = 0.05000000074505806
    #Subsurface Anisotropy
    principled_bsdf.inputs[11].default_value = 0.0
    #Specular IOR Level
    principled_bsdf.inputs[12].default_value = 0.5
    #Specular Tint
    principled_bsdf.inputs[13].default_value = (1.0, 1.0, 1.0, 1.0)
    #Anisotropic
    principled_bsdf.inputs[14].default_value = 0.0
    #Anisotropic Rotation
    principled_bsdf.inputs[15].default_value = 0.0
    #Tangent
    principled_bsdf.inputs[16].default_value = (0.0, 0.0, 0.0)
    #Transmission Weight
    principled_bsdf.inputs[17].default_value = 0.0
    #Coat Weight
    principled_bsdf.inputs[18].default_value = 0.0
    #Coat Roughness
    principled_bsdf.inputs[19].default_value = 0.029999999329447746
    #Coat IOR
    principled_bsdf.inputs[20].default_value = 1.5
    #Coat Tint
    principled_bsdf.inputs[21].default_value = (1.0, 1.0, 1.0, 1.0)
    #Coat Normal
    principled_bsdf.inputs[22].default_value = (0.0, 0.0, 0.0)
    #Sheen Weight
    principled_bsdf.inputs[23].default_value = 0.0
    #Sheen Roughness
    principled_bsdf.inputs[24].default_value = 0.5
    #Sheen Tint
    principled_bsdf.inputs[25].default_value = (1.0, 1.0, 1.0, 1.0)
    #Emission Strength
    principled_bsdf.inputs[27].default_value = 1.0
    #Thin Film Thickness
    principled_bsdf.inputs[28].default_value = 0.0
    #Thin Film IOR
    principled_bsdf.inputs[29].default_value = 1.3300000429153442

    #node Noise Texture
    noise_texture = nodegroup.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.noise_dimensions = '4D'
    noise_texture.noise_type = 'FBM'
    noise_texture.normalize = False
    #Scale
    noise_texture.inputs[2].default_value = 5.0
    #Detail
    noise_texture.inputs[3].default_value = 2.0
    #Roughness
    noise_texture.inputs[4].default_value = 0.5
    #Lacunarity
    noise_texture.inputs[5].default_value = 2.0
    #Distortion
    noise_texture.inputs[8].default_value = 0.0


    #Set locations
    group_output.location = (390.94061279296875, 0.0)
    group_input.location = (-300.94061279296875, 0.0)
    principled_bsdf.location = (100.94061279296875, 80.05790710449219)
    noise_texture.location = (-100.94061279296875, -80.05790710449219)

    #Set dimensions
    group_output.width, group_output.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    principled_bsdf.width, principled_bsdf.height = 240.0, 100.0
    noise_texture.width, noise_texture.height = 140.0, 100.0

    #initialize nodegroup links
    #noise_texture.Color -> principled_bsdf.Emission Color
    nodegroup.links.new(noise_texture.outputs[1], principled_bsdf.inputs[26])
    #group_input.Vector -> noise_texture.Vector
    nodegroup.links.new(group_input.outputs[0], noise_texture.inputs[0])
    #principled_bsdf.BSDF -> group_output.BSDF
    nodegroup.links.new(principled_bsdf.outputs[0], group_output.inputs[0])
    #group_input.Seed -> noise_texture.W
    nodegroup.links.new(group_input.outputs[1], noise_texture.inputs[1])
    return nodegroup

#initialize neon node group
def neon_node_group():
    matname = "Neon"
    while True:
        _is_neon_present = matname in bpy.data.materials
        if not _is_neon_present:
            mat = bpy.data.materials.new(name = matname)
            matname = matname
            break
        else:
            matname = "Neon" + str(random.randint(100, 1000))
    mat.use_nodes = True

    neon = mat.node_tree
    #start with a clean node tree
    for node in neon.nodes:
        neon.nodes.remove(node)
    neon.color_tag = 'NONE'
    neon.description = ""
    

    #neon interface

    #initialize neon nodes
    #node Material Output
    material_output = neon.nodes.new("ShaderNodeOutputMaterial")
    material_output.name = "Material Output"
    material_output.is_active_output = True
    material_output.target = 'ALL'
    #Displacement
    material_output.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Thickness
    material_output.inputs[3].default_value = 0.0

    #node Attribute
    attribute = neon.nodes.new("ShaderNodeAttribute")
    attribute.name = "Attribute"
    attribute.attribute_name = "S"
    attribute.attribute_type = 'GEOMETRY'

    #node Group
    group = neon.nodes.new("ShaderNodeGroup")
    group.name = "Group"
    group.node_tree = nodegroup_node_group()
    #Socket_2
    group.inputs[1].default_value = 2.799999713897705


    #Set locations
    material_output.location = (300.0, 300.0)
    attribute.location = (-428.53680419921875, 373.1016540527344)
    group.location = (-90.94061279296875, 219.9420928955078)

    #Set dimensions
    material_output.width, material_output.height = 140.0, 100.0
    attribute.width, attribute.height = 140.0, 100.0
    group.width, group.height = 140.0, 100.0

    #initialize neon links
    #group.BSDF -> material_output.Surface
    neon.links.new(group.outputs[0], material_output.inputs[0])
    #attribute.Fac -> group.Vector
    neon.links.new(attribute.outputs[2], group.inputs[0])
    return bpy.data.materials[matname]