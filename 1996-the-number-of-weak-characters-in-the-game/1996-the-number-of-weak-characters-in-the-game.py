class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))

        max_defense = count = 0

        for _, defense in reversed(properties):
            if defense < max_defense:
                count += 1
            max_defense = max(max_defense, defense)

        return count