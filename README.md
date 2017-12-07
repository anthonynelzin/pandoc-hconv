# pandoc-hconv

A (mostly useless) Pandoc filter to replace headings with custom-styled divs.

## How does it work?

This filter takes all level 3 and up headings (`<h3>`, `<h4>`, `<h5>` and `<h6>`) and replaces them with a matching div. Using this filter, this Markdown heading:

	### Lorem ipsum
	
or this HTML heading:

	<h3>Lorem ipsum</h3>

will be replaced with:

	<div class="h3"><p>Lorem ipsum</p></div>
	
at compilation.

## But wait, why?

This filter mainly exists to work around a bug in iBooks. iBooks will automatically create a table of contents from the headings in your book. That’s nice, right ? Well, this ToC is completely useless for complex books: only the second-level headings are indented, and all the other headings are put on the same level. Not so nice anymore. This filter allows the usage and formatting of headings without overcrowding the automatically generated ToC.

## Requirements

This filter requires the fantastic [Panflute](http://scorreia.com/software/panflute/ 'Panflute: pandoc filters made simple — panflute 1.9.7 documentation') package. You might want to [use a virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/ "Pipenv & Virtual Environments — The Hitchhiker’s Guide to Python"):

	virtualenv makebook
	. makebook/bin/activate
	pip install panflute

## Usage

Before using this filter, you should [read Pandoc’s documentation](https://pandoc.org/filters.html 'Pandoc - Pandoc filters'), where you’ll learn how to use filters. TL;DR:

	pandoc -f SOURCEFORMAT -t TARGETFORMAT --filter hconv.py
	
To format the resulting markup, don’t forget to add the corresponding CSS rules, like:

	.h3 {
 		font-size: 1.2em;
 		margin-top: 1.4em;
	}

Feel free to adapt this filter to your own needs. Want to replace all headings of level 2 and up ? Change :

	if elem.level > 2:
	
by:
	
	if elem.level > 1:
	
Want to change the class to a custom `data-heading-level` attribute? Swap:

	return Div(Para(*elem.content), attributes={'class': 'h{}'.format(elem.level)})
	
with:

	return Div(Para(*elem.content), attributes={'data-heading-level': 'h{}'.format(elem.level)})
	
for example.

## Rights

This filter is published by [Zinzolin](https://zinzolin.org/ 'Zinzolin // Publication numérique') under the terms of the [EUPL (v 1.2)](https://joinup.ec.europa.eu/page/eupl-text-11-12 'EUPL text (1.1 & 1.2) | Joinup').