import beta_table
import beta_shears
from interpoleit import interpoleit


class Slab:
    def __init__(self, ly, lx):
        self.ly = ly  # longer side
        self.lx = lx  # shorter side
        self.ly_lx = ly / lx  # ratio

    def assumed_depth(self, assumed_depth):
        """Assumed depth in metres"""
        self.assumed_depth = assumed_depth
        return self.assumed_depth
        # return assumed_depth

    def which_way(self):
        # Return string or return boolean?
        if self.ly_lx > 2.0:
            return "OneWay"
        else:
            return "TwoWay"

    def area(self):
        return self.ly * self.lx

    # def self_weight

    def restraint(self, restraint):
        if restraint == "SimplySupported":
            return "SimplySupported"
        elif restraint == "Restrained":
            return "Restrained"
        else:
            return ValueError


class OneWaySlab(Slab):
    def __init__(self, ly, lx):
        super().__init__(ly, lx)

    def beta_sx(self, ly_lx):
        pass

    def beta_sy(self, ly_lx):
        pass

    def beta_vx(self, slab_def):
        pass

    def beta_vy(self, slab_def):
        pass

    def actions(self, actions):
        pass

    def moments(self, actions):
        pass

    def shears(self, actions):
        pass


class TwoWaySlab(Slab):
    def __init__(self, ly, lx):
        super().__init__(ly, lx)

    def beta_sy(self, slab_def):
        slab_def_map = {
            "A": beta_table.slab_type_list[0],
            "B": beta_table.slab_type_list[1],
            "C": beta_table.slab_type_list[2],
            "D": beta_table.slab_type_list[3],
            "E": beta_table.slab_type_list[4],
            "F": beta_table.slab_type_list[5],
            "G": beta_table.slab_type_list[6],
            "H": beta_table.slab_type_list[7],
            "I": beta_table.slab_type_list[8],
        }

        slab_type = slab_def_map[slab_def.upper()]

        beta_sy = beta_table.beta[slab_type]["long"]
        if beta_sy:
            beta_sy_neg_M, beta_sy_pos_M = beta_sy
            self.beta_sy_neg_M, self.beta_sy_pos_M = beta_sy
            return [beta_sy_neg_M, beta_sy_pos_M]

    def beta_sx(self, slab_def):
        """
        Values for `slab_def` argument for the `beta_sx` function are:
        \n"a" - Interior panels
        \n"b" - One short edge discontinuous
        \n"c" - One long edge discontinuous
        \n"d" - Two adjacent edges discontinuous
        \n"e" - Two short edges discontinuous
        \n"f" - Two long edges discontinuous
        \n"g" - Three edges discontinuous (one long edge continuous)
        \n"h" - Three edges discontinuous (one short edge continuous)
        \n"i" - Four edges discontinuous
        """

        slab_def_map = {
            "A": beta_table.slab_type_list[0],
            "B": beta_table.slab_type_list[1],
            "C": beta_table.slab_type_list[2],
            "D": beta_table.slab_type_list[3],
            "E": beta_table.slab_type_list[4],
            "F": beta_table.slab_type_list[5],
            "G": beta_table.slab_type_list[6],
            "H": beta_table.slab_type_list[7],
            "I": beta_table.slab_type_list[8],
        }

        slab_type = slab_def_map[slab_def.upper()]

        bound_list = [
            1.0,
            1.1,
            1.2,
            1.3,
            1.4,
            1.5,
            1.75,
            2.0,
        ]

        for i in range(len(bound_list) - 1):
            if bound_list[i] <= self.ly_lx <= bound_list[i + 1]:
                lower_bound = bound_list[i]
                upper_bound = bound_list[i + 1]

                lower_pos_M = beta_table.beta[slab_type][str(lower_bound)][1]
                upper_neg_M = beta_table.beta[slab_type][str(upper_bound)][0]
                lower_neg_M = beta_table.beta[slab_type][str(lower_bound)][0]
                upper_pos_M = beta_table.beta[slab_type][str(upper_bound)][1]
                beta_sx_neg_M = interpoleit(
                    lower_bound, upper_bound, self.ly_lx, lower_neg_M, upper_neg_M
                )
                beta_sx_pos_M = interpoleit(
                    lower_bound, upper_bound, self.ly_lx, lower_pos_M, upper_pos_M
                )
                self.beta_sx_neg_M = beta_sx_neg_M
                self.beta_sx_pos_M = beta_sx_pos_M

                return [round(beta_sx_neg_M, 4), round(beta_sx_pos_M, 4)]

    def beta_vx(self, slab_def):
        slab_def_map = {
            "A": beta_shears.panel_types_list[0],
            "B": beta_shears.panel_types_list[1],
            "C": beta_shears.panel_types_list[2],
            "D": beta_shears.panel_types_list[3],
            "E": beta_shears.panel_types_list[4],
            "F": beta_shears.panel_types_list[5],
            "G": beta_shears.panel_types_list[6],
            "H": beta_shears.panel_types_list[7],
            "I": beta_shears.panel_types_list[8],
        }

        slab_type = slab_def_map[slab_def.upper()]

        bounds_list = [
            1.0,
            1.1,
            1.2,
            1.3,
            1.4,
            1.5,
            1.75,
            2.0,
        ]

        for i in range(len(bounds_list) - 1):
            if bounds_list[i] <= self.ly_lx <= bounds_list[i + 1]:
                lower_bound = bounds_list[i]
                upper_bound = bounds_list[i + 1]

                lower_disc_V = beta_shears.beta[slab_type][str(lower_bound)][1]
                upper_cont_V = beta_shears.beta[slab_type][str(upper_bound)][0]
                lower_cont_V = beta_shears.beta[slab_type][str(lower_bound)][0]
                upper_disc_V = beta_shears.beta[slab_type][str(upper_bound)][1]
                beta_vx_cont_V = interpoleit(
                    lower_bound, upper_bound, self.ly_lx, lower_cont_V, upper_cont_V
                )
                beta_vx_disc_V = interpoleit(
                    lower_bound, upper_bound, self.ly_lx, lower_disc_V, upper_disc_V
                )
                self.beta_vx_cont_V = beta_vx_cont_V
                self.beta_vx_disc_V = beta_vx_disc_V

                return [round(beta_vx_cont_V, 4), round(beta_vx_disc_V, 4)]

    def beta_vy(self, slab_def):
        slab_def_map = {
            "A": beta_shears.panel_types_list[0],
            "B": beta_shears.panel_types_list[1],
            "C": beta_shears.panel_types_list[2],
            "D": beta_shears.panel_types_list[3],
            "E": beta_shears.panel_types_list[4],
            "F": beta_shears.panel_types_list[5],
            "G": beta_shears.panel_types_list[6],
            "H": beta_shears.panel_types_list[7],
            "I": beta_shears.panel_types_list[8],
        }

        slab_type = slab_def_map[slab_def.upper()]
        beta_vy = beta_shears.beta[slab_type]["long"]
        if beta_vy:
            beta_vy_cont_V, beta_vy_disc_V = beta_vy
            self.beta_vy_cont_V = beta_vy_cont_V
            self.beta_vy_disc_V = beta_vy_disc_V
            return [beta_vy_cont_V, beta_vy_disc_V]

    def actions(self, actions):
        self.actions = actions
        return actions

    def moments(self):
        # short span
        m_sx_support = -self.beta_sx_neg_M * self.actions * self.lx**2.0
        m_sx_midspan = self.beta_sx_pos_M * self.actions * self.lx**2.0

        # long span
        m_sy_support = -self.beta_sy_neg_M * self.actions * self.lx**2.0
        m_sy_midspan = self.beta_sy_pos_M * self.actions * self.lx**2.0

        self.m_sx = [m_sx_support, m_sx_midspan]
        self.m_sy = [m_sy_support, m_sy_midspan]

        return [self.m_sx, self.m_sy]

    def shears(self):
        # short span
        v_sx_support = -self.beta_vx_cont_V * self.actions * self.lx
        v_sx_midspan = self.beta_vx_disc_V * self.actions * self.lx

        # long span
        v_sy_support = -self.beta_vy_cont_V * self.actions * self.lx
        v_sy_midspan = self.beta_vy_disc_V * self.actions * self.lx

        self.v_sx = [v_sx_support, v_sx_midspan]
        self.v_sy = [v_sy_support, v_sy_midspan]

        return [self.v_sx, self.v_sy]
