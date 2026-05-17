import ldap

def delete_principal(name):
    # Connect to the LDAP server
    ldap_client = ldap.initialize('ldap://ldap.example.com')
    ldap_client.simple_bind_s('cn=Directory Manager', 'password')

    # Delete the principal
    ldap_client.delete_s(name)

    # Close the connection
    ldap_client.unbind_s()