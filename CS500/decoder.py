Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import ast

def summarize_functions(source_code):
    # Parse the source code into an AST
    tree = ast.parse(source_code)

...     # Initialize a list to hold function summaries
...     function_summaries = []
... 
...     # Walk through the AST to find function definitions
...     for node in ast.walk(tree):
...         if isinstance(node, ast.FunctionDef):
...             # Extract function name and docstring
...             func_name = node.name
...             docstring = ast.get_docstring(node)
... 
...             # Create a summary for the function
...             summary = f"Function: {func_name}\n"
...             if docstring:
...                 summary += f"Description: {docstring}\n"
...             else:
...                 summary += "Description: No docstring provided.\n"
... 
...             # Add the summary to the list
...             function_summaries.append(summary)
... 
...     # Join all summaries into a single string
...     return "\n".join(function_summaries)
... 
... # Example usage
... if __name__ == "__main__":
...     # Example source code
...     source_code = """
...     def greet(name):
...         \"\"\"This function greets the person passed in as a parameter.\"\"\"
...         print(f"Hello, {name}!")
... 
...     def add(a, b):
...         return a + b
...     """
... 
...     # Get the summary of functions
...     summary = summarize_functions(source_code)
... 
...     # Print the summary
