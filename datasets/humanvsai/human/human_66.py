def query_paths(
        service_config: Dict[str, Any],
        our_address: Address,
        privkey: bytes,
        current_block_number: BlockNumber,
        token_network_address: Union[TokenNetworkAddress, TokenNetworkID],
        route_from: InitiatorAddress,
        route_to: TargetAddress,
        value: PaymentAmount,
) -> List[Dict[str, Any]]:
    max_paths = service_config['pathfinding_max_paths']
    url = service_config['pathfinding_service_address']
    payload = {
        'from': to_checksum_address(route_from),
        'to': to_checksum_address(route_to),
        'value': value,
        'max_paths': max_paths,
    }
    offered_fee = service_config.get('pathfinding_fee', service_config['pathfinding_max_fee'])
    scrap_existing_iou = False
    for retries in reversed(range(MAX_PATHS_QUERY_ATTEMPTS)):
        payload['iou'] = create_current_iou(
            config=service_config,
            token_network_address=token_network_address,
            our_address=our_address,
            privkey=privkey,
            block_number=current_block_number,
            offered_fee=offered_fee,
            scrap_existing_iou=scrap_existing_iou,
        )
        try:
            return post_pfs_paths(
                url=url,
                token_network_address=token_network_address,
                payload=payload,
            )
        except ServiceRequestIOURejected as error:
            code = error.error_code
            if retries == 0 or code in (PFSError.WRONG_IOU_RECIPIENT, PFSError.DEPOSIT_TOO_LOW):
                raise
            elif code in (PFSError.IOU_ALREADY_CLAIMED, PFSError.IOU_EXPIRED_TOO_EARLY):
                scrap_existing_iou = True
            elif code == PFSError.INSUFFICIENT_SERVICE_PAYMENT:
                if offered_fee < service_config['pathfinding_max_fee']:
                    offered_fee = service_config['pathfinding_max_fee']
                    # TODO: Query the PFS for the fee here instead of using the max fee
                else:
                    raise
            log.info(f'PFS rejected our IOU, reason: {error}. Attempting again.')
    # If we got no results after MAX_PATHS_QUERY_ATTEMPTS return empty list of paths
    return list()