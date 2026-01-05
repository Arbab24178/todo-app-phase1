"""
Main entry point for the Console Todo App.
"""
from .cli.cli_controller import CLIController


def main():
    """Main function to run the console todo application."""
    controller = CLIController()
    controller.run()


if __name__ == "__main__":
    main()