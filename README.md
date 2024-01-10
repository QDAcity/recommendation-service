# recommendation-service
An AI recommendation service intended to provide recommendations while working on [qualitative data analysis](https://qdacity.com/qda-help/) with https://qdacity.com


docker build -t your-image-name .
docker tag recommandation gcr.io/qdacity-app/recommandation
docker push gcr.io/qdacity-app/recommandation 

bq load --autodetect --source_format=CSV qdacity-app:recommandation_code.Code gs://code_recommandation/Code.csv