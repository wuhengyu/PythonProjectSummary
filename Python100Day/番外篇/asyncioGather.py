# import time
# def display(num):
#     time.sleep(1)
#     print(num)

# for num in range(10):
#     display(num)
    
import asyncio

# 每个任务在执行到 await 操作（如网络 I/O、定时器等）时会主动让出控制权，使得其他任务有机会得到执行
# 在等待所有任务完成的过程中，各个任务实际上是并发而非顺序执行的。
async def display(num):
    await asyncio.sleep(1)
    print(f"Task {num} done")

async def main():
  # 将display函数封装成一个异步任务并添加到tasks列表中。这样就创建了10个并发执行的display任务
    tasks = [asyncio.create_task(display(num)) for num in range(10)]
    # 这个函数接收一个可迭代对象（如列表）tasks，其中包含待执行的异步任务（通常是 asyncio.Task 或 Future 对象）
    # 它会等待这些任务中的任何一个完成（或在给定超时时间后返回），并返回一个 (done, pending) 元组，分别代表已完成的任务及其结果以及尚未完成的任务。
    # 需要在有任务完成后立即进行一些操作，那么 asyncio.wait() 是一个合适的选择
    # 设置超时时间，这意味着如果在指定时间内没有任务完成，则会提前返回
    
    # 等待一组异步任务（协程）中的任何一个或所有完成
    # asyncio.wait() 函数接收一个包含 asyncio.Future 或 asyncio.Task 对象的集合（通常是一个列表），然后返回两个集合：(done, pending)
    # done 是一个包含了已完成任务和它们的结果的集合、pending 是一个尚未完成的任务集合
    # 当前协程会挂起，直到至少有一个任务完成或者到达指定的超时时间
    # 在所有任务都完成之前，程序不会继续执行后续代码
    # 如果你想等待所有任务都完成，可以检查 pending 集合是否为空来确定所有任务是否已经完成
  
    # await asyncio.wait(tasks, timeout=None)
    
    # 或者
    # 接收一组异步任务，但它会等待所有提供的任务都完成。返回的结果是一个与传入任务顺序相对应的结果列表
    # 如果任何任务抛出了异常，在默认情况下，asyncio.gather() 会将该异常传播出来
    # 设置 return_exceptions=True，则会将异常作为结果的一部分返回
    # 需要确保所有任务都执行完毕后再继续后续操作时，asyncio.gather() 更为适用。
    # 它不会提供中途某个任务完成后的中间处理机会，而是统一在所有任务完成后才继续执行。
    
    # 同步等待多个异步任务完成
    # asyncio.gather()函数接收一系列异步任务作为参数，并发执行它们，直到所有任务完成
    # 这里的*tasks表示将tasks列表解压为多个参数传递给gather函数
    # 需要同时处理多个异步操作，并且不关心它们之间的顺序时，可能会使用 asyncio.gather(*tasks) 替代，因为它会等待所有提供的任务全部完成
    await asyncio.gather(*tasks, return_exceptions=True)

# 整个脚本运行的结果是每隔1秒打印出从0到9的数字，因为所有display任务几乎是同时开始并行执行的
asyncio.run(main())

# asyncio.wait() 提供了灵活的等待机制，可以等待任意数量的任务完成，或者在设定的时间内返回。
# asyncio.gather() 则是用于同时并发执行多个任务，并等待所有任务都完成之后再继续执行程序的下一个步骤。
