import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i}-й шар.')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task = [start_strongman('Andrey', 2), start_strongman('Vasya', 3),
            start_strongman('Kolya', 4)]

    await asyncio.gather(*task)

asyncio.run(start_tournament())