import .pkg

f: ( int , int ) -> int = lambda x, y {
    pkg.f(x, y)
}
x0 = [
    (lambda x, y {
        x + y
    })(x, y) for x in [1, 2, 3] for y in [1, 2, 3]
]
x1 = [f(x, y) for x in [1, 2, 3] for y in [1, 2, 3]]
