# these are tla and cfg models that are generated, and are then removed
find ../models -name "*.tla" -type f -exec rm -i {} \;
find ../models -name "cfg.tla" -type f -exec rm -i {} \;
find ../models -name "out.tla" -type f -exec rm -i {} \;

# remove all models within any folder named "states"
find ../models -type d -name "states" -exec find {} -type f -exec rm -i {} \;