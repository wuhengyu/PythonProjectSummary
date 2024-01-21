import asyncio

async def display(num):
    await asyncio.sleep(1)
    print(f"Task {num} done")

async def main():
    tasks = [asyncio.create_task(display(num)) for num in range(10)]

    while tasks:
        # 等待至少一个任务完成
        done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

        # 遍历已完成的任务并执行操作
        for task in done:
            # num = task.get_coro().__self__.num  # 获取display函数调用时的参数num
            name = task.get_name()  # 获取任务的名称
            num = int(name.split("-")[1])  # 从名称中提取num的值
            print(f"Received result from Task {num}, doing some operation...")
            # 这里添加你的操作...

        # 更新tasks列表为尚未完成的任务
        tasks = list(pending)

asyncio.run(main())