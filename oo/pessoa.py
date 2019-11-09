class Pessoa:
    def __init__(self, name=None, age=None, children=None):
        self.age = age
        self.name = name
        self.children = children

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Luciano')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.name)
    p.nome = 'George'
    print(p.name)
    print(p.age)
