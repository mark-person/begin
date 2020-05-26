

def req_to_object(request, obj):
    for arg in request.args:
        name = arg
        value = request.args[name]
        setattr(obj, name, value)
    for arg in request.form:
        name = arg
        value = request.form[name]
        setattr(obj, name, value)
    return obj

