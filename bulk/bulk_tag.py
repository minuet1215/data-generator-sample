from faker import Faker
import uuid

faker = Faker()
NUM_DATA = 100

def generate_tag_query():
    tag_id = uuid.uuid4()
    name = faker.word()
    return f"INSERT INTO tag (id, name) VALUES ('{tag_id}', '{name}');"

def generate_dummy_data(num_records):
    data = []
    for _ in range(num_records):
        tag_query = generate_tag_query()
        data.append(tag_query)
    return data

def write_to_sql_file(datas, file_name):
    with open(file_name, 'w') as f:
        for data in datas:
            full_query = ''.join(data) + '\n'
            f.write(full_query)

dummy_data = generate_dummy_data(NUM_DATA)
write_to_sql_file(dummy_data, 'sql/tag_dummy_data.sql')
