def response(data, status = "SUCCESS", error = False):
    return {
        "status": status,
        "data": data,
        "error": error
    }