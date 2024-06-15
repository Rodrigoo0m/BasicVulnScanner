import os
import stat
import logging

logging.basicConfig(filename='vulnerability_scan.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_permissions(path, fix_permissions=False):
    """
    Check for inappropriate permissions on files and directories.

    Args:
        path (str): Directory to scan.
        fix_permissions (bool): If True, fix inappropriate permissions.

    """
    for root, dirs, files in os.walk(path):
        for name in dirs + files:
            full_path = os.path.join(root, name)
            try:
                st = os.stat(full_path)
                mode = st.st_mode

                if stat.S_ISDIR(mode):
                    if (mode & stat.S_IWOTH) or (mode & stat.S_IXOTH):
                        message = f'Directory with inappropriate permissions: {full_path} -> {oct(mode)}'
                        print(message)
                        logging.warning(message)
                        if fix_permissions:
                            new_mode = mode & ~stat.S_IWOTH & ~stat.S_IXOTH
                            os.chmod(full_path, new_mode)
                            message = f'Permissions fixed for: {full_path} -> {oct(new_mode)}'
                            print(message)
                            logging.info(message)

                elif stat.S_ISREG(mode):
                    if mode & stat.S_IWOTH:
                        message = f'File with inappropriate permissions: {full_path} -> {oct(mode)}'
                        print(message)
                        logging.warning(message)
                        if fix_permissions:
                            new_mode = mode & ~stat.S_IWOTH
                            os.chmod(full_path, new_mode)
                            message = f'Permissions fixed for: {full_path} -> {oct(new_mode)}'
                            print(message)
                            logging.info(message)
            except Exception as e:
                logging.error(f'Error checking {full_path}: {e}')
                print(f'Error checking {full_path}: {e}')

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Basic Vulnerability Scanner to Check File and Directory Permissions.")
    parser.add_argument('directory', type=str, help='Directory to scan.')
    parser.add_argument('--fix', action='store_true', help='Fix inappropriate permissions.')

    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print("The provided path is not a valid directory.")
    else:
        print(f'Starting scan in directory: {args.directory}')
        logging.info(f'Starting scan in directory: {args.directory}')
        check_permissions(args.directory, fix_permissions=args.fix)
        print('Scan completed.')
        logging.info('Scan completed.')
