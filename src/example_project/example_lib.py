import urllib.request as req


def foo():
    print("inside foo")
    foo = Hello()
    foo.hi()
    #req.urlopen("https://www.google.fi").read()

class Hello:
    def __init__(self):
        self.y = 2

    def hi(self):
        print("inside hi")
