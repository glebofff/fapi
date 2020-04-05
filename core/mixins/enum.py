class ChoiceMixin:
    @classmethod
    def names(cls):
        return [enum.name for enum in cls]

    @classmethod
    def items(cls):
        return [(enum.value, enum.value) for enum in cls]

    @classmethod
    def choices(cls):
        return [(enum.name, enum.value) for enum in cls]

    @classmethod
    def values(cls, *enums):
        enums = enums or [e for e in cls]
        return [e.value for e in enums]
