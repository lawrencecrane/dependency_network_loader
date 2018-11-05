import example_project.example_lib as renamed

def b():
    testi = "dsajkldwas"
    print('inside b()\n')
    renamed.foo()


def a():
    print('inside a()\n')
    b()


def main():
    a()


if __name__ == '__main__':
    main()
