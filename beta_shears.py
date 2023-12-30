
panel_types = {
    "type_a": "Four edges continuous",
    "type_b": "One short edge discontinuous",
    "type_c": "One long edge discontinuous",
    "type_d": "Two adjacent edges discontinuous",
    "type_e": "Two short edges discontinuous",
    "type_f": "Two long edges discontinuous",
    "type_g": "Three edges discontinuous (one long edge continuous)",
    "type_h": "Three edges discontinuous (one short edge continuous)",
    "type_i": "Four edges discontinuous",
}
# should be combined into a good json with the bending moment table

panel_types_list = [
    "Four edges continuous",
    "One short edge discontinuous",
    "One long edge discontinuous",
    "Two adjacent edges discontinuous",
    "Two short edges discontinuous",
    "Two long edges discontinuous",
    "Three edges discontinuous (one long edge continuous)",
    "Three edges discontinuous (one short edge continuous)",
    "Four edges discontinuous",
]

panel_types_map = {
    "A": panel_types_list[0],
    "B": panel_types_list[1],
    "C": panel_types_list[2],
    "D": panel_types_list[3],
    "E": panel_types_list[4],
    "F": panel_types_list[5],
    "G": panel_types_list[6],
    "H": panel_types_list[7],
    "I": panel_types_list[8],
}

(
    type_a,
    type_b,
    type_c,
    type_d,
    type_e,
    type_f,
    type_g,
    type_h,
    type_i,
) = panel_types_list


# Values unpack to [continuous, discontinuous]
beta = {
    type_a: {
        "type": type_a,
        "1.0": [0.33, 0.0],
        "1.1": [0.36, 0.0],
        "1.2": [0.39, 0.0],
        "1.3": [0.41, 0.0],
        "1.4": [0.43, 0.0],
        "1.5": [0.45, 0.0],
        "1.75": [0.48, 0.0],
        "2.0": [0.50, 0.0],
        "long": [0.33, 0.0],
    },
    type_b: {
        "type": type_b,
        "1.0": [0.36, 0.0],
        "1.1": [0.39, 0.0],
        "1.2": [0.42, 0.0],
        "1.3": [0.44, 0.0],
        "1.4": [0.45, 0.0],
        "1.5": [0.47, 0.0],
        "1.75": [0.50, 0.0],
        "2.0": [0.52, 0.0],
        "long": [0.36, 0.24],
    },
    type_c: {
        "type": type_c,
        "1.0": [0.36, 0.24],
        "1.1": [0.40, 0.27],
        "1.2": [0.44, 0.29],
        "1.3": [0.47, 0.31],
        "1.4": [0.49, 0.32],
        "1.5": [0.51, 0.34],
        "1.75": [0.55, 0.36],
        "2.0": [0.59, 0.38],
        "long": [0.36, 0.0],
    },
    type_d: {
        "type": type_d,
        "1.0": [0.40, 0.26],
        "1.1": [0.44, 0.39],
        "1.2": [0.47, 0.31],
        "1.3": [0.50, 0.33],
        "1.4": [0.52, 0.34],
        "1.5": [0.54, 0.35],
        "1.75": [0.57, 0.48],
        "2.0": [0.60, 0.40],
        "long": [0.40, 0.26],
    },
    type_e: {
        "type": type_e,
        "1.0": [0.26, 0.0],
        "1.1": [0.30, 0.0],
        "1.2": [0.33, 0.0],
        "1.3": [0.36, 0.0],
        "1.4": [0.38, 0.0],
        "1.5": [0.40, 0.0],
        "1.75": [0.44, 0.0],
        "2.0": [0.47, 0.0],
        "long": [0.0, 0.40],
    },
    type_f: {
        "type": type_f,
        "1.0": [0.0, 0.26],
        "1.1": [0.0, 0.30],
        "1.2": [0.0, 0.33],
        "1.3": [0.0, 0.36],
        "1.4": [0.0, 0.38],
        "1.5": [0.0, 0.40],
        "1.75": [0.0, 0.44],
        "2.0": [0.0, 0.47],
        "long": [0.40, 0.0],
    },
    type_g: {
        "type": type_g,
        "1.0": [0.45, 0.30],
        "1.1": [0.48, 0.32],
        "1.2": [0.51, 0.34],
        "1.3": [0.53, 0.35],
        "1.4": [0.55, 0.36],
        "1.5": [0.57, 0.37],
        "1.75": [0.60, 0.39],
        "2.0": [0.63, 0.41],
        "long": [0.0, 0.29],
    },
    type_h: {
        "type": type_h,
        "1.0": [0.0, 0.29],
        "1.1": [0.0, 0.33],
        "1.2": [0.0, 0.36],
        "1.3": [0.0, 0.38],
        "1.4": [0.0, 0.40],
        "1.5": [0.0, 0.42],
        "1.75": [0.0, 0.45],
        "2.0": [0.0, 0.48],
        "long": [0.45, 0.30],
    },
    type_i: {
        "type": type_i,
        "1.0": [0.0, 0.33],
        "1.1": [0.0, 0.36],
        "1.2": [0.0, 0.39],
        "1.3": [0.0, 0.41],
        "1.4": [0.0, 0.43],
        "1.5": [0.0, 0.45],
        "1.75": [0.0, 0.48],
        "2.0": [0.0, 0.50],
        "long": [0.0, 0.33],
    },
}


# print(beta[type_a]["type"])
