def test_nested_exception_group():
    def f():
        raise ExceptionGroup(
            "group1",
            [
                OSError(1),
                SystemError(2),
                ExceptionGroup(
                    "group2",
                    [
                        RecursionError(4),
                        OSError(3),
                        ExceptionGroup(
                            "group3",
                            [
                                ValueError(5),
                            ]
                        )
                    ]
                )
            ]
        )

    try:
        f()
    except* OSError as e:
        print("There were OSErrors")
    except* SystemError as e:
        print("There were SystemErrors")
    except* ValueError as e:
        print("There were ValueError")
