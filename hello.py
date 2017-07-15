#coding=utf-8
# print 'hello, world',"second greeting"
# print '100+200=',100+200
# name=raw_input('please enter your name')
# print 'hello',name

# #判断输入的值是否大于100
# vle=raw_input('check if the number you inputed is beyond 100: ')
# if float(vle) > 100:
    # print 'Y'
# else:
    # print 'N'
	
# print '''...line1
# ...line2
# ...line3'''

# intarray=['A','P','P','L','E']
# for i in intarray:
	# print i
	
# sum=0
# for a in (1,2,3,4):
	# sum+=a
# print sum

class Student(object):
	@property
	def birth(self):
		return self._birth

	@birth.setter
	def birth(self,value):
		self._birth=value
			
	@property
	def age(self):
		return 2017-self._birth
	
	def __getattr__(self,attr):
		if attr=="score":
			return 99
		raise AttributeError("No such Attribute %s" % attr)
	
s= Student()
s.birth=1991
print s.age
print s.__getattr__('score')
print s.score
# s.test


class Animal(object):
	pass
	
class Mammal(Animal):
	pass

class Bird(Animal):
	pass
	
class Dog(Mammal):
	pass
	
class Bat(Mammal):
	pass
	
class Parrot(Bird):
	pass
	
class Ostrich(Bird):
	pass
	
class Runnable(object):
	def run(self):
		print ('Running...')
		
class Flyable(object):
	def fly(self):
		print('flying...')
		
class Dog(Mammal,Runnable):
	pass
	
class Bat(Mammal,Flyable):
	pass
	
dog=Dog()
dog.run()

class Fib(object):
	def __init__(self):
		self.a,self.b=0,1
		
	def __iter__(self):
		return self
		
	def next(self):
		self.a,self.b=self.b,self.a+self.b
		if self.a>100000:
			raise StopIteration()
		return self.a
	
	def __getitem__(self,n):
		if(isinstance(n,int)):
			a,b=1,1
			for x in range(n):
				a,b=b,a+b
			return a
		if(isinstance(n,slice)):
			start=n.start
			stop=n.stop
			a,b=1,1
			L=[]
			for x in range(stop):
				if(x>=start):
					L.append(a)
				a,b=b,a+b
			return L
		
for n in Fib():
	print n
	
fib=Fib()
print fib[5]
print fib[:10]
print fib[6:10]
print fib[2:3]


for x in range(10):
	if(x%2==0):
		print x
		print 'in'

class Chain(object):
	def __init__(self,path=''):
		self._path=path
		
	def __getattr__(self,path):
		return Chain('%s/%s' % (self._path,path))
		
	def __str__(self):
		return self._path
		
print Chain().category
print Chain().category.commic
print Chain().category.commic.character1
print Chain().category.commic.character1.page10


class CallTest(object):
	def __init__(self,name):
		self._name=name
	
	def __call__(self):
		print 'My Name is %s' % self._name
		
CallTest('Jack')()

try:
    print 'try...'
    r = 10 / 0
    print 'result:', r
except BaseException, e:
    print 'except:', e
finally:
    print 'finally...'
print 'END'

def divided():
	print '\n-----------------------------------------------------------------------\n'	
	
divided()	
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        logging.exception(e)

main()
print 'END'

divided()


assert(True),'Assert Is False'

divided()

import logging
logging.basicConfig(level=logging.INFO)

import pdb

# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# # pdb.set_trace()
# print 10 / n

divided()

class Dict(dict):
	def __init__(self,**kw):
		super(Dict,self).__init__(**kw)
		
	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AssertionError(r"'Dict' objext has no attribute '%s'" % key)
	
	def __setattr__(self,key,value):
		self[key]=value
		
		
kv={'a':1,'b':2,'c':3}

try:
	file=open('D:/file.txt','r')
	print file.read()
	file.close()
except Exception,e:
	print e
finally:
	print 'finally'

divided()
	
with open('D:/file.txt','r') as f:
	print f.read()

with open('D:/file.txt','w') as m:
	m.write(" added")
		
with open('D:/file.txt','r') as f:
	print f.read()

divided()

import os
print os.name
print os.environ
print os.getenv('path')
print os.getenv('classpath')

print 

