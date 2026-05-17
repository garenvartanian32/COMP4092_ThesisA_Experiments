def find_credentials():
    usernames = [__pillar__['proxy'].get('admin_username', 'root')]
    if 'fallback_admin_username' in __pillar__.get('proxy'):
        usernames.append(__pillar__['proxy'].get('fallback_admin_username'))
    for user in usernames:
        for pwd in __pillar__['proxy']['passwords']:
            r = __salt__['dracr.get_chassis_name'](host=__pillar__['proxy']['host'],
                                                   admin_username=user,
                                                   admin_password=pwd)
            # Retcode will be present if the chassis_name call failed
            try:
                if r.get('retcode', None) is None:
                    DETAILS['admin_username'] = user
                    DETAILS['admin_password'] = pwd
                    __opts__['proxy']['admin_username'] = user
                    __opts__['proxy']['admin_password'] = pwd
                    return (user, pwd)
            except AttributeError:
                # Then the above was a string, and we can return the username
                # and password
                DETAILS['admin_username'] = user
                DETAILS['admin_password'] = pwd
                __opts__['proxy']['admin_username'] = user
                __opts__['proxy']['admin_password'] = pwd
                return (user, pwd)
    log.debug('proxy fx2.find_credentials found no valid credentials, using Dell default')
    return ('root', 'calvin')