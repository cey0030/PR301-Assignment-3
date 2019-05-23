# PR301-Assignment 3 Documentation

## Design Patterns

### Name: Builder

Location: PR301-Assignment-2-Version-1-fileHandler.py-PrintClass-between Line 0 and 107

Reasons: 

1. PrintClass is doing more than one task. It is, building the individual components of the "result" on line 21, combining them into "result" in the output_class method, and then repeatedly calling the output_class method in the output_classes method to write them to files. Due to the Single Responsibility Principle of SOLID, therefore, this class should be modified such that the building of the individual components of "result" take place in a separate class from PrintClass, which should both be in a separate from the class which calls output_classes and writes the output to files. This is exactly what the builder design pattern does.

The builder design pattern enforces the single responsibility principle by ensuring that the building of individual components of a product is handled by one class (the builder); the steps needed to build it together is handled by another class (the director); and the code which calls the director to execute the steps in which the builder builds the product is separate from the builder and director classes. In this way each class does only one task, thus satisfying the single responsibility principle from SOLID. Hence, the builder pattern is suitable to apply to the code specified. 

2. 
