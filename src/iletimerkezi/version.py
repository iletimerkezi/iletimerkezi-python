class VersionInfo:
    MAJOR = "1"
    MINOR = "0"
    PATCH = "0"

    @classmethod
    def string(cls) -> str:
        return f"iletimerkezi-python/v{cls.MAJOR}.{cls.MINOR}.{cls.PATCH}"