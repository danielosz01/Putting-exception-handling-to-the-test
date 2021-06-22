def divisors(num):
    try:
      if num < 0 or num == 0:
        raise ValueError("No se pueden ingresar numeros negativos")
      divisors = []
      for i in range(1, num + 1):
          if num % i == 0:
              divisors.append(i)
      return divisors
    except ValueError as ve:
        print(ve)
        return false


def run():
    num = int(input('Ingresa un nÃºmero: '))
    print(divisors(num))
    print("TerminÃ³ mi programa")


if __name__ == '__main__':
    run()