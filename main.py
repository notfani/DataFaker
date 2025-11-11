import faker
import json
import random
import logging
from datetime import datetime

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

def fake_to_json():
    start_time = datetime.now()  # Начало отсчёта времени
    fake = faker.Faker()
    data = []
    num_records = int(input("Write number of data you want to generate: "))  # Количество записей для генерации
    logging.info(f"Starting data generation for {num_records} records.")

    for i in range(num_records):
        if i == 0 or random.random() < 0.2:  # С вероятностью 20% создается новый корневой узел
            parent_id = None
            ancestor_id = None
        else:
            parent_id = random.choice(data)["id"]  # Выбираем случайного родителя из уже созданных записей
            ancestor_id = next(
                (record["ancestor_id"] for record in data if record["id"] == parent_id),
                parent_id
            )  # Предок определяется по родителю

        record = {
            "id": i + 1,
            "parent_id": parent_id,
            "ancestor_id": ancestor_id,
            "name": fake.name(),
            "email": fake.email(),
        }
        data.append(record)

    # Сохранение данных в JSON файл
    with open("data.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    logging.info(f"Data generation completed. {num_records} records saved to 'data.json'.")

    end_time = datetime.now()  # Конец отсчёта времени
    elapsed_time = end_time - start_time
    logging.info(f"Script execution time: {elapsed_time}")

def run():
    logging.info("Program started.")
    print("Generating fake data to JSON...")
    fake_to_json()
    logging.info("Program finished.")

if __name__ == "__main__":
    run()