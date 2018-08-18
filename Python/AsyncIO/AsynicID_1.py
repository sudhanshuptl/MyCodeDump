import asyncio


async def delayed_hello():
    print('hello')
    await asyncio.sleep(1)  # when it goes to sleep other thread will continue as it threated as an event
    # after one sec timot event occure then it resumes
    print('World')

loop = asyncio.get_event_loop() # create an even loop object
loop.run_until_complete(delayed_hello()) #run loop untill all future object complete
loop.close() #close loop