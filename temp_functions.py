def temp_classifier(temp_celsius): # Создаем функцию с одним параметром
    if temp_celsius < -2: # ставим условия и возвращаем цифру 
        return 0
    if temp_celsius >= -2 and temp_celsius < 2:
        return 1
    if temp_celsius >= 2 and temp_celsius < 15:
        return 2
    if temp_celsius >= 15:
        return 3
    """
 Функция презбразования температуры в цельсиях в целые числа.

 Параметры 
 ----------
 temp_celsius: <числовое значение>
 convert_to: <int>

 Возвращает
 -------
 <float>
 Преобразованную температуру.
 """




def fahr_to_celsius(temp_fahrenheit):
    return (temp_fahrenheit -32)/1.8
    """
 Функция преобразования температуры в кельвинах в градусы Цельсия или Фаренгейта.

 Параметры 
 ----------
 temp_fahrenheit: <числовое значение>
 Температура в Фаренгейтах
 convert_to: <int>
 

 Возвращает
 -------
 <float>
 Преобразованную температуру.
 """