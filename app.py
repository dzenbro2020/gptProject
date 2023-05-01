import openai

print('Начало сессии...')

prompt = ""

while True:
    
    print()
    question = input("Вопрос: ")
    if question in ('выход','стоп','exit','quit','end'):
        print('Конец сессии...')
        break
    prompt += " " + question
    print()
    
    with open(r'E:\Coding\PyCode\GPT\api_key.txt', 'r') as f:
        key = f.read()

    openai.api_key = key        

    # задаем модель и промпт
    model_engine = "text-davinci-003"


    # задаем макс кол-во слов
    max_tokens = 128

    # генерируем ответc
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # выводим ответ
    print('Ответ:',completion.choices[0].text)