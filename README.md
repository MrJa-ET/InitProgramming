# Linux Basic Commands

Here is a list of basic Linux commands:
1. pwd command

Use the pwd command to find out the path of the current working directory (folder) you’re in. The command will return an absolute (full) path, which is basically a path of all the directories that starts with a forward slash (/). An example of an absolute path is /home/username.
2. cd command

To navigate through the Linux files and directories, use the cd command. It requires either the full path or the name of the directory, depending on the current working directory that you’re in.

Let’s say you’re in /home/username/Documents and you want to go to Photos, a subdirectory of Documents. To do so, simply type the following command: cd Photos.

Another scenario is if you want to switch to a completely new directory, for example,/home/username/Movies. In this case, you have to type cd followed by the directory’s absolute path: cd /home/username/Movies.

There are some shortcuts to help you navigate quickly:

    cd .. (with two dots) to move one directory up
    cd to go straight to the home folder
    cd- (with a hyphen) to move to your previous directory

On a side note, Linux’s shell is case sensitive. So, you have to type the name’s directory exactly as it is.
3. ls command

The ls command is used to view the contents of a directory. By default, this command will display the contents of your current working directory.

If you want to see the content of other directories, type ls and then the directory’s path. For example, enter ls /home/username/Documents to view the content of Documents.

There are variations you can use with the ls command:

    ls -R will list all the files in the sub-directories as well
    ls -a will show the hidden files
    ls -al will list the files and directories with detailed information like the permissions, size, owner, etc.

4. cat command

cat (short for concatenate) is one of the most frequently used commands in Linux. It is used to list the contents of a file on the standard output (sdout). To run this command, type cat followed by the file’s name and its extension. For instance: cat file.txt.

Here are other ways to use the cat command:

    cat > filename creates a new file
    cat filename1 filename2>filename3 joins two files (1 and 2) and stores the output of them in a new file (3)
    to convert a file to upper or lower case use, cat filename | tr a-z A-Z >output.txt

5. cp command

Use the cp command to copy files from the current directory to a different directory. For instance, the command cp scenery.jpg /home/username/Pictures would create a copy of scenery.jpg (from your current directory) into the Pictures directory.

