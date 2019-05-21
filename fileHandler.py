from fileProcessor import FileProcessor
from FileInput import FileInput
from pythonclassbuilder import PythonClassBuilder
from director import Director


class PrintClass:
    def __init__(self):
        self.fileProcessor = FileProcessor()
        self.fileInput = FileInput(self.fileProcessor)
        self.class_list = self.fileInput.class_list
        self.class_name_list = self.fileProcessor.class_name_list

    def output_classes(self, file_dir):
        files = []
        for classItem in self.class_list:
            files.append(file_dir + self.get_class_name(classItem) + '.py')
        for classItem, file in zip(self.class_list, files):
            pythonClassBuilder = PythonClassBuilder()
            director = Director(pythonClassBuilder)
            director.build_class(classItem)
            result = pythonClassBuilder.get_result()
            with open(file, "w") as output:
                output.write(result)
        print("Files are created")

    def get_all_num(self):
        return self.fileProcessor.get_all_num()

    def class_handler(self, file_name):
        return self.fileInput.class_handler(file_name)

    def identify_r_type(self, a_relationship, name):
        return self.fileProcessor.identify_r_type(a_relationship, name)

    def get_class_name(self, class_array):
        return self.fileProcessor.get_class_name(class_array)

    def read_txt_file(self, file_name):
        return self.fileInput.read_txt_file(file_name)

    def get_attributes(self, class_array):
        return self.fileProcessor.get_attributes(class_array)

    def get_methods(self, class_array):
        return self.fileProcessor.get_methods(class_array)

    def get_relationship(self, class_array):
        return self.fileProcessor.get_relationship(class_array)
