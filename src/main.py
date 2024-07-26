from pathlib import Path
from tutorial_in_official_docs import chapter_04_more_control_flow_tools
from tutorial_in_official_docs import chapter_05_data_structures
# from tutorial_in_official_docs import chapter_08_errors_and_exceptions
from tutorial_in_official_docs import chapter_09_classes
from standard_library import using_userDict
from lisa_test import roi
from lisa_test import cv2_merge
from lisa_test import cv2_multiply
from lisa_test import np_mask

def chapter04():
    chapter_04_more_control_flow_tools.else_with_loop()
    chapter_04_more_control_flow_tools.match_expression()
    chapter_04_more_control_flow_tools.test_concat()
    chapter_04_more_control_flow_tools.test_unpack()
    chapter_04_more_control_flow_tools.test_parrot()
    chapter_04_more_control_flow_tools.test_documentation_string()

def chapter05():
    chapter_05_data_structures.playing_with_list()
    chapter_05_data_structures.list_comprehensions()
    chapter_05_data_structures.nested_list_comprehensions()
    chapter_05_data_structures.playing_with_dictionary()

# def chapter08():
#     chapter_08_errors_and_exceptions.test_nested_exception_group()

def chapter09():
    chapter_09_classes.section_09_04_random_remarks()
    chapter_09_classes.section_09_08_iterators()
    chapter_09_classes.section_09_09_generators()
    chapter_09_classes.section_09_10_generator_expressions()

def with_userDict():
    using_userDict.test_box()

def lisa_test():
    # roi.run()
    # cv2_merge.run()
    # cv2_multiply.run()
    np_mask.run()

if __name__ == "__main__":
    import platform
    import sys
    print(f'now working on {platform.python_version()} ({sys.executable})')

    # chapter04()
    # chapter05()
    # chapter08()
    # chapter09()
    # with_userDict()
    lisa_test()
