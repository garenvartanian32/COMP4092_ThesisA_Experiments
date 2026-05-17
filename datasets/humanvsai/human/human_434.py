def coordination_geometry_symmetry_measures_separation_plane_optim(self,
                                                                       coordination_geometry,
                                                                       separation_plane_algo,
                                                                       points_perfect=None,
                                                                       nb_set=None,
                                                                       optimization=None):
        if optimization == 2:
            cgcsmoptim = self._cg_csm_separation_plane_optim2
        elif optimization == 1:
            cgcsmoptim = self._cg_csm_separation_plane_optim1
        else:
            raise ValueError('Optimization should be 1 or 2')
        cn = len(self.local_geometry.coords)
        permutations = list()
        permutations_symmetry_measures = list()
        algos = list()
        perfect2local_maps = list()
        local2perfect_maps = list()
        if separation_plane_algo.separation in nb_set.separations:
            for sep_indices, (local_plane, npsep) in nb_set.separations[separation_plane_algo.separation].items():
                cgsm = cgcsmoptim(coordination_geometry=coordination_geometry,
                                  sepplane=separation_plane_algo,
                                  local_plane=local_plane,
                                  points_perfect=points_perfect,
                                  separation_indices=npsep)
                csm, perm, algo, cgsm_stop_search = cgsm[0], cgsm[1], cgsm[2], cgsm[3]
                permutations_symmetry_measures.extend(csm)
                permutations.extend(perm)
                for thisperm in perm:
                    p2l = {}
                    l2p = {}
                    for i_p, pp in enumerate(thisperm):
                        p2l[i_p] = pp
                        l2p[pp] = i_p
                    perfect2local_maps.append(p2l)
                    local2perfect_maps.append(l2p)
                algos.extend(algo)
        # Get the local planes and separations up to 3 points
        for npoints in range(self.allcg.minpoints[cn], min(self.allcg.maxpoints[cn], 3) + 1):
            for ipoints_combination in itertools.combinations(
                    range(self.local_geometry.cn), npoints):
                if ipoints_combination in nb_set.local_planes:
                    continue
                # Set up new plane
                nb_set.local_planes[ipoints_combination] = None
                points_combination = [self.local_geometry.coords[ip] for ip in ipoints_combination]
                if npoints == 2:
                    if collinear(points_combination[0], points_combination[1],
                                 self.local_geometry.central_site,
                                 tolerance=0.25):
                        continue
                    plane = Plane.from_3points(points_combination[0],
                                               points_combination[1],
                                               self.local_geometry.central_site)
                elif npoints == 3:
                    if collinear(points_combination[0], points_combination[1],
                                 points_combination[2], tolerance=0.25):
                        continue
                    plane = Plane.from_3points(points_combination[0],
                                               points_combination[1],
                                               points_combination[2])
                elif npoints > 3:
                    plane = Plane.from_npoints(points_combination,
                                               best_fit='least_square_distance')
                else:
                    raise ValueError(
                        'Wrong number of points to initialize separation plane')
                # Takes a lot of time and happens rarely ...
                # if any([plane.is_same_plane_as(plane2) for comb2, plane2 in nb_set.local_planes.items() if plane2 is not None]):
                #     continue
                nb_set.local_planes[ipoints_combination] = plane
                # Get the separations for this plane
                # TODO: check sensitivity to delta/delta_factor parameter
                dig = plane.distances_indices_groups(points=self.local_geometry._coords, delta_factor=0.1,
                                                     sign=True)
                grouped_indices = dig[2]
                new_seps = []
                for ng in range(1, len(grouped_indices) + 1):
                    inplane = list(itertools.chain(*grouped_indices[:ng]))
                    if len(inplane) > self.allcg.maxpoints_inplane[cn]:
                        break
                    inplane = [ii[0] for ii in inplane]
                    outplane = list(itertools.chain(*grouped_indices[ng:]))
                    s1 = [ii_sign[0] for ii_sign in outplane if ii_sign[1] < 0]
                    s2 = [ii_sign[0] for ii_sign in outplane if ii_sign[1] > 0]
                    separation = sort_separation_tuple([s1, inplane, s2])
                    sep = tuple([len(gg) for gg in separation])
                    if sep not in self.allcg.separations_cg[cn]:
                        continue
                    if sep not in nb_set.separations:
                        nb_set.separations[sep] = {}
                    mysep = [np.array(ss, dtype=np.int8) for ss in separation]
                    nb_set.separations[sep][separation] = (plane, mysep)
                    if sep == separation_plane_algo.separation:
                        new_seps.append(mysep)
                for separation_indices in new_seps:
                    cgsm = cgcsmoptim(coordination_geometry=coordination_geometry,
                                      sepplane=separation_plane_algo,
                                      local_plane=plane,
                                      points_perfect=points_perfect,
                                      separation_indices=separation_indices)
                    csm, perm, algo, cgsm_stop_search = cgsm[0], cgsm[1], cgsm[2], cgsm[3]
                    permutations_symmetry_measures.extend(csm)
                    permutations.extend(perm)
                    for thisperm in perm:
                        p2l = {}
                        l2p = {}
                        for i_p, pp in enumerate(thisperm):
                            p2l[i_p] = pp
                            l2p[pp] = i_p
                        perfect2local_maps.append(p2l)
                        local2perfect_maps.append(l2p)
                    algos.extend(algo)
        if len(permutations_symmetry_measures) == 0:
            return self.coordination_geometry_symmetry_measures_fallback_random(
                coordination_geometry,
                points_perfect=points_perfect)
        return permutations_symmetry_measures, permutations, algos, local2perfect_maps, perfect2local_maps