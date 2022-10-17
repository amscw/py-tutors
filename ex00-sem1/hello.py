msg = "Hello, World"
print(msg)

L0 = []
L1 = [123, 'abc', 1.23, {}]
L2 = ['Bob', 40.0, ['dev', 'mgr']]
L3 = list('spam')
L4 = list(range(-4, 4))

print(f"Пустой список: {L0}\n\
Четыре элемента: индексы 0..3: {L1}\n\
Вложенные подсписки: {L2}\n\
Список элементов итерируемого объекта: {L3}\n\
Список последовательных целых чисел: {L4}")

print(f"L2[2] = {L2[2]}, L2[2][1] = {L2[2][1]}")

L3.append('er')
for x in L3: print(x)
L4.reverse()
print(f"reverse L4: {L4}")
print(f"Длина списка L4: {len(L4)}")