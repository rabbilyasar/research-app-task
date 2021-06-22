# research-app-task

## How to run
Get inside the environment
```
source env/bin/acitvate
```
Install files from requirements.txt
```
pip install -r requirements.txt
```
```
python manage.py runserver
```

## How to run test
```
python manage.py test
```

## Documentation for the url
### Task
For creating and listing
```
GET /api/task
POST /api/task
```
For delete and update retrieve
```
DELETE /api/task/<task_id>
GET /api/task/<task_id>
PATCH /api/task/<task_id>
```
### Tile
For creating and listing
```
GET /api/tile
POST /api/tile
```
For delete and update retrieve
```
DELETE /api/tile/<tile_id>
GET /api/task/<tile_id>
PATCH /api/tile/<tile_id>
```
