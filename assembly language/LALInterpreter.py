

class Assembler:
	def __init__(self, finame):
		fi = open(finame, 'r')
		self.lines = fi.readlines()
		fi.close()
		self.programCounter = 0
		self.memory = []
		self.memoryAmount = 1000
		self.stackMemCount = self.memoryAmount - 1
		self.ra = 0
		self.rb = 0
		self.end = False
		for i in range(self.memoryAmount):
			self.memory.append(0)
		count = 0
		lut = [0, 1024, 512, 341, 256, 204, 170, 146, 128, 113, 102, 93, 85, 78, 73, 68, 64, 60, 56, 53, 51, 48, 46, 44, 42, 40, 39, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 26, 25, 24, 24, 23, 23, 22, 22, 21, 21, 20, 20, 20, 19, 19, 18, 18, 18, 17, 17, 17, 17,  16, 16, 16, 16, 15, 15, 15, 15, 14, 14, 14, 14, 14, 13, 13, 13, 13, 13, 12, 12, 12, 12, 12, 12, 12, 11, 11, 11, 11, 11, 11, 11 , 11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 , 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,  2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 , 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 , 1]
		for i in range(300, 941):
			self.memory[i] = lut[count]
			count += 1
		self.setupStackMemory()
		self.functionNames = []
		self.functionLines = []
		self.setupFunctionNames()
		#self.printInfo()
		
	def setupFunctionNames(self):
		for i in range(len(self.lines)):
			st = self.lines[i]
			codes = st.split(' ')
			if(codes[0] == 'func'):
				self.functionNames.append(codes[1])
				self.functionLines.append(int(i))
		
		for i in range(len(self.lines)):
			st = self.lines[i]
			codes = st.split(' ')
			if(codes[0] == 'goto' or codes[0] == 'ifa' or codes[0] == 'ifan'):
				self.lines[i] = codes[0] + ' ' + str(self.findFunctionLine(codes[1], i))
				
	def findFunctionLine(self, name, xval):
		for i in range(len(self.functionNames)):
			if(name == self.functionNames[i]):
				return int(self.functionLines[i])
		return int(xval)
	def printInfo(self):
		print self.lines
		print 'Program Counter: ', self.programCounter
		print 'functions:'
		for i in range(len(self.functionNames)):
			print self.functionNames[i], ' on line: ', self.functionLines[i]
		print 'memory:'
		#for i in range(self.memoryAmount):
		for i in range(50):
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
		elif(codes[0] == 'ldafb'):
			self.ra = self.getMemory(int(self.rb))
		elif(codes[0] == 'bisa'):
			self.rb = int(self.ra)
		elif(codes[0] == 'sta'):
			self.setMem(int(codes[1]), self.ra)
		elif(codes[0] == 'stb'):
			self.setMem(int(codes[1]), self.rb) 
		elif(codes[0] == 'staib'):
			self.setMem(self.rb, self.ra) 
		elif(codes[0] == 'goto'):
			self.programCounter = int(codes[1])
			incit = False
		elif(codes[0] == 'goa'):
			self.programCounter = int(self.ra)-1
			incit = False
		elif(codes[0] == 'ifa'):
			if(self.ra != 0):
				self.programCounter = int(codes[1])
				incit = False
		elif(codes[0] == 'ifga'):
			if(self.ra != 0):
				self.programCounter = self.getMemory(int(codes[1]))-1
				incit = False
		elif(codes[0] == 'ifan'):
			if(self.ra == 0):
				self.programCounter = int(codes[1])
				incit = False
		elif(codes[0] == 'ifgan'):
			if(self.ra == 0):
				self.programCounter = self.getMemory(int(codes[1]))-1
				incit = False
		elif(codes[0] == 'altb'):
			if(self.ra < self.rb):
				self.ra = 1
			else:
				self.ra = 0
		elif(codes[0] == 'aeqb'):
			if(self.ra == self.rb):
				self.ra = 1
			else:
				self.ra = 0
		elif(codes[0] == 'agtb'):
			if(self.ra > self.rb):
				self.ra = 1
			else:
				self.ra = 0
		elif(codes[0] == 'add'):
			self.ra = self.ra + self.rb
		elif(codes[0] == 'inca'):
			self.ra = self.ra + 1
		elif(codes[0] == 'deca'):
			self.ra = self.ra - 1
		elif(codes[0] == 'sub'):
			self.ra = self.ra - self.rb
		elif(codes[0] == 'or'):
			self.ra = self.ra | self.rb
		elif(codes[0] == 'and'):
			self.ra = self.ra & self.rb
		elif(codes[0] == 'xor'):
			self.ra = self.ra ^ self.rb
		elif(codes[0] == 'not'):
			self.ra = ~self.ra
		elif(codes[0] == 'shla'):
			self.ra <<= int(codes[1])
		elif(codes[0] == 'shra'):
			self.ra >>= int(codes[1])
		elif(codes[0] == 'end'):
			self.end = True
		
		
		if(incit == True):
			self.programCounter += 1
			
assemblerA = Assembler('dividerProgram.txt')
assemblerA.run()
assemblerA.printInfo()
