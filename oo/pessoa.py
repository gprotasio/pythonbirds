class Pessoa:
    def __init__(self, name=None, age=None, children=None):
        self.age = age
        self.name = name
        self.children = list(children)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    George = Pessoa(name='George')
    Carlos = Pessoa(George, name='Carlos')
    print(Pessoa.cumprimentar(p))
    print(id(Carlos))
    print(Carlos.cumprimentar())
    print(Carlos.name)
    print(Carlos.age)
    for children in Carlos.children:
        print(children.name)
