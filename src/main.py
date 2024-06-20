from tutorial_in_official_docs import chapter_04_more_control_flow_tools
from tutorial_in_official_docs import chapter_05_data_structures

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

if __name__ == "__main__":
    import platform
    print('now working on', platform.python_version())

    # chapter04()
    chapter05()
