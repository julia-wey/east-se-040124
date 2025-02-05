#!/usr/bin/env python3
import ipdb; 

"""
Pet
    - name
    - age
    - breed
"""
#✅ 1. Create a Pet class
class Pet:
    def __init__(self, name="Pet", age=0, breed="Unknown"):
        self.name = name
        self.age = age
        self.breed = breed
    
    def hello(self):
        print('Hello')

    def speak(self):
        if self.breed =='dog':
            print('Bark')
        elif self.breed == 'cat':
            print('Meow')
        else:
            print('...silence')


    #✅ 2. Instantiate a few pet instances in ipdb
    #✅ 2a. Compare the two pet instances to demonstrate they are not the same object
    def __repr__(self):
        return f'<Pet name={self.name}>'
    #✅ 3. Demonstrate __init__
apollo = Pet(name="Apollo", age=2, breed= 'dog')
daisy = Pet(name="Daisy", breed='cat')

    #✅ 3a. Add parameters for attributes
    #✅ 3b. use dot notation to access their attributes
    #✅ 3c. update attributes with new values

    #✅ 4. Demonstrate INSTANCE methods
    #✅ 4a. Create a hello method that will print "Hello!"
    #✅ 4b. Create a print_pet_details function that will print the pet attributes
    #✅ 4c. Create a speak method that will print "Woof" for dogs and "Meow" for cats


#✅ 5. Set constraints for updating properties (attributes that are controlled by methods)
class Owner:
    def __init__(self, name='Unknown'):
        self.name = name 

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if type(new_name) == str:
            self._name = new_name
        else:
            raise TypeError("Name must be of type str.")

julia = Owner('Julia')



 #✅ 5a. Create Owner class
    #✅ 5b. Create get/set instance methods for name property
    #✅ 5c. Create constraint to make sure the name is of type string
    #✅ 5d. Compile get_name, set_name under the same property name (@ decorator is syntactic sugar)
    #✅ 5e. Add parameter to pass in name property value on instantiation
    #✅ 5f. Use the name property to set the name "private" attribute on instantiation

ipdb.set_trace()
