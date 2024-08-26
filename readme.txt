git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/Shantanu1395/map_info
git pull origin main --allow-unrelated-histories
git merge main --allow-unrelated-histories
git push origin main
docker build -t mega_project_map .
docker run --rm -v "$(pwd)/output:/app/output" mega_project_map

TODO fixes
1. fix not able to make https calls from docker container

TODO development
1. modularize code, make classes
2. add filters for topic + continent/country
3. add time vector and add filter as per time + (topic + continent/country)
4. deploy to ec2 and online access html file
5. make apis for chart creation with filters
6. move data to db