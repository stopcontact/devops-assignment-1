# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class GradeRecords(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, subject_name: str=None, grade: float=None):  # noqa: E501
        """GradeRecords - a model defined in Swagger

        :param subject_name: The subject_name of this GradeRecords.  # noqa: E501
        :type subject_name: str
        :param grade: The grade of this GradeRecords.  # noqa: E501
        :type grade: float
        """
        self.swagger_types = {
            'subject_name': str,
            'grade': float
        }

        self.attribute_map = {
            'subject_name': 'subject_name',
            'grade': 'grade'
        }
        self._subject_name = subject_name
        self._grade = grade

    @classmethod
    def from_dict(cls, dikt) -> 'GradeRecords':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GradeRecords of this GradeRecords.  # noqa: E501
        :rtype: GradeRecords
        """
        return util.deserialize_model(dikt, cls)

    @property
    def subject_name(self) -> str:
        """Gets the subject_name of this GradeRecords.


        :return: The subject_name of this GradeRecords.
        :rtype: str
        """
        return self._subject_name

    @subject_name.setter
    def subject_name(self, subject_name: str):
        """Sets the subject_name of this GradeRecords.


        :param subject_name: The subject_name of this GradeRecords.
        :type subject_name: str
        """
        if subject_name is None:
            raise ValueError("Invalid value for `subject_name`, must not be `None`")  # noqa: E501

        self._subject_name = subject_name

    @property
    def grade(self) -> float:
        """Gets the grade of this GradeRecords.


        :return: The grade of this GradeRecords.
        :rtype: float
        """
        return self._grade

    @grade.setter
    def grade(self, grade: float):
        """Sets the grade of this GradeRecords.


        :param grade: The grade of this GradeRecords.
        :type grade: float
        """
        if grade is None:
            raise ValueError("Invalid value for `grade`, must not be `None`")  # noqa: E501

        self._grade = grade
