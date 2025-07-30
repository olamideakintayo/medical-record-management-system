class StringUtils:
    @staticmethod
    def equals_ignore_case(str1: str, str2: str) -> bool:
        if str1 is None or str2 is None:
            return False
        return str1.lower() == str2.lower()
