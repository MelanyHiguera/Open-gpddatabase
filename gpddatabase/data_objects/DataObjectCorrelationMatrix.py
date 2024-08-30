import math
import numpy as np

from gpddatabase.data_objects.markdown.MarkdownDataObjectCorrelationMatrix import MarkdownDataObjectCorrelationMatrix as MarkdownFunctionalities

from gpddatabase.exceptions.Exceptions import ExceptionNoField
from gpddatabase.exceptions.Exceptions import ExceptionWrongType
from gpddatabase.exceptions.Exceptions import ExceptionWrongLength
from gpddatabase.exceptions.Exceptions import ExceptionWrongLabel
from gpddatabase.exceptions.Exceptions import ExceptionWrongCorrelationMatrix

class DataObjectCorrelationMatrix(MarkdownFunctionalities):

	'''Class representing correlation matrix.'''

	def __init__(self, data):

		#get label
		self.label = data[0]

		if  self.label is None:
			raise ExceptionNoField('label')

		if not isinstance(self.label, str):
			raise ExceptionWrongType('label')

		if len(self.label) > 20:
			raise ExceptionWrongLength('label', 20)

		if not self.label.replace('_', '').isalnum():
			raise ExceptionWrongLabel(self.label)

		#get size
		matrix_size = math.sqrt(len(data[1:]))

		if not matrix_size.is_integer():
			raise ExceptionWrongCorrelationMatrix(self.label)

		matrix_size = int(matrix_size)

		#check elements
		for element in data[1:]:

			if (not isinstance(element, int)) and (not isinstance(element, float)):
				raise ExceptionWrongCorrelationMatrix(self.label)

			if (element < -1.) or (element > 1.):
				raise ExceptionWrongCorrelationMatrix(self.label)

		#create matrix
		self.correlation_matrix = np.matrix(np.array(data[1:]).reshape((matrix_size, matrix_size)))

		#check if symmetric
		if not np.allclose(self.correlation_matrix, self.correlation_matrix.T):
			raise ExceptionWrongCorrelationMatrix(self.label)

		#check if 1 on diagonal
		for element in np.nditer(self.correlation_matrix.diagonal()):
			if element != 1.:
				raise ExceptionWrongCorrelationMatrix(self.label)

	def get_label(self):

		'''Get label of this matrix.'''

		return self.label

	def get_correlation_matrix(self):

		'''Get correlation matrix.'''

		return self.correlation_matrix
