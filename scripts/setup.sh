python --version

java --version


rm -rf ./libs
mkdir -p ./libs
cd ./libs
git clone https://github.com/WatForm/dashplus
cd ./dashplus
./gradlew spotlessApply && ./gradlew releaseJar

