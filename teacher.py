from sql_connection import get_sql_connection


def insert_classes(connection,tname,tid, sem, section, subject, time, day):
    print(sem, section, subject, time, day)
    cursor = connection.cursor()
    query = ("INSERT INTO tt (teacher_name,teacher_id,sem_no, section, subject, time, day) VALUES (%s, %s, %s, %s, %s)")
    cursor.execute(query,(tname,tid,sem, section, subject, time, day))
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_connection()
    # print(get_all_products(connection))
 