def convert_to_dict(obj):
    dict = {}
    dict.update(obj.__dict__)
    return dict


def convert_to_dicts(objs):
    obj_arr = []

    for o in objs:
        dict = {}
        dict.update(o.__dict__)
        obj_arr.append(dict)

    return obj_arr


def dict_to_xml(data):
    def to_xml(data):
        xx = []
        for k, v in data.items():
            if isinstance(v, dict):
                aa = to_xml(v)
                s = "<{key}>{value}</{key}>".format(key=k, value=aa)
            else:
                s = "<{key}>{value}</{key}>".format(key=k, value=v)
            xx.append(s)
        return "".join(xx)

    return to_xml(data)