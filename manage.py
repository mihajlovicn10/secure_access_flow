#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path


def main():
    """Run administrative tasks."""
    # Get the project root directory
    BASE_DIR = Path(__file__).resolve().parent

    # Add the project root directory to the Python path
    sys.path.insert(0, str(BASE_DIR))

    # Set the Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'secure_access_flow.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
