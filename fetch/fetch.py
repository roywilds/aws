import sys
import subprocess


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Fetch data files and store locally.')
    parser.add_argument('--input', type=str, action='store', default=None)
    parser.add_argument('--dir', type=str, action='store', default=None)
    args = parser.parse_args()

    if args.input is None:
        sys.stderr.write('No input list of website resources to download. Exiting\n')
        return 1
    wget_files = args.input
    out_dir = args.dir
    if out_dir is None:
        sys.stderr.write('No output directory provided. Using /tmp/\n')
        out_dir = '/tmp/'

    # Create a temp dir for storing files
    temp_dir = '/tmp/fetch_temp_dir'
    subprocess.run(['mkdir','-p', temp_dir])

    with open(wget_files, 'r') as file_list:
        for wgets in file_list.readlines():
            cmd = 'wget '+wgets
            sys.stdout.write('Executing ' + cmd + '\n')
            p = subprocess.Popen(cmd, cwd=temp_dir, stdout=subprocess.PIPE)
            wget_output = p.communicate()[0]
            sys.stdout.write('Output: ' + str(wget_output))
            sys.stdout.write('\n')


if __name__ == "__main__":
    sys.exit(main())