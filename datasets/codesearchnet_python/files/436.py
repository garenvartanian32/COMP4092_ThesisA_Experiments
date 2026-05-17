def standardize_jira_ref(text):
    """
    Standardize the [SPARK-XXXXX] [MODULE] prefix
    Converts "[SPARK-XXX][mllib] Issue", "[MLLib] SPARK-XXX. Issue" or "SPARK XXX [MLLIB]: Issue" to
    "[SPARK-XXX][MLLIB] Issue"

    >>> standardize_jira_ref(
    ...     "[SPARK-5821] [SQL] ParquetRelation2 CTAS should check if delete is successful")
    '[SPARK-5821][SQL] ParquetRelation2 CTAS should check if delete is successful'
    >>> standardize_jira_ref(
    ...     "[SPARK-4123][Project Infra][WIP]: Show new dependencies added in pull requests")
    '[SPARK-4123][PROJECT INFRA][WIP] Show new dependencies added in pull requests'
    >>> standardize_jira_ref("[MLlib] Spark  5954: Top by key")
    '[SPARK-5954][MLLIB] Top by key'
    >>> standardize_jira_ref("[SPARK-979] a LRU scheduler for load balancing in TaskSchedulerImpl")
    '[SPARK-979] a LRU scheduler for load balancing in TaskSchedulerImpl'
    >>> standardize_jira_ref(
    ...     "SPARK-1094 Support MiMa for reporting binary compatibility across versions.")
    '[SPARK-1094] Support MiMa for reporting binary compatibility across versions.'
    >>> standardize_jira_ref("[WIP]  [SPARK-1146] Vagrant support for Spark")
    '[SPARK-1146][WIP] Vagrant support for Spark'
    >>> standardize_jira_ref(
    ...     "SPARK-1032. If Yarn app fails before registering, app master stays aroun...")
    '[SPARK-1032] If Yarn app fails before registering, app master stays aroun...'
    >>> standardize_jira_ref(
    ...     "[SPARK-6250][SPARK-6146][SPARK-5911][SQL] Types are now reserved words in DDL parser.")
    '[SPARK-6250][SPARK-6146][SPARK-5911][SQL] Types are now reserved words in DDL parser.'
    >>> standardize_jira_ref("Additional information for users building from source code")
    'Additional information for users building from source code'
    """
    jira_refs = []
    components = []

    # If the string is compliant, no need to process any further
    if (re.search(r'^\[SPARK-[0-9]{3,6}\](\[[A-Z0-9_\s,]+\] )+\S+', text)):
        return text

    # Extract JIRA ref(s):
    pattern = re.compile(r'(SPARK[-\s]*[0-9]{3,6})+', re.IGNORECASE)
    for ref in pattern.findall(text):
        # Add brackets, replace spaces with a dash, & convert to uppercase
        jira_refs.append('[' + re.sub(r'\s+', '-', ref.upper()) + ']')
        text = text.replace(ref, '')

    # Extract spark component(s):
    # Look for alphanumeric chars, spaces, dashes, periods, and/or commas
    pattern = re.compile(r'(\[[\w\s,.-]+\])', re.IGNORECASE)
    for component in pattern.findall(text):
        components.append(component.upper())
        text = text.replace(component, '')

    # Cleanup any remaining symbols:
    pattern = re.compile(r'^\W+(.*)', re.IGNORECASE)
    if (pattern.search(text) is not None):
        text = pattern.search(text).groups()[0]

    # Assemble full text (JIRA ref(s), module(s), remaining text)
    clean_text = ''.join(jira_refs).strip() + ''.join(components).strip() + " " + text.strip()

    # Replace multiple spaces with a single space, e.g. if no jira refs and/or components were
    # included
    clean_text = re.sub(r'\s+', ' ', clean_text.strip())

    return clean_text