class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')

test=Solution()

print(test.defangIPaddr("1.1.1.1"))
print(test.defangIPaddr("255.100.50.0"))
