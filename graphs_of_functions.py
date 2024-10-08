import numpy as np
import matplotlib.pyplot as plt

# Задаем диапазон x
x = np.linspace(100, 100000, 99900)


# Определим функцию f(x)
def KuRL(x):
    return np.sqrt(190 ** 2 + (x * 100 * (10 ** -3)) ** 2) / np.sqrt(410 ** 2 + (x * 100 * (10 ** -3)) ** 2)


def KuLR(x):
    return 220 / np.sqrt(410 ** 2 + (x * 100 * (10 ** -3)) ** 2)


def fRL(x):
    return np.degrees(np.arctan((x * 100 * (10 ** -3)) / 190) - np.arctan((x * 100 * (10 ** -3)) / 410))


def fLR(x):
    return np.degrees(- np.arctan((x * 100 * (10 ** -3)) / 410))


def KuRC(x):
    return 1 / np.sqrt(1 + (220 * x * 4.4 * (10 ** -6)) ** 2)


def KuCR(x):
    return (220 * x * 4.4 * (10 ** -6)) / np.sqrt(1 + (220 * x * 4.4 * (10 ** -6)) ** 2)


def fRC(x):
    return np.degrees((np.pi / 2) - np.arctan(-1 / (220 * x * 4.4 * (10 ** -6))))


def fCR(x):
    return np.degrees(- np.arctan(-1 / (220 * x * 4.4 * (10 ** -6))))


# Определяем значения log10(x), которые нужно выделить
log_x_highlight = [2.1, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.0, 4.1]
x_highlight = [10 ** log_val for log_val in log_x_highlight]  # Находим соответствующие x

# Вычисляем значения функции f(x) в этих точках
f_highlight = [fCR(val) for val in x_highlight]

# Построение графика
plt.figure(figsize=(10, 8))

# Наносим на график значения функции, где по оси X логарифм от x
plt.plot(np.log10(x), fCR(x), label='f(x)', color='blue', linewidth=2)

# Добавляем точки для выделенных значений log10(x)
plt.scatter(log_x_highlight, f_highlight, color='red', zorder=5, s=50, label='Highlighted points')

# Добавляем проекции точек на оси абсцисс и ординат с подписью
for i, (log_val, f_val) in enumerate(zip(log_x_highlight, f_highlight)):
    # Вертикальная линия (проекция на ось X)
    plt.axvline(x=log_val, color='gray', linestyle='--', linewidth=1)
    # Горизонтальная линия (проекция на ось Y)
    plt.axhline(y=f_val, color='gray', linestyle='--', linewidth=1)
    # Добавляем подпись для каждой точки
    plt.text(log_val, f_val, f'{f_val:.3f}', fontsize=10, ha='left', va='bottom', color='black',
             bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.3'))

# Настройки осей
plt.xlabel('log10(w)', fontsize=12)
plt.ylabel('f(w)', fontsize=12)
plt.title('График функции f(w) с проекциями на ось абсцисс и ординат', fontsize=14)

# Настройка шкал и границ осей
plt.xlim(2, 4.2)
# plt.ylim(0, 1)
plt.ylim(-85, 90)

# Добавляем значения логарифмов на ось абсцисс
plt.xticks(log_x_highlight, labels=[f'{val:.1f}' for val in log_x_highlight])

# Добавляем легенду
# plt.legend(fontsize=10, loc='upper right')

# Включаем сетку
plt.grid(True, which="both", linestyle='--', linewidth=0.5)

# Выводим значения x и f(x) для наглядности
for log_val, x_val, f_val in zip(log_x_highlight, x_highlight, f_highlight):
    print(f'log10(w)={log_val}, w={x_val:.1f}, f(w)={f_val:.5f}')

# Отображаем график
plt.tight_layout()
plt.show()
