class Player:

	name = ""
	wallet = ""
	tokens = 0
	pchars = []

	def __init__(this, name, wallet,):
		this.name = name
		this.wallet = wallet
    

	@staticmethod
	def setTokens(this, tokens):
		this.tokens = tokens

	#@staticmethod
	#def getTokens(this)	
	