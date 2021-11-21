from time import strftime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello","hi"):
        return "hey! how are you"

    if user_message in ("what's your name?"):
        return "I am sk bot"

    if user_message in ("what can u do for me"):
        return "I can say you current time"

    if user_message in ("what is the time now"):
        string = strftime('%H:%M:%S  %p')
        return string


    return "I can't understand you, sorry..."