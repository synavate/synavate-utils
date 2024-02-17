''' A set of custom exceptions which are extensible'''

class CustomError(Exception):
    """Base class for custom errors."""
    pass

class OpenAIAPIError(CustomError):
    """Exception raised for errors returned by the OpenAI API."""

    def __init__(self, message, code=None):
        self.message = message
        self.code = code

        super().__init__(f"OpenAI API Error: {message}")

# Common OpenAI errors

class AuthenticationError(OpenAIAPIError):
    """Exception raised when authentication with OpenAI API fails."""
    pass

class AuthorizationError(OpenAIAPIError):
    """Exception raised when authorization with OpenAI API fails."""
    pass

class RateLimitError(OpenAIAPIError):
    """Exception raised when rate limit for OpenAI API is exceeded."""
    pass

class ServerError(OpenAIAPIError):
    """Exception raised when server error occurs with OpenAI API."""
    pass

class TimeoutError(OpenAIAPIError):
    """Exception raised when request to OpenAI API times out."""
    pass

class OpenAIError(Exception):
    """Base class for OpenAI related errors."""
    pass

class OpenAIAPIError(OpenAIError):
    """Exception raised for errors returned by the OpenAI API."""

    def __init__(self, message, code=None):
        self.message = message
        self.code = code

        super().__init__(f"OpenAI API Error: {message}")

class HTTPError(Exception):
    """Base class for HTTP related errors."""
    pass

class ServiceAPIError(HTTPError):
    """Exception raised for errors related to service APIs."""

    def __init__(self, service_name, status_code, message):
        self.service_name = service_name
        self.status_code = status_code
        self.message = message

        super().__init__(f"{service_name} API Error [{status_code}]: {message}")

class LibraryError(Exception):
    """Exception raised for errors related to library failures."""

    def __init__(self, library_name, message):
        self.library_name = library_name
        self.message = message

        super().__init__(f"{library_name} Error: {message}")