def magic_string():
    n = 1
    def inner():
        nonlocal n
        result = "BestSchool" * n
        n += 1
        return result
    return inner

