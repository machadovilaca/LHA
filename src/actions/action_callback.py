from typing import List, Dict


class ActionCallback:
	params: Dict[str,str]
	arguments: List[str]

	def __init__(self, params: Dict[str,str], arguments: List[str]):
		_ = params.pop('arguments', None)
		self.params = params
		self.arguments = arguments
