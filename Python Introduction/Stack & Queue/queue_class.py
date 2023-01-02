from collections import deque

bank = deque(["Price", "Nikolai", "Soap", "Gaz"])

print(bank)

# ? Remove Element using pop() { FIFO }

bank.popleft()

print(bank)

bank.popleft()

print(bank)
