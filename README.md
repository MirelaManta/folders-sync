# Folder Sync Project

#### This is a program that performs one-way synchronization of two folders.
* Synchronization is carried out periodically and changes(file update, copying, removal operations) are displayed in the console and written to a log file.
* Folder paths, synchronization interval and log file path can be provided using command line arguments, but there are also default values set for testing purposes.   

## Requirements

* Python 3.x
* Libraries: hashlib, os, time, shutil, argparse, logging
## How to Use

1. Ensure you have Python 3.x installed on your system.
2. Download or clone this repository to your local machine.

## Usage

```
python main.py [--source SOURCE] [--replica REPLICA] [--log-file LOG_FILE] [--time-interval TIME_INTERVAL]
```

- `--source`: Path to the source folder to be synchronized (default: "source").
- `--replica`: Path to the replica folder that will be updated to match the source folder (default: "replica").
- `--log-file`: Path to the log file (default: "log.txt").
- `--time-interval`: Time interval for synchronization in seconds (default: 60).

## Example

To synchronize a folder named "source_folder" to "replica_folder" with a time interval of 120 seconds and log the synchronization process to "sync_log.txt", run the following command:

```
python main.py --source source_folder --replica replica_folder --log-file sync_log.txt --time-interval 120
```

## Notes

- The script uses the MD5 hash of files to compare and determine if a file needs to be updated in the replica folder.
- If the replica folder does not exist, the script will create it.
- If the source folder does not exist, the script will raise an error.
- The script will continuously monitor the source folder and synchronize it with the replica folder based on the specified time interval.
- To stop the script manually, use the keyboard interrupt (CTRL+C).

