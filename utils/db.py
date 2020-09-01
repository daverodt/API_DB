from databases import Database
from const import DB_URL
from orm_db import authors

async def connect_db():
	db = Database(DB_URL)
	await db.connect()
	return db


async def disconnect_db(db):
	await db.disconnect()


async def execute(query, is_many, values=None):
	db = await connect_db()

	if is_many:
		await db.execute_many(query=query, values=values)
	else:
		await db.execute(query=query, values=values)

	await disconnect_db(db)


async def fetch(query, is_one, values=None):
	db = await connect_db()
	
	if is_one:
		result = await db.fetch_one(query=query, values=values)
		out = dict(result)
	else:
		result = await db.fetch_all(query=query, values=values)
		out = []
		for row in result:
			out.append(dict(row))

	await disconnect_db(db)

	return out


import asyncio
async def test_orm():
	query = authors.select().where(authors.c.id==2)
	out = await fetch(query, True)
	print(out)


loop = asyncio.get_event_loop()
loop.run_until_complete(test_orm())