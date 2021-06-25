from collections import deque, Counter


def add_to_ready(soldier):  # better to do it using heap
    j = 0
    while j < len(ready) and force_amount[ready[j]] > force_amount[soldier]:
        j += 1
    ready.insert(j, soldier)


def go_to_fight(soldier):
    ans.append(soldier)
    force_amount[soldier] -= 1
    global total_force
    total_force -= 1
    on_rest.append(soldier)


def skip_turn():
    ans.append('idle')
    on_rest.append('idle')


# data = ['A', 'B', 'A', 'A', 'A', 'A', 'D', 'A', 'D', 'C', 'C', 'C', 'B', 'B', 'A', 'A', 'A', 'A']
# n = 1
# data = ["A", "A", "A", "B", "B", "B"]
# n = 2
data = ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'D']
n = 3

force_amount = Counter(data)
force_amount['idle'] = 0
total_force = len(data)
ready = deque(map(lambda x: x[0], force_amount.most_common()))
on_rest = deque()
ans = []

while total_force > 0:
    if len(on_rest) > n:
        add_to_ready(on_rest.popleft())
    else:
        if len(ready) == 0 or force_amount[ready[0]] == 0:
            skip_turn()
        else:
            go_to_fight(ready.popleft())

print(ans)
print(len(ans))
