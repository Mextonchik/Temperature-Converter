print("Привет! Это конвертер-температур, он поможет тебе не запутаться в переводе градусов!")
def cels_to_fahren(celsius):
    return celsius * 1.8 + 32
def fahren_to_cels(fahrenheit):
    return (fahrenheit - 32) / 1.8 
temp = True   
while temp:
    try:        
        choice = int(input("Если вы хотите перевести градусы Цельсия в градусы Фаренгейта, напишите - 1. Если вы хотите перевести градусы Фаренгейта в градусы Цельсия, напишите - 2. Если хотите выйти - 3. Введите число: "))
        if choice == 1:
            celsius = float(input("Введите градусы Цельсия: "))
            result = cels_to_fahren(celsius)
            print(f"Результат: {celsius}°C = {result:.2f}°F")
        elif choice == 2:
            fahrenheit = float(input("Введите градусы Фаренгейта: "))
            result = fahren_to_cels(fahrenheit)
            print(f"Результат: {fahrenheit}°F = {result:.2f}°C")
        elif choice == 3:
            print("До свидания!")
            temp = False
        else:
            print("Пожалуйста, выбери число: 1, 2, 3!")    
    except ValueError:
        print("Ошибка: введите число!")