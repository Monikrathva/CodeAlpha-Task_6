import logging

def secure_function():
    """This function does not have any security issues."""
    logging.info('This is a secure function.')

def used_function():
    """This function is used properly."""
    secure_function()

used_function()
