'''
通过读取result.sql中的sql语句，以AS和--作为分隔符，提取出每行的字段名
并且两个字段为一行，写到输出结果中
可以快速完成sql语句中update...set... 中字段的书写
'''

index = 1

with open(r'C:\Users\test\Desktop\result.sql', 'w', encoding='utf-8') as file:
    with open(r'C:\Users\test\Desktop\temp.sql', 'r', encoding='utf-8') as file_t:
        data = file_t.readlines()
        for d in data:
            if 'AS' in d:
                field_name = d.split('AS')[-1].split('--')[0].replace(',', '').strip()
                file.write(f"{field_name} = EXCLUDED.{field_name}, ")
                if index % 2 == 0:
                    file.write('\n')
                index += 1
            