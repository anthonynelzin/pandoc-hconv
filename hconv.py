#!/usr/bin/env python
# -*- coding: utf-8 -*-
from panflute import *

def hconv(elem, doc):
	if isinstance(elem, Header):
		if elem.level > 2:
			return Div(Para(*elem.content), attributes={'class': 'h{}'.format(elem.level)})

def main(doc=None):
	return run_filter(hconv, doc=doc)

if __name__ == '__main__':
	main()