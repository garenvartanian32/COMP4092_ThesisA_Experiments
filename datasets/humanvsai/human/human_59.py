def unwrap_html(html):
    from . import _html
    tree = _html.get_html_tree(html)
    start_refs, end_refs, lines = _html.get_line_info(tree)
    result = _internal.unwrap(lines, 1, _patterns.MIN_HEADER_LINES, 1)
    if result:
        typ, top_range, hdrs, main_range, bottom_range, needs_unindent = result
        result = {
            'type': typ,
        }
        top_range = _html.trim_slice(lines, top_range)
        main_range = _html.trim_slice(lines, main_range)
        bottom_range = _html.trim_slice(lines, bottom_range)
        if top_range:
            top_tree = _html.slice_tree(tree, start_refs, end_refs, top_range,
                                        html_copy=html)
            html_top = _html.render_html_tree(top_tree)
            if html_top:
                result['html_top'] = html_top
        if bottom_range:
            bottom_tree = _html.slice_tree(tree, start_refs, end_refs,
                                           bottom_range, html_copy=html)
            html_bottom = _html.render_html_tree(bottom_tree)
            if html_bottom:
                result['html_bottom'] = html_bottom
        if main_range:
            main_tree = _html.slice_tree(tree, start_refs, end_refs, main_range)
            if needs_unindent:
                _html.unindent_tree(main_tree)
            html = _html.render_html_tree(main_tree)
            if html:
                result['html'] = html
        if hdrs:
            result.update(hdrs)
    return result