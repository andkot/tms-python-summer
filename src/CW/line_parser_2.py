import argparse
import time

parser = argparse.ArgumentParser()

parser.add_argument('-fn', '--first-name', required=True)
parser.add_argument('-ln', '--last-name', required=True)
parser.add_argument('-t', '--time', required=True)

args = parser.parse_args()
print(args)

print(args.time)

t = time.strftime("%H, %M, $S", args.time)
print(t)

with open('log.txt', 'w') as file:
    try:
        file.write(args.first_name)
        file.write(' ')
        file.write(args.last_name)
        file.write('\n')

        file.write(f'time: {args.time}')
    except:
        print('empty')
