import bpy

#initialize creating_curves_v0 node group
def creating_curves_v0_node_group():
    creating_curves_v0 = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Creating Curves v0")

    creating_curves_v0.color_tag = 'NONE'
    creating_curves_v0.description = ""
    


    #creating_curves_v0 interface
    #Socket Geometry
    geometry_socket = creating_curves_v0.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'

    #Socket Count
    count_socket = creating_curves_v0.interface.new_socket(name = "Count", in_out='INPUT', socket_type = 'NodeSocketInt')
    count_socket.default_value = 12
    count_socket.min_value = 1
    count_socket.max_value = 2147483647
    count_socket.subtype = 'NONE'
    count_socket.attribute_domain = 'POINT'

    #Socket Size
    size_socket = creating_curves_v0.interface.new_socket(name = "Size", in_out='INPUT', socket_type = 'NodeSocketFloat')
    size_socket.default_value = 1.0
    size_socket.min_value = 0.0
    size_socket.max_value = 3.4028234663852886e+38
    size_socket.subtype = 'DISTANCE'
    size_socket.attribute_domain = 'POINT'

    #Socket Offset
    offset_socket = creating_curves_v0.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketFloat')
    offset_socket.default_value = 0.8299999833106995
    offset_socket.min_value = -10000.0
    offset_socket.max_value = 10000.0
    offset_socket.subtype = 'NONE'
    offset_socket.attribute_domain = 'POINT'

    #Socket Seed
    seed_socket = creating_curves_v0.interface.new_socket(name = "Seed", in_out='INPUT', socket_type = 'NodeSocketInt')
    seed_socket.default_value = 2
    seed_socket.min_value = -10000
    seed_socket.max_value = 10000
    seed_socket.subtype = 'NONE'
    seed_socket.attribute_domain = 'POINT'

    #Socket Grain
    grain_socket = creating_curves_v0.interface.new_socket(name = "Grain", in_out='INPUT', socket_type = 'NodeSocketFloat')
    grain_socket.default_value = 0.20000004768371582
    grain_socket.min_value = -10000.0
    grain_socket.max_value = 10000.0
    grain_socket.subtype = 'NONE'
    grain_socket.attribute_domain = 'POINT'

    #Socket Resolution of Curve
    resolution_of_curve_socket = creating_curves_v0.interface.new_socket(name = "Resolution of Curve", in_out='INPUT', socket_type = 'NodeSocketInt')
    resolution_of_curve_socket.default_value = 16
    resolution_of_curve_socket.min_value = 2
    resolution_of_curve_socket.max_value = 256
    resolution_of_curve_socket.subtype = 'NONE'
    resolution_of_curve_socket.attribute_domain = 'POINT'

    #Socket Radius of Tubes
    radius_of_tubes_socket = creating_curves_v0.interface.new_socket(name = "Radius of Tubes", in_out='INPUT', socket_type = 'NodeSocketFloat')
    radius_of_tubes_socket.default_value = 0.009999999776482582
    radius_of_tubes_socket.min_value = 0.0
    radius_of_tubes_socket.max_value = 3.4028234663852886e+38
    radius_of_tubes_socket.subtype = 'DISTANCE'
    radius_of_tubes_socket.attribute_domain = 'POINT'

    #Socket Resolution of Tubes
    resolution_of_tubes_socket = creating_curves_v0.interface.new_socket(name = "Resolution of Tubes", in_out='INPUT', socket_type = 'NodeSocketInt')
    resolution_of_tubes_socket.default_value = 32
    resolution_of_tubes_socket.min_value = 3
    resolution_of_tubes_socket.max_value = 512
    resolution_of_tubes_socket.subtype = 'NONE'
    resolution_of_tubes_socket.attribute_domain = 'POINT'

    #Socket 1st Curve Segments
    _1st_curve_segments_socket = creating_curves_v0.interface.new_socket(name = "1st Curve Segments", in_out='INPUT', socket_type = 'NodeSocketInt')
    _1st_curve_segments_socket.default_value = 10
    _1st_curve_segments_socket.min_value = 1
    _1st_curve_segments_socket.max_value = 100000
    _1st_curve_segments_socket.subtype = 'NONE'
    _1st_curve_segments_socket.attribute_domain = 'POINT'

    #Socket 2nd Curve Segements
    _2nd_curve_segements_socket = creating_curves_v0.interface.new_socket(name = "2nd Curve Segements", in_out='INPUT', socket_type = 'NodeSocketInt')
    _2nd_curve_segements_socket.default_value = 10
    _2nd_curve_segements_socket.min_value = 1
    _2nd_curve_segements_socket.max_value = 100000
    _2nd_curve_segements_socket.subtype = 'NONE'
    _2nd_curve_segements_socket.attribute_domain = 'POINT'

    #Socket Material
    material_socket = creating_curves_v0.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    material_socket.attribute_domain = 'POINT'


    #initialize creating_curves_v0 nodes
    #node Group Output
    group_output = creating_curves_v0.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    #node Group Input
    group_input = creating_curves_v0.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    #node Set Material
    set_material = creating_curves_v0.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    #Selection
    set_material.inputs[1].default_value = True

    #node Random Value
    random_value = creating_curves_v0.nodes.new("FunctionNodeRandomValue")
    random_value.name = "Random Value"
    random_value.data_type = 'FLOAT'
    #Min_001
    random_value.inputs[2].default_value = 0.0
    #Max_001
    random_value.inputs[3].default_value = 1.0
    #ID
    random_value.inputs[7].default_value = 0
    #Seed
    random_value.inputs[8].default_value = 0

    #node Arc
    arc = creating_curves_v0.nodes.new("GeometryNodeCurveArc")
    arc.name = "Arc"
    arc.mode = 'RADIUS'
    #Radius
    arc.inputs[4].default_value = 1.0
    #Start Angle
    arc.inputs[5].default_value = 0.0
    #Sweep Angle
    arc.inputs[6].default_value = 1.5707963705062866
    #Connect Center
    arc.inputs[8].default_value = False
    #Invert Arc
    arc.inputs[9].default_value = False

    #node Instance on Points
    instance_on_points = creating_curves_v0.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points.name = "Instance on Points"
    #Selection
    instance_on_points.inputs[1].default_value = True
    #Pick Instance
    instance_on_points.inputs[3].default_value = False
    #Instance Index
    instance_on_points.inputs[4].default_value = 0
    #Rotation
    instance_on_points.inputs[5].default_value = (0.0, 0.0, 0.0)

    #node Points
    points = creating_curves_v0.nodes.new("GeometryNodePoints")
    points.name = "Points"
    #Position
    points.inputs[1].default_value = (0.0, 0.0, 0.0)
    #Radius
    points.inputs[2].default_value = 0.09999999403953552

    #node Index
    index = creating_curves_v0.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"

    #node Map Range
    map_range = creating_curves_v0.nodes.new("ShaderNodeMapRange")
    map_range.name = "Map Range"
    map_range.clamp = True
    map_range.data_type = 'FLOAT'
    map_range.interpolation_type = 'LINEAR'
    #From Min
    map_range.inputs[1].default_value = 1.0

    #node Realize Instances.002
    realize_instances_002 = creating_curves_v0.nodes.new("GeometryNodeRealizeInstances")
    realize_instances_002.name = "Realize Instances.002"
    #Selection
    realize_instances_002.inputs[1].default_value = True
    #Realize All
    realize_instances_002.inputs[2].default_value = True
    #Depth
    realize_instances_002.inputs[3].default_value = 0

    #node Math
    math = creating_curves_v0.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'SUBTRACT'
    math.use_clamp = False
    #Value_001
    math.inputs[1].default_value = 1.0

    #node Transform Geometry
    transform_geometry = creating_curves_v0.nodes.new("GeometryNodeTransform")
    transform_geometry.name = "Transform Geometry"
    transform_geometry.mode = 'COMPONENTS'
    #Translation
    transform_geometry.inputs[1].default_value = (1.0, 1.0, 0.0)
    #Rotation
    transform_geometry.inputs[2].default_value = (0.0, 0.0, 3.1415927410125732)
    #Scale
    transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)

    #node Join Geometry
    join_geometry = creating_curves_v0.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"

    #node Grid
    grid = creating_curves_v0.nodes.new("GeometryNodeMeshGrid")
    grid.name = "Grid"

    #node Instance on Points.001
    instance_on_points_001 = creating_curves_v0.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_001.name = "Instance on Points.001"
    #Selection
    instance_on_points_001.inputs[1].default_value = True
    #Pick Instance
    instance_on_points_001.inputs[3].default_value = False
    #Instance Index
    instance_on_points_001.inputs[4].default_value = 0
    #Rotation
    instance_on_points_001.inputs[5].default_value = (0.0, 0.0, 0.0)
    #Scale
    instance_on_points_001.inputs[6].default_value = (1.0, 1.0, 1.0)

    #node Merge by Distance
    merge_by_distance = creating_curves_v0.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance.name = "Merge by Distance"
    merge_by_distance.mode = 'ALL'
    #Selection
    merge_by_distance.inputs[1].default_value = True
    #Distance
    merge_by_distance.inputs[2].default_value = 0.0010000000474974513

    #node Math.001
    math_001 = creating_curves_v0.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = 'ADD'
    math_001.use_clamp = False
    #Value_001
    math_001.inputs[1].default_value = 1.0

    #node Transform Geometry.001
    transform_geometry_001 = creating_curves_v0.nodes.new("GeometryNodeTransform")
    transform_geometry_001.name = "Transform Geometry.001"
    transform_geometry_001.mode = 'COMPONENTS'
    #Translation
    transform_geometry_001.inputs[1].default_value = (-0.5, -0.5, 0.0)
    #Rotation
    transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Scale
    transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)

    #node Math.002
    math_002 = creating_curves_v0.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = 'SUBTRACT'
    math_002.use_clamp = False
    #Value
    math_002.inputs[0].default_value = 1.0

    #node Realize Instances
    realize_instances = creating_curves_v0.nodes.new("GeometryNodeRealizeInstances")
    realize_instances.name = "Realize Instances"
    #Selection
    realize_instances.inputs[1].default_value = True
    #Realize All
    realize_instances.inputs[2].default_value = True
    #Depth
    realize_instances.inputs[3].default_value = 0

    #node Curve to Mesh
    curve_to_mesh = creating_curves_v0.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh.name = "Curve to Mesh"
    #Fill Caps
    curve_to_mesh.inputs[2].default_value = False

    #node Delete Geometry
    delete_geometry = creating_curves_v0.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry.name = "Delete Geometry"
    delete_geometry.domain = 'POINT'
    delete_geometry.mode = 'ALL'

    #node Position
    position = creating_curves_v0.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"

    #node Vector Math
    vector_math = creating_curves_v0.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = 'LENGTH'

    #node Compare
    compare = creating_curves_v0.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.data_type = 'FLOAT'
    compare.mode = 'ELEMENT'
    compare.operation = 'LESS_THAN'

    #node Store Named Attribute
    store_named_attribute = creating_curves_v0.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.data_type = 'FLOAT'
    store_named_attribute.domain = 'CURVE'
    #Selection
    store_named_attribute.inputs[1].default_value = True
    #Name
    store_named_attribute.inputs[2].default_value = "S"

    #node Math.003
    math_003 = creating_curves_v0.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.operation = 'ADD'
    math_003.use_clamp = True

    #node Rotate Instances
    rotate_instances = creating_curves_v0.nodes.new("GeometryNodeRotateInstances")
    rotate_instances.name = "Rotate Instances"
    #Selection
    rotate_instances.inputs[1].default_value = True
    #Pivot Point
    rotate_instances.inputs[3].default_value = (0.5, 0.5, 0.0)
    #Local Space
    rotate_instances.inputs[4].default_value = True

    #node Math.004
    math_004 = creating_curves_v0.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.operation = 'MULTIPLY'
    math_004.use_clamp = False
    #Value
    math_004.inputs[0].default_value = 1.5707963705062866

    #node Random Value.001
    random_value_001 = creating_curves_v0.nodes.new("FunctionNodeRandomValue")
    random_value_001.name = "Random Value.001"
    random_value_001.data_type = 'INT'
    #Min_002
    random_value_001.inputs[4].default_value = 0
    #Max_002
    random_value_001.inputs[5].default_value = 3
    #ID
    random_value_001.inputs[7].default_value = 0

    #node Combine XYZ
    combine_xyz = creating_curves_v0.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    #X
    combine_xyz.inputs[0].default_value = 0.0
    #Y
    combine_xyz.inputs[1].default_value = 0.0

    #node Curve Circle
    curve_circle = creating_curves_v0.nodes.new("GeometryNodeCurvePrimitiveCircle")
    curve_circle.name = "Curve Circle"
    curve_circle.mode = 'RADIUS'

    #node Curve to Mesh.001
    curve_to_mesh_001 = creating_curves_v0.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh_001.name = "Curve to Mesh.001"
    #Fill Caps
    curve_to_mesh_001.inputs[2].default_value = True

    #node Mesh to Curve
    mesh_to_curve = creating_curves_v0.nodes.new("GeometryNodeMeshToCurve")
    mesh_to_curve.name = "Mesh to Curve"
    #Selection
    mesh_to_curve.inputs[1].default_value = True

    #node Realize Instances.001
    realize_instances_001 = creating_curves_v0.nodes.new("GeometryNodeRealizeInstances")
    realize_instances_001.name = "Realize Instances.001"
    #Selection
    realize_instances_001.inputs[1].default_value = True
    #Realize All
    realize_instances_001.inputs[2].default_value = True
    #Depth
    realize_instances_001.inputs[3].default_value = 0

    #node Curve to Mesh.002
    curve_to_mesh_002 = creating_curves_v0.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh_002.name = "Curve to Mesh.002"
    #Fill Caps
    curve_to_mesh_002.inputs[2].default_value = False

    #node Resample Curve
    resample_curve = creating_curves_v0.nodes.new("GeometryNodeResampleCurve")
    resample_curve.name = "Resample Curve"
    resample_curve.mode = 'COUNT'
    #Selection
    resample_curve.inputs[1].default_value = True

    #node Resample Curve.001
    resample_curve_001 = creating_curves_v0.nodes.new("GeometryNodeResampleCurve")
    resample_curve_001.name = "Resample Curve.001"
    resample_curve_001.mode = 'COUNT'
    #Selection
    resample_curve_001.inputs[1].default_value = True

    #node Reroute
    reroute = creating_curves_v0.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    #node Reroute.001
    reroute_001 = creating_curves_v0.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    #node Reroute.002
    reroute_002 = creating_curves_v0.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    #node Reroute.003
    reroute_003 = creating_curves_v0.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    #node Reroute.004
    reroute_004 = creating_curves_v0.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    #node Reroute.005
    reroute_005 = creating_curves_v0.nodes.new("NodeReroute")
    reroute_005.name = "Reroute.005"
    #node Reroute.006
    reroute_006 = creating_curves_v0.nodes.new("NodeReroute")
    reroute_006.name = "Reroute.006"
    #node Reroute.007
    reroute_007 = creating_curves_v0.nodes.new("NodeReroute")
    reroute_007.name = "Reroute.007"
    #node Reroute.008
    reroute_008 = creating_curves_v0.nodes.new("NodeReroute")
    reroute_008.name = "Reroute.008"
    #node Reroute.009
    reroute_009 = creating_curves_v0.nodes.new("NodeReroute")
    reroute_009.name = "Reroute.009"
    #node Reroute.010
    reroute_010 = creating_curves_v0.nodes.new("NodeReroute")
    reroute_010.name = "Reroute.010"
    #node Reroute.011
    reroute_011 = creating_curves_v0.nodes.new("NodeReroute")
    reroute_011.name = "Reroute.011"
    #node Reroute.012
    reroute_012 = creating_curves_v0.nodes.new("NodeReroute")
    reroute_012.name = "Reroute.012"
    #node Reroute.013
    reroute_013 = creating_curves_v0.nodes.new("NodeReroute")
    reroute_013.name = "Reroute.013"



    #Set locations
    group_output.location = (2155.064453125, -903.20556640625)
    group_input.location = (-1639.9354248046875, 717.79443359375)
    set_material.location = (1965.0645751953125, -903.20556640625)
    random_value.location = (1357.5645751953125, -342.20556640625)
    arc.location = (-1072.4354248046875, 1605.29443359375)
    instance_on_points.location = (-844.9354248046875, 935.79443359375)
    points.location = (-1072.4354248046875, 1344.29443359375)
    index.location = (-1349.9354248046875, 1495.79443359375)
    map_range.location = (-1072.4354248046875, 1011.79443359375)
    realize_instances_002.location = (977.5645751953125, -188.70556640625)
    math.location = (-1349.9354248046875, 1200.79443359375)
    transform_geometry.location = (-414.9354248046875, -218.70556640625)
    join_geometry.location = (382.5645751953125, -188.70556640625)
    grid.location = (-1072.4354248046875, 618.79443359375)
    instance_on_points_001.location = (585.0645751953125, -188.70559692382812)
    merge_by_distance.location = (1167.5645751953125, -188.70556640625)
    math_001.location = (-1349.9354248046875, 490.79443359375)
    transform_geometry_001.location = (-844.9354248046875, 618.79443359375)
    math_002.location = (-1349.9354248046875, 1002.79443359375)
    realize_instances.location = (-224.9354248046875, -218.70556640625)
    curve_to_mesh.location = (-34.9354248046875, -218.70556640625)
    delete_geometry.location = (180.06454467773438, -308.20556640625)
    position.location = (-1639.9354248046875, -1192.20556640625)
    vector_math.location = (-1349.9354248046875, -1192.20556640625)
    compare.location = (-1072.4354248046875, -615.70556640625)
    store_named_attribute.location = (1572.5645751953125, -663.20556640625)
    math_003.location = (-1349.9354248046875, 688.79443359375)
    rotate_instances.location = (787.5645751953125, -188.70556640625)
    math_004.location = (382.5645751953125, 193.29443359375)
    random_value_001.location = (180.0645751953125, 193.29443359375)
    combine_xyz.location = (585.0645751953125, 193.29443359375)
    curve_circle.location = (-1349.9354248046875, -903.20556640625)
    curve_to_mesh_001.location = (1775.0645751953125, -903.2055053710938)
    mesh_to_curve.location = (1357.5645751953125, -188.70556640625)
    realize_instances_001.location = (-414.9354248046875, -23.70557403564453)
    curve_to_mesh_002.location = (-224.9354248046875, -23.70556640625)
    resample_curve.location = (-604.9354248046875, -218.70556640625)
    resample_curve_001.location = (-604.9354248046875, -23.70557403564453)
    reroute.location = (-1349.9354248046875, 746.79443359375)
    reroute_001.location = (-1209.9354248046875, 746.79443359375)
    reroute_002.location = (-1349.9354248046875, 1519.1156005859375)
    reroute_003.location = (-1349.9354248046875, 1284.747802734375)
    reroute_004.location = (-1349.9354248046875, 787.9349365234375)
    reroute_005.location = (-1349.9354248046875, 41.33463668823242)
    reroute_006.location = (-1349.9354248046875, -1076.20556640625)
    reroute_007.location = (-704.9354248046875, -1076.20556640625)
    reroute_008.location = (-1349.9354248046875, -1134.20556640625)
    reroute_009.location = (-704.9354248046875, -1134.20556640625)
    reroute_010.location = (1712.5645751953125, -938.5228271484375)
    reroute_011.location = (105.0645751953125, -650.4595336914062)
    reroute_012.location = (522.5645751953125, 584.1868896484375)
    reroute_013.location = (320.0645751953125, -58.31468200683594)

    #Set dimensions
    group_output.width, group_output.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    set_material.width, set_material.height = 140.0, 100.0
    random_value.width, random_value.height = 140.0, 100.0
    arc.width, arc.height = 140.0, 100.0
    instance_on_points.width, instance_on_points.height = 140.0, 100.0
    points.width, points.height = 140.0, 100.0
    index.width, index.height = 140.0, 100.0
    map_range.width, map_range.height = 140.0, 100.0
    realize_instances_002.width, realize_instances_002.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0
    transform_geometry.width, transform_geometry.height = 140.0, 100.0
    join_geometry.width, join_geometry.height = 140.0, 100.0
    grid.width, grid.height = 140.0, 100.0
    instance_on_points_001.width, instance_on_points_001.height = 140.0, 100.0
    merge_by_distance.width, merge_by_distance.height = 140.0, 100.0
    math_001.width, math_001.height = 140.0, 100.0
    transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
    math_002.width, math_002.height = 140.0, 100.0
    realize_instances.width, realize_instances.height = 140.0, 100.0
    curve_to_mesh.width, curve_to_mesh.height = 140.0, 100.0
    delete_geometry.width, delete_geometry.height = 140.0, 100.0
    position.width, position.height = 140.0, 100.0
    vector_math.width, vector_math.height = 140.0, 100.0
    compare.width, compare.height = 140.0, 100.0
    store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
    math_003.width, math_003.height = 140.0, 100.0
    rotate_instances.width, rotate_instances.height = 140.0, 100.0
    math_004.width, math_004.height = 140.0, 100.0
    random_value_001.width, random_value_001.height = 140.0, 100.0
    combine_xyz.width, combine_xyz.height = 140.0, 100.0
    curve_circle.width, curve_circle.height = 140.0, 100.0
    curve_to_mesh_001.width, curve_to_mesh_001.height = 140.0, 100.0
    mesh_to_curve.width, mesh_to_curve.height = 140.0, 100.0
    realize_instances_001.width, realize_instances_001.height = 140.0, 100.0
    curve_to_mesh_002.width, curve_to_mesh_002.height = 140.0, 100.0
    resample_curve.width, resample_curve.height = 140.0, 100.0
    resample_curve_001.width, resample_curve_001.height = 140.0, 100.0
    reroute.width, reroute.height = 16.0, 100.0
    reroute_001.width, reroute_001.height = 16.0, 100.0
    reroute_002.width, reroute_002.height = 16.0, 100.0
    reroute_003.width, reroute_003.height = 16.0, 100.0
    reroute_004.width, reroute_004.height = 16.0, 100.0
    reroute_005.width, reroute_005.height = 16.0, 100.0
    reroute_006.width, reroute_006.height = 16.0, 100.0
    reroute_007.width, reroute_007.height = 16.0, 100.0
    reroute_008.width, reroute_008.height = 16.0, 100.0
    reroute_009.width, reroute_009.height = 16.0, 100.0
    reroute_010.width, reroute_010.height = 16.0, 100.0
    reroute_011.width, reroute_011.height = 16.0, 100.0
    reroute_012.width, reroute_012.height = 16.0, 100.0
    reroute_013.width, reroute_013.height = 16.0, 100.0

    #initialize creating_curves_v0 links
    #curve_to_mesh_001.Mesh -> set_material.Geometry
    creating_curves_v0.links.new(curve_to_mesh_001.outputs[0], set_material.inputs[0])
    #vector_math.Value -> compare.A
    creating_curves_v0.links.new(vector_math.outputs[1], compare.inputs[0])
    #delete_geometry.Geometry -> join_geometry.Geometry
    creating_curves_v0.links.new(delete_geometry.outputs[0], join_geometry.inputs[0])
    #mesh_to_curve.Curve -> store_named_attribute.Geometry
    creating_curves_v0.links.new(mesh_to_curve.outputs[0], store_named_attribute.inputs[0])
    #combine_xyz.Vector -> rotate_instances.Rotation
    creating_curves_v0.links.new(combine_xyz.outputs[0], rotate_instances.inputs[2])
    #realize_instances_001.Geometry -> curve_to_mesh_002.Curve
    creating_curves_v0.links.new(realize_instances_001.outputs[0], curve_to_mesh_002.inputs[0])
    #map_range.Result -> instance_on_points.Scale
    creating_curves_v0.links.new(map_range.outputs[0], instance_on_points.inputs[6])
    #random_value_001.Value -> math_004.Value
    creating_curves_v0.links.new(random_value_001.outputs[2], math_004.inputs[1])
    #instance_on_points_001.Instances -> rotate_instances.Instances
    creating_curves_v0.links.new(instance_on_points_001.outputs[0], rotate_instances.inputs[0])
    #position.Position -> vector_math.Vector
    creating_curves_v0.links.new(position.outputs[0], vector_math.inputs[0])
    #math.Value -> map_range.From Max
    creating_curves_v0.links.new(math.outputs[0], map_range.inputs[2])
    #rotate_instances.Instances -> realize_instances_002.Geometry
    creating_curves_v0.links.new(rotate_instances.outputs[0], realize_instances_002.inputs[0])
    #math_004.Value -> combine_xyz.Z
    creating_curves_v0.links.new(math_004.outputs[0], combine_xyz.inputs[2])
    #realize_instances_002.Geometry -> merge_by_distance.Geometry
    creating_curves_v0.links.new(realize_instances_002.outputs[0], merge_by_distance.inputs[0])
    #math_003.Value -> compare.B
    creating_curves_v0.links.new(math_003.outputs[0], compare.inputs[1])
    #realize_instances.Geometry -> curve_to_mesh.Curve
    creating_curves_v0.links.new(realize_instances.outputs[0], curve_to_mesh.inputs[0])
    #transform_geometry.Geometry -> realize_instances.Geometry
    creating_curves_v0.links.new(transform_geometry.outputs[0], realize_instances.inputs[0])
    #arc.Curve -> instance_on_points.Instance
    creating_curves_v0.links.new(arc.outputs[0], instance_on_points.inputs[2])
    #store_named_attribute.Geometry -> curve_to_mesh_001.Curve
    creating_curves_v0.links.new(store_named_attribute.outputs[0], curve_to_mesh_001.inputs[0])
    #curve_to_mesh.Mesh -> delete_geometry.Geometry
    creating_curves_v0.links.new(curve_to_mesh.outputs[0], delete_geometry.inputs[0])
    #math_001.Value -> grid.Vertices Y
    creating_curves_v0.links.new(math_001.outputs[0], grid.inputs[3])
    #math_001.Value -> grid.Vertices X
    creating_curves_v0.links.new(math_001.outputs[0], grid.inputs[2])
    #math_002.Value -> map_range.To Min
    creating_curves_v0.links.new(math_002.outputs[0], map_range.inputs[3])
    #index.Index -> map_range.Value
    creating_curves_v0.links.new(index.outputs[0], map_range.inputs[0])
    #random_value.Value -> store_named_attribute.Value
    creating_curves_v0.links.new(random_value.outputs[1], store_named_attribute.inputs[3])
    #resample_curve.Curve -> transform_geometry.Geometry
    creating_curves_v0.links.new(resample_curve.outputs[0], transform_geometry.inputs[0])
    #resample_curve_001.Curve -> realize_instances_001.Geometry
    creating_curves_v0.links.new(resample_curve_001.outputs[0], realize_instances_001.inputs[0])
    #join_geometry.Geometry -> instance_on_points_001.Instance
    creating_curves_v0.links.new(join_geometry.outputs[0], instance_on_points_001.inputs[2])
    #points.Points -> instance_on_points.Points
    creating_curves_v0.links.new(points.outputs[0], instance_on_points.inputs[0])
    #grid.Mesh -> transform_geometry_001.Geometry
    creating_curves_v0.links.new(grid.outputs[0], transform_geometry_001.inputs[0])
    #group_input.Size -> math_001.Value
    creating_curves_v0.links.new(group_input.outputs[1], math_001.inputs[0])
    #group_input.Offset -> math_002.Value
    creating_curves_v0.links.new(group_input.outputs[2], math_002.inputs[1])
    #set_material.Geometry -> group_output.Geometry
    creating_curves_v0.links.new(set_material.outputs[0], group_output.inputs[0])
    #group_input.Count -> math.Value
    creating_curves_v0.links.new(group_input.outputs[0], math.inputs[0])
    #group_input.Offset -> math_003.Value
    creating_curves_v0.links.new(group_input.outputs[2], math_003.inputs[0])
    #group_input.Radius of Tubes -> curve_circle.Radius
    creating_curves_v0.links.new(group_input.outputs[6], curve_circle.inputs[4])
    #group_input.Resolution of Tubes -> curve_circle.Resolution
    creating_curves_v0.links.new(group_input.outputs[7], curve_circle.inputs[0])
    #merge_by_distance.Geometry -> mesh_to_curve.Mesh
    creating_curves_v0.links.new(merge_by_distance.outputs[0], mesh_to_curve.inputs[0])
    #instance_on_points.Instances -> resample_curve.Curve
    creating_curves_v0.links.new(instance_on_points.outputs[0], resample_curve.inputs[0])
    #instance_on_points.Instances -> resample_curve_001.Curve
    creating_curves_v0.links.new(instance_on_points.outputs[0], resample_curve_001.inputs[0])
    #group_input.Grain -> math_003.Value
    creating_curves_v0.links.new(group_input.outputs[4], math_003.inputs[1])
    #group_input.Size -> reroute.Input
    creating_curves_v0.links.new(group_input.outputs[1], reroute.inputs[0])
    #reroute.Output -> reroute_001.Input
    creating_curves_v0.links.new(reroute.outputs[0], reroute_001.inputs[0])
    #reroute_001.Output -> grid.Size Y
    creating_curves_v0.links.new(reroute_001.outputs[0], grid.inputs[1])
    #reroute_001.Output -> grid.Size X
    creating_curves_v0.links.new(reroute_001.outputs[0], grid.inputs[0])
    #group_input.Resolution of Curve -> reroute_002.Input
    creating_curves_v0.links.new(group_input.outputs[5], reroute_002.inputs[0])
    #reroute_002.Output -> arc.Resolution
    creating_curves_v0.links.new(reroute_002.outputs[0], arc.inputs[0])
    #group_input.Count -> reroute_003.Input
    creating_curves_v0.links.new(group_input.outputs[0], reroute_003.inputs[0])
    #reroute_003.Output -> points.Count
    creating_curves_v0.links.new(reroute_003.outputs[0], points.inputs[0])
    #group_input.Offset -> reroute_004.Input
    creating_curves_v0.links.new(group_input.outputs[2], reroute_004.inputs[0])
    #reroute_004.Output -> map_range.To Max
    creating_curves_v0.links.new(reroute_004.outputs[0], map_range.inputs[4])
    #group_input.Seed -> reroute_005.Input
    creating_curves_v0.links.new(group_input.outputs[3], reroute_005.inputs[0])
    #reroute_005.Output -> random_value_001.Seed
    creating_curves_v0.links.new(reroute_005.outputs[0], random_value_001.inputs[8])
    #group_input.1st Curve Segments -> reroute_006.Input
    creating_curves_v0.links.new(group_input.outputs[8], reroute_006.inputs[0])
    #reroute_006.Output -> reroute_007.Input
    creating_curves_v0.links.new(reroute_006.outputs[0], reroute_007.inputs[0])
    #reroute_007.Output -> resample_curve_001.Count
    creating_curves_v0.links.new(reroute_007.outputs[0], resample_curve_001.inputs[2])
    #group_input.2nd Curve Segements -> reroute_008.Input
    creating_curves_v0.links.new(group_input.outputs[9], reroute_008.inputs[0])
    #reroute_008.Output -> reroute_009.Input
    creating_curves_v0.links.new(reroute_008.outputs[0], reroute_009.inputs[0])
    #reroute_009.Output -> resample_curve.Count
    creating_curves_v0.links.new(reroute_009.outputs[0], resample_curve.inputs[2])
    #curve_circle.Curve -> reroute_010.Input
    creating_curves_v0.links.new(curve_circle.outputs[0], reroute_010.inputs[0])
    #reroute_010.Output -> curve_to_mesh_001.Profile Curve
    creating_curves_v0.links.new(reroute_010.outputs[0], curve_to_mesh_001.inputs[1])
    #compare.Result -> reroute_011.Input
    creating_curves_v0.links.new(compare.outputs[0], reroute_011.inputs[0])
    #reroute_011.Output -> delete_geometry.Selection
    creating_curves_v0.links.new(reroute_011.outputs[0], delete_geometry.inputs[1])
    #transform_geometry_001.Geometry -> reroute_012.Input
    creating_curves_v0.links.new(transform_geometry_001.outputs[0], reroute_012.inputs[0])
    #reroute_012.Output -> instance_on_points_001.Points
    creating_curves_v0.links.new(reroute_012.outputs[0], instance_on_points_001.inputs[0])
    #curve_to_mesh_002.Mesh -> reroute_013.Input
    creating_curves_v0.links.new(curve_to_mesh_002.outputs[0], reroute_013.inputs[0])
    #group_input.Material -> set_material.Material
    creating_curves_v0.links.new(group_input.outputs[10], set_material.inputs[2])
    #reroute_013.Output -> join_geometry.Geometry
    creating_curves_v0.links.new(reroute_013.outputs[0], join_geometry.inputs[0])
    return creating_curves_v0

#initialize creating_curves node group
def creating_curves_node_group():
    creating_curves = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Creating curves")

    creating_curves.color_tag = 'NONE'
    creating_curves.description = ""
    

    creating_curves.is_modifier = True

    #creating_curves interface
    #Socket Geometry
    geometry_socket_1 = creating_curves.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'

    #Socket Count
    count_socket_1 = creating_curves.interface.new_socket(name = "Count", in_out='INPUT', socket_type = 'NodeSocketInt')
    count_socket_1.default_value = 12
    count_socket_1.min_value = 1
    count_socket_1.max_value = 2147483647
    count_socket_1.subtype = 'NONE'
    count_socket_1.attribute_domain = 'POINT'
    count_socket_1.description = "Number of curves "

    #Socket Size
    size_socket_1 = creating_curves.interface.new_socket(name = "Size", in_out='INPUT', socket_type = 'NodeSocketInt')
    size_socket_1.default_value = 4
    size_socket_1.min_value = 1
    size_socket_1.max_value = 2147483647
    size_socket_1.subtype = 'NONE'
    size_socket_1.attribute_domain = 'POINT'

    #Socket Offset
    offset_socket_1 = creating_curves.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketFloat')
    offset_socket_1.default_value = 0.800000011920929
    offset_socket_1.min_value = 0.0
    offset_socket_1.max_value = 1.0
    offset_socket_1.subtype = 'NONE'
    offset_socket_1.attribute_domain = 'POINT'

    #Socket Seed
    seed_socket_1 = creating_curves.interface.new_socket(name = "Seed", in_out='INPUT', socket_type = 'NodeSocketInt')
    seed_socket_1.default_value = 2
    seed_socket_1.min_value = -10000
    seed_socket_1.max_value = 10000
    seed_socket_1.subtype = 'NONE'
    seed_socket_1.attribute_domain = 'POINT'

    #Socket Grain
    grain_socket_1 = creating_curves.interface.new_socket(name = "Grain", in_out='INPUT', socket_type = 'NodeSocketFloat')
    grain_socket_1.default_value = 0.0
    grain_socket_1.min_value = 0.0
    grain_socket_1.max_value = 0.5
    grain_socket_1.subtype = 'NONE'
    grain_socket_1.attribute_domain = 'POINT'

    #Socket Resolution of curves
    resolution_of_curves_socket = creating_curves.interface.new_socket(name = "Resolution of curves", in_out='INPUT', socket_type = 'NodeSocketInt')
    resolution_of_curves_socket.default_value = 16
    resolution_of_curves_socket.min_value = 2
    resolution_of_curves_socket.max_value = 256
    resolution_of_curves_socket.subtype = 'NONE'
    resolution_of_curves_socket.attribute_domain = 'POINT'

    #Socket Radius of Tubes
    radius_of_tubes_socket_1 = creating_curves.interface.new_socket(name = "Radius of Tubes", in_out='INPUT', socket_type = 'NodeSocketFloat')
    radius_of_tubes_socket_1.default_value = 0.009999999776482582
    radius_of_tubes_socket_1.min_value = 9.999999747378752e-05
    radius_of_tubes_socket_1.max_value = 3.4028234663852886e+38
    radius_of_tubes_socket_1.subtype = 'DISTANCE'
    radius_of_tubes_socket_1.attribute_domain = 'POINT'

    #Socket Resolution of Tubes
    resolution_of_tubes_socket_1 = creating_curves.interface.new_socket(name = "Resolution of Tubes", in_out='INPUT', socket_type = 'NodeSocketInt')
    resolution_of_tubes_socket_1.default_value = 32
    resolution_of_tubes_socket_1.min_value = 3
    resolution_of_tubes_socket_1.max_value = 512
    resolution_of_tubes_socket_1.subtype = 'NONE'
    resolution_of_tubes_socket_1.attribute_domain = 'POINT'

    #Socket 1st Curve Segments
    _1st_curve_segments_socket_1 = creating_curves.interface.new_socket(name = "1st Curve Segments", in_out='INPUT', socket_type = 'NodeSocketInt')
    _1st_curve_segments_socket_1.default_value = 16
    _1st_curve_segments_socket_1.min_value = 1
    _1st_curve_segments_socket_1.max_value = 100000
    _1st_curve_segments_socket_1.subtype = 'NONE'
    _1st_curve_segments_socket_1.attribute_domain = 'POINT'

    #Socket 2nd Curve Segements
    _2nd_curve_segements_socket_1 = creating_curves.interface.new_socket(name = "2nd Curve Segements", in_out='INPUT', socket_type = 'NodeSocketInt')
    _2nd_curve_segements_socket_1.default_value = 16
    _2nd_curve_segements_socket_1.min_value = 1
    _2nd_curve_segements_socket_1.max_value = 100000
    _2nd_curve_segements_socket_1.subtype = 'NONE'
    _2nd_curve_segements_socket_1.attribute_domain = 'POINT'

    #Socket Material
    material_socket_1 = creating_curves.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    material_socket_1.attribute_domain = 'POINT'


    #initialize creating_curves nodes
    #node Group Output
    group_output_1 = creating_curves.nodes.new("NodeGroupOutput")
    group_output_1.name = "Group Output"
    group_output_1.is_active_output = True

    #node Group Input.003
    group_input_003 = creating_curves.nodes.new("NodeGroupInput")
    group_input_003.name = "Group Input.003"

    #node Group
    group = creating_curves.nodes.new("GeometryNodeGroup")
    group.name = "Group"
    group.node_tree = creating_curves_v0_node_group()




    #Set locations
    group_output_1.location = (2213.55810546875, 216.89891052246094)
    group_input_003.location = (1374.5816650390625, 252.07553100585938)
    group.location = (1846.0189208984375, 278.208251953125)

    #Set dimensions
    group_output_1.width, group_output_1.height = 140.0, 100.0
    group_input_003.width, group_input_003.height = 140.0, 100.0
    group.width, group.height = 140.0, 100.0

    #initialize creating_curves links
    #group.Geometry -> group_output_1.Geometry
    creating_curves.links.new(group.outputs[0], group_output_1.inputs[0])
    #group_input_003.Grain -> group.Grain
    creating_curves.links.new(group_input_003.outputs[4], group.inputs[4])
    #group_input_003.Count -> group.Count
    creating_curves.links.new(group_input_003.outputs[0], group.inputs[0])
    #group_input_003.Size -> group.Size
    creating_curves.links.new(group_input_003.outputs[1], group.inputs[1])
    #group_input_003.Seed -> group.Seed
    creating_curves.links.new(group_input_003.outputs[3], group.inputs[3])
    #group_input_003.Offset -> group.Offset
    creating_curves.links.new(group_input_003.outputs[2], group.inputs[2])
    #group_input_003.Resolution of curves -> group.Resolution of Curve
    creating_curves.links.new(group_input_003.outputs[5], group.inputs[5])
    #group_input_003.Radius of Tubes -> group.Radius of Tubes
    creating_curves.links.new(group_input_003.outputs[6], group.inputs[6])
    #group_input_003.Resolution of Tubes -> group.Resolution of Tubes
    creating_curves.links.new(group_input_003.outputs[7], group.inputs[7])
    #group_input_003.1st Curve Segments -> group.1st Curve Segments
    creating_curves.links.new(group_input_003.outputs[8], group.inputs[8])
    #group_input_003.2nd Curve Segements -> group.2nd Curve Segements
    creating_curves.links.new(group_input_003.outputs[9], group.inputs[9])
    #group_input_003.Material -> group.Material
    creating_curves.links.new(group_input_003.outputs[10], group.inputs[10])
    return creating_curves