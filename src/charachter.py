class Charachter:

	name = "" #charachters name?  we would need to raid a random name generate but could be fun
	staminaMax = 0 # the total amount a charachter
	stamina = 0 #the current amount of stamina a charachter has
	droprate = 0 #multiplier for improved rcs collection
	price = 0.0
	bag = []
	#rarity = ["Common", ["Uncommon"], ["Rare"], ["Epic"] ]

	

	def __init__(this, name, stamina,droprate, price):
		this.name = name
		this.stamina = stamina
		this.droprate = droprate
		this.price = price
		this.staminaMax = this.stamina

	@staticmethod
	def setStamina(this, stamina):
		this.stamina = stamina

	#def checkStamina() - do this instead of long bits of code in the functions