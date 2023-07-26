import hashlib
import os
import time
import shutil
import argparse
import logging


def sync_folders(source, replica, log_file, time_interval):
    if not os.path.isdir(replica):
        os.makedirs(replica)

    if not os.path.isdir(source):
        raise argparse.ArgumentError(None, "The source folder doesn't exist.")

    logging.info(f"Start with parameters:\nsource:{source}\nreplica:{replica}\nlog:{log_file}\ntime_interval:{time_interval}\n")

    while True:
        try:
            compare_folders(source, replica)
            time.sleep(time_interval)
        except KeyboardInterrupt:
            print("The Program is terminated manually!")
            raise SystemExit


def compare_files(file1, file2):
    with open(file1, "rb") as f1, open(file2, "rb") as f2:
        return hashlib.md5(f1.read()).hexdigest() == hashlib.md5(f2.read()).hexdigest()


def compare_folders(source_f, replica_f):
    files_source = os.listdir(source_f)
    files_replica = os.listdir(replica_f)

    for file in files_source:
        source_file_path = os.path.join(source_f, file)
        replica_file_path = os.path.join(replica_f, file)

        if file in files_replica:
            if compare_files(source_file_path, replica_file_path):
                log_message = f"{file} is up to date."
            else:
                os.remove(replica_file_path)
                shutil.copy2(source_file_path, replica_file_path)
                log_message = f"{file} has been updated."
        else:
            shutil.copy2(source_file_path, replica_file_path)
            log_message = f"{file} has been copied."

        logging.info(log_message)
        print(log_message)

    for file in files_replica:
        if file not in files_source:
            os.remove(os.path.join(replica_f, file))
            log_message = f"{file} has been deleted."
            logging.info(log_message)
            print(log_message)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Folder synchronization program')
    parser.add_argument('--source', type=str, default="source", help='Source folder path')
    parser.add_argument('--replica', type=str, default="replica", help='Replica folder path')
    parser.add_argument('--log-file', type=str, default='log.txt', help='Log file path')
    parser.add_argument('--time-interval', type=int, default=60, help='Time interval for synchronization in seconds')
    args = parser.parse_args()

    logging.basicConfig(filename=args.log_file, level=logging.INFO, format='%(asctime)s [%(levelname)s]: %(message)s')
    sync_folders(args.source, args.replica, args.log_file, args.time_interval)
