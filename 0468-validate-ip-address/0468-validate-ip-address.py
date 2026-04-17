class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        def is_valid_ipv4():
            parts = queryIP.split(".")
            return len(parts) == 4 and not any(not p.isdigit() or p[0] == '0' and len(p) > 1 or int(p) > 255 for p in parts)

        def is_valid_ipv6():
            parts = queryIP.split(":")
            hexdigits = '0123456789abcdefABCDEF'
            return len(parts) == 8 and not any(len(p) == 0 or len(p) > 4 or any(c not in hexdigits for c in p)for p in parts)

        if "." in queryIP:
            return "IPv4" if is_valid_ipv4() else "Neither"

        return "IPv6" if is_valid_ipv6() else "Neither"