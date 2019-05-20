from fileHandler import PrintClass
from chart_maker import ChartMaker


class Controller:
    file = PrintClass()
    chart = ChartMaker()

    @staticmethod
    def load_file(infile):
        r"""
        >>> Controller.load_file("test_read_file.csv")
        Incorrect file type, please see help load
        >>> Controller.load_file("test.docx")
        The PlantUML file is loaded
        [['class ToyBox {\n', '}\n'], ['class Toy {\n', '}\n']]
        >>> Controller.load_file("test.txt")
        The PlantUML file is loaded
        [['class ToyBox {\n', '}\n'], ['class Toy {\n', '}\n']]
        >>> Controller.load_file("C:\\Users\Luna\ICT\\test2.docx")
        File is not found
        """
        try:
            if ".txt" in infile[-4:] or ".docx" in infile[-5:]:
                Controller.file.class_handler(infile)
                content = Controller.file.class_list
                print("The PlantUML file is loaded")
                return content

            else:
                message = "Incorrect file type, please see help load"
                raise NameError(message)

        except NameError as e:
            print(e)
        except FileNotFoundError:
            print("File is not found")
        except Exception as e:
            print(e)

    def save_file(self, file_location):
        self.file.output_classes(file_location)

    def create_bar_chart(self):
        all_num = self.file.get_all_num()
        self.chart.create_bar_chart(all_num)

    def create_pie_chart(self):
        all_num = self.file.get_all_num()
        self.chart.create_pie_chart(all_num)

    def create_line_chart(self):
        all_num = self.file.get_all_num()
        self.chart.create_line_graph(all_num)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
