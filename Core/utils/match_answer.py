async def match(user_answer: str, answer: str):
    statistics  = 0
    if user_answer == answer:
        return "Верно"
    else:
        return "Неверно"