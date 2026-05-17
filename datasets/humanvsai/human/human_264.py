def get_nn_data(self, structure, n, length=None):
        length = length or self.fingerprint_length
        # determine possible bond targets
        target = None
        if self.cation_anion:
            target = []
            m_oxi = structure[n].specie.oxi_state
            for site in structure:
                if site.specie.oxi_state * m_oxi <= 0:  # opposite charge
                    target.append(site.specie)
            if not target:
                raise ValueError(
                    "No valid targets for site within cation_anion constraint!")
        # get base VoronoiNN targets
        cutoff = self.search_cutoff
        vnn = VoronoiNN(weight="solid_angle", targets=target, cutoff=cutoff)
        nn = vnn.get_nn_info(structure, n)
        # solid angle weights can be misleading in open / porous structures
        # adjust weights to correct for this behavior
        if self.porous_adjustment:
            for x in nn:
                x["weight"] *= x["poly_info"][
                                   "solid_angle"] / x["poly_info"]["area"]
        # adjust solid angle weight based on electronegativity difference
        if self.x_diff_weight > 0:
            for entry in nn:
                X1 = structure[n].specie.X
                X2 = entry["site"].specie.X
                if math.isnan(X1) or math.isnan(X2):
                    chemical_weight = 1
                else:
                    # note: 3.3 is max deltaX between 2 elements
                    chemical_weight = 1 + self.x_diff_weight * \
                                      math.sqrt(abs(X1 - X2) / 3.3)
                entry["weight"] = entry["weight"] * chemical_weight
        # sort nearest neighbors from highest to lowest weight
        nn = sorted(nn, key=lambda x: x["weight"], reverse=True)
        if nn[0]["weight"] == 0:
            return self.transform_to_length(self.NNData([], {0: 1.0}, {0: []}),
                                            length)
        # renormalize weights so the highest weight is 1.0
        highest_weight = nn[0]["weight"]
        for entry in nn:
            entry["weight"] = entry["weight"] / highest_weight
        # adjust solid angle weights based on distance
        if self.distance_cutoffs:
            r1 = self._get_radius(structure[n])
            for entry in nn:
                r2 = self._get_radius(entry["site"])
                if r1 > 0 and r2 > 0:
                    d = r1 + r2
                else:
                    warnings.warn(
                        "CrystalNN: cannot locate an appropriate radius, "
                        "covalent or atomic radii will be used, this can lead "
                        "to non-optimal results.")
                    d = CrystalNN._get_default_radius(structure[n]) + \
                        CrystalNN._get_default_radius(entry["site"])
                dist = np.linalg.norm(
                    structure[n].coords - entry["site"].coords)
                dist_weight = 0
                cutoff_low = d + self.distance_cutoffs[0]
                cutoff_high = d + self.distance_cutoffs[1]
                if dist <= cutoff_low:
                    dist_weight = 1
                elif dist < cutoff_high:
                    dist_weight = (math.cos((dist - cutoff_low) / (
                            cutoff_high - cutoff_low) * math.pi) + 1) * 0.5
                entry["weight"] = entry["weight"] * dist_weight
        # sort nearest neighbors from highest to lowest weight
        nn = sorted(nn, key=lambda x: x["weight"], reverse=True)
        if nn[0]["weight"] == 0:
            return self.transform_to_length(self.NNData([], {0: 1.0}, {0: []}),
                                            length)
        for entry in nn:
            entry["weight"] = round(entry["weight"], 3)
            del entry["poly_info"]  # trim
        # remove entries with no weight
        nn = [x for x in nn if x["weight"] > 0]
        # get the transition distances, i.e. all distinct weights
        dist_bins = []
        for entry in nn:
            if not dist_bins or dist_bins[-1] != entry["weight"]:
                dist_bins.append(entry["weight"])
        dist_bins.append(0)
        # main algorithm to determine fingerprint from bond weights
        cn_weights = {}  # CN -> score for that CN
        cn_nninfo = {}  # CN -> list of nearneighbor info for that CN
        for idx, val in enumerate(dist_bins):
            if val != 0:
                nn_info = []
                for entry in nn:
                    if entry["weight"] >= val:
                        nn_info.append(entry)
                cn = len(nn_info)
                cn_nninfo[cn] = nn_info
                cn_weights[cn] = self._semicircle_integral(dist_bins, idx)
        # add zero coord
        cn0_weight = 1.0 - sum(cn_weights.values())
        if cn0_weight > 0:
            cn_nninfo[0] = []
            cn_weights[0] = cn0_weight
        return self.transform_to_length(self.NNData(nn, cn_weights, cn_nninfo),
                                        length)