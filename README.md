# String_Matching_Project
In this project, the goal is to identify exact matches between two Excel files that share some similarities. However, these files may contain variations in the formatting of their data, which makes comparing them difficult. To overcome this challenge, the Python programming language offers a built-in module named "difflib," which provides a SequenceMatcher class that can compare two strings and calculate their similarity ratio.

Using the SequenceMatcher class, I compared the strings from both Excel files and obtained a score that represents the similarity ratio between the two strings. The score ranges from 0 to 1, where 0 means the strings have no similarities, and 1 indicates that the strings are identical.

After obtaining the scores, I selected the highest score as my output, which represents the closest match between the two strings. This approach allows me to identify the best matching data from the two Excel files, even if the formatting is slightly different.
