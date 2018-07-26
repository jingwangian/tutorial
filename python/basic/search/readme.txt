Local Measure - Technical Test

Preface:

Do not use any extended functionality of the framework to solve this problem. (For example, don't use the string methods that have functionality such as IndexOf, substring, regular expression classes, LINQ etc). The test should take no longer than an hour for you to complete, please submit the working source code to solve the problem along with any supporting code that you might have used in testing. 

Problem: 

We need a way of finding all the occurrences of a particular set of characters in a string. It should 
• Accept two strings as input. One called 'textToSearch' and one called 'subtext' 
• The solution should match the subtext against the textToSearch, outputting the positions of the beginning of each match for the subtext within the textToSearch. 
• Multiple matches are possible 
• Matching is case insensitive 
• If no matches have been found, no output is generated 

Sample Acceptance Criteria 

Text: 
textToSearch = "Peter told me that Peter the pickle piper piped a pitted pickle before he petered out. Phew!" 

Subtext: Expected Result 
Peter "1, 20, 75" 
peter "1, 20, 75" 
pick "30, 58" 
pi "30, 37, 43, 51, 58" 
z "<No Output>" 
Peterz “<No Output>” 
