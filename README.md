# ScreenShot-API
A simple api that lets you take screenshot of webpages.

## Prerequisites

For run this project you'll need python3, pip3, google-chrome and mozilla firefox installed.

## Generate access key

To use the API you need to generate the key that will be used as token, using the following command:

```sh
./screenshotApi.sh generate_key "description"
```

Save this key, you'll need for make requests, if you don't remember the key, you can access at authorized_keys.

## Running the project locally

First of all you need to change the paths on screenshotApi.sh and index.py, using the paths that you want to use, make sure that the paths are the same on screenshotApi.sh and index.py.

To install all the necessary packages just use the following command:

```sh
./screenshotApi.sh install
```

After installing the packages, you can run the project using the following command:

```sh
./screenshotApi.sh start_debug
```

To stop the API, just use this command:

```sh
./screenshotApi.sh stop
```

## Deploying with apache2 without ssl certificate


You need to create a folder with the same name as the project folder and put your project inside it.

If you the path your o project was /home/user/ScreenShot-API, now will be /home/user/ScreenShot-API/ScreenShot-API.

For deploy the project you need apache2 installed. If you don't have, just use the following line to install:

```sh
sudo apt install apache2
```

After install apache2, you need to create a file on /etc/apache2/sites-available/ with the name you want .conf, I created screenshot-api.conf.

```sh
sudo vim /etc/apache2/sites-available/screenshot-api.conf
```

And you need to put this on the file, if you want, you can change the port:

```sh
<VirtualHost *:80*>
    ServerAdmin webmaster@localhost
    ServerName mywebsite.com

    WSGIScriptAlias /api /home/user/ScreenShot-API/ScreenShot-API/index.wsgi
    <Directory /home/user/ScreenShot-API/ScreenShot-API/>
            Options FollowSymLinks
            AllowOverride None
            Require all granted
    </Directory>
    ErrorLog ${APACHE_LOG_DIR}/error.log
    LogLevel warn
    CustomLog ${APACHE_LOG_DIR}/access.log combined

</VirtualHost>
```

Now you need to enable the virtual host with the following command:

```sh
sudo a2ensite screenshot-api
```

Restart Apache with the following command to apply the changes:

```sh
systemctl restart apache2
```

After that, you need to [activate](#activation-of-the-automatic-cleaning-script-for-screenshots) the automatic cleaning script, for delete the files insides ./temp/screenshots.

Now the API is running with apache and can be use for production.

## Deploying with apache with ssl certificate

It's basiclly the same process of deploy without the ssl certificate, the diference is that you'll edit /etc/apache2/sites-enabled/default-ssl.conf, I recommend that you make a backup of this file before change, use this following command to make the backup:

```sh
sudo cp /etc/apache2/sites-enabled/default-ssl.conf /etc/apache2/sites-enabled/default-ssl.conf.bak
```

After backup you can change the file.

```sh
sudo vim /etc/apache2/sites-enabled/default-ssl.conf
```

And the file you look like that:

```sh
<IfModule mod_ssl.c>
	<VirtualHost mydomain.com:443>
		ServerAdmin webmaster@localhost
		ServerName mydomain.com

        WSGIScriptAlias /api /home/user/ScreenShot-API/ScreenShot-API/index.wsgi
        <Directory /home/user/ScreenShot-API/ScreenShot-API/>
                Options FollowSymLinks
                AllowOverride None
                Require all granted
        </Directory>
        ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel info ssl:warn
        CustomLog ${APACHE_LOG_DIR}/access.log combined
		ErrorLog ${APACHE_LOG_DIR}/error.log
		SSLEngine on
		SSLCertificateFile	pathToFile
		SSLCertificateKeyFile pathToFile

		<FilesMatch "\.(cgi|shtml|phtml|php)$">
            SSLOptions +StdEnvVars
		</FilesMatch>
		<Directory /usr/lib/cgi-bin>
            SSLOptions +StdEnvVars
		</Directory>
	</VirtualHost>
</IfModule>

```

Now you need to restart the apache to apply the changes.

```sh
systemctl restart apache2
```

After that, you need to [activate](#activation-of-the-automatic-cleaning-script-for-screenshots) the automatic cleaning script, for delete the files insides ./temp/screenshots.

Now the API is running on production mode with ssl certificate.

## Activation of the automatic cleaning script for screenshots

Now you need to start the script that will clean files of /temp/screenshots, you can run the script with the following command:

```sh
./screenshotApi.start
```

Or you can change the file src/deleteScreenshots.sh to remove the loop and create a cron job.

After the change, the file will lock like that:

```sh
find $1 -mmin +1 -type f -name "mps_*.png" -exec rm -fv {} \;
find $1 -mmin +1 -type f -name "mps_*.jpg" -exec rm -fv {} \;
find $1 -mmin +1 -type f -name "mps_*.jpeg" -exec rm -fv {} \;
```

For create a cron job, use the following line:

```sh
crontab -e
```

And add this line to the end of the file, and save:

```sh
* * * * * /pathToProject/src/deleteScreenshots.sh "/pathToProject/temp/screenshots"
```

## Documentation

To know more about how the API works read the [documentation.](DOCUMENTATION.md)
