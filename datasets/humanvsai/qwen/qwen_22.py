def get_purged_review_history_for(brain_or_object):
    workflow = brain_or_object.get_workflow()
    allowed_actions = workflow.get_allowed_actions()
    review_history = brain_or_object.get_review_history()
    purged_review_history = [entry for entry in review_history if entry['action'] in allowed_actions or entry['action'] is None]
    return purged_review_history