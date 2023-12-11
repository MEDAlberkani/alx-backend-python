def gen():
    yield 0x10, 0x20, 0x30
    g = gen()

    next(g)
