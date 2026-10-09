# Session 19 Concepts: Working with Files

This folder contains a detailed article about file handling in Python. These concepts build on the lecture covering reading and writing text files.

## Table of Contents

### File Handling Fundamentals
- **📄 [File Handling Basics](file-handling-basics.md)**: Reading and writing text files with `open()`, `with`, and error handling

## Detailed Article Descriptions

### 📄 [File Handling Basics](file-handling-basics.md)
Master file operations in Python. Learn how to read files line by line, write text to files, append to existing files, and handle common file errors like FileNotFoundError and PermissionError. Includes practical examples for word counting, copying files, parsing CSV data, and generating reports.

## How to Use These Articles

1. **Read the article**: Start with the fundamentals of file paths and modes
2. **Practice the examples**: Work through the code examples
3. **Apply the patterns**: Use the safe file handling patterns in your own programs

## Key Themes

- **`with` statement**: Always use it for automatic file closing
- **File modes**: `'r'` read, `'w'` write (truncates), `'a'` append
- **Error handling**: Catch FileNotFoundError and PermissionError
- **Line-by-line processing**: Memory-efficient for large files

## Prerequisites

These articles assume you've completed the lecture covering:
- Basic Python syntax and functions
- try/except error handling basics

## Learning Objectives

After reading these articles, you'll understand:
- How to open, read, write, and close files safely
- The difference between `'w'` and `'a'` modes
- Why the `with` statement is essential
- How to handle file errors gracefully
- Practical patterns for common file operations

## Next Steps

After mastering file handling, you'll have:
- **Module 5: Software Development** - Complete application development skills
- Understanding of file I/O, error handling, and data persistence
- Ready to move to organizing code into modules and files

---

*These articles give you the skills to make your programs remember data between runs.*