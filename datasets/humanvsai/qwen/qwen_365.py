def GetValueByPath(self, path_segments):
    current_node = self.plist_root
    for segment in path_segments:
        if isinstance(current_node, dict):
            current_node = current_node.get(segment)
        elif isinstance(current_node, list):
            try:
                current_node = current_node[int(segment)]
            except (ValueError, IndexError):
                return None
        else:
            return None
        if current_node is None:
            return None
    return current_node