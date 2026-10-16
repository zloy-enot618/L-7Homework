from fastapi import FastAPI, HTTPException

app = FastAPI()

#список роботов

robots_list = [
    {
        "id": 1,
        "name": "Луноход-чистильщик",
        "planet": "Луна",
        "status": "active"
    },
    {
        "id": 2,
        "name": "Марс-сканнер",
        "planet": "Марс",
        "status": "notactive"
    },
    {
        "id": 3,
        "name": "Меркурий-засеяватель",
        "planet": "Меркурий",
        "status": "notactive"
    },
    {
        "id": 4,
        "name": "Венера-опаласкиватель",
        "planet": "Венера",
        "status": "active"
    },
    {
        "id": 5,
        "name": "Земля-экологист",
        "planet": "Земля",
        "status": "active"
    }
]

#конец списка роботов

#стартовая страница
@app.get("/")
def say_hello():
    return {
        "api-info": "Robots Catalog API",
        "directories": "/robots, /robots?status={active/notactive}, /robots/{id}"
    }


#вывод роботов по статусу active/notactive
@app.get("/robots")
def show_robots_by_status(status: str = ""):
    if status:
        robots_filtered_list = []
        for every_robot in robots_list:
            if every_robot["status"].lower() == status.lower():
                robots_filtered_list.append(every_robot)
        if not robots_filtered_list:
            raise HTTPException(status_code=404, detail=f"Robots with status '{status}' not found!")
            #если пользователь не ввёл после /robots ничего то типо просто список вывожу.
        return robots_filtered_list
    return robots_list



#вывод роботов по айди
@app.get("/robots/{robot_id}")
def show_robots_by_id(robot_id: int):
    if robot_id:
        robots_id_filtered = []
        for all_robot in robots_list:
            if all_robot["id"] == robot_id:
                return all_robot
                
    raise HTTPException(status_code=404, detail="Robot not found!")