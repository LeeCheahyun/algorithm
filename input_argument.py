import argparse
# from typing_extensions import Required

args = argparse.ArgumentParser()

args.add_argument('-x','--xval',required=True)
# args.add_argument('-y', '--yVal', required=False)

argvar = vars(args.parse_args())

print(argvar['xval'])

pass