import json

from sqlalchemy import Column, Integer, String, DateTime

from superagi.models.base_model import DBBaseModel


class WaitBlockStep(DBBaseModel):
    """
    Step for a wait block

    Attributes:
        id (int): The unique identifier of the wait block step.
        name (str): The name of the wait block step.
        description (str): The description of the wait block step.
        delay (int): The delay time in milliseconds.
        wait_begin_time (DateTime): The start time of the wait block.
    """

    __tablename__ = 'wait_block_steps'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    delay = Column(Integer)
    wait_begin_time = Column(DateTime)

    def __repr__(self):
        """
        Returns a string representation of the WaitBlockStep object.

        Returns:
            str: String representation of the WaitBlockStep.
        """

        return f"WaitBlockStep(id={self.id}, name='{self.name}', delay='{self.delay}', " \
               f"wait_begin_time='{self.wait_begin_time}'"

    def to_dict(self):
        """
        Converts the WaitBlockStep object to a dictionary.

        Returns:
            dict: Dictionary representation of the WaitBlockStep.
        """

        return {
            'id': self.id,
            'name': self.name,
            'delay': self.delay,
            'wait_begin_time': self.wait_begin_time
        }

    def to_json(self):
        """
        Converts the WaitBlockStep object to a JSON string.

        Returns:
            str: JSON string representation of the WaitBlockStep.
        """

        return json.dumps(self.to_dict())
