# SETUP AND MANAGE JENKINS IN DOCKER

# GET IMAGE
`docker pull jenkines`

# Run instance
* `docker run -d -p 8080:8080 jenkins` but you can loss all the data once close the jenkins instance.
* To keep data even after closing the instance<br>
   `docker run --name myJenkins -d -p 8080:8080 -v /Users/iopexses/Jenkins:/var/jenkins_home jenkins`

    * `docker run -d` – it runs container in the background
    * `-v /var/jenkins_home:/var/jenkins_home:z` – it attaches the container’s directory at the local system directory and it sets up appropriate SELinux fcontext
    * `-p 8080:8080` – it exposes container’s port 8080 to the local system port 8080
    * `-p 50000:50000` – same as above, but with the port 50000
    * `–name myjenkins` – display name of our container
    * `jenkins/jenkins:lts` – it tells “use the LTS version of Jenkins from the jenkins docker repository”

* Remove a container `docker container rm  container_name`

* start container in future : `docker start myJenkins`

# Open and Login
* after running jenkins server open `localhost:port` 
* provide initial password can be found  `secrets/initialAdminPassword`
* then it will prompt to install basic packages, that can be done from user interface navigation there.
* Register yourself and set a username (Ex: sudhanshu) and password :(password :dummypass)