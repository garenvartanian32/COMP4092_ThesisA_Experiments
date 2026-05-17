def get_review_history(workflow, actions, states, object):
    workflow_actions = workflow.get_actions()
    workflow_states = workflow.get_states()
    matched_actions = [a for a in actions if a in workflow_actions or a is None]
    matched_states = [s for s in states if s in workflow_states or s is None]
    return object.get_review_history(actions=matched_actions, states=matched_states)
