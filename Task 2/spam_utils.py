"""Модуль для антиспам‑проверки сообщений """

from datetime import datetime

LINKS = ["http://", "https://", "www."]

def count_spam_words(message, spam_words):
    """Возвращает количество спам‑слов в сообщении."""

    user_message = message.lower()
    spam_words_count = 0

    for el in user_message.split(" "):
        word = el.strip("!,?.:;-()\"")
        if word in spam_words:
            spam_words_count += 1
    return spam_words_count



def has_suspicious_links(message):
    """Проверяет, содержит ли сообщение подозрительные ссылки."""

    user_message = message.lower()
    # for el in LINKS:
    #     if el in message:
    #         return True
    # return False
    return any(link in user_message for link in LINKS)



def check_spam(message, spam_words):
    """Проверяет сообщение на наличие спам‑слов и возвращает предупреждение или None."""
    spam_words_count = count_spam_words(message, spam_words)

    if spam_words_count > 4:
        print("В тексте найдено большое количество спам слов")
        return {
            "warning_txt": "В тексте найдено большое количество спам слов"
        }
    elif 0 < spam_words_count <= 4:
        print("В тексте найдены спам слова")
        return {
            "text": message,
            "warning_txt": "В тексте найдены спам слова",
        }
    else:
        return {
            "text": message
        }



def check_links(message, spam_count):
    """Проверяет сообщение на наличие ссылок и возвращает предупреждение или None."""

    has_links = has_suspicious_links(message)

    if has_links and spam_count >= 1:
        print("В тексте найдены ссылки и спам слова")
        return {
            "warning_txt": "В тексте найдены ссылки и спам слова"
        }
    elif has_links and not spam_count:
        print("В тексте есть ссылки")
        return {
            "warning_txt": "В тексте есть ссылки",
            "text": message,
        }

    return {
        "text": message
    }



def moderate_message(message, spam_words):
    """
    Выполняет все проверки и возвращает:
    - список предупреждений
    - флаг публикации (True/False)
    """

    spam_words_count = count_spam_words(message, spam_words)

    check_message = check_spam(message, spam_words)
    check_links_in_message = check_links(message, spam_words_count)

    data = [check_message, check_links_in_message]

    is_valid = all("text" in el for el in data)
    warnings = [el["warning_txt"] for el in data if "warning_txt" in el ]

    return {
        "warnings" : warnings,
        "isValid": is_valid
    }


def add_publish_timestamp(message):
    """Добавляет к сообщению дату и время публикации."""
    pass
