func:(int|str, int|str) -> int = lambda x: int | str, y: int | str {
    int(x) + int(y)
}
a = func(1, 1)
b = func("1", "1")
