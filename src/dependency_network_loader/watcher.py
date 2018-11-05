import sys
from functools import partial

def parse_frame(x):
    name = x.f_code.co_name

    try:
        module = x.f_globals['__name__']
    except AttributeError:
        module = ''

    try:
        if 'self' in x.f_locals:
            cls = x.f_locals['self'].__class__.__name__
        elif 'cls' in x.f_locals:
            cls = x.f_locals['cls'].__name__
        elif 'flags' in x.f_locals:
            cls = x.f_locals['flags'].__class__.__name__
        else:
            # maybe log the f_locals...
            cls = ''
    except AttributeError:
        cls = ''

    return {
          'name': name,
          'class': cls,
          'module': module
    }


# also implement the watch for c_call
def tracer(frame, event, arg, f=lambda x: x):
    if event != "call":
        return

    caller = parse_frame(frame.f_back)
    callee = parse_frame(frame)

    f({
          'caller': caller,
          'callee': callee
    })

    return tracer


def start(main, f):
    """
    Traces a callstack of given function (main), and passes the data to the given function (f)
    every time function in main is called
    """
    _tracer = partial(tracer, f=f)
    sys.settrace(_tracer)

    main()

    sys.settrace(None)
