import random
import string
import tkinter as tk
from tkinter import ttk

def generate_password(length):
    """
    Генерирует случайный пароль заданной длины, содержащий
    буквы, цифры и специальные символы.
    
    Параметры:
    length (int): Длина пароля (не менее 6 символов).
    
    Возвращает:
    str: Сгенерированный пароль.
    """
    if length < 6:
        raise ValueError("Длина пароля должна быть не менее 6 символов для безопасности.")

    # Определяем набор символов: буквы (все регистры), цифры и спецсимволы
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation
    characters = letters + digits + punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def calculate_strength(password):
    """
    Оценка сложности пароля.
    
    Параметры:
    password (str): Пароль для оценки сложности.
    
    Возвращает:
    str: Оценка сложности пароля.
    """
    length_score = len(password) / 8  # Чем длиннее, тем лучше
    char_types_score = 0
    if any(c in string.ascii_lowercase for c in password):
        char_types_score += 1
    if any(c in string.ascii_uppercase for c in password):
        char_types_score += 1
    if any(c in string.digits for c in password):
        char_types_score += 1
    if any(c in string.punctuation for c in password):
        char_types_score += 1

    # Оценка сложности: чем больше типы символов и длина, тем выше сложность
    complexity = length_score * char_types_score
    if complexity < 1:
        return "Очень слабый"
    elif complexity < 2:
        return "Слабый"
    elif complexity < 3:
        return "Средний"
    elif complexity < 4:
        return "Хороший"
    else:
        return "Очень хороший"

def on_generate_button_click():
    try:
        password_length = int(password_length_entry.get())
        if password_length < 6:
            raise ValueError("Пароль должен быть минимум из 6 символов.")
        
        password = generate_password(password_length)
        password_label.config(text=f"Пароль: {password}")
        
        strength = calculate_strength(password)
        strength_label.config(text=f"Сложность: {strength}")
    except ValueError as e:
        password_label.config(text=f"Ошибка: {e}")
        strength_label.config(text="")

# Настройка интерфейса Tkinter
root = tk.Tk()
root.title("Генератор паролей")

# Ввод длины пароля
ttk.Label(root, text="Длина пароля:").grid(row=0, column=0, padx=10, pady=5)
password_length_entry = ttk.Entry(root)
password_length_entry.grid(row=0, column=1, padx=10, pady=5)
password_length_entry.insert(0, "12")  # Значение по умолчанию

# Кнопка для генерации пароля
generate_button = ttk.Button(root, text="Генерировать пароль", command=on_generate_button_click)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Метки для отображения пароля и его сложности
password_label = ttk.Label(root, text="Пароль: ")
password_label.grid(row=2, column=0, columnspan=2, pady=5)

strength_label = ttk.Label(root, text="Сложность: ")
strength_label.grid(row=3, column=0, columnspan=2, pady=5)

# Запуск основного цикла Tkinter
root.mainloop()
