import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from abc import ABCMeta, abstractmethod


class ChartMaker(object):
    def __init__(self, chart):
        self.chart_type = chart

    def draw(self, all_num):
        self.chart_type.draw(all_num)


class AbstractChartMaker(metaclass=ABCMeta):
    @abstractmethod
    def draw(self, all_num):
        pass


class BarChartMaker(AbstractChartMaker):
    def draw(self, all_num):
        name_list = ["Class", "Attribute", "Method"]
        numbers = all_num
        size = range(len(numbers))
        plt.bar(size, numbers, tick_label=name_list)
        plt.ylabel("Number")
        plt.xlabel("Elements of UML")
        plt.title("The total counts for three elements of the UML")
        plt.show()


class PieChartMaker(AbstractChartMaker):
    def draw(self, all_num):
        plt.figure(figsize=(5, 5))
        labels = ["Total number of ClassNum", "Total number of AttributeNum",
                  "Total number of MethodNum"]
        values = all_num
        explode = [0, 0.05, 0]
        plt.pie(values, labels=labels, autopct="%.1f%%", explode=explode)
        plt.title("Number of Classes, Attributes and Methods\n")
        plt.legend(labels, loc=3)
        plt.show()


class LineGraphMaker(AbstractChartMaker):
    def draw(self, all_num):
        fig, ax = plt.subplots()
        label = "Classes, Attributes and Methods"
        for axis in [ax.xaxis, ax.yaxis]:
            axis.set_major_locator(ticker.MaxNLocator(integer=True))
        plt.title(label)
        plt.xlabel(label)
        plt.ylabel("Number of " + label)
        plt.plot([1, 2, 3], all_num)
        plt.show()
