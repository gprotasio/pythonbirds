class Pessoa:
    def __init__(self, nome=None, age=40):
        self.age = age
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Luciano')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'George'
    print(p.nome)
    print(p.age)
