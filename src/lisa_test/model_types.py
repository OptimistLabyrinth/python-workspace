from enum import Enum

class ProjectType(Enum):
    CLASSIFICATION = 1
    OBJECT_DETECTION = 2
    SEGMENTATION = 3
    ANOMALY_DETECTION = 4
    SNAP_ANOMALY_DETECTION = 5

    @classmethod
    def has_key(cls, key):
        return key in cls._member_names_

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


def test():
    params = {
        'type': 'CLASSIFICATION',
    }
    proj_type = ProjectType[params['type']]
    print('proj_type =', proj_type)

    params = {
        'type': 1,
    }
    proj_type = ProjectType(params['type'])
    print('proj_type =', proj_type)


test()


