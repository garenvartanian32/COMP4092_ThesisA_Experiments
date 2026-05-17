def validate_metadata(self, xml):
        assert isinstance(xml, compat.text_types)
        if len(xml) == 0:
            raise Exception('Empty string supplied as input')
        errors = []
        root = OneLogin_Saml2_XML.validate_xml(xml, 'saml-schema-metadata-2.0.xsd', self.__debug)
        if isinstance(root, str):
            errors.append(root)
        else:
            if root.tag != '{%s}EntityDescriptor' % OneLogin_Saml2_Constants.NS_MD:
                errors.append('noEntityDescriptor_xml')
            else:
                if (len(root.findall('.//md:SPSSODescriptor', namespaces=OneLogin_Saml2_Constants.NSMAP))) != 1:
                    errors.append('onlySPSSODescriptor_allowed_xml')
                else:
                    valid_until, cache_duration = root.get('validUntil'), root.get('cacheDuration')
                    if valid_until:
                        valid_until = OneLogin_Saml2_Utils.parse_SAML_to_time(valid_until)
                    expire_time = OneLogin_Saml2_Utils.get_expire_time(cache_duration, valid_until)
                    if expire_time is not None and int(time()) > int(expire_time):
                        errors.append('expired_xml')
        # TODO: Validate Sign
        return errors