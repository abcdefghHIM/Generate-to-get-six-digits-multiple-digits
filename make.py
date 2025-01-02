max_num = 1000000
sp_num = 10000

# 生成清理文件
f = open("zclean.cmd", "w", encoding="gbk")
f.write("@echo off\n")
f.write(f"del zlink.cmd\n")
f.write(f"del zmake.cmd\n")

f.write(f"del main.c\n")
f.write(f"del main.h\n")
f.write(f"del main.o\n")
ncur = 0
mcur = ncur + sp_num - 1
index = 0
while True:
    if mcur >= max_num:
        mcur = max_num - 1
    f.write(f"del func{ncur}_{mcur}.c\n")
    f.write(f"del func{ncur}_{mcur}.o\n")
    f.write(f"del func{ncur}_{mcur}.cmd\n")
    ncur += sp_num
    mcur = ncur + sp_num - 1
    if ncur >= max_num:
        break
f.write(f"del zclean.cmd\n")
f.flush()
f.close()

# 生成链接文件
f = open("zlink.cmd", "w", encoding="gbk")
f.write("@echo off\n")
f.write(f"gcc -c main.c\n")
f.write(f"gcc ")
ncur = 0
mcur = ncur + sp_num - 1
while True:
    if mcur >= max_num:
        mcur = max_num - 1
    f.write(f"func{ncur}_{mcur}.o ")
    ncur += sp_num
    mcur = ncur + sp_num - 1
    if ncur >= max_num:
        break
f.write(f"main.o -o six.exe")
f.flush()
f.close()

# 生成主文件
f = open("zmake.cmd", "w", encoding="gbk")
f.write("@echo off\n")
ncur = 0
mcur = ncur + sp_num - 1
while True:
    if mcur >= max_num:
        mcur = max_num - 1
    f.write(f"start func{ncur}_{mcur}.cmd\n")
    ncur += sp_num
    mcur = ncur + sp_num - 1
    if ncur >= max_num:
        break
f.flush()
f.close()


# 生成编译文件
ncur = 0
mcur = ncur + sp_num - 1
while True:
    if mcur >= max_num:
        mcur = max_num - 1
    f = open(f"func{ncur}_{mcur}.cmd", "w", encoding="gbk")
    f.write("@echo off\n")
    f.write(f"echo 检查是否存在 func{ncur}_{mcur}.o 文件...\n")
    f.write(f"if exist func{ncur}_{mcur}.o (\n")
    f.write(f"    echo func{ncur}_{mcur}.o 已存在，跳过编译。\n")
    f.write(") else (\n")
    f.write(f"    gcc -c func{ncur}_{mcur}.c\n")
    f.write(")\n")
    f.write("exit")
    f.flush()
    f.close()
    ncur += sp_num
    mcur = ncur + sp_num - 1
    if ncur >= max_num:
        break
