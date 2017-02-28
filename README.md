# django-restmodels

## Расширение реализующее REST API для доступа к моделям Django проекта

### Описание
Расширение распознает все существующие модели, подключённые в проекте
приложений и публикует REST интерфейс для внешнего взаимодействия


API позволяет:
+ запрашивать объекты по нескольким полям (логика - AND) с возможностью
сортировки (ORDER BY), ограничения кол-ва (LIMIT) (метод GET)
+ создавать новые объекты (метод POST)
+ удалять объекты по первичному ключу (метод DELETE)
+ обновлять объекты по первичному ключу (метод PUT)

Данные клиенту возвращаются в формате JSON

### Требования
python

### Установка
```markdown
python setup.py install

### Примеры
GET запроса:

```markdown
curl --dump-header - http://localhost:8000/api/v1/logistics/pek/26363/?cache=false&volume=1.41&weight=118.07&isPickUp=false&isDelivery=true&urgently=false

POST запроса:
```markdown
curl --dump-header -  -H "Content-Type: application/json; charset=utf-8" -X POST --data '{"name": "new_group2"}' http://localhost:8000/api/v1/group/

