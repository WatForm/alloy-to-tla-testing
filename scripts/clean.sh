# these are tla and cfg models that are generated, and are then removed
find ./simple-models -name "*.tla" -type f -exec rm -i {} \;
find ./simple-models -name "cfg.tla" -type f -exec rm -i {} \;
find ./simple-models -name "out.tla" -type f -exec rm -i {} \;



# remove all models within any folder named "states"
find ./simple-models -type d -name "states" -exec find {} -type f -exec rm -i {} \;