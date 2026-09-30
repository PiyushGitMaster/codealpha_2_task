# Python Security Demo: From `eval()` to `ast.literal_eval()`

## 📖 Overview

This repository demonstrates a common security vulnerability in Python applications: the unsafe use of the `eval()` function. It serves as an educational example of how to identify arbitrary code execution risks and how to properly mitigate them using `ast.literal_eval()`.

The project contains a sample security review report and the corresponding "fixed" code that adheres to secure coding standards.

## 🚨 The Vulnerability

**Topic:** Remote Code Execution (RCE) via `eval()`

The original code (conceptually represented in the security notes) used Python's built-in `eval()` function to parse configuration data. Because `eval()` parses and executes any valid Python expression, it allows an attacker to execute arbitrary commands on the host machine if they can control the input data.

**Example of an attack:**
If user input is `__import__('os').system('rm -rf /')`, `eval()` will execute it, potentially destroying the system.

## 🛡️ The Fix

The code has been refactored to use `ast.literal_eval()`. This function safely evaluates a string containing a Python literal (strings, bytes, numbers, tuples, lists, dicts, sets, booleans, and None). It **does not** execute function calls or arbitrary code.

### Comparison

**❌ Vulnerable Code:**
```python
def load_configuration(data):
    # DANGEROUS: Executes any Python expression
    return eval(data)
