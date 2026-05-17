def remove_phonetic_markup(root: str) -> str:
    return ''.join(filter(lambda c: c not in ['ˈ', 'ˌ'], root))
