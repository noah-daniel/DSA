#given a rectangular plot into maximum size square plots
def dividePlot(l, w):
    if l == w:
        return [l,w]
    else:
        if l > w:
            return dividePlot(l-w, w)
        else:
            return dividePlot(l, w-l)

print(dividePlot(1680, 640))