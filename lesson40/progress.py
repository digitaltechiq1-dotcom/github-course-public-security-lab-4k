def progress(done, total):
    if type(done) is not int or type(total) is not int:
        raise TypeError("integer inputs required")
    if total <= 0 or not 0 <= done <= total:
        raise ValueError("invalid progress range")
    return int(done / total * 100)

def summary(done, total):
    return f"{done}/{total} complete ({progress(done, total)}%)"
