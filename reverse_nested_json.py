#!/usr/bin/env python
#coding=utf-8

import json
import sys

keyStack = []

def add_elem(json, keys, val):
    parent = json
    for k in keys[:-1]:
        try:	
        	if k not in parent:
        		parent[k] = {}
        except Exception as e:
        	print("your seach key is not correct,please check search key")
        	sys.exit(1)
        parent = parent[k]
    parent[keys[-1]] = val

def reverseJson(keyStack,val_result):
	
	keyStack.reverse()
	keyStack = [val_result] + keyStack
	jsondata = {}
	paths = [
	    keyStack[:-1],
	]

	for keys in paths:
		add_elem(jsondata, keys, keyStack[-1] )

	print("result:",jsondata)
	
	return jsondata

def key_generator(d,keyVal):
	for k, v in d.items():
		keyStack.append(k)
		if k == keyVal:
			yield v
		elif isinstance(v, dict):
			for id_val in key_generator(v,keyVal):
				yield id_val


def reverse_nested_json(input_value,SearchKey):
	val_result ="null"
	for val in key_generator(input_value,SearchKey):
		val_result = val
		
	# print("init key stack:",keyStack)
	output = reverseJson(keyStack,val_result)
	return output


if __name__ == '__main__':
	input_value  = {
	  'hired': {
	    'be': {
	      'to': {
	        'deserve': 'I'
	      }
	    }
	  }
	}

	output = reverse_nested_json(input_value,"deserve ")

	print("output_value:",output)
	

	





