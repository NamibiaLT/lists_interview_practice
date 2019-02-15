import unittest

'''
SIMPLE SOLUTION:
def merge_lists(my_list, alices_list):

    # Combine the sorted lists into one large sorted list
    combined_lists = my_list + alices_list

    # Note .sort() return none while sorted(list) keeps original
    # and returns new sorted list

    return sorted(combined_lists)
DRAWBACKS: this solution is faster until
n gets large. EX: n = 1,000,000.
'''

'''
DATA STRUCTURE SOLUTION
'''
def merge_lists(my_list, alices_list):

    # Combine the sorted lists into one large sorted list
    merged_list_size = len(my_list) + len(alices_list)
    merged_list = [None] * merged_list_size

    current_index_alices = 0
    current_index_mine = 0
    current_index_merged = 0

    while current_index_merged < merged_list_size:
        is_my_list_exhausted = current_index_mine >= len(my_list)
        is_alices_list_exhausted = current_index_alices >= len(alices_list)

        if (not is_my_list_exhausted and
                (is_alices_list_exhausted or my_list[current_index_mine] < alices_list[current_index_alices])):

            # Case: next comes from my list
            # My list must not be exhausted, and EITHER:
            # 1) Alice's list IS exhausted, or
            # 2) the current element in my list is less
            #    than the current element in Alice's list

            merged_list[current_index_merged] = my_list[current_index_mine]
            current_index_mine += 1

        else:
            # Case: next comes Alice's list
            merged_list[current_index_merged] = alices_list[current_index_alices]
            current_index_alices += 1

        current_index_merged += 1

    return merged_list

'''
O(n) time and O(n) additional space,

where n is the number of items in the merged list.
The added space comes from allocating the merged_list.
There's no way to do this " in place"
because neither of our input lists are
necessarily big enough to hold the merged list.

But if our inputs were linked lists,
we could avoid allocating a new structure and do the merge
by simply adjusting the next pointers in the list nodes!
'''

# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
