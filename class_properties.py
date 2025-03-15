class classproperties():
    def __init__(self):
        self.geometrynode_name = "Creating curves"
        self.variables_and_sockets = {
            "count_sizeandshape": "Socket_1",
            "size_sizeandshape": "Socket_2",
            "offset_sizeandshape": "Socket_3",
            "seed_sizeandshape": "Socket_4",
            "grain_sizeandshape": "Socket_5",
            "resolution_of_curves_curves": "Socket_6",
            "radius_of_tubes_curves": "Socket_7",
            "resolution_of_tubes_curves": "Socket_8",
            "first_curve_segments_curves": "Socket_9",
            "second_curve_segments_curves": "Socket_10",
            "material_curves": "Socket_11"
        }
    def get_geometrynode_name(self):
        return self.geometrynode_name
    
    def get_variable_and_sockets(self):
        return self.variables_and_sockets
        