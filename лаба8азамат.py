import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import math


# --- 1. ФУНКЦИЯ ВЫЧИСЛЕНИЯ РЯДА ТЕЙЛОРА ---
def calculate_taylor(x, eps):
    # Формула: 1 - x + x^2/2! - x^3/3! ...
    # term - текущий член ряда, total - сумма
    total = 1.0
    term = 1.0
    n = 0

    # Пока член ряда больше точности eps, продолжаем суммировать
    while abs(term) > eps:
        n += 1
        term = term * (-x) / n  # Получаем следующий член из предыдущего
        total += term
    return total


# --- 2. ГЛАВНАЯ ФУНКЦИЯ ПОСТРОЕНИЯ ---
def draw_graph():
    try:
        # Получаем данные из полей ввода (превращаем текст в числа float)
        x_start = float(entry_x_start.get())
        x_end = float(entry_x_end.get())
        dx = float(entry_dx.get())
        eps = float(entry_eps.get())
        b = float(entry_b.get())

        # Проверка на дурака (чтобы программа не зависла)
        if dx <= 0 or x_start >= x_end:
            messagebox.showerror("Ошибка", "Проверьте X_нач, X_кон и dx!")
            return

        # Создаем списки для координат
        x_list = []
        y_list = []
        z_list = []

        # Считаем значения от x_start до x_end с шагом dx
        x = x_start
        while x <= x_end:
            x_list.append(x)

            # Считаем y(x) через ряд Тейлора
            y_list.append(calculate_taylor(x, eps))

            # Считаем z(x) по обычной формуле
            z_list.append(math.exp(-x) + b)

            x += dx

        # --- 3. РИСОВАНИЕ ГРАФИКА ---
        plt.figure(figsize=(8, 5))  # Размер окна

        # Рисуем первую линию (синюю)
        plt.plot(x_list, y_list, 'b-', label='y(x) - Ряд Тейлора')

        # Рисуем вторую линию (красную пунктирную)
        plt.plot(x_list, z_list, 'r--', label='z(x) = e^(-x) + b')

        plt.title('График функций')  # Заголовок
        plt.xlabel('X')  # Ось X
        plt.ylabel('Y / Z')  # Ось Y
        plt.grid(True)  # Сетка
        plt.legend()  # Легенда (подписи линий)

        plt.show()  # Показать окно с графиком

    except ValueError:
        messagebox.showerror("Ошибка", "Введите числа в поля!")


# --- 4. СОЗДАНИЕ ОКНА (ИНТЕРФЕЙС) ---
root = tk.Tk()
root.title("Лаба 8 - Вариант 2")
root.geometry("300x300")

# Создаем подписи и поля ввода вручную (без циклов, для наглядности)
tk.Label(root, text="X начальное:").pack()
entry_x_start = tk.Entry(root)
entry_x_start.insert(0, "-2")
entry_x_start.pack()

tk.Label(root, text="X конечное:").pack()
entry_x_end = tk.Entry(root)
entry_x_end.insert(0, "2")
entry_x_end.pack()

tk.Label(root, text="Шаг dx:").pack()
entry_dx = tk.Entry(root)
entry_dx.insert(0, "0.2")
entry_dx.pack()

tk.Label(root, text="Точность E:").pack()
entry_eps = tk.Entry(root)
entry_eps.insert(0, "0.0001")
entry_eps.pack()

tk.Label(root, text="Параметр b:").pack()
entry_b = tk.Entry(root)
entry_b.insert(0, "1.0")
entry_b.pack()

# Кнопка запуска
btn = tk.Button(root, text="Построить", command=draw_graph, bg="lightgreen")
btn.pack(pady=10)

root.mainloop()