class Director(object):
    def __init__(self, builder):
        self.__builder = builder

    def build_class(self, class_item):
        self.__builder.add_class_name(class_item)

        self.__builder.add_attributes(class_item)

        self.__builder.add_relationships(class_item)

        self.__builder.add_methods(class_item)
        return self.__builder.get_result()


