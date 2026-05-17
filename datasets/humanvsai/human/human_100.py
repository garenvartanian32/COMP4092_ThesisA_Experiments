def get_mesh_assets_by_site(self):
        assets_by_loc = general.groupby(self, key=lambda a: a.location)
        mesh = geo.Mesh.from_coords(list(assets_by_loc))
        assets_by_site = [
            assets_by_loc[lonlat] for lonlat in zip(mesh.lons, mesh.lats)]
        return mesh, assets_by_site