"""
WayScript Errors
"""


class MissingCredentialsError(Exception):
    """Error thrown when a workspace integration does not have requisite credentials"""
    pass


class UnauthorizedUserError(Exception):
    """Error thrown when a user does not have the necessary authorization for the operation"""
    pass
