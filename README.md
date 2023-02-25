# edu-site-backend

Версия Python 3.10.7

1. Установка пакетов:
```
    python -m venv venv
    
    venv\Scripts\activate
  
    pip install django
  
    pip install djangorestframework
```
2. Использование
   
   Запуск тестового сервера:
    
    cd EduSite
    
    python manage.py runserver
      
      (адрес тестового сервера - 127.0.0.1:8000, адрес на хостинге - quizbackend.pythonanywhere.com)
      
  Адреса API:
  
  1.

  Запрос GET - получение данных о тестах, вопросах, ответах без информации о правильных ответах (для проходящих тест)

    http://127.0.0.1:8000/api/partial/quizzes/
    http://127.0.0.1:8000/api/partial/quizzes/{connection_code}

    http://127.0.0.1:8000/api/partial/questions/
    http://127.0.0.1:8000/api/partial/questions/{id}

    http://127.0.0.1:8000/api/partial/answers/
    http://127.0.0.1:8000/api/partial/answers/{id}

  2.

  Запросы: GET, POST, PUT, PATCH.

    http://127.0.0.1:8000/api/full/quizzes/{quiz_id}/ - полные данные о тесте, получение только по id

    http://127.0.0.1:8000/api/full/quiz/{quiz_id}/questions/ - полные данные о вопросах данного quiz

    http://127.0.0.1:8000/api/full/quiz/{quiz_id}/questions/{question_id}/ - полные данные по вопросу

    http://127.0.0.1:8000/api/full/quiz/{quiz_id}/question/{question_id}/answers/

    http://127.0.0.1:8000/api/full/quiz/{quiz_id}/question/{question_id}/answers/{answer_id}/ - аналогично, данные по ответам

  3.

  Запросы GET, POST

    http://127.0.0.1:8000/api/full/quiz/{quiz_id}/results/

    http://127.0.0.1:8000/api/full/quiz/{quiz_id}/results/{id} - результаты quiz

    http://127.0.0.1:8000/api/full/quiz/{quiz_id}/results/question-results/

    http://127.0.0.1:8000/api/full/quiz/{quiz_id}/results/question-results/{id} - результаты по вопросам
    
  Формат данных в JSON:
    
Запрос POST/PUT(где это возможно):

Quiz:
```
{
    "connection_code": "test",
    "questions": [
        {
            "text": "q1",
            "order": "1",
            "answers": [
                {
                    "text": "a",
                    "is_correct": "false"
                },
                {
                    "text": "b",
                    "is_correct": "true"
                },
                {
                    "text": "c",
                    "is_correct": "false"
                }
            ]
        }
    ]
}
```
Question:
```
{
    "text": "q2",
    "order": 2,
    "score": 1,
    "answers": [
        {
            "text": "e",
            "is_correct": true
        },
        {
            "text": "f",
            "is_correct": true
        },
        {
            "text": "g",
            "is_correct": false
        }
    ]
}
```
Answer:
```
{
    "text": "h",
    "is_correct": false
}
```
Результат прохождения Quiz:
```
{
    "participant": "Johnny",
    "quiz": 40
}
```
Ответ на вопрос:
```
{
    "chosen_answers": [
        172
    ],
    "question": 49,
    "quiz_result":  6
}
```
PATCH аналогичен PUT, но позволяет не упоминать все поля



Инфа по Django:

https://www.youtube.com/playlist?list=PLA0M1Bcd0w8xO_39zZll2u1lz_Q-Mwn1F

https://www.youtube.com/playlist?list=PLA0M1Bcd0w8xZA3Kl1fYmOH_MfLpiYMRs

https://proproprogs.ru/django
