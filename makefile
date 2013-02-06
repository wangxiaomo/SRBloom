.PHONY: clean

clean:
	find . -name "*.pyc" | xargs rm -f
	rm -f *.jpg
