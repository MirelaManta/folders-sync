### folders-synchronization-program

#### This is a program that performs one-way  synchronization of two folders.
* Synchronization is carried out periodically and changes(file update, copying, removal operations) are displayed in the console and written to a log file.
* Folder paths, synchronization interval and log file path can be provided using command line arguments, but there are also default values set for testing purposes.   

To run the program:  
```
python main.py
```
__sync_folders() arguments__:  
--source - It holds the path to the source folder, from where all contained files will be copied;  
--replica - It holds the path to the mirror folder, the destination where the source files will be copied to;  
--log-file - It holds the name of the file to which the logs will be written;  
--time_interval - It represents the time interval between two synchronizations, in seconds;


