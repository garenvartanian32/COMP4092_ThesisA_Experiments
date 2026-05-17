def mesh_instance(site_assets: dict) -> tuple:
    from mesh import Mesh
    
    mesh = Mesh()
    assets_by_site = []
    
    for site_name, assets in site_assets.items():
        assets_by_site.append((site_name, len(assets)))
        for asset in assets:
            mesh.add_asset(asset)
    
    return mesh, assets_by_site
