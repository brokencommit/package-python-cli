import argparse
from . import spell, verbose, sushi

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--verbose", help="increase output verbosity", action="store_true")
	parser.add_argument("--sushi", help="make rolls", action="store_true")
	parser.add_argument("--spell", help="let me cast a spell", action="store_true")

	args = parser.parse_args()
	if args.verbose:
		verbose()

	if args.sushi:
		sushi()

	if args.spell:
		spell()