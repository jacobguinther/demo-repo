import psycopg2

# conn = psycopg2.connect(
#     dbname="jjodesty",
#     user="jjodesty",
#     password="jjodesty",
#     # host="3.139.77.161",
#     host="127.0.0.1",
#     port="5432"
# )
from tabulate import tabulate

conn = psycopg2.connect(
    dbname="labs",
    user="postgres",
    password="labs123",
    host="3.139.77.161",
    port="5432"
)


my_table = psycopg2.read_sql('select * from job_result limit 5', conn)

tabulate(my_table, headers='keys', tablefmt='psql')

# q = "INSERT INTO job_result (job_id, data) VALUES(1, '{\"test\":1}');"
# cur = conn.cursor()
# cur.execute(q)
# conn.commit()
# cur.close()

# query = """
#     INSERT INTO job_result (
#       job_id,
#       data,
#     ) VALUES (%s, %s::jsonb[])
# """
#
# def insert_job(conn, query, job_id, data):
#     values = (
#         job_id,
#         map(psycopg2.extras.Json, data),
#     )
#
#
#     cur = conn.cursor()
#     cur.execute(query, values)
#     conn.commit()
#     cur.close()

