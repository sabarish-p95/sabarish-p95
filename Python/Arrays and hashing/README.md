# Arrays and Hashing

This folder collects solutions to array and hash map problems.

## 2sum.py
Implements the classic Two Sum problem. Iterates through `nums` and for each index `i` looks for `target - nums[i]` in the remaining slice `nums[i+1:]`. Returns the pair of indices when found or an empty list if no pair exists.

## TopkfrequentElement.py
Counts occurrences of each number with `collections.Counter` and returns the `k` most common elements via the `most_common` method.

## arrays_duplicate_easy.py
Detects duplicates by building a dictionary of counts. If any value appears more than once, the function returns `True`; otherwise it returns `False`.

## group_anagram_medium.py
Groups words that are anagrams. It uses a `defaultdict(list)` where the key is the sorted letters of each word, appending words with the same sorted form and finally returning all groups.

## valid_anagram.py
Determines whether two strings are anagrams by comparing their sorted character lists. If the lengths differ or the sorted lists are not equal, the result is `False`.
