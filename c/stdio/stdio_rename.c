#include <stdio.h>

/*
int rename ( const char * oldname, const char * newname );

Rename file
    Changes the name of the file or directory specified by oldname to newname.

This is an operation performed directly on a file; No streams are involved in the operation.

If oldname and newname specify different paths and this is supported by the system, the file is moved to the new location.

If newname names an existing file, the function may either fail or override the existing file, depending on the specific system and library implementation.

Proper file access shall be available.
*/

int main()
{
    int result;
    char old_file_name[] = "oldfile.txt";
    char new_file_name[] = "newfile.txt";

    result = rename(old_file_name,new_file_name);

    if(result == 0)
        puts("File successfully renamed");
    else
        perror("Error renamingfile");

    return 0;
}
