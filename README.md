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

   Вспомогательные программы: 
   
   Пока сайт в разработке, в качестве БД используется SQLite. Для просмотра использую SQLiteStudio (https://sqlitestudio.pl/)
   
   Для проверки API - Postman (https://www.postman.com/)
   
   
   Запуск тестового сервера:
```
    cd eduSite
    python manage.py runserver
````
      (адрес тестового сервера - 127.0.0.1:8000)
      
  Адреса API:
  
  1.

  Запрос GET - получение данных о тестах, вопросах, ответах без информации о правильных ответах

    http://127.0.0.1:8000/api/participant/quizzes/
    http://127.0.0.1:8000/api/participant/quizzes/{connection_code}

    http://127.0.0.1:8000/api/participant/questions/
    http://127.0.0.1:8000/api/participant/questions/{id}

    http://127.0.0.1:8000/api/participant/answers/
    http://127.0.0.1:8000/api/participant/answers/{id}
    
    http://127.0.0.1:8000/api/participant/quiz/question-ids/connection_code/{connection_code}/ - данные о quiz со списком id вопросов
    http://127.0.0.1:8000/api/participant/quiz/question-ids/id/{id}/ - аналогично, но получение через id quiz

    http://127.0.0.1:8000/api/author/quiz/{quiz_id}/questions/order/{номер}
    http://127.0.0.1:8000/api/participant/quiz/{connection_code}/questions/order/{номер} - получение вопроса по порядковому номеру в тесте

  2.

  Запросы: GET, POST, PUT, PATCH.
  
    http://127.0.0.1:8000/api/author/quizzes/ - только POST

    http://127.0.0.1:8000/api/author/quizzes/{quiz_id}/ - полные данные о тесте, получение только по id

    http://127.0.0.1:8000/api/author/quiz/{quiz_id}/questions/ - полные данные о вопросах данного quiz

    http://127.0.0.1:8000/api/author/quiz/{quiz_id}/questions/{question_id}/ - полные данные по вопросу

    http://127.0.0.1:8000/api/author/quiz/{quiz_id}/question/{question_id}/answers/

    http://127.0.0.1:8000/api/author/quiz/{quiz_id}/question/{question_id}/answers/{answer_id}/ - аналогично, данные по ответам

  3.

  Запросы GET, POST

    http://127.0.0.1:8000/api/author/quiz/{quiz_id}/results/

    http://127.0.0.1:8000/api/author/quiz/{quiz_id}/results/{id} - результаты quiz

    http://127.0.0.1:8000/api/author/quiz/{quiz_id}/results/question-results/

    http://127.0.0.1:8000/api/author/quiz/{quiz_id}/results/question-results/{id} - результаты по вопросам
    
  Формат данных в JSON:
    
Запрос POST/PUT(где это возможно):

*Поле score пока не используется, его не нужно писать в запросах

Quiz:
```
{
    "connection_code": "test",
    "is_published": true,
    "questions": [
        {
            "text": "q1",
            "score": "1",
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
Пример ответа сервера:
```
{
    "id": 48,
    "connection_code": "test1",
    "questions": [
        {
            "id": 63,
            "text": "q1",
            "score": 1,
            "answers": [
                {
                    "id": 229,
                    "text": "a",
                    "is_correct": false
                },
                {
                    "id": 230,
                    "text": "b",
                    "is_correct": true
                },
                {
                    "id": 231,
                    "text": "c",
                    "is_correct": false
                }
            ],
            "correct_answers": [
                230
            ]
        }
    ]
}
```
Question:
```
{
    "text": "q2",
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
