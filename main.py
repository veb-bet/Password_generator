import random
import string

def generate_password(length):
    """
    Генерирует случайный пароль заданной длины, содержащий
    буквы, цифры и специальные символы.

    :param length: Длина пароля (целое число)
    :return: Строка с сгенерированным паролем
    """
    if length < 6:
        raise ValueError("Длина пароля должна быть не менее 6 символов для безопасности.")

    # Определяем набор символов: буквы (все регистры), цифры и спецсимволы
    characters = string.ascii_letters + string.digits + string.punctuation

    # Генерация случайного пароля
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        password_length = int(input("Введите длину пароля (минимум 6 символов): "))
        password = generate_password(password_length)
        print(f"Сгенерированный пароль: {password}")
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
