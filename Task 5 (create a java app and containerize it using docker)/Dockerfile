# ==== Stage 1: build ====
FROM eclipse-temurin:21-jdk AS build
WORKDIR /app

# Copy source and compile
COPY src/ src/
RUN javac -d out $(find src -name "*.java") \
 && echo "Main-Class: com.example.Main" > manifest.mf \
 && jar cfm app.jar manifest.mf -C out .

# ==== Stage 2: runtime ====
FROM eclipse-temurin:21-jre AS runtime
WORKDIR /app
COPY --from=build /app/app.jar /app/app.jar
ENTRYPOINT ["java","-jar","/app/app.jar"]
