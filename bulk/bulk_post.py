from faker import Faker
import random
import uuid

faker = Faker("ko_KR")

VISIBLE = [True, False]
DELETED = [True, False]

NUM_DATA = 100

def generate_post_query():
    post_id = uuid.uuid4()
    title = faker.slug()
    body = faker.text(max_nb_chars=100)
    image_url = faker.image_url()
    is_visible = random.choice(VISIBLE)
    is_deleted = random.choice(DELETED)
    reported_count = 0
    views = random.randint(0, 100)
    return f"\
        DO $$ \
        DECLARE \
            user_id uuid; \
            category_id uuid; \
        BEGIN \
            SELECT id INTO user_id FROM users ORDER BY RANDOM() LIMIT 1; \
            SELECT id INTO category_id FROM category ORDER BY RANDOM() LIMIT 1; \
            INSERT INTO post (id, fk_category_id, fk_user_id, title, body, image_url, is_visible, is_deleted, reported_count, views) \
            VALUES ('{post_id}', category_id, user_id, '{title}', '{body}', '{{{image_url}}}', '{is_visible}', '{is_deleted}', '{reported_count}', '{views}'); \
        END $$;\
    "

def generate_post_dummy_data(num_records):
    data = []
    for _ in range(num_records):
        post_query = generate_post_query()
        data.append(post_query)
    return data


def write_to_sql_file(datas, file_name):
    with open(file_name, 'w') as f:
        for data in datas:
            full_query = ''.join(data) + '\n'
            f.write(full_query)


dummy_data = generate_post_dummy_data(NUM_DATA)
write_to_sql_file(dummy_data, 'sql/post_dummy_data.sql')
