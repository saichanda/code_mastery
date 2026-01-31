# date:31 Jan
import pytest

from collections import defaultdict

class AnagramGrouper:
    def group(self, words):
        groups = defaultdict(list)
        for word in words:
            key = ''.join(sorted(word))
            groups[key].append(word)
        return list(groups.values())
    
    def normalize(result):
        return sorted([sorted(group) for group in result])

    @pytest.mark.parametrize(
        "words, expected",
        [
            (
                ["eat", "tea", "tan", "ate", "nat", "bat"],
                [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
            ),
            (
                [],
                [],
            ),
            (
                ["abc"],
                [["abc"]],
            ),
        ]
    )

    def test_group_anagrams(words, expected):
        grouper = AnagramGrouper()
        assert normalize(grouper.group(words)) == normalize(expected)

# if __name__ == '__main__':
#     anagram_grouper = AnagramGrouper()
#     words = ["eat", "tea", "tan", "ate", "nat", "bat"]
#     print("Grouped anagrams:")
#     print(anagram_grouper.group(words))
#     print()