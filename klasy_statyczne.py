class Math:

    def add(a,b):
        return a + b

    def substract(a,b):
        return a - b

    def multiply(a,b):
        return a * b

    def divide(a,b):
        if b == 0:
            return "Division by zero impossible"
        return a/b


print(Math.add(2,3))
# print(Math.substract(2,3))
# print(Math.multiply(2,3))
# print(Math.divide(2,3))
# print(Math.divide(2,3))
# print(Math.divide(2,0))
# print(m.calculate_circle_area(10))
