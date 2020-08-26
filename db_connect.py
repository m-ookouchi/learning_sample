import psycopg2
import json

def connect_db():
    connecter = psycopg2.connect(
        host = 'localhost',
        port = '53867',
        database = 'postgres',
        user = 'postgres',
        password = 'UM7ECXZLHSZZY4CXUDSRKYIS5EGWSXIIC7AABJE54TCVUH56KA2Q====',
    )
    return connecter

def get_table_id(name):
    connecter = connect_db()

    # get tables
    cursor = connecter.cursor()
    sql = "select id from app_storage_tables where app_storage_tables.name = '" + name +"'"
    cursor.execute(sql)

    result = cursor.fetchall()
    connecter.close()

    if len(result) == 1 :
        return result[0][0]
    else:
        raise Exception

def get_column_id(table_id, name):
    connecter = connect_db()

    cursor = connecter.cursor()
    sql = "select columns from app_storage_tables where app_storage_tables.id = '" + str(table_id) + "'"
    cursor.execute(sql)

    result = cursor.fetchall()
    connecter.close()

    if len(result) == 1 :
        column_data = result[0][0]
        for i in column_data.items():
            if i[1]['name'] == name :
                return i[0]
    else:
        raise Exception

table_id = get_table_id('categories')
column_id = get_column_id(table_id, 'name')

print('table id is ' + str(table_id))
print('column id 1 is ' + column_id)

data = []
data.append("entertainment")
data.append("business")
data.append("travel")
data.append("sport")

connecter = connect_db()
cursor = connecter.cursor()
#cursor.execute("delete from app_storage_data where app_storage_data.table_id = '" + str(table_id) + "'")

for i in data :
    new_data = { column_id: i }
    print(new_data)
    print(json.dumps(new_data))

    sql = "insert into app_storage_data (table_id, data) values(" + str(table_id) + ", '" + json.dumps(new_data) + "')"
    print(sql)
    cursor.execute(sql)

connecter.commit()

cursor.close()
connecter.close()
