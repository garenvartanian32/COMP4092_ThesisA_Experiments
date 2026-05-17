import json

def save_configuration(opened_projects, tree_widget_state, is_dock_widget_visible):
    configuration = {
        "opened_projects": opened_projects,
        "tree_widget_state": tree_widget_state,
        "is_dock_widget_visible": is_dock_widget_visible
    }
    with open("configuration.json", "w") as f:
        json.dump(configuration, f)
