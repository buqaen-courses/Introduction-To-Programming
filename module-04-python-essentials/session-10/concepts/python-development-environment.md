# Python Development Environment: Tools for Coding

## What You'll Learn
- What tools you need to write Python code
- How to choose a code editor
- How to run Python programs

---

## What You Need to Start Coding

To write and run Python programs, you need:

1. **Python** installed on your computer (the interpreter)
2. A **code editor** (where you write your code)
3. A **terminal/command prompt** (where you run your code)

That's it! Let's look at each one.

---

## 1. Installing Python

### Checking if Python is Already Installed

Open your terminal/command prompt and type:

```bash
python --version
```

Or on some systems:

```bash
python3 --version
```

If you see something like `Python 3.9.7`, you're all set!

### Installing Python (If You Don't Have It)

#### Windows
1. Go to [python.org/downloads](https://python.org/downloads)
2. Click "Download Python" (the big yellow button)
3. Run the installer
4. **Important:** Check the box "Add Python to PATH" during installation
5. Click "Install Now"

#### Mac
1. Open Terminal
2. Install Homebrew (if you don't have it): visit [brew.sh](https://brew.sh)
3. Type: `brew install python3`

#### Linux
Python is usually pre-installed. If not:

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3

# Verify installation
python3 --version
```

---

## 2. Choosing a Code Editor

A code editor is like a word processor for programming. Here are some good options:

### For Beginners: IDLE (Comes with Python)

**IDLE** is included when you install Python. It's simple and perfect for learning.

**How to open IDLE:**
- **Windows:** Search for "IDLE" in the Start menu
- **Mac:** Find it in Applications → Python
- **Linux:** Type `idle` in terminal

**Features:**
- Simple interface
- Shows your code in colors (syntax highlighting)
- Built-in help for beginners

### For Intermediate Users: VS Code

**VS Code** (Visual Studio Code) is free, powerful, and popular among programmers.

**How to get it:**
1. Download from [code.visualstudio.com](https://code.visualstudio.com)
2. Install it
3. Install the Python extension (VS Code will suggest this)

**Why VS Code?**
- Free and works on all platforms
- Helps you write better code with suggestions
- Built-in terminal

### Other Options

| Editor | Best For | How to Get It |
|--------|----------|---------------|
| **Thonny** | Complete beginners | [thonny.org](https://thonny.org) |
| **PyCharm** | Professional development | [jetbrains.com/pycharm](https://jetbrains.com/pycharm) |
| **Sublime Text** | Fast, lightweight editing | [sublimetext.com](https://sublimetext.com) |

---

## 3. Using the Terminal/Command Prompt

The terminal (also called command prompt, console, or shell) is where you type commands to run your programs.

### Opening the Terminal

- **Windows:** Press `Win + R`, type `cmd`, press Enter
  - Or use PowerShell (more modern)
- **Mac:** Press `Cmd + Space`, type `terminal`, press Enter
- **Linux:** Press `Ctrl + Alt + T`

### Basic Terminal Commands

These help you navigate to your Python files:

```bash
# See what folder you're in
pwd          # Mac/Linux
cd           # Windows

# List files in the current folder
ls           # Mac/Linux
dir          # Windows

# Change to a different folder
cd Documents
cd my_project

# Go up one folder
cd ..

# Go to your home folder
cd ~         # Mac/Linux
cd %USERPROFILE%   # Windows
```

---

## Running Your First Python Program

### Method 1: Using IDLE

1. Open IDLE
2. Click **File → New File**
3. Type: `print("Hello, World!")`
4. Click **Run → Run Module** (or press F5)
5. Save the file when prompted (use `.py` extension)

### Method 2: Using VS Code

1. Open VS Code
2. Click **File → New File**
3. Save it as `hello.py`
4. Type: `print("Hello, World!")`
5. Click the "Play" button (▶) in the top right, or right-click and select "Run Python File"

### Method 3: Using Terminal

1. Create a file called `hello.py` in your editor
2. Add this code: `print("Hello, World!")`
3. Open terminal
4. Navigate to the folder with your file using `cd`
5. Run: `python hello.py` (or `python3 hello.py`)

---

## Your Coding Workflow

Here's the typical process for writing and running Python code:

```
1. Open your code editor
        ↓
2. Write or edit your code
        ↓
3. Save the file (Ctrl+S / Cmd+S)
        ↓
4. Open terminal
        ↓
5. Navigate to your file's folder
        ↓
6. Run: python filename.py
        ↓
7. See the output!
        ↓
8. Go back to step 2 to make changes
```

---

## Common Beginner Mistakes

### Mistake 1: Not Saving Before Running

**Problem:** You make changes, run the program, but see old output.

**Solution:** Always save your file before running (Ctrl+S / Cmd+S).

### Mistake 2: Wrong File Extension

**Problem:** Your file is named `myprogram.txt` instead of `myprogram.py`.

**Solution:** Python files must end with `.py`.

### Mistake 3: Python Not in PATH (Windows)

**Problem:** You type `python` but get an error saying it's not recognized.

**Solution:** During Python installation, check "Add Python to PATH". If you missed this, reinstall Python.

### Mistake 4: Running Python from the Wrong Folder

**Problem:** You try to run `python hello.py` but you're in the wrong folder.

**Solution:** Use `cd` to navigate to the folder containing your Python file.

---

## Try It Yourself: Setup Exercise

### Exercise 1: Verify Your Setup

1. Open your terminal
2. Type `python --version` (or `python3 --version`)
3. You should see your Python version
4. Type `python` (or `python3`) to enter interactive mode
5. Type `print("It works!")`
6. You should see "It works!"
7. Type `exit()` to quit

### Exercise 2: Create and Run a File

1. Open your code editor
2. Create a new file
3. Save it as `test.py`
4. Type: `print("My first Python program!")`
5. Save the file
6. Open terminal and navigate to the file's location
7. Run: `python test.py`
8. You should see the output!

---

## Quick Reference

### Opening the Terminal

| Operating System | How to Open |
|------------------|-------------|
| Windows | Press `Win + R`, type `cmd` |
| Mac | Press `Cmd + Space`, type `terminal` |
| Linux | Press `Ctrl + Alt + T` |

### Running Python

| Task | Command |
|------|---------|
| Check version | `python --version` |
| Interactive mode | `python` |
| Run a file | `python filename.py` |

### Common Terminal Commands

| Task | Mac/Linux | Windows |
|------|-----------|---------|
| Current folder | `pwd` | `cd` |
| List files | `ls` | `dir` |
| Change folder | `cd foldername` | `cd foldername` |
| Go up | `cd ..` | `cd ..` |
| Go home | `cd ~` | `cd %USERPROFILE%` |

---

## Key Takeaways

1. **You need three things:** Python, a code editor, and a terminal
2. **IDLE is great for beginners** - it comes with Python
3. **VS Code is popular** for when you're ready for more features
4. **Save before running** - Python runs what's saved on disk
5. **Use the terminal** to run your Python programs
6. **Navigate to the right folder** before running your code

---

## What's Next?

Now that your environment is set up, let's start learning Python:
- How to write your first programs
- Understanding variables and data types
- Making your programs interactive
