"""协程的使用 模块asyncio"""


import asyncio
import time


async def work_1():
    print("work_1 start")
    await asyncio.sleep(1)
    print("work_1 finished")
    return "yes"


async def work_2():
    print("work_2 start")
    await asyncio.sleep(2)
    print("work_2 finished")


async def main():
    task_1 = asyncio.create_task(work_1())
    task_2 = asyncio.create_task(work_2())
    await task_1
    await task_2
    print(task_1.result())


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print("use time:", time.time()-start)
