from floe.api import BooleanParameter
from cuberecord import OERecordCube


class MyCube(OERecordCube):
    # Cube documentation.  This documentation for this cube, and all other cubes in this repository, can be converted
    # to html by calling 'invoke docs' from the root directory of this repository.  This documentation will also
    # appear in the Orion Floe editor.
    title = "My Fancy Cube"
    classification = [["Examples"]]
    tags = ["Example", "I didn't edit the tags"]
    description = "A cube that passes records to the success or failure port depending on the switch parameter"

    # The first variable passed to a parameter must always be the variable the parameter is assigned to as a string.
    switch = BooleanParameter("switch",
                              required=True,
                              title="Switch",
                              description="If true records are sent to the success, otherwise they are send to "
                                          "the failure port.")

    # Uncomment this and implement if you need to initialize the cube
    # def begin(self):
    #     pass

    # Records are passed to this function for processing.
    def process(self, record, port):
        if self.args.switch:
            self.success.emit(record)
        else:
            self.failure.emit(record)

    # Uncomment this and implement to cleanup the cube at the end of the run
    # def end(self):
    #     pass
