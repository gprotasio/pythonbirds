class Pessoa:
    def __init__(self, *children, name=None, age=None):
        self.age = age
        self.name = name
        self.children = list(children)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    george = Pessoa(name='George', age=40)
    carlos = Pessoa(george, name='Carlos', age=63)
    print(Pessoa.cumprimentar(carlos))
    print(id(carlos))
    print(carlos.cumprimentar())
    for children in carlos.children:
        print(children.name)
        print(children.age)
