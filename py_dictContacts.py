#!/usr/bin/env python

_contacts = {}

def init():
	with open('contacts.txt') as _f:
		for _i in _f.readlines():
			_line = _i.strip().split()
			_contacts[_line[0]] = _line[1:]
#		print _contacts

def lookup():
	_name = raw_input("Enter the name: ")
	if _contacts.has_key(_name):
		print _name,"'s contact info: ", _contacts[_name]
	else:
		for _k,_v in _contacts.items():
			if _name in _v:
				print "Find you!"
				break
			else:
				continue
		else:
			print "Name isn't exsit!"

init()
lookup()

