**Task:**

Create a function `decode(<file_name>)` to read an encrypted message stored in a file and return the decoded message as a string.

Each line in the file contains a word and an identifier number starting from 1 separated by a space character. Get the word identified by the last number on each line of the following pyramid and form a sentence (the decoded message). Numbers are separated by a space character.
```
   1
  2 3
 4 5 6
  ...
```

> [!NOTE]
> This task description is approximate because the original one wasn't saved.

**Sample input:**
```
3 love
6 computers
2 dogs
4 cats
1 i
5 you
```

**Sample output:**
```
i love computers
```

> [!TIP]
> [sample_input.txt](sample_input.txt) is a simple input test file copied from the task description.
> 
> [coding_qual_input.txt](coding_qual_input.txt) is a more complex test file provided by DataAnnotation on which the decoding function will be tested.
