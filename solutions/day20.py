import re
from tools.arithmetic import product
from tools.general import load_input

def parse_tiles(tile_data):

    tile_map = {}
    id_pattern = re.compile("^Tile ([0-9]+):$")

    for tile in tile_data.split('\n\n'):
        rows = tile.split('\n')
        tile_id = int(id_pattern.match(rows[0]).group(1))
        tile_map[tile_id] = rows[1:]

    return tile_map

def flip_horizontal_axis(tile):
    return tile[::-1]

def rotate_clockwise(tile):
    # Last row becomes first column, etc.
    return [''.join(row[x] for row in tile[::-1]) for x in range(len(tile[0]))]

def orientations(tile):
    for t in (tile, flip_horizontal_axis(tile)):
        yield t
        for _ in range(3):
            t = rotate_clockwise(t)
            yield t

def get_border(tile):
    # Ordered N, E, S, W
    return [tile[0], ''.join(row[-1] for row in tile), tile[-1], ''.join(row[0] for row in tile)]

def find_neighbours(all_tiles, tile_id):

    # Consider each edge forwards and backwards to allow for flipping and rotating
    edges = [i for e in get_border(all_tiles[tile_id]) for i in [e, e[::-1]]]
    nbrs  = []

    for i, other_tile in all_tiles.items():

        if i == tile_id:
            continue

        for e in get_border(other_tile):
            if e in edges:
                nbrs.append(i)
                break

    return nbrs

def find_corner_tiles(all_tiles):
    # Corners are tiles with exactly two neighbours
    return [tid for tid in all_tiles if len(find_neighbours(all_tiles, tid)) == 2]

def find_nw_corner(all_tiles):

    # Take an arbitrary corner tile and flip/rotate it into Northwest/top left orientation
    nwc = find_corner_tiles(all_tiles)[0]

    neighbour_edges = []
    for nbr_id in find_neighbours(all_tiles, nwc):
        neighbour_edges += [j for i in get_border(tiles[nbr_id]) for j in [i, i[::-1]]]

    for o in orientations(all_tiles[nwc]):
        _, s_edge, e_edge, _ = get_border(o)
        if (e_edge in neighbour_edges) and (s_edge in neighbour_edges):
            # Desired orientation
            all_tiles.pop(nwc)
            return o

    return None

def find_eastern_neighbour(all_tiles, tile):

    east_edge = ''.join(row[-1] for row in tile)

    for other_id, other_tile in all_tiles.items():

        for o in orientations(other_tile):
            west_edge = ''.join(row[0] for row in o)
            if west_edge == east_edge:
                all_tiles.pop(other_id)
                return o

    return None

def find_southern_neighbour(all_tiles, tile):

    south_edge = tile[-1]

    for other_id, other_tile in all_tiles.items():

        for o in orientations(other_tile):
            north_edge = o[0]
            if north_edge == south_edge:
                all_tiles.pop(other_id)
                return o

    return None

def complete_row(all_tiles, west_tile):

    row = []
    last_tile = west_tile

    while last_tile:

        row.append(last_tile)
        last_tile = find_eastern_neighbour(all_tiles, last_tile)

    return row

def strip_borders(tile):
    return [row[1:-1] for row in tile[1:-1]]

def complete_image(all_tiles, northwest_tile):

    assembled = []
    last_tile = northwest_tile

    while last_tile:

        assembled.append(complete_row(all_tiles, last_tile))
        last_tile = find_southern_neighbour(all_tiles, last_tile)

    # Strip borders and assemble into one giant "tile"
    image = []
    for row in assembled:
        for i in range(1, len(row[0]) - 1):
            image.append(''.join(tile[i][1:-1] for tile in row))

    return image

def encode_pattern(pattern):

    points = []

    for y, row in enumerate(pattern):
        for x, point in enumerate(row):
            if point == '#':
                points.append((x, y))

    return tuple(points)

def search_in_image(image, pattern):

    image_h, image_w = len(image), len(image[0])
    pttrn_h, pttrn_w = len(pattern), len(pattern[0])
    encoded = encode_pattern(pattern)
    matches = []

    for y in range(0, image_h - pttrn_h):
        for x in range(0, image_w - pttrn_w):
            for dx, dy in encoded:
                if image[y + dy][x + dx] != '#':
                    break
            else:
                matches.append((x, y))

    return matches

def count_sea_monsters(image):

    for o in orientations(image):
        monster_count = len(search_in_image(o, SEA_MONSTER))
        if monster_count > 0:
            return monster_count

    return 0

def water_roughness(image):
    return sum(row.count('#') for row in image) - count_sea_monsters(image) * sum(row.count('#') for row in SEA_MONSTER)


tiles = parse_tiles(load_input("day20.txt"))
corners = find_corner_tiles(tiles)

print(f"Part 1 => {product(corners)}")

nwc_tile = find_nw_corner(tiles)
recovered_image = complete_image(tiles, nwc_tile)

SEA_MONSTER = (
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   "
)

print(f"Part 2 => {water_roughness(recovered_image)}")
