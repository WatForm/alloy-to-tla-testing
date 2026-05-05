# these are tla and cfg models that are generated, and are then removed
find ./models/simple-models -name "*.tla" -type f -exec rm {} \;
find ./models/simple-models -name "*.cfg" -type f -exec rm {} \;
find ./models/simple-models -name "*.out" -type f -exec rm {} \;



# remove all models within any folder named "states"
find ./models/simple-models -type d -name "states" -exec find {} -type f -exec rm -i {} \;

# remove logs generated during translation
rm -f *.log*