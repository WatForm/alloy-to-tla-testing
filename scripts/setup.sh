python --version

java --version

mkdir -p ./libs
rm -rf ./libs
cd ./libs
git clone https://github.com/WatForm/dashplus
cd ./dashplus
./gradlew spotlessApply && ./gradlew releaseJar
cd ..
cd ..