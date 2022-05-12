# 1 задание
# def asd(a):
#     return '*' * len(a[:-4]) + a[-4:]
# print(asd("123456789"))


# 2 задание
# def palindrom(a):
#     return a[::-1] == a
# while True:
#     a = input('введите  палиндром: ')
#     print(f'{a}  палиндром' if palindrom(a) else 'не  палиндром')


# 3 задание
# class Tomato:
#     states = {0: 'ничего', 1: 'появление всходов', 2: 'разрастание надземной массы и корней',
#               3: 'цветение', 4: 'формирование плодов (зеленый, желтый)', 5: 'плод созрел (красный)' }
#     def __init__(self, index):
#         self._index = index
#         self._state = 0
#     def grow(self):
#         self._a_state()
#     def is_ripe(self):
#         if self._state == 5:
#             return True
#     def _a_state(self):
#         if self._state < 5:
#             self._state += 1
#         self._b_state()
#     def _b_state(self):
#         print(f'Tomato {self._index} is {Tomato.states[self._state]}')
# class TomatoBush:
#     def __init__(self, num):
#         self.tomatoes = [Tomato(index) for index in range(0, num)]
#     def grow_all(self):
#         for tomato in self.tomatoes:
#             tomato.grow()
#     def all_are_ripe(self):
#         return all([tomato.is_ripe() for tomato in self.tomatoes])
#     def give_away_all(self):
#         self.tomatoes = []
# class Gardener:
#     def __init__(self, name, plant):
#         self.name = name
#         self._plant = plant
#     def work(self):
#         print('Cадовник работат')
#         self._plant.grow_all()
#         print('Cадовник закончил работать')
#     def harvest(self):
#         print('Садовник собирает урожай')
#         if self._plant.all_are_ripe():
#             self._plant.give_away_all()
#             print('Садовник собрал урожай')
#         else:
#             print('Плоды еще не созрели, подожите')
#     @staticmethod
#     def knowledge_base():
#         print("Сбор урожая происходит когда томаты стоновяться зрелыми красными.")
# if __name__ == '__main__':
#     Gardener.knowledge_base()
#     asd = TomatoBush(10)
#     gardener = Gardener('Anton', asd)
#     gardener.work()
#     gardener.work()
#     gardener.work()
#     gardener.work()
#     gardener.harvest()
#     gardener.work()
#     gardener.harvest()