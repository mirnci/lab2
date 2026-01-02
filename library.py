def fibonacci(n):
    """
    Функция возвращает список из n чисел Фибоначчи
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n должно быть положительным целым числом")
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

def bubble_sort(lst):
    """
    Сортировка пузырьком
    """
    if not isinstance(lst, list):
        raise ValueError("Входной параметр должен быть списком")
    sorted_lst = lst.copy()
    n = len(sorted_lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if sorted_lst[j] > sorted_lst[j+1]:
                sorted_lst[j], sorted_lst[j+1] = sorted_lst[j+1], sorted_lst[j]
    return sorted_lst

def sieve_of_eratosthenes(n):
    """
    Решето Эратосфена для нахождения всех простых чисел до n
    """
    if not isinstance(n, int) or n < 2:
        raise ValueError("n должно быть целым числом >= 2")
    sieve = [True] * (n+1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [i for i, prime in enumerate(sieve) if prime]

