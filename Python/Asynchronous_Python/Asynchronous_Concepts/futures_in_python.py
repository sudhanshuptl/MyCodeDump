# Future is Indirect reference to forthcoming result
# You can ask future to call back when results are ready

import asyncio


def annie(when_frank_is_done_future):
    print(" Anything You can do I can do better")
    print("   I can do anything better than You")

    def defiance(_):
        print("Yes I can! ")

    when_frank_is_done_future.add_done_callback(defiance)
    # above is callback when when_frank_is_done_future is completed or result is set
    # it automatically get called


def frank(when_frank_is_done_future):
    print("No You can't!")
    when_frank_is_done_future.set_result(None)


# asyncio to run
loop = asyncio.get_event_loop()
future = loop.create_future()
annie(future)
frank(future)
loop.run_until_complete(future)

# Note We can this thing using more simple and fancy keyword await
