def read_pos(pos):
    pos = pos.split(",")
    return int(pos[0]), int(pos[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])
