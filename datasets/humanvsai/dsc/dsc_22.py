def get_purged_review_history_for(brain_or_object):
    # Assuming brain_or_object has a method called get_workflow()
    # and a property called review_history
    workflow = brain_or_object.get_workflow()
    review_history = brain_or_object.review_history

    # Filter the review history
    purged_review_history = [
        entry for entry in review_history 
        if entry.action in workflow or entry.action is None
    ]

    return purged_review_history