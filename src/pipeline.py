'''
Generic pipelion implementation in Python

@author Ryan Schostag
@version 1.0
'''
import logging
from types import FunctionType, MethodType
from typing import Any, Type, Self
from settings import pipeline as config


class ValidationError(TypeError):
    pass


class ExecutionError(Exception):
    pass


class Step:
    '''
    Model class for a Step in an instance of <class Pipeline>
    '''
    func:FunctionType|MethodType
    description:str = config.default_description

    def __init__(self, func:FunctionType|MethodType, description:str=description) -> None:
        '''
        Initializer for the Step model.

        self.func:          This must be a function that accepts a 
                            single argument.
        self.description:str   (optional)
        '''
        self.func = self.validate(func, (FunctionType, MethodType))
        self.description:str = description

    def validate(self, input_data:Any, expected_types:tuple[Type]|Type) -> Any:
        '''
        @input_data <any>
        @returns input <any>
        @raises ValidationError
        '''
        if not isinstance(input_data, expected_types):
            raise ValidationError(
                f'input_data: {input_data}\n'
                f'expected_types: {expected_types}\n'
                f'received_type: {type(input_data)}'
            )

        return input_data


class Pipeline:
    '''
    pipeline class
    '''
    def __init__(self):
        self.steps:list[FunctionType|MethodType] = []

    def add_step(self, step:Step) -> Self:
        '''
        Adds the function to self.steps
        '''
        if isinstance(step, Step):
            self.steps.append(step)
        else:
            raise ValidationError(
                 'failed to add step because it is not an '
                 'instance of <class Step> model\n'
                 f'Some documentation on the Step module:\n{Step.__doc__}\n'
            )

    def execute(self, input_data:Any) -> None:
        '''
        Executes each step in self.steps. Passes the responsibility
        of exceeption handling to the step function being called.

        It will try to send an INFO message to the logging module if 
        there is a <Step.description> that is not null.
        '''
        for step in self.steps:
            if step.description:
                logging.info(
                    'step_function: %s\n'
                    'description: %s',
                    step.func,
                    step.description
                )

            input_data = step.func(input_data)
        return input_data
