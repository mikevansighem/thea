import random

def model_updater(things, target_value):

    current_on = sum([t.value for t in things]) / float(len(things))
    difference = target_on - current_on

    if difference > 0:

        number_to_change = int(difference * len(things))

        # Prevent nervous switching of a single light
        if number_to_change != 1:
            
            random.shuffle(things)
            to_change = [i for i in things if i.value is False][:number_to_change]

            for thing in to_change:
                thing.value = True

    elif difference < 0:

        number_to_change = int(difference * -1 * len(things))
        random.shuffle(things)
        to_change = [i for i in things if i.value is True][:number_to_change]

        for thing in to_change:
            thing.value = False


def shops(things_of_single_type, shops_open, **unused):

    model_updater(things=things_of_single_type, target_value=shops_open)

            
