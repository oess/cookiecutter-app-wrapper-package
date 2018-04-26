from floe.api import WorkFloe
from cuberecord import (DataSetReaderCube,
                        DataSetWriterCube)
from {{cookiecutter.module_name}} import MyCube


# Declare and document floe
my_floe = WorkFloe('my_floe', title="My Floe")
my_floe.description = "Outputs the input records unchanged unless the parameter is set to false, in which case nothing " \
                   "is outputted"
my_floe.classification = [["Examples"]]
my_floe.tags = ["Examples", "I didn't edit the tags"]

# Declare Cubes
input_cube = DataSetReaderCube('input_cube')
switch_cube =MyCube('switch_cube')
output_cube = DataSetWriterCube('output_cube')

# Add cubes to floe
my_floe.add_cube(input_cube)
my_floe.add_cube(switch_cube)
my_floe.add_cube(output_cube)

# Promote parameters
input_cube.promote_parameter('data_in', promoted_name='in', title='Input data set of records')
switch_cube.promote_parameter('switch', promoted_name='switch', title="Switch controlling Output")
output_cube.promote_parameter('data_out', promoted_name='out', title='Output File of Molecules')

input_cube.success.connect(switch_cube.intake)
switch_cube.success.connect(output_cube.intake)

if __name__ == "__main__":
    my_floe.run()