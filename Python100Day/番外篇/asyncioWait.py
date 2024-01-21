import asyncio

async def display(num):
    await asyncio.sleep(1)
    print(f"Task {num} done")

class DisplayWrapper:
    def __init__(self, num):
        self.num = num
        self.coro = display(num)

    async def run_and_process(self):
        await self.coro
        process_done_task(self)

def process_done_task(wrapper):
    num = wrapper.num
    print(f"Received result from Task {num}, doing some operation...")
    # 这里添加你的操作...

async def main():
    tasks = [DisplayWrapper(num).run_and_process() for num in range(10)]

    await asyncio.gather(*tasks)

asyncio.run(main())