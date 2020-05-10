import numpy as np

def evaluate(submission, correct):
    """Checks if two grids (submitted and correct) are the same.

    Args:
        submission (list, numpy array): The submitted grid. If it is 
            a list, it will be converted to a numpy array.
        correct (list, numpy): The ground truth grid. If it is a
            a list, it will be converted to a numpy array

    Returns:
        bool: True if the two grids are the same, False otherwise.
    """
    submission = np.array(submission)
    correct = np.array(correct)
    return np.array_equal(submission, correct)
