class Value:
    def init(self, val, err=0):
        self.val = float(val)
        self.err = abs(float(err))
    def str(self):
        return f"{self.val} погрешность {self.err}"
    def add(self, other):
        other = self._make_value(other)
        val = self.val + other.val
        err = self.err + other.err
        return Value(val, err)
    def sub(self, other):
        other = self._make_value(other)
        val = self.val - other.val
        err = self.err + other.err
        return Value(val, err)
    def mul(self, other):
        other = self._make_value(other)
        val = self.val * other.val
        err = abs(other.val) * self.err + abs(self.val) * other.err
        return Value(val, err)
    def truediv(self, other):
        other = self._make_value(other)
        if other.val == 0:
            return Value(float('inf'), float('inf'))
        val = self.val / other.val
        err = (abs(other.val) * self.err + abs(self.val) * other.err) / (other.val ** 2)
        return Value(val, err)
    def power(self, n):
        n = float(n)
        val = self.val ** n
        err = abs(n) * abs(self.val) ** (n - 1) * self.err
        return Value(val, err)
    def sqrt(self):
        if self.val < 0:
            return Value(float('nan'), float('nan'))
        val = self.val ** 0.5
        err = self.err / (2 * val) if val != 0 else float('inf')
        return Value(val, err)
    def _make_value(self, other):
        if isinstance(other, (int, float)):
            return Value(other, 0)
        return other
def main():
    print("КАЛЬКУЛЯТОР ПОГРЕШНОСТЕЙ")
    v1, e1 = map(float, input("Первое число (значение погрешность): ").split())
    current = Value(v1, e1)
    while True:
        print(f"\nСейчас: {current}")
        print("\nВыберите:")
        print("1. Сложить \n2. Вычисть\n3. Умножить\n4. Разделить\n5. Степень\n6. Корень\n7. Новое число\n8. Выход")
        cmd = input("> ")
        if cmd == '8':
            break
        elif cmd == '7':
            v1, e1 = map(float, input("Новое число: ").split())
            current = Value(v1, e1)
        elif cmd == '6':
            current = current.sqrt()
        elif cmd == '5':
            n = float(input("Степень: "))
            current = current.power(n)
        elif cmd in '1234':
            v2, e2 = map(float, input("Второе число: ").split())
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
            print("Непонятно")
    print(f"\nРезультат: {current}")
if name == "main":
    main()