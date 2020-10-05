import inspect
import os
import sys

# Add script directory to sys.path.
# This is complicated due to the fact that __file__ is not always defined.

def get_script_directory():
    """
    Get current script directory

    Returns:
        dir (path): Global path with current script directory

    """
    if hasattr(get_script_directory, "dir"):
        return get_script_directory.dir
    module_path = ""
    try:
        # The easy way. Just use __file__.
        # Unfortunately, __file__ is not available when cx_freeze is used or in IDLE.
        module_path = __file__
    except NameError:
        if len(sys.argv) > 0 and len(sys.argv[0]) > 0 and os.path.isabs(sys.argv[0]):
            module_path = sys.argv[0]
        else:
            module_path = os.path.abspath(inspect.getfile(get_script_directory))
            if not os.path.exists(module_path):
                # If cx_freeze is used the value of the module_path variable at this point is in the following format.
                # {PathToExeFile}\{NameOfPythonSourceFile}. This makes it necessary to strip off the file name to get the correct
                # path.
                module_path = os.path.dirname(module_path)
    get_script_directory.dir = os.path.dirname(module_path)
    return get_script_directory.dir


def add_dir_to_pythonpath():
    """
    Add current script directory to $pythonpath

    """
    sys.path.append(get_script_directory())
