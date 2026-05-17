def stream_reports_to_logs(reports):
    """
    Stream reports to application logs

    :param reports: list of reports to be streamed to logs
    """
    import logging
    
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    for report in reports:
        logging.info(report)