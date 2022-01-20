class contentEXT:
	"""
	contentEXT description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.playlistSwitchOP = op('switch')
		