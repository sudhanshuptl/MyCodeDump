# Ubuntu in Docker
* Run : `docker run -it ubuntu`
* commit changes : `docker commit 8548be10a0d0 Reposeratory:tag`
* Stop docker images running state `docker stop name_of_runnig_instance`
* To see details of Running states :`docker ps`
* To see all available images `docker images`
* To run your custom image `docker run REPOSITORY_name:tag_name` these information is available with `docker images`
* to open terminal of ubuntu `docker exec -it fde82fe8d2ff bash`
