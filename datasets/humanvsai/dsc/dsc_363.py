def orthologize_context(context, target):
    """
    Orthologize context

    Replace Species context with new orthologize target and add a annotation type of OrthologizedFrom
    """
    # Replace context with target
    context = target

    # Add annotation type
    annotation_type = "OrthologizedFrom"

    return context, annotation_type