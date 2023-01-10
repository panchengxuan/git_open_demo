import os

path = r'D:\py_workspace\api_test\PRE_199401-202012'
output_path = r'D:\py_workspace\api_test\output'
if not os.path.exists(output_path):
    os.mkdir(output_path)
files = sorted(os.listdir(path))
output = dict()
summer_water = 0
for file_name in files:
    year = file_name[31:35]
    month = file_name[35:37]
    if 2011 <= int(year) and 2020 >= int(year) and 6 <= int(month) and 8 >= int(month):
        with open(path + '\\' + file_name) as file:
            lines = file.readlines()
            for line in lines:
                line = line.replace('\n', '')
                splits = [content for content in line.split(' ') if content != '']
                position = splits[0]
                l = splits[1]
                h = splits[2]

                half_water_day = 0 if splits[7] == '32700' else int(splits[7])
                half_water_night = 0 if splits[8] == '32700' else int(splits[8])
                half_water_all_day = half_water_day + half_water_night
                if output.get(position + ' ' + l + ' ' + h) is None:
                    output[position + ' ' + l + ' ' + h] = half_water_all_day
                else:
                    output[position + ' ' + l + ' ' + h] += half_water_all_day
                summer_water += half_water_all_day
        if int(month) == 8:
            filename = output_path + '\\' + year+".csv"
            with open(filename, 'w') as file_object:
                for key, value in output.items():
                    print(key ,value)
                    file_object.write( ','.join(((key + ' ' + str(value)).split(' ')))+"\n")  # 写入第一行内容，为避免内容挤在一起，用‘\n’换行
            output = dict()