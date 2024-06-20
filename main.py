def main(input_str: str) -> str:
  input_str = input_str.strip()
  if '+' in input_str:
      operands = input_str.split('+')
      operator = '+'
  elif '-' in input_str:
      operands = input_str.split('-')
      operator = '-'
  elif '*' in input_str:
      operands = input_str.split('*')
      operator = '*'
  elif '/' in input_str:
      operands = input_str.split('/')
      operator = '/'
  else:
      raise ValueError("Unsupported operation. Valid operations are +, -, *, /")


  if len(operands) != 2:
      raise ValueError("Invalid input format. Please provide two integers and one operator.")

  try:
      a = int(operands[0].strip())
      b = int(operands[1].strip())
  except ValueError:
      raise ValueError("Invalid input. Please enter integers only.")
    
  if not (1 <= a <= 10) or not (1 <= b <= 10):
        raise ValueError("Numbers must be between 1 and 10 inclusive.")

  if operator == '+':
      result = a + b
  elif operator == '-':
      result = a - b
  elif operator == '*':
      result = a * b
  elif operator == '/':
      # Деление с округлением вниз до целого
      result = a // b

  return str(result)


if __name__ == "__main__":
  try:
      user_input = input("Введите арифметическое выражение (например, '2 + 3'): ")
      print(main(user_input))
  except Exception as e:
      print(f"Ошибка: {e}")
