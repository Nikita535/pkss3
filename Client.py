import socket


def client_program():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    menu = "Введите цифру для выбора задачи:\n1) Напечатать значения функции y=ln(x-1/x).\n" \
           "2) Дано натуральное число N. Получить наименьшее число вида 4^k, большее N.\n" \
           "3) Определить, является ли натуральное N степенью числа 3 или нет.\n" \
           "4) Вывести на печать отpицательные значения функции z=tg(x)+5cos(x-2) для x изменяющегося на отрезке [12, 1] с шагом 1,2.\n" \
           "5) Hайти пеpвый отpицательный член последовательности sin(tg(n/2)) для nизменяющегося на следующим обpазом: n=1,2,3... .\n" \
           "Введите 0 для выхода\n"

    message = input(menu)  # take input

    while message.lower().strip() != '0':
        client_socket.send(message.encode())

        if (message != "4"):
            if (message != "5"):
                data = client_socket.recv(1024).decode()
                clientInput = input(data + ": ")
                client_socket.send(clientInput.encode())

        data = client_socket.recv(1024).decode()
        print(data, "\n")

        message = input(menu)

    client_socket.close()


if __name__ == '__main__':
    client_program()