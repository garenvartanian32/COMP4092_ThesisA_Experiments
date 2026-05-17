def convert_coordinates_to_displacements(coordinates):
    displacements = []
    for i in range(len(coordinates)-1):
        x1,y1 = coordinates[i]
        x2,y2 = coordinates[i+1]
        displacement = ((x2-x1)**2 + (y2-y1)**2)**0.5
        displacements.append(displacement)
    return displacements
