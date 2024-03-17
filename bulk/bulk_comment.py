from faker import Faker
import random
import uuid

faker = Faker("ko_KR")

VISIBLE = [True, False]
DELETED = [True, False]

NUM_DATA = 5000

def generate_comment_query():
    comment_id = uuid.uuid4()
    body = faker.text(max_nb_chars=100)
    is_visible = random.choice(VISIBLE)
    is_deleted = random.choice(DELETED)
    reported_count = 0

    return f"\
        DO $$ \
        DECLARE \
            post_id uuid; \
            user_id uuid; \
        BEGIN \
            SELECT id INTO post_id FROM post ORDER BY RANDOM() LIMIT 1; \
            SELECT id INTO user_id FROM users ORDER BY RANDOM() LIMIT 1; \
            INSERT INTO comment (id, fk_post_id, fk_user_id, body, is_visible, is_deleted, reported_count) \
            VALUES ('{comment_id}', post_id, user_id, '{body}', '{is_visible}', '{is_deleted}', '{reported_count}'); \
        END $$;\
    "

def generate_post_dummy_data(num_records):
    data = []
    for _ in range(num_records):
        post_query = generate_comment_query()
        data.append(post_query)
    return data


def write_to_sql_file(datas, file_name):
    with open(file_name, 'w') as f:
        for data in datas:
            full_query = ''.join(data) + '\n'
            f.write(full_query)


dummy_data = generate_post_dummy_data(NUM_DATA)
write_to_sql_file(dummy_data, 'sql/comment_dummy_data.sql')
