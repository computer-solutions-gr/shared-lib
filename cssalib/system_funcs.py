from socket import gethostname


def host_name():
    """Return the hostname of the current machine."""
    return gethostname()
