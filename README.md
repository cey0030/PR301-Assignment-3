# PR301-Assignment 3 Documentation

## Design Patterns

### Name: Builder

Location: PR301-Assignment-2-Version-1-fileHandler.py-PrintClass-between Line 0 and 107

Reasons this design pattern is suitable to be applied: 

1. PrintClass is doing more than one task. It is, building the individual components of the "result" on line 21, combining them into "result" in the output_class method, and then repeatedly calling the output_class method in the output_classes method to write them to files. Due to the Single Responsibility Principle of SOLID, therefore, this class should be modified such that the building of the individual components of "result" take place in a separate class from PrintClass, which should both be in a separate from the class which calls output_classes and writes the output to files. This is exactly what the builder design pattern does.

 2. The builder design pattern enforces the single responsibility principle by ensuring that the building of individual components of a product is handled by one class (the builder, which in my case would contain the methods required to build all the components of the "result" string, i.e. add_methods, add_attributes, add_relationships, add_class_names, etc); the steps needed to build it together is handled by another class (the director, which would contain a method to call add_class_names, add_attributes, add_relationships, etc in the correct order); and the code which calls the director (in this case, output_classes since that is identified as the client code) to execute the steps in which the builder builds the product is separate from the builder and director classes. In this way each class does only one task, thus satisfying the single responsibility principle from SOLID. Hence, the builder pattern is suitable to apply to the code specified. 

3. Applying the builder design pattern helps the code to become more extendable. Since, in the builder design pattern, there is an abstract class which defines all builder classes, and one of them will be used to create the Python code string which is the product in this case; this abstract class allows for more builder classes to be created, for example if JavaScript code was to be created as the final product instead of Python code, then another builder which would create JavaScript components would be made. The director remains independent of the way by which the builder builds the components since it only tells the builder the order in which to build the product, therefore, the program is now easily extendable and programmers may now add whatever extra builder classes they require, without having to worry about having to change director or the calls in the client code every single time. All they need to do is create a new builder to handle the new functionality required, and the rest is taken care of by the structure of the builder design pattern. Thus, applying the builder design pattern to this code allows it to be extended easily since all of the implementation to build specific outputs is contained within the builder class, which is one of the reasons why it is a suitable design pattern to apply to the code. Furthermore, applying the builder design pattern and thus making the code more extendable helps the code conform better to the Open-closed principle from SOLID, which states that software entities should be open for extension. 

4. Applying the builder design pattern to PrintClass makes it more flexible. If, for example, there was a builder class which built Python code as the final product string, and another builder class which built JavaScript code as the final product string, the client can then call either, thus giving more flexibility to the client, since they can call whichever one they require. In the original code, it is very rigid and inflexible since the client can only create a Python code string, so if they wanted to create a JavaScript code string or one of any other language, they couldn't, and this is inflexible. Therefore, applying the builder design pattern to PrintClass is suitable as it allows the code to be more flexible. 

### Decorator

Location: PR301-Assignment-2-Version-1-chart_maker.py-ChartMaker-between Line 0 and 39

Reasons this design pattern is suitable to be applied: 

1. 
