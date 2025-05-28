import random
import string
import tkinter as tk
from tkinter import ttk
import secrets

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
        raise ValueError("Пароль должен быть не менее 6 символов.")

    # Гарантируем присутствие всех типов символов
    lowercase = secrets.choice(string.ascii_lowercase)
    uppercase = secrets.choice(string.ascii_uppercase)
    digit = secrets.choice(string.digits)
    special = secrets.choice(string.punctuation)

    # Остальные символы
    remaining = length - 4
    all_chars = string.ascii_letters + string.digits + string.punctuation
    others = ''.join(secrets.choice(all_chars) for _ in range(remaining))

    # Финальный пароль
    full_password = list(lowercase + uppercase + digit + special + others)
    secrets.SystemRandom().shuffle(full_password)
    return ''.join(full_password)

def calculate_strength(password):
    """
    Оценка сложности пароля.
    
    Параметры:
    password (str): Пароль для оценки сложности.
    
    Возвращает:
    str: Оценка сложности пароля и цвет для метки.
    """
    score = 0
    length = len(password)

    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if any(c in string.ascii_lowercase for c in password):
        score += 1
    if any(c in string.ascii_uppercase for c in password):
        score += 1
    if any(c in string.digits for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Очень слабый", "red"
    elif score == 3:
        return "Слабый", "orange"
    elif score == 4:
        return "Средний", "yellow"
    elif score == 5:
        return "Хороший", "green"
    else:
        return "Очень хороший", "dark green"

def on_generate_button_click():
    try:
        length = int(password_length_entry.get())
        password = generate_password(length)
        password_label.config(text=f"Пароль: {password}")

        strength, color = calculate_strength(password)
        strength_label.config(text=f"Сложность: {strength}", foreground=color)
    except ValueError as e:
        password_label.config(text=f"Ошибка: {e}", foreground="red")
        strength_label.config(text="", foreground="black")

# UI
root = tk.Tk()
root.title("Генератор безопасных паролей")
root.resizable(False, False)

# Стили
style = ttk.Style(root)
style.theme_use("clam")

ttk.Label(root, text="Длина пароля:").grid(row=0, column=0, padx=10, pady=10)
password_length_entry = ttk.Entry(root, width=10)
password_length_entry.insert(0, "12")
password_length_entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = ttk.Button(root, text="Сгенерировать", command=on_generate_button_click)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

password_label = ttk.Label(root, text="Пароль: ")
password_label.grid(row=2, column=0, columnspan=2, pady=5)

strength_label = ttk.Label(root, text="Сложность: ")
strength_label.grid(row=3, column=0, columnspan=2, pady=5)
