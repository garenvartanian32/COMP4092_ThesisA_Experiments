from metaknowledge import Citation

def CR_Tag(_val_: list[str]) -> list[Citation]:
    citations = []
    for item in _val_:
        try:
            citation = Citation(item)
            citations.append(citation)
        except ValueError:
            pass
    return citations
