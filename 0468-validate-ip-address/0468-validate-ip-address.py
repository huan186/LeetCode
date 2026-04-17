class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        def is_valid_ipv4():
            parts = queryIP.split(".")
            if len(parts) != 4:
                return False
            def valid(p):
                if len(p) == 0 or len(p) > 3 or p[0] == '0' and len(p) > 1:
                    return False
                return all(c.isdigit() for c in p) and int(p) <= 255
            return all(valid(p) for p in parts)

        def is_valid_ipv6():
            parts = queryIP.split(":")
            if len(parts) != 8:
                return False
            def valid(p):
                if len(p) == 0 or len(p) > 4:
                    return False
                for c in p.lower():
                    if not c.isdigit() and ('a' > c or 'f' < c):
                        return False
                return True
            return all(valid(p) for p in parts)


        if "." in queryIP:
            return "IPv4" if is_valid_ipv4() else "Neither"

        return "IPv6" if is_valid_ipv6() else "Neither"