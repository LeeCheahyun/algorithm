import argparse
# from typing_extensions import Required

args = argparse.ArgumentParser()

args.add_argument('-x', '--xVal', required= True)
# args.add_argumnt('-y', '--yVal', required=False)

garuvar = vars(args.parse_args())

pass