# import os
# import re
#
#
# def iso_split_lines_to_files(input_file_folder_path, workflow_name):
#     # Get files form the folder and also use the folder path to get write the other files
#     src_input_file = os.listdir(input_file_folder_path)
#
#     folder_path = os.path.dirname(input_file_folder_path)
#     src_input_file = os.path.join(folder_path, src_input_file[0])
#     valid_mt_file = os.path.join(folder_path, f"{workflow_name}_valid_mt.txt")
#     valid_mx_file = os.path.join(folder_path, f"{workflow_name}_valid_mx.txt")
#     valid_error_file = os.path.join(folder_path, f"{workflow_name}_valid_error.txt")
#     file_count_file = os.path.join(folder_path, f"{workflow_name}_file_count.txt")
#
#     # Define the regular expression patterns
#     valid_mt_pattern = re.compile(r"{1:")
#     valid_mx_pattern = re.compile(r"pacs\.008|\bMsgDefIdr>pacs\.008</MsgDefIdr>")
#     # valid_error_pattern = re.compile(r"")
#
#     # Initialize the counters
#     valid_mt_count = 0
#     valid_mx_count = 0
#     valid_error_count = 0
#
#     # Loop through the data and write each line to the appropriate file
#     with open(src_input_file, "r") as src_input_line, \
#             open(valid_mt_file, "w") as mt_file, \
#             open(valid_mx_file, "w") as mx_file, \
#             open(valid_error_file, "w") as error_file:
#         for line in src_input_line:
#             if valid_mt_pattern.search(line):
#                 mt_file.writelines(line)
#                 valid_mt_count += 1
#             elif valid_mx_pattern.search(line):
#                 mx_file.writelines(line)
#                 valid_mx_count += 1
#             else:
#                 error_file.writelines(line)
#                 valid_error_count += 1
#
#     # Write the file count data to file_count.txt
#     with open(file_count_file, "w+") as count_file:
#         count_file.write(f"Valid MT = {valid_mt_count}\n")
#         count_file.write(f"Valid MX = {valid_mx_count}\n")
#         count_file.write(f"Valid Error = {valid_error_count}\n")
#
# def read_count_file(file_path):
#     with open(file_path, 'r') as f:
#         lines = f.readlines()
#     valid_mt_count, valid_mx_count, valid_error_count = [int(x.split('=')[1]) for x in lines]
#     return valid_mt_count, valid_mx_count, valid_error_count
#
#
# source = "/Users/arun/PycharmProjects/xml/data/brains/"
# iso_split_lines_to_files(source, "Brains")
# count = "/Users/arun/PycharmProjects/xml/data/brains/Brains_file_count.txt"
#
# valid_mt_count, valid_mx_count, valid_error_count = read_count_file(count)
# print(valid_mt_count, valid_mx_count, valid_error_count)

import os
import re


def iso_split_lines_to_files(input_file_folder_path, workflow_name):
    # Get files form the folder and also use the folder path to get write the other files
    src_input_file = os.listdir(input_file_folder_path)

    folder_path = os.path.dirname(input_file_folder_path)
    src_input_file = os.path.join(folder_path, src_input_file[0])


    valid_mt_file = os.path.join(folder_path, f"{workflow_name}_valid_mt.txt")
    valid_mx_file = os.path.join(folder_path, f"{workflow_name}_valid_mx.txt")
    valid_error_file = os.path.join(folder_path, f"{workflow_name}_valid_error.txt")
    file_count_file = os.path.join(folder_path, f"{workflow_name}_file_count.txt")

    # Delete the output files if they already exist
    for output_file in [valid_mt_file, valid_mx_file, valid_error_file, file_count_file]:
        if os.path.exists(output_file):
            os.remove(output_file)



    # Define the regular expression patterns
    valid_mt_pattern = re.compile(r"{1:")
    valid_mx_pattern = re.compile(r"pacs\.008|\bMsgDefIdr>pacs\.008</MsgDefIdr>")
    # valid_error_pattern = re.compile(r"")

    # Initialize the counters
    valid_mt_count = 0
    valid_mx_count = 0
    valid_error_count = 0

    # Loop through the data and write each line to the appropriate file
    with open(src_input_file, "r") as src_input_line, \
            open(valid_mt_file, "w") as mt_file, \
            open(valid_mx_file, "w") as mx_file, \
            open(valid_error_file, "w") as error_file:
        for line in src_input_line:
            if valid_mt_pattern.search(line):
                mt_file.write(line)
                valid_mt_count += 1
            elif valid_mx_pattern.search(line):
                mx_file.write(line)
                valid_mx_count += 1
            else:
                error_file.write(line)
                valid_error_count += 1

    # Write the file count data to file_count.txt
    with open(file_count_file, "w+") as count_file:
        count_file.write(f"Valid MT = {valid_mt_count}\n")
        count_file.write(f"Valid MX = {valid_mx_count}\n")
        count_file.write(f"Valid Error = {valid_error_count}\n")


def read_count_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    valid_mt_count, valid_mx_count, valid_error_count = [int(x.split('=')[1]) for x in lines]
    return valid_mt_count, valid_mx_count, valid_error_count


def main():
    source = "/Users/arun/PycharmProjects/xml/data/brains/"
    workflow_name = "Brains"
    iso_split_lines_to_files(source, workflow_name)
    count = os.path.join(source, f"{workflow_name}_file_count.txt")
    valid_mt_count, valid_mx_count, valid_error_count = read_count_file(count)
    print(valid_mt_count, valid_mx_count, valid_error_count)


if __name__ == '__main__':
    main()

