def get_purged_review_history_for(brain_or_object):
    history = review_history_cache.get(api.get_uid(brain_or_object), [])
    # Boil out those actions not supported by object's current workflow
    available_actions = get_workflow_actions_for(brain_or_object)
    history = filter(lambda action: action["action"] in available_actions
                                    or action["action"] is None, history)
    # Boil out those states not supported by object's current workflow
    available_states = get_workflow_states_for(brain_or_object)
    history = filter(lambda act: act["review_state"] in available_states,
                     history)
    # If no meaning history found, create a default one for initial state
    if not history:
        history = create_initial_review_history(brain_or_object)
    return history