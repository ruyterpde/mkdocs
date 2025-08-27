---
title: Developing and Documenting Public Python Functions
description: A comprehensive tutorial on creating, documenting, and managing public functions in Python for clear, reusable, and maintainable code.
---

# Developing and Documenting Public Python Functions

## Introduction

In software development, especially when creating libraries, modules, or reusable components, **public functions** serve as the primary interface for users to interact with your code. These functions are part of the public API (Application Programming Interface) and are designed to be used by other parts of your application or by external developers.

This tutorial guides you through the process of designing, implementing, and most importantly, documenting public functions effectively in Python. Mastering this skill ensures your code is not only functional but also intuitive, easy to use, and maintainable for anyone consuming it.

## Overview

The challenge with creating reusable code lies in its accessibility and clarity. Without proper structure and documentation, even the most robust functions can become a burden to use and understand. This leads to:

*   **Confusion**: Users struggle to understand what a function does, its parameters, or what it returns.
*   **Misuse**: Functions are used incorrectly, leading to bugs or unexpected behavior.
*   **Maintenance Overhead**: Developers spend more time deciphering existing code than writing new features.
*   **Limited Adoption**: Your well-crafted code goes unused because it's too difficult to integrate.

This tutorial addresses these problems by demonstrating best practices for defining public functions, emphasizing the critical role of docstrings and type hints in making your code self-documenting and user-friendly.

## Prerequisites

Before you begin this tutorial, ensure you have the following:

*   **Python 3.6+**: Installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
*   **Basic Python Knowledge**: Familiarity with Python syntax, functions, and modules.
*   **Text Editor or IDE**: Such as VS Code, PyCharm, or Sublime Text.
*   **Command Line Interface (CLI)**: Basic understanding of navigating directories and executing Python scripts.

## Execution

Follow these steps to create and document your first public Python function.

### Step 1: Set Up Your Project Directory

First, create a new directory for your project and navigate into it.

```bash
mkdir public_functions_tutorial
cd public_functions_tutorial
```

### Step 2: Create a Module with a Public Function

We will create a file named `shapes.py` that will contain our public function for calculating the area of a rectangle.

Create a file named `shapes.py` in your `public_functions_tutorial` directory and add the following content:

```python
# shapes.py

def calculate_rectangle_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.

    This function takes the length and width of a rectangle
    and returns its area.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The calculated area of the rectangle.

    Raises:
        ValueError: If length or width is negative.

    Examples:
        >>> calculate_rectangle_area(5, 10)
        50.0
        >>> calculate_rectangle_area(7.5, 2.0)
        15.0
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative values.")
    return length * width

# This function is considered 'private' by convention
# because its name starts with an underscore.
def _private_helper_function(value: float) -> float:
    """A helper function not intended for public use."""
    return value * 2
```

!!! tip "Docstring Standards"
    The example above uses the [Google Style Docstring](https://google.github.io/styleguide/pyguide.html#pyguide-docstrings) format, which is highly readable and widely adopted. Other popular formats include reStructuredText (used by Sphinx) and NumPy style. Choose one and stick to it for consistency.

#### Understanding the Code:

*   **Function Naming**: `calculate_rectangle_area` follows Python's [PEP 8](https://peps.python.org/pep-0008/#function-and-variable-names) guidelines for function names (lowercase, words separated by underscores). Public functions should have clear, descriptive names.
*   **Docstring**: This multi-line string immediately after the function signature is crucial. It describes what the function does, its arguments (`Args`), what it returns (`Returns`), potential errors (`Raises`), and usage examples (`Examples`).
*   **Type Hints (`: float`, `-> float`)**: These provide static type information, making the code easier to understand and enabling static analysis tools (like MyPy) to catch potential type-related errors.
*   **Error Handling**: The `ValueError` demonstrates how to handle invalid inputs gracefully, providing clear feedback to the user.
*   **Private Functions**: The `_private_helper_function` demonstrates a convention where functions prefixed with an underscore (`_`) are considered internal to the module and not part of the public API.

### Step 3: Use the Public Function

Now, let's create a script to import and use our public function. Create a file named `main.py` in the same directory:

```python
# main.py
import shapes

def run_example():
    """Demonstrates how to use the calculate_rectangle_area function."""
    print("--- Using calculate_rectangle_area ---")

    # Valid usage
    length = 5
    width = 10
    area = shapes.calculate_rectangle_area(length, width)
    print(f"The area of a rectangle with length {length} and width {width} is: {area}")

    # Another valid usage
    length = 7.5
    width = 2.0
    area = shapes.calculate_rectangle_area(length, width)
    print(f"The area of a rectangle with length {length} and width {width} is: {area}")

    # Invalid usage (demonstrates error handling)
    print("\n--- Demonstrating error handling ---")
    try:
        shapes.calculate_rectangle_area(-1, 5)
    except ValueError as e:
        print(f"Caught an expected error: {e}")

    # Attempting to use a "private" function (discouraged)
    print("\n--- Attempting to use a 'private' function (discouraged) ---")
    result = shapes._private_helper_function(10)
    print(f"Result from _private_helper_function: {result}")

if __name__ == "__main__":
    run_example()
```

### Step 4: Run the Script

Execute the `main.py` script from your terminal:

```bash
python main.py
```

## Validation

After running the `main.py` script, verify the output and explore the function's documentation.

### Check Console Output

Your console output should look similar to this:

```
--- Using calculate_rectangle_area ---
The area of a rectangle with length 5 and width 10 is: 50.0
The area of a rectangle with length 7.5 and width 2.0 is: 15.0

--- Demonstrating error handling ---
Caught an expected error: Length and width must be non-negative values.

--- Attempting to use a 'private' function (discouraged) ---
Result from _private_helper_function: 20.0
```

This confirms that:
1.  The `calculate_rectangle_area` function correctly computes the area for valid inputs.
2.  The `ValueError` is raised and caught as expected for invalid inputs.
3.  The "private" function can technically be called, but its usage is discouraged.

### Inspecting Documentation

Python's built-in `help()` function is invaluable for inspecting the documentation of modules, classes, and functions.

Open a Python interactive shell in the same directory:

```bash
python
```

Now, import your `shapes` module and use `help()`:

```python
>>> import shapes
>>> help(shapes.calculate_rectangle_area)
```

You should see the beautifully formatted docstring displayed, making it easy to understand the function's purpose, parameters, return value, and examples:

```
Help on function calculate_rectangle_area in module shapes:

calculate_rectangle_area(length: float, width: float) -> float
    Calculate the area of a rectangle.

    This function takes the length and width of a rectangle
    and returns its area.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The calculated area of the rectangle.

    Raises:
        ValueError: If length or width is negative.

    Examples:
        >>> calculate_rectangle_area(5, 10)
        50.0
        >>> calculate_rectangle_area(7.5, 2.0)
        15.0
```

This live documentation is a direct benefit of writing clear docstrings and is one of the most powerful tools for developers using your public functions.

## Tearing Down

To clean up the resources created during this tutorial, simply remove the `public_functions_tutorial` directory:

```bash
cd ..
rm -rf public_functions_tutorial
```

## Conclusion

Developing and documenting public functions effectively is a cornerstone of writing high-quality, maintainable, and reusable code. By following the practices outlined in this tutorial, you can ensure your Python modules and libraries are a pleasure for others to use.

Key takeaways:

*   **Descriptive Naming**: Give your functions clear, unambiguous names that convey their purpose.
*   **Comprehensive Docstrings**: Every public function *must* have a docstring that explains its purpose, parameters, return values, and any exceptions it might raise. Use a consistent style (e.g., Google, reStructuredText, NumPy).
*   **Type Hints**: Use type hints to improve readability, enable static analysis, and clearly define the expected types of arguments and return values.
*   **Error Handling**: Implement robust error handling to guide users when they provide invalid input.
*   **Public vs. Private**: Distinguish between public API functions and internal helper functions (often by convention using a leading underscore `_`).

By adhering to these principles, you contribute to a more collaborative and efficient development ecosystem.
```