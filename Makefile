# default target is first
default: server

# start the local web server
server: convert
	bundle exec jekyll serve -H 0.0.0.0 -P 4100

# convert nb notebooks to markdown
convert:
	python scripts/convert_notebooks.py
