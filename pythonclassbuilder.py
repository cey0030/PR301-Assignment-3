from validator import Validator
from abc import ABCMeta, abstractmethod
from fileProcessor import FileProcessor


class AbstractBuilder(metaclass=ABCMeta):
    def __init__(self):
        self.result = ""

    def get_result(self):
        return self.result

    @abstractmethod
    def add_class_name(self):
        pass

    @abstractmethod
    def add_attributes(self):
        pass

    @abstractmethod
    def add_methods(self):
        pass

    @abstractmethod
    def add_relationships(self):
        pass


class PythonClassBuilder(AbstractBuilder):
    def __init__(self):
        self.fileProcessor = FileProcessor()
        self.class_name_list = self.fileProcessor.class_name_list

    def check_methods(self, listitem):
        if Validator.validate_method_name(listitem):
            self.result += '\n'
            self.result += 'def ' + listitem + '(self):\n     # Todo: inco' \
                                          'mplete\n        pass\n'
        else:
            self.result += "# method name is invalid\n"

    def add_methods(self, class_item):
        for listItem in self.fileProcessor.get_methods(class_item):
            self.check_methods(listItem)

    def add_relationships(self, class_item):
        for list_item in self.fileProcessor.get_relationship(
                self.fileProcessor.get_class_name(class_item)):
            self.result += list_item

    def add_attributes(self, class_item):
        for listItem in self.fileProcessor.get_attributes(class_item):
            self.check_attributes(listItem)
        if len(self.fileProcessor.get_attributes(class_item)) == 0:
            self.result += "        pass\n"

    def check_attributes(self, listitem):
        try:
            if Validator.validate_attribute_name(listitem):
                self.result += '        self.' + \
                          listitem + ' = ' + listitem + '\n'
            else:
                raise NameError('Invalid name: ' + listitem)
        except NameError as e:
            print(e)


    def add_class_name(self, class_item):
        self.class_name_list.append(self.fileProcessor.get_class_name(class_item))
        self.result = "class " + \
            self.fileProcessor.get_class_name(class_item) + ":\n    def __init__(self"
        for listItem in self.fileProcessor.get_attributes(class_item):
            self.result += ', ' + listItem
        self.result += '):\n'
        self.check_class_names(class_item)

    def check_class_names(self, class_item):
        if not Validator.validate_class_name(self.fileProcessor.get_class_name(class_item)):
            print("Invalid class name: " + self.get_class_name(class_item))


pythonClassBuilder = PythonClassBuilder()
pythonClassBuilder.add_class_name(['class Animal {\n',
                                       '    name : String\n',
                                       '    number : Integer\n',
                                       '    __str__()\n',
                                       '}\n'])
pythonClassBuilder.add_attributes(['class Animal {\n',
                                       '    name : String\n',
                                       '    number : Integer\n',
                                       '    __str__()\n',
                                       '}\n'])
pythonClassBuilder.add_methods(['class Animal {\n',
                                       '    name : String\n',
                                       '    number : Integer\n',
                                       '    __str__()\n',
                                       '}\n'])
pythonClassBuilder.add_relationships(['class Animal {\n',
                                       '    name : String\n',
                                       '    number : Integer\n',
                                       '    __str__()\n',
                                       '}\n'])
print(pythonClassBuilder.get_result())
