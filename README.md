# Генератор паролей с оценкой сложности

Этот проект представляет собой генератор случайных паролей с интерфейсом на основе библиотеки Tkinter. Программа генерирует случайный пароль заданной длины, оценивает его сложность и отображает ее в графическом интерфейсе с использованием цветового выделения сложности пароля.

## Особенности:

- Генерация пароля с буквами (все регистры), цифрами и специальными символами.
- Оценка сложности пароля в зависимости от его длины и разнообразия символов (нижний/верхний регистр, цифры, специальные символы).
- Визуальное отображение сложности пароля через цвет:
  - **Красный** — очень слабый или слабый.
  - **Желтый** — средний.
  - **Зеленый** — хороший или очень хороший.

## Установка и запуск

1. Скачайте или скопируйте этот код в файл с расширением `.py`, например `password_generator.py`.
2. Убедитесь, что у вас установлен Python версии 3.6 или выше.
3. Убедитесь, что у вас установлены библиотеки `tkinter` и `string` (они должны быть установлены по умолчанию).
4. Запустите программу с помощью следующей команды:

   ```
   python password_generator.py
   ```

5. Введите желаемую длину пароля и нажмите кнопку "Генерировать пароль". Программа сгенерирует пароль, отобразит его и оценит его сложность с визуализацией цвета.

## Основные функции программы

### 1. Генерация пароля
Функция `generate_password(length)` генерирует случайный пароль, который включает в себя буквы, цифры и специальные символы. Длина пароля не может быть меньше 6 символов для обеспечения безопасности.

```python
def generate_password(length):
    if length < 6:
        raise ValueError("Длина пароля должна быть не менее 6 символов для безопасности.")
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
```

### 2. Оценка сложности пароля
Функция `calculate_strength(password)` оценивает сложность пароля в зависимости от длины и разнообразия символов (буквы, цифры, спецсимволы). Чем больше уникальных символов и чем длиннее пароль, тем выше его сложность.

```python
def calculate_strength(password):
    length_score = len(password) / 10  # Чем длиннее, тем лучше
    char_types_score = 0
    if any(c in string.ascii_lowercase for c in password):
        char_types_score += 1
    if any(c in string.ascii_uppercase for c in password):
        char_types_score += 1
    if any(c in string.digits for c in password):
        char_types_score += 1
    if any(c in string.punctuation for c in password):
        char_types_score += 2

    complexity = length_score * char_types_score
    if complexity < 2:
        return "Очень слабый", "red"
    elif complexity < 3:
        return "Слабый", "red"
    elif complexity < 4:
        return "Средний", "yellow"
    elif complexity < 5:
        return "Хороший", "green"
    else:
        return "Очень хороший", "green"
```

### 3. Интерфейс пользователя
Интерфейс был создан с использованием библиотеки `Tkinter`. Пользователь может ввести желаемую длину пароля, и программа сгенерирует пароль с отображением его сложности.

```python
def on_generate_button_click():
    try:
        password_length = int(password_length_entry.get())
        if password_length < 6:
            raise ValueError("Пароль должен быть минимум из 6 символов.")
        
        password = generate_password(password_length)
        password_label.config(text=f"Пароль: {password}")
        
        strength, color = calculate_strength(password)
        strength_label.config(text=f"Сложность: {strength}", foreground=color)
    except ValueError as e:
        password_label.config(text=f"Ошибка: {e}")
        strength_label.config(text="", foreground="black")
```

## Пример интерфейса:

1. **Поле для ввода длины пароля** — где пользователь вводит желаемую длину пароля.
2. **Кнопка "Генерировать пароль"** — по нажатию которой генерируется новый случайный пароль.
3. **Отображение сгенерированного пароля** — сгенерированный пароль будет отображен на экране.
4. **Отображение сложности пароля** — будет отображаться оценка сложности пароля с цветовым выделением (красный, желтый, зеленый).

## Пример работы программы

Когда вы запустите программу, она предложит вам ввести длину пароля. Например, если вы введете "12", программа сгенерирует пароль длиной 12 символов, оценит его сложность и отобразит оценку в виде текста с соответствующим цветом.

### Пример:

1. **Ввод:** Длина пароля: 12
2. **Генерация пароля:** `3sG$zZ8!wrp@`
3. **Сложность:** `Хороший` (Зеленый цвет)

![image](https://github.com/user-attachments/assets/46a6e4b1-894d-4691-bd04-84844d6b8ca3)

![image](https://github.com/user-attachments/assets/efa65002-99fd-42e5-a179-835c17410b67)

![image](https://github.com/user-attachments/assets/c7a91da0-7935-4946-8e5f-2d709434c037)


## Заключение

Эта программа является полезным инструментом для генерации случайных паролей с высокой степенью безопасности, особенно для тех случаев, когда необходимо быстро создать сложные пароли для новых учетных записей. С помощью цветового отображения сложности вы сможете быстро понять, насколько сильным является ваш пароль.
