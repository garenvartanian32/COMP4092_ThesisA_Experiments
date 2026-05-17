def provider_of(iface):
    def check(value):
        return (
            iface.providedBy(value),
            u"{value!r} does not provide {interface!s}".format(
                value=value,
                interface=fullyQualifiedName(iface),
            ),
        )
    return check