def section_09_04_random_remarks():
    class Warehouse:
        purpose = 'storage'
        region = 'west'

    w1 = Warehouse()
    w1.purpose = 'inspection'
    print(w1.purpose, w1.region)

    w2 = Warehouse()
    w2.region = 'east'
    print(w2.purpose, w2.region)
    print(w1.purpose, w1.region)

    print(Warehouse.purpose, Warehouse.region)

def section_09_08_iterators():
    class Reverse:
        def __init__(self, data: str):
            self.data = data
            self.index = len(data)

        def __iter__(self):
            return self

        def __next__(self):
            if  self.index == 0:
                raise StopIteration
            self.index = self.index - 1
            return self.data[self.index]

    rev = Reverse('spam')
    print('iterators')
    for char in rev:
        print(char)

def section_09_09_generators():
    def reverse(data: str):
        for index in range(len(data)-1, -1, -1):
            yield data[index]

    print('generators')
    for char in reverse('golf'):
        print(char)

def section_09_10_generator_expressions():
    print('generator expressions')
    print(
        sum(i * i for i in range(10))
    )
    xvec = [10, 20, 30]
    yvec = [7, 5, 3]
    print(
        sum(x * y for x,y in zip(xvec, yvec))
    )
    data = 'golf'
    print(
        tuple(data[i] for i in range(len(data)-1, -1, -1))
    )
