import asyncio
import random


async def demo_func(_id):
    random_int = random.randint(1,5) # generate randpm num between 1 to 5
    await asyncio.sleep(random_int)
    print(f'demo functio Id = {_id} with wait time {random_int}')


async def main():
    task = []
    for i in range(10):
        task.append(asyncio.ensure_future(demo_func(i)))

    await asyncio.gather(*task) # wait till all task completed

if __name__=='__main__':
    loop  = asyncio.get_event_loop()  # create an event loop
    loop.run_until_complete(main())  # bind to main Coroutine and loop and run until it completed
    loop.close()  # closing event loop
