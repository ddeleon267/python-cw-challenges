def create_dict(keys, values):
    dict = {}
    # looping over keys instead of vals since instructions say to disregard extra values if len(keys) < len(values)
    for idx, key in enumerate(keys):    
        # need to account for having fewer values than keys - will throw an exception
        try:
            dict[key] = values[idx]
        except:
            dict[key] = None

    return dict