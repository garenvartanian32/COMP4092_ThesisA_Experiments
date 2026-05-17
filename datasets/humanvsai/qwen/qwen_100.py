def get_mesh_assets_by_site(self):
    mesh = self.mesh
    assets_by_site = []
    for site in mesh.sites:
        assets = site.assets
        assets_by_site.append((site.name, assets))
    return (mesh, assets_by_site)