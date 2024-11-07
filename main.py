from Queqe import Queqe

queqe = Queqe(7)


for i in range(10):
    number = int(input("Podaj liczbe:"))
    queqe.add(number)

for i in range(10):
    print(queqe.remove())

