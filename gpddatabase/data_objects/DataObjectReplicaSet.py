from gpddatabase.data_objects.markdown.MarkdownDataObjectReplicaSet import MarkdownDataObjectReplicaSet as MarkdownFunctionalities

from gpddatabase.exceptions.Exceptions import ExceptionNoField
from gpddatabase.exceptions.Exceptions import ExceptionWrongType

class DataObjectReplicaSet(MarkdownFunctionalities):

	'''Class representing replica set.'''

	def __init__(self, data):

		#values
		self.values = []

		if not data:
			raise ExceptionNoField('replica')

		for value in data:

			if (not isinstance(value, int)) and (not isinstance(value, float)):
				raise ExceptionWrongType('replica')

			self.values.append(value)

	def get_values(self):

		'''Get replica values.'''

		return self.values
