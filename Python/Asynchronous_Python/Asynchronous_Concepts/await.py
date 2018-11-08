import asyncio


async def annie():
    print(" Anything You can do I can do better")
    print("   I can do anything better than You")
    await frank() # wait for frank() to complete
    print('Yes I can !')
    await frank()  # wait for frank() to complete
    print('Yes I can !')
    await frank()  # wait for frank() to complete
    print('Yes I can !')
    await frank()  # wait for frank() to complete
    print('Yes I can !')


async def frank():
    print('No You Can not !')


# create an eventloop to complete

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.ensure_future(annie()))