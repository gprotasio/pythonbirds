class Pessoa:
    def __init__(self, *children, name=None, age=None):
        self.age = age
        self.name = name
        self.children = list(children)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    gizelly = Pessoa(name='Gizelly', age=32)
    paula = Pessoa(name='Paula', age=38)
    george = Pessoa(name='George', age=40)
    carlos = Pessoa(george, paula, gizelly, name='Carlos', age=63)
    adelia = Pessoa(name='Adélia', age=60)
    print(Pessoa.cumprimentar(carlos))
    print(id(carlos))
    print(carlos.cumprimentar())
    print(carlos.name)
    print(carlos.age)
    print(adelia.name)
    print(adelia.age)
    for children in carlos.children:
        print(children.name)
        print(children.age)

