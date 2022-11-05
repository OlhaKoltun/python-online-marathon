import sqlalchemy as db

engine = db.create_engine('sqlite:///q1.db')

connection = engine.connect()
print("Connected to SQLite")

metadata = db.MetaData(engine)

customers = db.Table('customers', metadata, autoload=True)

query = db.select([customers]).where(customers.columns.grade > 200).order_by(customers.columns.id)

result_proxy = connection.execute(query)

result_set = result_proxy.fetchall()

print(f'Total rows are:   {len(result_set)}')
print('Printing each row')

for item in result_set:
    print(f'Id:  {item[0]}')
    print(f'Name:  {item[1]}')
    print(f'City:  {item[2]}')
    print(f'Grade:  {item[3]}')
    print(f'Seller:  {item[4]}')
    print('\n')

print("The SQLite connection is closed")
