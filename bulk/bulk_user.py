from faker import Faker
import random
import uuid

faker = Faker()

PROVIDERS = ['kakao', 'google', 'naver']
IS_ACTIVE = [True, False]
IS_CERTIFIED = [True, False]

NUM_DATA = 100

def generate_user_query():
    user_id = uuid.uuid4()
    provider = random.choice(PROVIDERS)
    provider_id = uuid.uuid4().hex[:8]
    is_active = random.choice(IS_ACTIVE)
    return f"INSERT INTO users (id, provider, \"providerId\", is_active) VALUES ('{user_id}','{provider}', '{provider_id}', '{is_active}');", user_id

def generate_profile_query(user_id):
    user_profile_id = uuid.uuid4()
    nickname = faker.user_name()
    short_bio = faker.text(max_nb_chars=100)
    email = faker.email()
    is_certified = random.choice(IS_CERTIFIED)
    return f"INSERT INTO user_profile (id, fk_user_id, nickname, short_bio, email, is_certified) VALUES ('{user_profile_id}','{user_id}', '{nickname}', '{short_bio}', '{email}', '{is_certified}');"

def generate_image_query(user_id):
    user_image_id = uuid.uuid4()
    files_size = random.randint(1, 1000)
    image_url = faker.image_url()
    return f"INSERT INTO user_image (id, fk_user_id, files_size, image_url) VALUES ('{user_image_id}','{user_id}', {files_size}, '{image_url}');"

def generate_dummy_data(num_records):
    data = []
    for _ in range(num_records):
        user_query, user_id = generate_user_query()
        profile_query = generate_profile_query(user_id)
        image_query = generate_image_query(user_id)
        data.append((user_query, profile_query, image_query))
    return data

def write_to_sql_file(datas, file_name):
    with open(file_name, 'w') as f:
        for data in datas:
            full_query = '\n'.join(data) + '\n'
            f.write(full_query)

dummy_data = generate_dummy_data(NUM_DATA)
write_to_sql_file(dummy_data, 'sql/user_dummy_data.sql')
