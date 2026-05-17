def group(seq: ActualIterable[T]) -> Dict[TR, List[T]]:
    ret = defaultdict(list)
    for each in seq:
        ret[each].append(each)
    return ret