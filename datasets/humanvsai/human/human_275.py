def get_profile_names_and_default() -> (
        typing.Tuple[typing.Sequence[str], typing.Optional[Profile]]):
    with ProfileStore.open() as config:
        return sorted(config), config.default