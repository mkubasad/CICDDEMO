sudo systemctl stop nginx
sudo systemctl stop gunicorn
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl start nginx
