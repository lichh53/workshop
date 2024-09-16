pdf:
	mkdir -p build
	python3 scripts/combine_md_files.py textbook.md . build/textbook.md \
		&> build/combine_md_files.log
	pandoc --pdf-engine=xelatex build/textbook.md -o build/textbook.pdf \
		&> build/textbook.log