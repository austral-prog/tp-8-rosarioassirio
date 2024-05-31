def get_coordinate(record):
    treasure, coordinate = record
    return = coordinate

def convert_coordinate(coordinate):
    return coordinate[0], coordinate[1]

def create_record(azara_record, rui_record):
    tesoro, coordenada = azara_record
    ubicacion, coordenada1, cuadrante = rui_record
    if convert_coodinate(coordenada) == rui_record[1]:
        return azara_record + rui_record
    else:
        return "not a match"
