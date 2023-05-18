import time
import matplotlib.pyplot as plt

# Функция для вычисления F(n) рекурсивно
def recursive_F(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_F(n - 1) * recursive_F(n - 2) + 1

# Функция для вычисления F(n) итерационно
def iterative_F(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a * b + 1
        return b

# Параметры исследования
start_n = 30  # Начальное значение n
end_n = 35  # Конечное значение n

# Сравнительный анализ времени выполнения
recursive_times = []
iterative_times = []

for n in range(start_n, end_n + 1):
    start_time = time.time()
    recursive_F(n)
    recursive_time = time.time() - start_time
    recursive_times.append(recursive_time)

    start_time = time.time()
    iterative_F(n)
    iterative_time = time.time() - start_time
    iterative_times.append(iterative_time)

# Вывод результатов в табличной форме
print("n\tRecursive\tIterative")
for n in range(start_n, end_n + 1):
    print(f"{n}\t{recursive_times[n-start_n]:.6f}\t{iterative_times[n-start_n]:.6f}")

# Вывод результатов в графической форме
plt.plot(range(start_n, end_n + 1), recursive_times, label='Recursive')
plt.plot(range(start_n, end_n + 1), iterative_times, label='Iterative')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Comparative Analysis of Recursive and Iterative Approaches')
plt.legend()
plt.show()