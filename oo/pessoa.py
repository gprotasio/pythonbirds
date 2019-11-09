class Pessoa:
    def __init__(self, *children, name=None, age=None):
        """

        :param children: Instância Filhos
        :param name: Atribui Nome
        :param age: Atribui Idade

        """
        self.age = age
        self.name = name
        self.children = list(children)

    def cumprimentar(self):
        """

        :return: Retorna mensagem do usuário

        """
        return f'Olá pessoal, este é o meu ID: {id(self)}'

if __name__ == '__main__':
    julie = Pessoa(name='Julie', age=32)
    marise = Pessoa(name='Marise', age=38)
    lucca = Pessoa(name='Lucca', age=40)
    karl = Pessoa(lucca, marise, julie, name='Karl', age=63)
    katie = Pessoa(name='Katie', age=60)
    print(Pessoa.cumprimentar(karl))
    print(id(karl))
    print(karl.cumprimentar())
    print(karl.name)
    print(karl.age)
    print(katie.name)
    print(katie.age)
    for children in karl.children:
        print(children.name)
        print(children.age)