def lost_sheep(friday, saturday, total):
    returned_sheep = sum(friday) + sum(saturday)
    lost_sheep = total - returned_sheep
    return lost_sheep
