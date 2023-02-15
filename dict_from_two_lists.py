def create_dict(keys, values):
    dict = {}
    # looping over keys since instructions say to disregard extra values if len(keys) < len(values)
    for idx, key in enumerate(keys):
        try:
            dict[key] = values[idx]
        except:
            dict[key] = None

    return dict