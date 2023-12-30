from operator import neg


def fixed_end_forces(udl, pl, span, EI):
    # KEY: should there be separate FEF functions for point loads and UDLs?
    # KEY: add calcs for moments at midspan i.e at C
    if udl != 0 and pl[0] == 0:
        # Handout Case 3
        VAB_F = udl * span / 2
        MAB_F = neg(udl) * span**2 / 12

        VBA_F = neg(udl) * span / 2
        MBA_F = udl * span**2 / 12

        delta_mid = udl * span**4 / (384 * EI)
        return [VAB_F, MAB_F, VBA_F, MBA_F, delta_mid]

    elif udl == 0 and pl[0] != 0:
        # FIXME: verify for correctness
        # Handout Case 1
        a = pl[1]  # distance L to R i.e from origin x left
        b = span - a  # distance R to L
        P = pl[0]  # magnitude

        VAB_F = (P * b**2 / span**3) * ((2 * a) + span)
        MAB_F = neg(P) * a * b**2 / span**2

        VBA_F = (neg(P) * a**2 / span**3) * ((2 * b) + span)
        MBA_F = P * b * a**2 / span**2

        # Maximum deflection under the load
        delta_max = (P * a * b**2) / (6 * EI * span)

        return [VAB_F, MAB_F, VBA_F, MBA_F, delta_max]

    # elif udl != 0 and pl[0] != 0:
    #     # Check Kassimali
    #     MAB_F = 1.0
    #     VAB_F = 1.0
    #     MBA_F = 1.0
    #     VBA_F = 1.0
    #     delta_mid = 0.00
    #     return [VAB_F, MAB_F, VBA_F, MBA_F, delta_mid]

    else:
        return [0.0, 0.0, 0.0, 0.0, 0.0]
