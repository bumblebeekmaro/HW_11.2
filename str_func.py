def capitalize_string(input_string):
    """
        Функция преобразует входную строку в верхний регистр.

        Аргументы:
            input_string (str): Входная строка.

        Возвращает:
            str: Строка, в которой все символы приведены к верхнему регистру.
        """
    return input_string.upper()


def capitalize_words(input_string):
    """
    Функция для заглавных букв каждого слова в строке.

    Аргументы:
        input_string (str): Входная строка.

    Возвращает:
        str: Строка с заглавными буквами первой буквы каждого слова.
    """
    return ' '.join(word.capitalize() for word in input_string.split())
