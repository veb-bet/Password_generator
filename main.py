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

    # Минимальные требования
    lowercase = secrets.choice(string.ascii_lowercase)
    uppercase = secrets.choice(string.ascii_uppercase)
    digit = secrets.choice(string.digits)
    special = secrets.choice(string.punctuation)

    # Остальные символы
    remaining_length = length - 4
    if remaining_length > 0:
        other_chars = ''.join(secrets.choice(
            string.ascii_letters + string.digits + string.punctuation
        ) for _ in range(remaining_length))
    else:
        other_chars = ''

    # Объединяем и перемешиваем символы
    password_list = list(lowercase + uppercase + digit + special + other_chars)
    secrets.SystemRandom().shuffle(password_list)
    return ''.join(password_list)

def main():
    try:
        user_input = input("Введите длину пароля (минимум 6 символов): ").strip()
        if not user_input.isdigit():
            raise ValueError("Введите целое число.")

        password_length = int(user_input)
        password = generate_password(password_length)
        print(f"Сгенерированный безопасный пароль: {password}")

    except ValueError as e:
        print(f"\033[91mОшибка: {e}\033[0m")  # Красный текст ошибки
        sys.exit(1)

if __name__ == "__main__":
    main()
