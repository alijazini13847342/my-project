def process_number():
    num = float(input("Enter a decimal number: "))
    
    integer_part = int(num)
    fractional_part = round(num - integer_part, 10)
    
    result = (integer_part * 10) + (fractional_part * 100)
    
    print(result)

if __name__ == "__main__":
    process_number()
  
