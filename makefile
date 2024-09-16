pdf:
	pandoc --pdf-engine=xelatex textbook.md -o tmp/textbook.pdf &> tmp/textbook.log