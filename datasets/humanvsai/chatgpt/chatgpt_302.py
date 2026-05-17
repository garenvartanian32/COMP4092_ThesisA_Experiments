def replace_broker(replica_set, source_broker, destination_broker):
    for i in range(len(replica_set)):
        if replica_set[i] == source_broker:
            replica_set[i] = destination_broker
    return replica_set
