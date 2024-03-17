from faker import Faker
import uuid


faker = Faker()
NUM_DATA = 30


def generate_category_query():
    category_id = uuid.uuid4()
    name = faker.word()
    return f"INSERT INTO category (id, name) VALUES ('{category_id}', '{name}');"

def generate_dummy_data(num_records):
    data = []
    for _ in range(num_records):
        category_query = generate_category_query()
        data.append(category_query)
    return data

def write_to_sql_file(datas, file_name):
    with open(file_name, 'w') as f:
        for data in datas:
            full_query = ''.join(data) + '\n'
            f.write(full_query)

dummy_data = generate_dummy_data(NUM_DATA)
write_to_sql_file(dummy_data, 'sql/category_dummy_data.sql')
