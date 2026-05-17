def inventory(host, port, time, report_every_n_tags, antennas, tx_power,
              tari, session, mode_identifier,
              tag_population, reconnect, tag_filter_mask,
              impinj_extended_configuration,
              impinj_search_mode, impinj_reports, impinj_fixed_freq):
    # XXX band-aid hack to provide many args to _inventory.main
    Args = namedtuple('Args', ['host', 'port', 'time', 'every_n', 'antennas',
                               'tx_power', 'tari', 'session',
                               'population', 'mode_identifier',
                               'reconnect', 'tag_filter_mask',
                               'impinj_extended_configuration',
                               'impinj_search_mode',
                               'impinj_reports',
                               'impinj_fixed_freq'])
    args = Args(host=host, port=port, time=time, every_n=report_every_n_tags,
                antennas=antennas, tx_power=tx_power,
                tari=tari, session=session, population=tag_population,
                mode_identifier=mode_identifier,
                reconnect=reconnect, tag_filter_mask=tag_filter_mask,
                impinj_extended_configuration=impinj_extended_configuration,
                impinj_search_mode=impinj_search_mode,
                impinj_reports=impinj_reports,
                impinj_fixed_freq=impinj_fixed_freq)
    logger.debug('inventory args: %s', args)
    _inventory.main(args)