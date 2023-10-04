import socket
import math

def handle_task_number(number):
    if (number == 1):
        return "Введите значение X"
    if (number == 2):
        return "Введите натуральное число N"
    if (number == 3):
        return "Введите натуральное число N"
    if (number == 4):
        return ""
    if (number == 5):
        return ""

def handle_user_input(taskNumber, input):
    if (taskNumber == 1):
        return compute_ln_function(int(input))

    if (taskNumber == 2):
        result = smallest_4_power_k_greater_than_N(int(input))
        return "Наименьшее число вида 4^k, большее N: ", result

    if (taskNumber == 3):
        result = is_power_of_three(int(input))
        return result

    if (taskNumber == 4):
        result = calculate_and_return_values()
        return result

    if (taskNumber == 5):
        result = find_first_negative_term()
        return result

def compute_ln_function(x):
    try:
        if x <= 1 or x == 0:
            return "Ошибка: x должен быть больше 1 и не равен 0."
        else:
            result = math.log(x - 1/x)
            return f"Значение функции y = ln(x-1/x) при x = {x}: {result}"
    except ValueError:
        return "Ошибка: Введите корректное число для x."


def smallest_4_power_k_greater_than_N(N):
    try:
        if N <= 0:
            return "N должно быть натуральным числом больше 0"
        k = math.ceil(math.log(N, 4))
        result = 4 ** k
        return result
    except ValueError as e:
        return "Ошибка: Введите корректное число для N."


def is_power_of_three(N):
    try:
        if N <= 0:
            return "N должно быть натуральным числом больше 0"

        while N > 1:
            if N % 3 != 0:
                return "Не является"
            N = N // 3
        return "Является"
    except ValueError as e:
        return "Ошибка: Введите корректное число для N."

def calculate_and_return_values():
    x = 12.0  # Начальное значение x
    step = -1.2  # Шаг изменения x
    negative_values_str = ""  # Строка для хранения отрицательных значений

    while x >= 1:
        z = math.tan(x) + 5 * math.cos(x - 2)
        if z < 0:
            negative_values_str += f"При x = {x}, z = {z} (отрицательное значение)\n"
        x += step

    return negative_values_str

def find_first_negative_term():
    n = 1
    while True:
        term = math.sin(math.tan(n / 2))
        if term < 0:
            return f"Первый отрицательный член последовательности при n = {n}: {term}"
        n += 1
def server_program():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("Start handle task with number: " + str(data))
        taskNumber = int(data)
        responseForTaskNumber = handle_task_number(taskNumber)
        if (responseForTaskNumber != ""):
            conn.send(responseForTaskNumber.encode())
            data = conn.recv(1024).decode()

        result = handle_user_input(taskNumber, str(data))
        conn.send(str(result).encode())
    conn.close()


if __name__ == '__main__':
    server_program()
