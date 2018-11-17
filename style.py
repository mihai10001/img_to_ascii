def get_default_style():
    return " .`'\"^,:;Il!i><~+jrdbk*#M@"


def get_mapping():
    style = get_default_style()
    mapping, start = [], 0
    part = int(255/len(style))
    for c in reversed(style):
        mapping += [{'ch': c, 'st': start, 'en': start+part}]
        start += part + 1
    return mapping