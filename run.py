from app import organizeFiles
import argparse


parser = argparse.ArgumentParser()
parser.add_argument( "-d", "--directory", help="Directory absolute path." )
args = parser.parse_args()

if __name__ == '__main__':
    # desktop = "D:\\Downloads\\folderTest"
    organizeFiles(args.directory)