import argparse
from src.HW12.task_12_1 import MyTime

parser = argparse.ArgumentParser()

parser.add_argument('-fn', '--first-name', required=True)
parser.add_argument('-ln', '--last-name', required=True)
parser.add_argument('-t', '--time', required=True)

args = parser.parse_args()
print(args)

second =  MyTime('00:00:01')
time = MyTime()
