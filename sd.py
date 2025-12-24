import math
class Value:
    def __init__(self, val, err=0):
        self.val = float(val)
        self.err = abs(float(err))
    def __str__(self):
        return f"{self.val} погрешность {self.err}"
    def rel(self):
        """Относительная погрешность"""
        if self.val == 0:
            return float('inf')
        return self.err / abs(self.val)
    def __add__(self, other):
        other = self._check(other)
        return Value(self.val + other.val, self.err + other.err)
    def __sub__(self, other):
        other = self._check(other)
        return Value(self.val - other.val, self.err + other.err)
    def __mul__(self, other):
        other = self._check(other)
        val = self.val * other.val
        rel = self.rel() + other.rel()
        return Value(val, abs(val) * rel)
    def __truediv__(self, other):
        other = self._check(other)
        if other.val == 0:
            return Value(float('inf'), float('inf'))
        val = self.val / other.val
        rel = self.rel() + other.rel()
        return Value(val, abs(val) * rel)
    def power(self, n):
        n = float(n)
        val = self.val ** n
        rel = abs(n) * self.rel()
        return Value(val, abs(val) * rel)
    def sqrt(self):
        return self.power(0.5)
    def _check(self, other):
        if isinstance(other, (int, float)):
            return Value(other, 0)
        return other
def main():
    print("Калькулятор погрешностей")
    v1, e1 = map(float, input("Число и погрешность: ").split())
    current = Value(v1, e1)
    while True:
        print(f"\nТекущее: {current}")
        print("1: Сложить \n2: Вычисть \n3: Умножить \n4: Делить \n5: Степень \n6: Корень \n7: Новое число \n8: Выйти")
        cmd = input("> ").strip()
        if cmd == '8':
            break
        elif cmd == '7':
            v1, e1 = map(float, input("Новое число и погрешность: ").split())
            current = Value(v1, e1)
        elif cmd == '6':
            current = current.sqrt()
        elif cmd == '5':
            n = float(input("Степень: "))
            current = current.power(n)
        elif cmd in '1234':
            v2, e2 = map(float, input("Второе число и погрешность: ").split())
            b = Value(v2, e2)
            if cmd == '1':
                current = current + b
            elif cmd == '2':
                current = current - b
            elif cmd == '3':
                current = current * b
            elif cmd == '4':
                current = current / b
        else:
            print("?")
    print(f"\nИтог: {current}")
if __name__ == "__main__":
    main()