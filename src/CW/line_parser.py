import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument('-fn', '--first-name', required=False)
parser.add_argument('-ln', '--last-name', required=False)
parser.add_argument('-m', '--message', required=False)
args = parser.parse_args()
print(parser.parse_args())

with open('line_data.txt', 'w') as file:
    try:
        file.write(args.first_name)
        file.write(' ')
        file.write(args.last_name)
        file.write('\n')

        file.write(f'Message: {args.message}')
    except:
        print('empty')

# file_path = os.path.realpath(__file__)
# print(file_path)
# dir_name = os.path.dirname(file_path)
# print(dir_name)
# os.mkdir('path_to_dir_2')
