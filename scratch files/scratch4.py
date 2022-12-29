# print(format(211, 'x').upper())
[{'header': 'a'}, {'header': 'b'}]

from infodict import total_df_human_column_list, total_df_zombie_column_list

result = ""
for item in total_df_zombie_column_list:
    result = ', '.join([result, ''.join(["{'header': ", f"'{item}'", "}"])])

print(result)