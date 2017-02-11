

class Assembler:
	def __init__(self, finame):
		fi = open(finame, 'r')
		self.lines = fi.readlines()
		fi.close()
		self.programCounter = 0
		self.memory = []
		self.memoryAmount = 50
		self.stackMemCount = self.memoryAmount - 1
		self.ra = 0
		self.rb = 0
		self.rc = 0
		self.end = False
		for i in range(self.memoryAmount):
			self.memory.append(0)
		self.setupStackMemory()
		#self.printInfo()
		
				
	def printInfo(self):
		print self.lines
		print 'Program Counter: ', self.programCounter
		print 'memory:'
		for i in range(self.memoryAmount):
			print '\t', i, '\t', self.memory[i]
	def setMem(self, addr, val):
		self.memory[addr] = int(val)
	def getMemory(self, addr):
		return int(self.memory[addr])
	def addStackMem(self, val):
		self.memory[self.stackMemCount] = val
		r = self.stackMemCount
		self.stackMemCount -= 1
		return r
	def chomp(self, strin):
		return strin.rstrip()
			
	def setupStackMemory(self):
		for i in range(len(self.lines)):
			st = self.chomp(self.lines[i])
			self.lines[i] = st
			codes = st.split(' ')
			if(codes[0] == 'lda' or codes[0] == 'ldb'):
				if(codes[1][0] == 'v'):
					lnch = codes[1]
					lnch = lnch[1:]
					val = int(lnch)
					naddr = self.addStackMem(val)
					self.lines[i] = str(codes[0]) + ' ' + str(naddr)
	def run(self):
		while(1):
			self.iterateProgram()
			if(self.end == True):
				return
		
	def iterateProgram(self):
		st = self.lines[self.programCounter]
		incit = True
		codes = st.split(' ')
		if(codes[0] == 'lda'):
			self.ra = self.getMemory(int(codes[1]))
		elif(codes[0] == 'ldb'):
			self.rb = self.getMemory(int(codes[1]))
		elif(codes[0] == 'stc'):
			self.setMem(int(codes[1]), self.rc) 
		elif(codes[0] == 'goto'):
			self.programCounter = int(codes[1])
			incit = False
		elif(codes[0] == 'if'):
			if(self.rc != 0):
				self.programCounter = int(codes[1])
				incit = False
		elif(codes[0] == 'add'):
			self.rc = self.ra + self.rb
		elif(codes[0] == 'sub'):
			self.rc = self.ra - self.rb
		elif(codes[0] == 'or'):
			self.rc = self.ra | self.rb
		elif(codes[0] == 'and'):
			self.rc = self.ra & self.rb
		elif(codes[0] == 'xor'):
			self.rc = self.ra ^ self.rb
		elif(codes[0] == 'not'):
			self.rc = ~self.ra
		elif(codes[0] == 'end'):
			self.end = True
		
		
		if(incit == True):
			self.programCounter += 1
			
assemblerA = Assembler('myprogram.txt')
assemblerA.run()
assemblerA.printInfo()
