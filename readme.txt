git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/Shantanu1395/map_info
git pull origin main --allow-unrelated-histories
git merge main --allow-unrelated-histories
git push origin main
docker build -t mega_project_map .
docker run --rm -v "$(pwd)/output:/app/output" mega_project_map

TODO
1. fix not able to make https calls from docker container