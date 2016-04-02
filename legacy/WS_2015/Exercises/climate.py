import numpy
from windspharm.standard import VectorWind

def _component(u, v, name):

    uchi = u * 0
    vchi = v * 0
    dims = list(u.dims)
    dims.remove('latitude')
    dims.remove('longitude')
    if len(dims) == 0:
        vw = VectorWind(u.values, v.values)
        func = getattr(vw, name)
        _uchi, _vchi = func()
        uchi = uchi + _uchi
        vchi = vchi + _vchi
    elif len(dims) == 1:
        d = dims[0]
        for i, p in enumerate(u[d]):
            arg = dict()
            arg[d] = p.values
            vw = VectorWind(u.sel(**arg).values, v.sel(**arg).values)
            func = getattr(vw, name)
            _uchi, _vchi = func()
            uchi[i] = _uchi
            vchi[i] = _vchi
    elif len(dims) == 2:
        d1 = dims[0]
        d2 = dims[1]
        for i, p in enumerate(u[d1]):
            for j, q in enumerate(u[d2]):
                arg = dict()
                arg[d1] = p.values
                arg[d2] = q.values
                vw = VectorWind(u.sel(**arg).values, v.sel(**arg).values)
                func = getattr(vw, name)
                _uchi, _vchi = func()
            uchi[i, j] = _uchi
            vchi[i, j] = _vchi
    else:
        raise RuntimeError()
    return uchi, vchi


def irrotationalcomponent(u, v):
    return _component(u, v, 'irrotationalcomponent')


def rotationalcomponent(u, v):
    return _component(u, v, 'rotationalcomponent')
