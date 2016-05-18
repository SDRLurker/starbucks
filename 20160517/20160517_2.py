#!/usr/bin/python
# -*- coding: utf-8 -*-

def parentheses(s):
	stack = []
	for c in s:	
		if c in ('{', '(', '['):
			stack.append(c)
		else:
			if len(stack) == 0:
				return False
			poped = stack[-1]
			if c == '}' and poped == '{' or \
			   c == ')' and poped == '(' or \
			   c == ']' and poped == '[':
			   	del stack[-1]
			else:		
				return False

	return len(stack) == 0

#print parentheses("{[()]}")
#print parentheses("{[(])}")
#print parentheses("{{[[(())]]}}")

t = int(raw_input())
for _ in range(t):
	s = raw_input()
	print "YES" if parentheses(s) else "NO"
