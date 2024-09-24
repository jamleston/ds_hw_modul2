from sqlite3 import Error

from connect import create_connection, database

import faker

def create_user(conn, user):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = '''
    INSERT INTO users(id,fullname,email) VALUES(?,?,?);
    '''
    cur = conn.cursor()
    try:
        cur.execute(sql, user)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()

    return cur.lastrowid

def create_status(conn, status):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = '''
    INSERT INTO status(id,name) VALUES(?,?);
    '''
    cur = conn.cursor()
    try:
        cur.execute(sql, status)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()

    return cur.lastrowid

def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = '''
    INSERT INTO tasks(id,title,description,status_id,user_id) VALUES(?,?,?,?,?);
    '''
    cur = conn.cursor()
    try:
        cur.execute(sql, task)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()

    return cur.lastrowid

# fake data

fake_names, fake_emails, fake_titles, fake_descriptions = [],[],[],[]

fake_data = faker.Faker()

for i in range(3):
    fake_names.append(fake_data.name())
    fake_emails.append(fake_data.email())
    fake_titles.append(fake_data.company())
    fake_descriptions.append(fake_data.text())

# start

if __name__ == '__main__':
    with create_connection(database) as conn:
# create a new user
        user1 = (1,fake_names[0], fake_emails[0])
        user1_id = create_user(conn, user1)
        print(user1_id)

        user2 = (2,fake_names[2], fake_emails[2])
        user2_id = create_user(conn, user2)
        print(user2_id)

# create a new status
        status1 = (1,'done')
        status1_id = create_status(conn, status1)

        status2 = (2,'in progress')
        status2_id = create_status(conn, status2)

        status3 = (3,'failed')
        status3_id = create_status(conn, status3)

# tasks
        task_1 = (1,fake_titles[0], fake_descriptions[0], status1_id, user1_id)
        task_2 = (2,fake_titles[1], fake_descriptions[1], status2_id, user1_id)
        task_3 = (3,fake_titles[2], fake_descriptions[2], status3_id, user2_id)


# create tasks
        print(create_task(conn, task_1))
        print(create_task(conn, task_2))
        print(create_task(conn, task_3))

