import hashlib
import os
import time
import shutil
import click as click


@click.command()
@click.option('--source', type=str, default="source")
@click.option('--replica', type=str,  default="replica")
@click.option('--log-file', type=str,  default="log.txt")
@click.option('--time-interval', type=int,  default=300)
def sync_folders(source, replica, log_file, time_interval):

    if not os.path.isdir(replica):
        os.makedirs("replica")

    if not os.path.isdir("source"):
        raise SystemExit("The source folder doesn't exist.")

    write_log(f'''
        Start with parameters:
        source:{source}
        replica:{replica}
        log:{log_file}
        time_interval:{time_interval}
        ''')

    while True:
        try:
            compare_folders(source, replica)
            time.sleep(time_interval)
        except KeyboardInterrupt:
            print("The Program is terminated manually!")
            raise SystemExit


def write_log(message):
    time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"[{time_now}] {message}")
    with open("log.txt", "a") as log_file:
        log_file.write(f"[{time_now}] {message}\n")


def compare_files(file1, file2):
    with open(file1, "rb") as f1:
        content = f1.read()
        with open(file2, "rb") as f2:
            content_f2 = f2.read()
            if hashlib.md5(content).hexdigest() == hashlib.md5(content_f2).hexdigest():
                return True
            else:
                return False


def compare_folders(source_f, replica_f):
    files_source = os.listdir(source_f)
    files_replica = os.listdir(replica_f)

    for file in files_source:
        if file in files_replica:
            if compare_files(f"{source_f}/{file}", f"{replica_f}/{file}"):
                write_log(f"{file} is up to date.")
            else:
                os.remove(f"{replica_f}/{file}")
                shutil.copyfile(f"{source_f}/{file}", f"{replica_f}/{file}")
                write_log(f"{file} has been updated.")
        else:
            shutil.copyfile(f"{source_f}/{file}", f"{replica_f}/{file}")
            write_log(f"{file} has been copied.")

    for file in files_replica:
        if file not in files_source:
            os.remove(f"{replica_f}/{file}")
            write_log(f"{file} has been deleted.")


if __name__ == '__main__':
    sync_folders()
