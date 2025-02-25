from typing import Optional
#from pymmcore_plus.mda import MDAEngine

# This module comntains the differents signal's events  captured by the microsoft

# spatial light modulator of the device changes
def slme_exposure_changed(name: str, newExpoxure: float):
    print(f'The SLM of {name} microscope has a new value of {newExpoxure}')



# coordinates (x,y) of the stages have changed
def xy_stagePosition_changed(name: str, xpos: float, ypos: float):
    print(f'The new coordinate (x,y) of the stage of {name} are ({xpos},{ypos})')

#print(f'The auto shutter of the microscope has been set on {set_auto}') # to modifiy later specifying what does means True and False in the settings
# set the auto shutter of a microscope
def set_auto_shutter(set_auto: bool):
    return f'{set_auto}'


# new channel group name (ex. DAPI, FITC, TRITC)
def channelGroup_changed(newChannelGroupName: str):
    print(f'The new channel group name is {newChannelGroupName}')


# define the a new configuration
def define_config(var_1: str, var_2: str, var_3: str, var_4: str, var_5: str):
    print(f'A new configuration has been added with the following values ({var_1},{var_2},{var_3},{var_4},{var_5})')

# delete a configuration
def delete_config(var_1: str, var_2: str):
    print(f'The configuration ({var_1}, {var_2}) was deleted.')

# change the configuration of a channel group
#def config_group_changed(groupName: str, newConfigGroup: str):
#    print(f'The channel {groupName} has chaned the configuration with the following value {newConfigGroup}')

# delete a configuration group
def config_group_deleted(var: str):
    print(f'The config group {var} was deleted')


# set a new configuration
def set_config(var_1: str, var_2: str):
    print(f'The configuration ({var_1},{var_2}) was set.')


# Start of a continuos sequence acquisition (after)
def continuos_sequence_acquisistion_started():
    print('A continuos sequence acquisition has started.')

# Before the start of a sequence acquisition
def continuos_sequence_acquisition_starting():
    print('A sequence acquisition is starting.')

#  A new exposure is set
def exposure_changed(name: str, newExposure: float):
    print(f'The exposure {name} has a new value of {newExposure}')

# A new image has been snap
def image_snapped():
    print('A new image was snapped.')

# Multi dimensional acquisation engine registered
#def mda_engine_registered(var_1: MDAengine, var_2: MDAEngine):
#    print(f'The MDA engine {var_1} has been shut off. The MDA engine {var_2} has been registered.')

# pixel size affine (see affine transformation was changed)
def pixel_size_affine_changed(var_1: float, var_2: float, var_3: float, var_4: float, var_5: float, var_6: float):
    print(f'The affine pixel size was changed in ({var_1},{var_2},{var_3},{var_4},{var_5},{var_6})')

# new pixel size in micro-meter
def new_pixel_size(newPixelSizeUm: float):
    print(f'The new pixel size is {newPixelSizeUm} um.')

# properties of the microscope were changed
def properties_changed():
    print('The properties were changed.')

# A specific property was changed
def property_changed(name: str, propName: str, propValue: str):
    print(f'The device {name} has changed the property {propName} in {propValue}')

# A new Region of interest (ROI) was set
def set_ROI(var_1: str, var_2: int, var_3: int, var_4: int, var_5: int):
    print(f'The ROI {var_1} was set with the values ({var_2}, {var_3}, {var_4}, {var_5})')

# A sequence acquisition has started (after)
def sequence_acquisition_started(cameraLabel: str, numImages: int, intervalMs: float, stopOnOverflow: bool):
    print(f'The {cameraLabel} has started a sequence acquisition of {numImages} images in a time inteval of {intervalMs} Ms with a overflow parameter of value {stopOnOverflow}.')

# A sequence acquisition is starting
def sequence_acquisition_starting(cameraLabel: str, numImages: int, intervalMs: float, stopOnOverflow: bool):
    print(f'The {cameraLabel} is starting a sequence acquisition of {numImages} images in a time inteval of {intervalMs} Ms with a overflow parameter of value {stopOnOverflow}.')


# A sequence acquisitition was stopped
def sequence_acquisition_stopped(cameraLabel: str):
    print(f'The {cameraLabel} has stopped the sequence acquisition.')

# The position of the stage has changed
def stage_position_changed(name: str, pos: float):
    print(f'The stage position {name} was changed in {pos}.')


# The system configuration was loaded
def system_config_load():
    print('The microscope configuration was loaded.')

# The property of the microscope were changed
#def property_device_changed(device: str, property: Optional[str]):
#    print(f'')


# See once this events works if the other functions are needed.
