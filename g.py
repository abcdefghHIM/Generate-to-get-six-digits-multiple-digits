max_num = 1000000
sp_num = 10000

# 生成主函数
f = open("main.c", "w", encoding="gbk")
f.write('#include "main.h"\n')
f.write("int main() {\n")
f.write("    int number;\n")
f.write('    printf("请输入一个六位数: ");\n')
f.write('    scanf("%d", &number);\n')

ncur = 0
mcur = ncur + sp_num - 1
while True:
    if mcur >= max_num:
        mcur = max_num - 1
    f.write(f"    if (number <= {mcur}) ")
    f.write("{\n")
    f.write(f"        func{ncur}_{mcur}(number);\n")
    f.write("        return 0;\n")
    f.write("    }\n")
    ncur += sp_num
    mcur = ncur + sp_num - 1
    if ncur >= max_num:
        break
f.write("}\n")
f.flush()
f.close()

# 生成头文件
f = open("main.h", "w", encoding="gbk")
f.write("#include <stdio.h>\n")
ncur = 0
mcur = ncur + sp_num - 1
while True:
    if mcur >= max_num:
        mcur = max_num - 1
    f.write(f"void func{ncur}_{mcur}(int num);\n")
    ncur += sp_num
    mcur = ncur + sp_num - 1
    if ncur >= max_num:
        break
f.flush()
f.close()

# 生成函数
ncur = 0
mcur = ncur + sp_num - 1
while True:
    if mcur >= max_num:
        mcur = max_num - 1
    f = open(f"func{ncur}_{mcur}.c", "w", encoding="gbk")
    f.write('#include "main.h"\n')
    f.write(f"void func{ncur}_{mcur}(int num) ")
    f.write("{\n")
    f.write("    switch(num) {\n")
    for i in range(sp_num):
        n = ncur + i
        f.write(f"        case {n}:\n")
        f.write(f'            printf("第六位：%d\\n", {n//100000});\n')
        f.write(f'            printf("第五位：%d\\n", {(n//10000)%10});\n')
        f.write(f'            printf("第四位：%d\\n", {(n//1000)%10});\n')
        f.write(f'            printf("第三位：%d\\n", {(n//100)%10});\n')
        f.write(f'            printf("第二位：%d\\n", {(n//10)%10});\n')
        f.write(f'            printf("第一位：%d\\n", {n%10});\n')
        f.write("            break;\n")
    f.write("    }\n")
    f.write("}\n")
    f.flush()
    f.close()
    ncur += sp_num
    mcur = ncur + sp_num - 1
    if ncur >= max_num:
        break
