# Определите может ли Боб выкупить какое-то поддерево так, чтобы у него оказались все нужные ему акции, и если да, то какое минимальное количество денег он для этого должен потратить.
# 5 2
# A
# B
# 0 1 A
# 1 2 A
# 1 2 B
# 1 1 B
# 4 2 A ->>> 3
# потратит столько денег, сколько суммарно стоят пакеты в поддереве и получит все акции из этого поддерева. В результате покупки Боб хочет, чтобы у него были акции всех интересующих его компаний. Поскольку Боб ещё студент, он хочет потратить минимальное количество денег.
class Node:
    def __init__(self, value, cost):
        self.value = value
        self.cost = cost
        self.children = []


def minimum_cost(root, interests):
    if not root:
        return 0

    if root.value in interests:
        interests.remove(root.value)
        total_cost = root.cost
    else:
        total_cost = 0

    for child in root.children:
        child_cost = minimum_cost(child, interests)
        total_cost += child_cost

    return total_cost


n, k = map(int, input().split())

companies = set(input() for _ in range(k))

nodes = [None] * (n + 1)

for i in range(1, n + 1):
    parent, cost, company = input().split()
    parent = int(parent)
    cost = int(cost)
    nodes[i] = Node(company, cost)
    if parent != 0:
        nodes[parent].children.append(nodes[i])

min_cost = minimum_cost(nodes[1], companies)

if len(companies) == 0:
    print(min_cost)
else:
    print(-1)
