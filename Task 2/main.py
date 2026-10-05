# main.py
# Основная программа для проверки сообщений на спам

import spam_utils as su

SPAM_WORDS = ["скидка", "бесплатно", "выигрыш", "кликни", "подпишись"]


def main():
    # Ваш код здесь
    text = input("Введите ваше сообщениие: ")

    moderated_res = su.moderate_message(text, SPAM_WORDS)

    if moderated_res["warnings"]:
        print(moderated_res["warnings"])

    if moderated_res["isValid"]:
        print("Можно отправлять")
    else:
        print("Сообщение не прошло проверку")



if __name__ == "__main__":
    main()
