def transition(states_dict, current_state, input_signal):
    next_state = states_dict[current_state][input_signal]['next_state']
    output = states_dict[current_state][input_signal]['output']
    return (next_state, output)
