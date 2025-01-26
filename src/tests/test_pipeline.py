'''
Automated tests for the pipeline.py module
'''
import pytest
from src import pipeline


sample_func_1 = lambda x: x + 1
sample_func_2 = lambda x: x ** 2
sample_func_3 = lambda x: x ** 3
sample_func_4 = lambda x: str(x) + str(x)
input_data_1 = 1
steps_1 = [sample_func_1]
steps_2 = [sample_func_1, sample_func_2]
steps_3 = [sample_func_1, sample_func_2, sample_func_3]
steps_4 = [sample_func_1, sample_func_4]
expected_output_1 = 2
expected_output_2 = 4
expected_output_3 = 64
expected_output_4 = '22'
@pytest.mark.parametrize('steps, input_data, expected_output', [
    (steps_1, input_data_1, expected_output_1),
    (steps_2, input_data_1, expected_output_2),
    (steps_3, input_data_1, expected_output_3),
    (steps_4, input_data_1, expected_output_4)
])
def test_execute(steps, input_data, expected_output):
    '''
    Ensures the pipeline works as expected
    '''
    instance = pipeline.Pipeline()
    for index, step_function in enumerate(steps):
        step = pipeline.Step(func=step_function, description=f'test#{index}')
        instance.add_step(step)
    output = instance.execute(input_data)
    assert output == expected_output
