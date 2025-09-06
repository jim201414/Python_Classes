class SmartObjects():
    def __init__(self, name, properties, objects):
        self.name = name
        self.properties = properties
        self.objects = objects

    objects = []

    # Add a new object with name and properties
    def defineObject(self, obj_name, obj_properties):
        obj_name = obj_name
        if obj_name == "":
            obj_name = "Unanamed"
        obj_properties = obj_properties
        if obj_properties == "":
            obj_properties = "<empty>"
        object = {"name": obj_name, "properties": obj_properties}
        self.objects.append(object)
        print(f"Added object: {object}")


    # List all objects
    def listObjects(self):
        if not self.objects:
            print("No objects to display.")
        else:
            for idx, obj in enumerate(self.objects, start=1):
                print(f"{idx}. Name: {obj['name']}, Properties: {obj['properties']}")