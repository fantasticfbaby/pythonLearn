#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 在Python中获取系统信息的另一个好办法是使用psutil这个第三方模块。
# 顾名思义，psutil = process and system utilities，它不仅可以通过一两行代码实现系统监控，还可以跨平台使用，
# 支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块。

import psutil
# CPU逻辑数量
print('CPU逻辑数量:', psutil.cpu_count())
print()
# CPU物理核心
# 2说明是双核超线程, 4则是4核非超线程
print('CPU物理核心:', psutil.cpu_count(logical=False))
print()
# 统计CPU的用户／系统／空闲时间
print('统计CPU的用户／系统／空闲时间:', psutil.cpu_times())
print()
# 再实现类似top命令的CPU使用率，每秒刷新一次，累计10次
# print('再实现类似top命令的CPU使用率，每秒刷新一次，累计10次')
# for x in range(10):
#     print(psutil.cpu_percent(interval=1, percpu=True))

# 使用psutil获取物理内存和交换内存信息，分别使用：
print('使用psutil获取物理内存和交换内存信息，分别使用：')
print(psutil.virtual_memory())
print(psutil.swap_memory())
# 返回的是字节为单位的整数，可以看到，总内存大小是total，已用4559048704，使用了percent。
# 而交换区大小是total。
print()
# 通过psutil获取磁盘分区、磁盘使用率和磁盘IO信息
print('通过psutil获取磁盘分区、磁盘使用率和磁盘IO信息')
# 磁盘分区信息
print('磁盘分区信息:', psutil.disk_partitions())
# 磁盘使用情况
print('磁盘使用情况:', psutil.disk_usage('/'))
# 磁盘IO
print('磁盘IO:', psutil.disk_io_counters())
print()

# 获取网络接口和网络连接信息
print('获取网络接口和网络连接信息')
# 获取网络读写字节／包的个数
print('获取网络读写字节／包的个数:', psutil.net_io_counters())
# 获取网络接口信息
print('获取网络接口信息:', psutil.net_if_addrs())
# 获取网络接口状态
print('获取网络接口状态:', psutil.net_if_stats())
print()

# 获取当前网络连接信息，使用net_connections()
print('获取当前网络连接信息，使用net_connections()')
print(psutil.net_connections())
# 可能会得到一个AccessDenied错误，原因是psutil获取信息也是要走系统接口，
# 而获取网络连接信息需要root权限，这种情况下，可以退出Python交互环境，用sudo重新启动

# 获取到所有进程的详细信息
print('获取到所有进程的详细信息')
# 所有进程ID
print('所有进程ID:', psutil.pids())
# 获取指定进程
p = psutil.Process(9484)
# 进程名称
print('进程名称:', p.name())
# 进程exe路径
print('进程exe路径:', p.exe())
# 进程工作目录
print('进程工作目录:', p.cwd())
# 进程启动的命令行
print('进程启动的命令行:', p.cmdline())
# 父进程ID
print('父进程ID:', p.ppid())
# 父进程
print('父进程:', p.parent())
# 子进程列表
print('子进程列表:', p.children())
# 进程状态
print('进程状态:', p.status())
# 进程用户名
print('进程用户名:', p.username())
# 进程创建时间
print('进程创建时间:', p.create_time())
# 进程终端
# print('进程终端:', p.terminal())
# 进程使用的CPU时间
print('进程使用的CPU时间:', p.cpu_times())
# 进程使用的内存
print('进程使用的内存:', p.memory_info())
# 进程打开的文件
print('进程打开的文件:', p.open_files())
# 进程相关网络连接
print('进程相关网络连接:', p.connections())
# 进程的线程数量
print('进程的线程数量:', p.num_threads())
# 所有线程信息
print('所有线程信息:', p.threads())
# 进程环境变量
print('进程环境变量:', p.environ())
# 结束进程
# p.terminate()
print()

# psutil还提供了一个test()函数，可以模拟出ps命令的效果
psutil.test()