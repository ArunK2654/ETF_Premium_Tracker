class AppException(Exception):
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(message)

class MarketDataError(AppException):
    def __init__(self, message="Market data unavailable"):
        super().__init__(message, 502)


class NavDataError(AppException):
    def __init__(self, message="INav data unavailable"):
        super().__init__(message, 502)


class DatabaseError(AppException):
    def __init__(self, message="Database error"):
        super().__init__(message, 500)