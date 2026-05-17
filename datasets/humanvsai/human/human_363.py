def orthologize_context(
    orthologize_target: str, annotations: Mapping[str, Any]
) -> Mapping[str, Any]:
    url = f'{config["bel_api"]["servers"]["api_url"]}/terms/{orthologize_target}'
    r = utils.get_url(url)
    species_label = r.json().get("label", "unlabeled")
    orthologized_from = {}
    for idx, annotation in enumerate(annotations):
        if annotation["type"] == "Species":
            orthologized_from = {"id": annotation["id"], "label": annotation["label"]}
            annotations[idx] = {"type": "Species", "id": orthologize_target, "label": species_label}
    if "id" in orthologized_from:
        annotations.append(
            {
                "type": "OrigSpecies",
                "id": f'Orig-{orthologized_from["id"]}',
                "label": f'Orig-{orthologized_from["label"]}',
            }
        )
    return annotations