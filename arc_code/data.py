import numpy as np
import glob
import json
import os

def get_data(data_dir, training_set = True, grouped_by_problem = False):
    '''
        Returns all the data as 4 lists. 
        If training_set is true, return data in 'training' directory.
            Else, return data in 'test' directory (so Y_train and Y_test will
            be empty)
        If grouped_by_problem is true, return data as a list of lists of 
                numpy array. The second list corresponds to the specific
                problem, hence each data entry is grouped by problem
            Else, return the data as a list of numpy arrays, where the data
                isn't grouped by problem.
    '''
    if training_set:
        folder = 'training'
    else:
        folder = 'test'
    files = glob.glob(os.path.join(data_dir,folder,"*.json"))
    all_data = {
        "train" : {"x":[],"y":[]},
        "test": {"x":[],"y":[]},
    }
    if training_set:
        phases_to_consider = ['train','test']
    else:
        # for test data set, ignore test inputs, since they don't have outputs
        phases_to_consider = ['train']
    for task_file in files:
        with open(task_file, 'r') as f:
            task = json.load(f)
            for phase in phases_to_consider:
                x_group, y_group = [], []
                for t in task[phase]:
                    x_group.append(np.array(t['input']))
                    y_group.append(np.array(t['output']))
                if grouped_by_problem:
                    all_data[phase]['x'].append(x_group)
                    all_data[phase]['y'].append(y_group)
                else:
                    all_data[phase]['x'].extend(x_group)
                    all_data[phase]['y'].extend(y_group)
    X_train, Y_train = all_data['train'].values()
    X_test, Y_test = all_data['test'].values()
    return X_train, Y_train, X_test, Y_test, files 

