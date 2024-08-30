from gpddatabase.data_objects.markdown.MarkdownDataObjectUncertainty import MarkdownDataObjectUncertainty as MarkdownFunctionalities

from gpddatabase.exceptions.Exceptions import ExceptionValuesLEQ
from gpddatabase.exceptions.Exceptions import ExceptionWrongLength
from gpddatabase.exceptions.Exceptions import ExceptionWrongType
from gpddatabase.exceptions.Exceptions import ExceptionNoField
from gpddatabase.exceptions.Exceptions import ExceptionAsymmetricUnc

class DataObjectUncertainty(MarkdownFunctionalities):

	'''Class representing a single uncertainty.'''

	def __init__(self, data):

		#get
		if not data:
			raise ExceptionNoField('unc')

		if isinstance(data, (int, float)):

			if data <= 0.:
				raise ExceptionValuesLEQ(data, 0)

			self.unc_lower = data
			self.unc_upper = data

		elif isinstance(data, list):

			if len(data) != 2:
				raise ExceptionWrongLength('unc', 2)

			for value in data:

				if (not isinstance(value, int)) and (not isinstance(value, float)):
					raise ExceptionWrongType('unc')

				if value <= 0.:
					raise ExceptionValuesLEQ(value, 0)

			if len(data) == 2:
				self.unc_lower = data[0]
				self.unc_upper = data[1]

		else:

			raise ExceptionWrongType('unc')

	def get_unc_lower(self):

		'''Get lower value of uncertainty.'''

		return self.unc_lower

	def get_unc_upper(self):

		'''Get upper value of uncertainty.'''

		return self.unc_upper

	def is_asymmetric(self):

		'''Returns true is uncertainty asymmetric.'''

		return self.unc_lower != self.unc_upper

	def get_unc(self):

		'''Get value of uncertainty. If asymmetric exception will be raised.'''

		if self.is_asymmetric():
			raise ExceptionAsymmetricUnc()

		return self.unc_upper