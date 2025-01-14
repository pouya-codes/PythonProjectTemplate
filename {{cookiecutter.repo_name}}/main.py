"""
This module contains examples of Python code.
"""

import {{cookiecutter.package_name}}


def main() -> None:
    """Main function."""
    vec1 = {{cookiecutter.package_name}}.Vector2D(-1, 1)
    vec2 = {{cookiecutter.package_name}}.Vector2D(2.5, -2.5)
    print(vec1 - vec2)


if __name__ == "__main__":
    main()
