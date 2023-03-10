## os.path

os.path is used to process file names and directory paths.

As a standard library module, it provides a portable way of using operating system dependent functionality like pathname manipulation. The os.path module contains functions for manipulating file paths, such as joining paths, splitting paths, getting the basename of a file, and so on. Here's an example of how to use os.path to manipulate file paths:

```python
import os

# Join two paths together
path1 = 'folder1'
path2 = 'file.txt'
full_path = os.path.join(path1, path2)
print(full_path)  # Output: 'folder1/file.txt'

# Split a path into its directory and filename parts
dir_path, file_name = os.path.split(full_path)
print(dir_path)   # Output: 'folder1'
print(file_name)  # Output: 'file.txt'

# Get the basename of a path
base_name = os.path.basename(full_path)
print(base_name)  # Output: 'file.txt'

# Check if a file exists
exists = os.path.exists(full_path)
print(exists)     # Output: True
```

### os.path questions

Which of the following os.path functions can be used to join multiple paths together?

a. os.path.getsize

b. os.path.abspath

c. os.path.join

d. os.path.dirname

What is the difference between os.path.abspath and os.path.realpath?

a. abspath returns an absolute path while realpath returns the canonical path.

b. abspath returns the canonical path while realpath returns an absolute path.

c. abspath returns a relative path while realpath returns an absolute path.

d. abspath and realpath both return the same result.

Which of the following os.path functions can be used to split a path into its directory and file name parts?

a. os.path.join

b. os.path.basename

c. os.path.dirname

d. os.path.split

Which of the following os.path functions can be used to check if a path exists?

a. os.path.exists

b. os.path.getsize

c. os.path.isabs

d. os.path.isdir

Which of the following os.path functions can be used to get the size of a file in bytes?

a. os.path.getsize

b. os.path.abspath

c. os.path.isdir

d. os.path.split

Which of the following os.path functions can be used to check if a path is an absolute path?

a. os.path.abspath

b. os.path.realpath

c. os.path.isabs

d. os.path.join

Which of the following os.path functions can be used to get the last modification time of a file?

a. os.path.getatime

b. os.path.getctime

c. os.path.getmtime

d. os.path.getsize

### Code Evaluation: 

What will be the output of the following code?

```python
import os
print(os.path.join("/home/user", "Downloads", "file.txt"))
```

a) /home/user/Downloads/file.txt

b) \home\user\Downloads\file.txt

c) /home/user\Downloads\file/

d) /home/user/Downloads/

What will be the output of the following code?

```python
import os
print(os.path.splitext("file.txt"))
```

a) ("file", ".txt")

b) "file.txt"

c) "file"

d) ".txt"

What will be the output of the following code?

```python
import os
print(os.path.basename("/home/user/Downloads/file.txt"))
```

a) file.txt

b) /home/user/Downloads

c) /home/user/Downloads/file.txt

d) file

What will be the output of the following code?

```python
import os
print(os.path.exists("/home/user/Downloads/file.txt"))
```

a) True

b) False

c) Error

d) None

What will be the output of the following code?

```python
import os
print(os.path.isdir("/home/user/Downloads/"))
```
a) True

b) False

c) Error

d) None

What will be the output of the following code?

```python
import os
print(os.path.split("/home/user/Downloads/file.txt"))
```

a) ("/home/user/Downloads", "file.txt")

b) "/home/user/Downloads/file.txt"

c) ("file", ".txt")

d) ("/home/user", "Downloads", "file.txt")

What will be the output of the following code?

```python
import os
print(os.path.commonprefix(["/home/user/Downloads/file.txt", "/home/user/Downloads/file2.txt"]))
```

a) /home/user/Downloads/

b) /home/user/

c) /home/user/Downloads/file

d) /home/user/Downloads/file.txt

Which method returns the size of a file in bytes?

a) os.path.getsize()

b) os.path.isfile()

c) os.path.abspath()

d) os.path.isdir()

What is the output of the following code?

```python
import os.path
path = "/Users/john/Documents"
folder = os.path.basename(path)
print(folder)
```python

a) john

b) Documents

c) Users

d) /Users/john/Documents

Which method is used to join two or more pathname components, inserting the appropriate separator character?

a) os.path.join()

b) os.path.basename()

c) os.path.exists()

d) os.path.split()

What is the output of the following code?

```python
import os.path
path = "/Users/john/Documents/example.txt"
extension = os.path.splitext(path)[1]
print(extension)
```

a) txt

b) example.txt

c) /Users/john/Documents/

d) None

Which method is used to check if a file or directory exists at a given path?

a) os.path.abspath()

b) os.path.exists()

c) os.path.join()

d) os.path.split()

What is the output of the following code?

```python
import os.path
path = "/Users/john/Documents/example.txt"
is_file = os.path.isfile(path)
print(is_file)
```

a) True

b) False

c) None

d) An error occurs due to an invalid path.

Which method is used to split a pathname into a pair (root, ext) where ext is the extension and root is everything else?

a) os.path.join()

b) os.path.basename()

c) os.path.splitext()

d) os.path.isdir()

What is the output of the following code?

```python
import os.path
path = "/Users/john/Documents"
is_dir = os.path.isdir(path)
print(is_dir)
```

a) True

b) False
c) None

d) An error occurs due to an invalid path.

Which method returns the directory name of a path?

a) os.path.dirname()

b) os.path.join()

c) os.path.splitext()

d) os.path.abspath()

What is the output of the following code?

import os.path
path = "/Users/john/Documents/example.txt"
basename = os.path.basename(path)
print(basename)

a) example

b) example.txt

c) /Users/john/Documents/

d) None
