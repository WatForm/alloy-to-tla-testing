
# these are generated, and are then removed
find ./models -name "*.tla" -type f -exec rm {} \;
find ./models -name "*.cfg" -type f -exec rm {} \;
find ./models -name "*.out" -type f -exec rm {} \;
find ./models -name "*.als.json" -type f -exec rm {} \;
find ./models -name "*.tla.out" -type f -exec rm {} \;
find ./models -name "*.bin" -type f -exec rm {} \;
find ./models -name "*.tlc" -type f -exec rm {} \;

# remove any folder named "states"
find ./models -type d -name "states" -exec find {} -type f -exec rm -i {} \;

# remove logs generated during translation
rm -f *.log*