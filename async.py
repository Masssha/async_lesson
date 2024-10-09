import requests
import datetime
import asyncio
import aiohttp
from models import Swapi, init_orm, Session, engine
from more_itertools import chunked

MAX_CHUNK = 10

async def get_people(pers_id, session):
    async with session.get(f'https://swapi.py4e.com/api/people/{pers_id}/') as response:
        json_data = await response.json()
        return json_data


async def insert_people(list_people_json):
    async with Session() as session:
        orm_objects = [Swapi(JSON=person_json) for person_json in list_people_json]
        session.add_all(orm_objects)
        await session.commit()


async def main():
    # await init_orm()
    async with aiohttp.ClientSession() as session:
        p_ids = chunked(range(1, 101), MAX_CHUNK)
        for p_ids_ch in p_ids:
            coroutines = [get_people(p_id, session) for p_id in p_ids_ch]
            results = await asyncio.gather(*coroutines)
            await insert_people(results)
            print(results)


# async def main_02():
#     coroutine_01 = get_people(1)
#     coroutine_02 = get_people(2)
#     coroutine_03 = get_people(3)
#     coroutine_04 = get_people(4)
#     # response_01 = await coroutine_01
#     # response_02 = await coroutine_02
#     # response_03 = await coroutine_03
#     # response_04 = await coroutine_04
#     results = await asyncio.gather(coroutine_01, coroutine_02, coroutine_03, coroutine_04)
#
#     print(results)


# async def get_people(pers_id):
#     session = aiohttp.ClientSession()
#     response = await session.get(f'https://swapi.py4e.com/api/people/{pers_id}/')
#     json_data = await response.json()
#     await session.close()
#     return json_data

# async def main_03():
#     coroutine_01 = get_people(1)
#     response_01 = await coroutine_01
#
#     print(response_01)



start = datetime.datetime.now()
asyncio.run(main())
print(datetime.datetime.now() - start)